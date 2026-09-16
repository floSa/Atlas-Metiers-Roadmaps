#!/usr/bin/env python3
"""Verifie les URL du corpus et classe les reponses.

Le corpus cite des sources tierces. Une source meurt sans prevenir : le blog
est ferme, l'article est deplace, le domaine est revendu. Ce script mesure
l'etat du parc de liens, il ne le repare pas : il produit un rapport, et la
decision de remplacer ou de retirer reste humaine.

Trois principes de fonctionnement :

  respectueux   un delai entre deux requetes, un delai plus long entre deux
                requetes vers le meme domaine, un User-Agent qui dit qui
                appelle et pourquoi, aucun parallelisme. On interroge des
                serveurs qui ne nous doivent rien.
  incremental   chaque resultat est mis en cache avec sa date. Une URL
                verifiee il y a moins de --revoir jours n'est pas retestee.
                C'est ce qui rend la veille tenable.
  sans effet    le script n'ecrit que dans data/liens/. Il ne touche jamais
                a content/.

Les statuts :
  ok            2xx, atteignable en l'etat
  redirection   atteignable, mais l'URL finale differe -> l'URL citee est a
                mettre a jour
  introuvable   404 ou 410, la page n'existe plus
  erreur        5xx, le serveur est en panne -> a reverifier avant de conclure
  bloque        401, 403, 429 ou interstitiel anti-robot. Ne veut PAS dire
                mort : a verifier a la main dans un navigateur
  domaine-mort  DNS introuvable ou connexion refusee
  delai         pas de reponse dans le temps imparti

Usage :
  python3 tools/verifier_liens.py --selection        # les URL de content/ressources/
  python3 tools/verifier_liens.py --corpus           # les URL citees dans content/
  python3 tools/verifier_liens.py --amont            # les URL de data/extract/*.json
  python3 tools/verifier_liens.py --url URL [URL...] # une verification ponctuelle
  python3 tools/verifier_liens.py --corpus --revoir 0  # force le retest complet

Options utiles :
  --limite N     s'arreter apres N verifications reelles (le cache ne compte pas)
  --delai S      secondes entre deux requetes (defaut 1.5)
  --delai-domaine S  secondes entre deux requetes vers le meme domaine (defaut 5)
  --revoir J     ne pas retester une URL vue il y a moins de J jours (defaut 30)
  --rapport P    chemin du rapport (defaut data/liens/rapport.md)
"""
from __future__ import annotations

import argparse
import datetime as dt
import collections
import glob
import http.client
import json
import pathlib
import re
import socket
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
EXTRACT = ROOT / "data" / "extract"
CONTENT = ROOT / "content"
LIENS = ROOT / "data" / "liens"
CACHE = LIENS / "cache.json"

# Un User-Agent honnete : il dit ce qu'est le programme et ou regarder. Se
# faire passer pour un navigateur serait a la fois inutile et malpoli.
UA = (
    "atlas-ia-verifier-liens/1.0 (+https://github.com/ ; verification de liens "
    "d'un corpus pedagogique ; contact via le depot)"
)

TIMEOUT = 20

# Marqueurs d'interstitiel anti-robot renvoyes avec un code 2xx. Une page qui
# repond 200 mais ne contient que ca n'est pas une page vivante pour autant.
ANTIROBOT = re.compile(
    r"just a moment|checking your browser|cf-browser-verification|enable javascript and cookies|"
    r"are you a robot|captcha|incapsula|access denied|attention required",
    re.I,
)

# Un lien markdown ordinaire : [titre](url). On ignore les wikilinks, qui sont
# internes par construction.
MD_LINK = re.compile(r"\[[^\]]*\]\((https?://[^\s)]+)\)")
# Le champ source: du frontmatter, qui n'est pas un lien markdown.
MD_SOURCE = re.compile(r"^source:\s*(https?://\S+)\s*$", re.M)
# Une URL nue dans du texte courant.
MD_NUE = re.compile(r"(?<![(\[<])\bhttps?://[^\s<>)\]\"]+")


# --------------------------------------------------------------------------
# Collecte des URL a verifier
# --------------------------------------------------------------------------

def urls_amont() -> dict[str, list[str]]:
    """Les URL des ressources extraites, avec la liste des roadmaps qui les citent."""
    origines: dict[str, list[str]] = collections.defaultdict(list)
    for chemin in sorted(EXTRACT.glob("*.json")):
        donnees = json.loads(chemin.read_text(encoding="utf-8"))
        slug = donnees["slug"]
        for section in donnees.get("sections", []):
            for noeud in section.get("nodes", []):
                for res in noeud.get("resources", []):
                    if slug not in origines[res["url"]]:
                        origines[res["url"]].append(slug)
    return dict(origines)


def urls_selection() -> dict[str, list[str]]:
    """Les URL de la selection commentee, sous content/ressources/.

    C'est le perimetre le plus important a surveiller : ce sont les adresses
    que l'atlas met en avant. Une source morte y coute plus cher qu'ailleurs.
    """
    return _urls_markdown(CONTENT / "ressources")


def urls_corpus() -> dict[str, list[str]]:
    """Les URL citees dans les notes redigees, avec les fichiers qui les citent."""
    return _urls_markdown(CONTENT)


def _urls_markdown(racine: pathlib.Path) -> dict[str, list[str]]:
    origines: dict[str, list[str]] = collections.defaultdict(list)
    for chemin in sorted(racine.rglob("*.md")):
        texte = chemin.read_text(encoding="utf-8")
        relatif = str(chemin.relative_to(ROOT))
        trouvees = set(MD_LINK.findall(texte)) | set(MD_SOURCE.findall(texte)) | set(MD_NUE.findall(texte))
        for url in trouvees:
            url = url.rstrip(".,;:")
            if relatif not in origines[url]:
                origines[url].append(relatif)
    return dict(origines)


# --------------------------------------------------------------------------
# Verification d'une URL
# --------------------------------------------------------------------------

class SansRedirection(urllib.request.HTTPRedirectHandler):
    """Suit les redirections mais retient la chaine, pour signaler l'URL finale."""

    def __init__(self) -> None:
        self.chaine: list[str] = []

    def redirect_request(self, req, fp, code, msg, headers, newurl):  # noqa: N802
        self.chaine.append(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def interroger(url: str, methode: str) -> tuple[int, str, str]:
    """Une requete. Renvoie (code, url finale, debut du corps)."""
    handler = SansRedirection()
    opener = urllib.request.build_opener(handler)
    requete = urllib.request.Request(
        url,
        method=methode,
        headers={
            "User-Agent": UA,
            "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
            "Accept-Language": "fr,en;q=0.8",
        },
    )
    with opener.open(requete, timeout=TIMEOUT) as reponse:
        corps = ""
        if methode == "GET":
            brut = reponse.read(4096)
            corps = brut.decode(reponse.headers.get_content_charset() or "utf-8", "replace")
        return reponse.status, reponse.geturl(), corps


# Un segment de langue insere par le serveur selon l'en-tete Accept-Language :
# aws.amazon.com/fr/..., asana.com/fr/..., learn.microsoft.com/en-us/...
# Ce n'est pas un deplacement de la ressource, et le signaler a chaque passage
# ne ferait que noyer les vraies redirections.
LOCALE = re.compile(r"^(?:[a-z]{2}|[a-z]{2}[-_][a-z]{2})$", re.I)

# Le meme bruit, mais passe en parametre de requete : ?hl=fr chez Google,
# ?lang=, ?locale=, et les drapeaux de banniere de consentement de YouTube.
LOCALE_PARAM = {"hl", "lang", "locale", "setlang", "cbrd", "ucbcb"}


def normaliser(url: str) -> str:
    """Pour comparer une URL de depart et une URL d'arrivee sans bruit inutile."""
    p = urllib.parse.urlsplit(url)
    hote = p.netloc.lower()
    if hote.startswith("www."):
        hote = hote[4:]
    segments = [s for s in p.path.split("/") if s and not LOCALE.match(s)]
    chemin = "/" + "/".join(segments)
    requete = urllib.parse.urlencode(
        [(k, v) for k, v in urllib.parse.parse_qsl(p.query) if k.lower() not in LOCALE_PARAM]
    )
    return urllib.parse.urlunsplit((p.scheme.replace("http", "https"), hote, chemin, requete, ""))


def redirection_generique(depart: str, arrivee: str) -> bool:
    """La redirection mene-t-elle a une page d'accueil plutot qu'a la ressource ?

    Un article retire est rarement servi en 404 : le site redirige vers sa racine,
    vers l'index de la rubrique, ou vers le domaine de celui qui l'a rachete. C'est
    un 404 deguise, et c'est le cas le plus perfide parce qu'il repond 200.
    """
    d, a = urllib.parse.urlsplit(depart), urllib.parse.urlsplit(arrivee)
    segs_d = [s for s in d.path.split("/") if s and not LOCALE.match(s)]
    segs_a = [s for s in a.path.split("/") if s and not LOCALE.match(s)]
    if len(segs_d) < 2:
        return False  # la source etait deja une racine, rien a dire
    if segs_a and segs_a[-1] == segs_d[-1]:
        # La feuille est intacte : la ressource a demenage, elle n'a pas disparu.
        # C'est le cas d'un site rachete qui republie ses pages a l'identique.
        return False
    return len(segs_a) < len(segs_d)


def verifier(url: str) -> dict:
    """Teste une URL et renvoie son verdict.

    HEAD d'abord : c'est la requete la plus legere pour le serveur. Beaucoup de
    sites la refusent (405, 403, parfois un 200 mensonger), on repasse alors en
    GET en ne lisant que les premiers kilo-octets.
    """
    resultat = {"statut": "erreur", "code": None, "final": None, "note": ""}
    for methode in ("HEAD", "GET"):
        try:
            code, final, corps = interroger(url, methode)
        except urllib.error.HTTPError as err:
            code, final, corps = err.code, url, ""
            if methode == "HEAD" and code in (400, 403, 405, 406, 429, 500, 501):
                continue  # beaucoup de serveurs n'acceptent que GET
        except urllib.error.URLError as err:
            motif = err.reason
            if isinstance(motif, socket.gaierror):
                return {**resultat, "statut": "domaine-mort", "note": "DNS introuvable"}
            if isinstance(motif, (socket.timeout, TimeoutError)):
                return {**resultat, "statut": "delai", "note": "pas de reponse"}
            if isinstance(motif, ssl.SSLError):
                return {**resultat, "statut": "erreur", "note": f"TLS : {motif}"}
            if isinstance(motif, ConnectionError):
                return {**resultat, "statut": "domaine-mort", "note": str(motif)}
            return {**resultat, "statut": "erreur", "note": str(motif)[:120]}
        except (socket.timeout, TimeoutError):
            return {**resultat, "statut": "delai", "note": "pas de reponse"}
        except (http.client.HTTPException, ValueError, UnicodeError, OSError) as err:
            return {**resultat, "statut": "erreur", "note": f"{type(err).__name__} : {err}"[:120]}

        resultat["code"] = code
        resultat["final"] = final

        if code in (401, 403, 429):
            resultat["statut"] = "bloque"
            resultat["note"] = "a verifier a la main dans un navigateur"
            if methode == "HEAD":
                continue
            return resultat
        if code in (404, 410):
            if methode == "HEAD":
                continue  # un 404 sur HEAD arrive sur des serveurs mal configures
            return {**resultat, "statut": "introuvable", "note": ""}
        if code >= 500:
            if methode == "HEAD":
                continue
            return {**resultat, "statut": "erreur", "note": "erreur serveur"}
        if 200 <= code < 300:
            # Cas EUR-Lex : 202 Accepted, corps vide. Le serveur accuse
            # reception et renvoie la requete vers un controle navigateur.
            # Un HEAD ne permet pas de le voir, il faut le corps.
            if code == 202 or (methode == "GET" and not corps.strip()):
                if methode == "HEAD":
                    continue
                return {
                    **resultat,
                    "statut": "bloque",
                    "note": "reponse vide derriere un controle navigateur, a verifier a la main",
                }
            if methode == "HEAD":
                # Un 200 sur HEAD ne dit rien du contenu : on ne peut pas
                # detecter un interstitiel. On repasse en GET pour le savoir.
                continue
            if ANTIROBOT.search(corps):
                return {
                    **resultat,
                    "statut": "bloque",
                    "note": "interstitiel anti-robot, a verifier a la main",
                }
            if normaliser(final) != normaliser(url):
                note = f"-> {final}"
                if redirection_generique(url, final):
                    note += " (page generique : la ressource a probablement disparu)"
                return {**resultat, "statut": "redirection", "note": note}
            if normaliser(final) != normaliser(url).replace("//", "//", 1) or final != url:
                pass  # meme ressource a une variante de langue pres
            return {**resultat, "statut": "ok", "note": ""}
    return resultat


# --------------------------------------------------------------------------
# Cache
# --------------------------------------------------------------------------

def charger_cache() -> dict:
    if CACHE.exists():
        return json.loads(CACHE.read_text(encoding="utf-8"))
    return {}


def ecrire_cache(cache: dict) -> None:
    LIENS.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")


def perime(entree: dict, jours: int) -> bool:
    vu = entree.get("verifie_le")
    if not vu:
        return True
    try:
        age = (dt.date.today() - dt.date.fromisoformat(vu)).days
    except ValueError:
        return True
    # Un statut instable merite d'etre reteste plus tot qu'un statut stable.
    if entree.get("statut") in ("erreur", "delai", "bloque"):
        jours = min(jours, 7)
    return age >= jours


# --------------------------------------------------------------------------
# Rapport
# --------------------------------------------------------------------------

ORDRE = ["introuvable", "domaine-mort", "redirection", "erreur", "delai", "bloque", "ok"]

COMMENTAIRE = {
    "introuvable": "La page a disparu. A remplacer par un equivalent verifie, ou a retirer.",
    "domaine-mort": "Le domaine ne repond plus du tout. A retirer.",
    "redirection": "Atteignable, mais l'URL citee n'est plus l'URL reelle. A mettre a jour.",
    "erreur": "Panne serveur ou defaut TLS au moment du test. A reverifier avant de conclure.",
    "delai": "Aucune reponse dans le temps imparti. A reverifier.",
    "bloque": "Le serveur refuse les robots. Ne veut pas dire mort : verification humaine requise.",
    "ok": "Atteignable a l'URL citee.",
}


def ecrire_rapport(chemin: pathlib.Path, cache: dict, origines: dict[str, list[str]], perimetre: str) -> None:
    par_statut: dict[str, list[str]] = collections.defaultdict(list)
    for url in origines:
        entree = cache.get(url)
        if entree:
            par_statut[entree["statut"]].append(url)

    total = sum(len(v) for v in par_statut.values())
    lignes = [
        "# Rapport de verification des liens",
        "",
        f"> Produit par `tools/verifier_liens.py` le {dt.date.today().isoformat()}.",
        f"> Perimetre : **{perimetre}** — {len(origines)} URL uniques, {total} verifiees.",
        "> Ce rapport ne modifie rien. Il liste ce qu'il y a a decider.",
        "",
        "## Vue d'ensemble",
        "",
        "| Statut | Nombre | Part | Ce que ca veut dire |",
        "|---|---:|---:|---|",
    ]
    for statut in ORDRE:
        n = len(par_statut.get(statut, []))
        if not n:
            continue
        lignes.append(f"| `{statut}` | {n} | {100 * n / max(total, 1):.1f} % | {COMMENTAIRE[statut]} |")

    for statut in ORDRE:
        urls = sorted(par_statut.get(statut, []))
        if not urls or statut == "ok":
            continue
        lignes += ["", f"## {statut} — {len(urls)}", "", COMMENTAIRE[statut], ""]
        for url in urls:
            entree = cache[url]
            note = f" — {entree['note']}" if entree.get("note") else ""
            code = f" `{entree['code']}`" if entree.get("code") else ""
            cites = ", ".join(origines[url][:4])
            lignes.append(f"- `{url}`{code}{note}")
            lignes.append(f"  cite par : {cites}")

    ok = len(par_statut.get("ok", []))
    lignes += [
        "",
        f"## ok — {ok}",
        "",
        "Non detaillees : la liste est dans `data/liens/cache.json`.",
        "",
    ]
    chemin.parent.mkdir(parents=True, exist_ok=True)
    chemin.write_text("\n".join(lignes), encoding="utf-8")


# --------------------------------------------------------------------------

def affiche(chemin: pathlib.Path) -> str:
    """Un chemin relatif au depot quand c'est possible, absolu sinon."""
    try:
        return str(chemin.resolve().relative_to(ROOT))
    except ValueError:
        return str(chemin)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--amont", action="store_true", help="verifier les URL de data/extract/*.json")
    ap.add_argument("--corpus", action="store_true", help="verifier les URL citees dans content/")
    ap.add_argument("--selection", action="store_true", help="verifier les URL de content/ressources/")
    ap.add_argument("--url", nargs="+", default=[], help="verifier ces URL et rien d'autre")
    ap.add_argument("--limite", type=int, default=0, help="arreter apres N verifications reelles")
    ap.add_argument("--delai", type=float, default=1.5, help="secondes entre deux requetes")
    ap.add_argument("--delai-domaine", type=float, default=5.0, help="secondes entre deux requetes vers un meme domaine")
    ap.add_argument("--revoir", type=int, default=30, help="ne pas retester une URL vue il y a moins de N jours")
    ap.add_argument("--rapport", default=str(LIENS / "rapport.md"), help="chemin du rapport")
    args = ap.parse_args()

    if args.url:
        origines = {u: ["--url"] for u in args.url}
        perimetre = "verification ponctuelle"
    elif args.selection:
        origines = urls_selection()
        perimetre = "selection commentee (content/ressources/)"
    elif args.corpus:
        origines = urls_corpus()
        perimetre = "corpus redige (content/)"
    elif args.amont:
        origines = urls_amont()
        perimetre = "ressources amont (data/extract/)"
    else:
        ap.print_help()
        return 2

    cache = charger_cache()
    a_faire = [u for u in origines if u not in cache or perime(cache[u], args.revoir)]
    print(f"{len(origines)} URL au perimetre, {len(origines) - len(a_faire)} deja en cache, {len(a_faire)} a tester.")
    if args.limite:
        a_faire = a_faire[: args.limite]
        print(f"limite a {len(a_faire)} cette passe.")

    dernier_domaine: dict[str, float] = {}
    compte = collections.Counter()
    try:
        for i, url in enumerate(a_faire, 1):
            domaine = urllib.parse.urlsplit(url).netloc.lower()
            attente = args.delai_domaine - (time.monotonic() - dernier_domaine.get(domaine, -1e9))
            if attente > 0:
                time.sleep(attente)
            resultat = verifier(url)
            dernier_domaine[domaine] = time.monotonic()
            resultat["verifie_le"] = dt.date.today().isoformat()
            cache[url] = resultat
            compte[resultat["statut"]] += 1
            marque = " " if resultat["statut"] == "ok" else "!"
            print(f"{marque} [{i}/{len(a_faire)}] {resultat['statut']:13} {url[:95]}")
            if i % 25 == 0:
                ecrire_cache(cache)
            time.sleep(args.delai)
    except KeyboardInterrupt:
        print("\ninterrompu — le cache est conserve, relancer reprend ou on s'est arrete.")

    ecrire_cache(cache)
    rapport = pathlib.Path(args.rapport)
    ecrire_rapport(rapport, cache, origines, perimetre)
    print("\n" + "  ".join(f"{k}={v}" for k, v in sorted(compte.items())))
    print(f"cache   : {affiche(CACHE)}")
    print(f"rapport : {affiche(rapport)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
