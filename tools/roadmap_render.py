#!/usr/bin/env python3
"""Rendu d'une roadmap en carte SVG cliquable, integrable dans une note du corpus.

Pourquoi du SVG et pas le `click` natif de Mermaid : voir
quartz/essai-carte-cliquable/VERDICT.md. En deux lignes, Mermaid rend sa carte
dans le navigateur, apres que Quartz a resolu les liens : l'URL n'est jamais
reecrite, donc le clic part en 404 depuis une page imbriquee, la carte disparait
sans JavaScript, et elle n'alimente ni le graphe ni les retroliens. Un SVG pose
en HTML brut dans le Markdown traverse, lui, le resolveur de Quartz.

Deux sources, combinees :
  - data/raw/<slug>/<date>.json     la capture brute de l'API : position, largeur
    et hauteur de chaque noeud -> la disposition de roadmap.sh est reproduite,
    pas reinventee
  - data/extract/<slug>.json        la forme normalisee : sections, ordre de
    lecture, libelles -> sert la version en liste

Ou pointe un noeud, dans cet ordre :
  1. une correspondance explicite      -> content/notions/<slug-du-registre>
  2. sinon, l'ancre de section         -> <page-du-parcours>#<ancre-du-libelle>
  3. un bouton amont (href roadmap.sh) -> la note locale qui declare cette URL en
     `source:` dans son frontmatter, sinon l'URL amont elle-meme

Un noeud dont la cible n'existe pas encore reste cliquable et recoit la classe
`a-ecrire` : trait pointille, libelle en italique. C'est voulu, les chantiers
metier ecrivent en parallele.

Produit une page Markdown autonome : le SVG en HTML brut, puis la meme carte en
liste repliable — c'est la sortie de secours au telephone, sans SVG et au
lecteur d'ecran. Deterministe : meme entree, meme sortie, octet pour octet.
Aucune dependance hors bibliotheque standard.

Usage :
  python3 tools/roadmap_render.py forward-deployed-engineer
  python3 tools/roadmap_render.py forward-deployed-engineer \
      --parcours parcours/forward-deployed-engineer \
      --sortie content/parcours/forward-deployed-engineer/carte.md
  python3 tools/roadmap_render.py <slug> --liens correspondances.json --verifier
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import re
import sys
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
EXTRACT = ROOT / "data" / "extract"
CONTENU = ROOT / "content"
REGISTRE = CONTENU / "notions" / "_registre.md"

# Correspondance libelle amont -> slug du registre des notions.
#
# Elle ne peut pas etre deduite : l'amont est en anglais, le registre en
# francais, et le decoupage ne se recouvre pas noeud pour noeud. Elle vit ici
# parce que le registre appartient au chantier 07 et l'amont au chantier 01.
# Volontairement courte : on n'y met que les equivalences franches. Un noeud de
# section -- << AI Engineering Skills >>, << DevOps Skills >> -- couvre trop de
# notions pour en designer une ; il tombe sur l'ancre de sa section, c'est le bon
# niveau de granularite.
#
# Pour l'etendre sans toucher au script : --liens correspondances.json, un objet
# {"<slug-roadmap>": {"<libelle amont>": "<cible>"}}. Une cible prend trois formes :
#   "cadrage-besoin"        -> content/notions/cadrage-besoin
#   "#etape-2-le-cadrage"   -> cette ancre dans la note du parcours
#   "roadmaps/05 - ..."     -> n'importe quelle page, telle quelle
# C'est par la que le chantier metier raccroche les libelles anglais de l'amont
# aux titres francais de sa note.
CORRESPONDANCES: dict[str, dict[str, str]] = {
    "forward-deployed-engineer": {
        "Requirements Gathering": "cadrage-besoin",
        "Technical Scoping & Sequencing": "cadrage-besoin",
        "Enterprise Workflow": "systemes-patrimoniaux",
        "ROI & AI Impact": "roi-des-projets-ia",
        "Stakeholder Management": "gestion-parties-prenantes",
        "Technical Writing": "redaction-technique",
    },
}

# Les noeuds qui portent du sens et meritent un lien. Le reste du canevas
# roadmap.sh -- paragraphes d'ambiance, traits de separation -- est dessine mais
# n'est pas cliquable.
CLIQUABLES = {"topic", "subtopic", "button"}
# Le canevas roadmap.sh porte aussi des elements de mise en page. Recenses sur
# les treize captures : `section` un cadre de regroupement vide, `vertical` et
# `horizontal` des filets pointilles, `todo` une ligne de liste, `resourceButton`
# un renvoi vers une ressource -- souvent un lien d'affiliation, qu'on dessine
# sans le rendre cliquable ; la selection des ressources revient au chantier 08.
FILETS = {"vertical", "horizontal"}
CADRES = {"section"}

MARGE = 40
LARGEUR_CAR = 0.55  # largeur moyenne d'un caractere, en fraction de la police


# --------------------------------------------------------------------------- #
# Lecture des sources
# --------------------------------------------------------------------------- #

def derniere_capture(slug: str) -> pathlib.Path:
    """La capture brute la plus recente. Les noms sont des dates ISO, donc triables."""
    dossier = RAW / slug
    captures = sorted(dossier.glob("*.json")) if dossier.is_dir() else []
    if not captures:
        raise SystemExit(f"Aucune capture dans {dossier} : lancer roadmap_extract.py {slug}")
    return captures[-1]


def charger(chemin: pathlib.Path) -> dict:
    return json.loads(chemin.read_text(encoding="utf-8"))


def slugs_du_registre() -> set[str]:
    """Les slugs de notions declares dans le registre, lus dans la colonne 1 des tables."""
    if not REGISTRE.is_file():
        return set()
    return set(re.findall(r"^\|\s*`([a-z0-9-]+)`\s*\|", REGISTRE.read_text(encoding="utf-8"), re.M))


def index_des_sources() -> dict[str, str]:
    """URL roadmap.sh -> slug Quartz de la note locale qui la declare en `source:`.

    C'est ce qui permet a un bouton << AI Engineer Roadmap >> de renvoyer vers
    notre propre note plutot que vers l'amont.
    """
    index: dict[str, str] = {}
    if not CONTENU.is_dir():
        return index
    for fichier in sorted(CONTENU.rglob("*.md")):
        tete = fichier.read_text(encoding="utf-8")[:1200]
        found = re.search(r"^source:\s*(\S+)\s*$", tete, re.M)
        if found:
            index.setdefault(found.group(1).rstrip("/"), slug_quartz(fichier))
    return index


# --------------------------------------------------------------------------- #
# Slugs et ancres, a l'identique de Quartz
# --------------------------------------------------------------------------- #

def slug_quartz(fichier: pathlib.Path) -> str:
    """Le slug d'un fichier de content/, selon sluggify() de quartz/util/path.ts.

    Quartz ne met pas en minuscules et ne touche pas aux accents : il remplace
    les espaces par des tirets, `&` par `-and-`, `%` par `-percent`, et supprime
    `?` et `#`. Reproduire la regle exactement, sinon les liens tombent a cote.
    """
    relatif = fichier.relative_to(CONTENU).with_suffix("")
    segments = []
    for segment in relatif.parts:
        segment = re.sub(r"\s", "-", segment)
        segment = segment.replace("&", "-and-").replace("%", "-percent")
        segment = segment.replace("?", "").replace("#", "")
        segments.append(segment)
    slug = "/".join(segments)
    return slug[: -len("_index")] + "index" if slug.endswith("_index") else slug


def ancre(texte: str) -> str:
    """L'ancre d'un titre, selon github-slugger, que Quartz utilise pour son sommaire.

    Minuscules, ponctuation supprimee, espaces en tirets, accents conserves.
    """
    texte = texte.strip().lower()
    garde = []
    for car in texte:
        categorie = unicodedata.category(car)
        if categorie[0] in "LMN" or car in "-_":
            garde.append(car)
        elif car.isspace():
            garde.append(" ")
    return "".join(garde).replace(" ", "-")


def titres_de(chemin: pathlib.Path) -> set[str]:
    """Les ancres des titres d'une note, pour savoir si une cible #ancre existe."""
    if not chemin.is_file():
        return set()
    return {ancre(m) for m in re.findall(r"^#{1,6}\s+(.+?)\s*$", chemin.read_text(encoding="utf-8"), re.M)}


# --------------------------------------------------------------------------- #
# Ou pointe un noeud
# --------------------------------------------------------------------------- #

class Resolveur:
    """Decide de la cible d'un noeud et dit si elle existe deja."""

    def __init__(self, slug: str, parcours: str, correspondances: dict[str, str]):
        self.parcours = parcours
        self.correspondances = correspondances
        self.registre = slugs_du_registre()
        self.sources = index_des_sources()
        page = CONTENU / f"{parcours}.md"
        if not page.is_file():
            page = CONTENU / parcours / "index.md"
        self.ancres_parcours = titres_de(page)
        self.parcours_existe = page.is_file()
        self.hors_registre: list[str] = []

    def pour(self, noeud: dict) -> tuple[str | None, bool]:
        """(href, la cible existe-t-elle). href None = noeud non cliquable."""
        libelle = (noeud.get("data") or {}).get("label") or ""
        type_ = noeud.get("type")

        if type_ == "button":
            url = (noeud.get("data") or {}).get("href")
            if not url:
                return None, False
            locale = self.sources.get(url.rstrip("/")) or self.sources.get(url.split("?")[0].rstrip("/"))
            if locale:
                return locale, True
            return url, True  # l'amont existe, par construction

        if type_ not in CLIQUABLES:
            return None, False

        explicite = self.correspondances.get(libelle)
        if explicite:
            if explicite.startswith("#"):
                cle = explicite[1:]
                return f"{self.parcours}#{cle}", self.parcours_existe and cle in self.ancres_parcours
            if "/" in explicite:
                return explicite, (CONTENU / f"{explicite}.md").is_file()
            if explicite not in self.registre:
                self.hors_registre.append(explicite)
            return f"notions/{explicite}", (CONTENU / "notions" / f"{explicite}.md").is_file()

        cle = ancre(libelle)
        return f"{self.parcours}#{cle}", self.parcours_existe and cle in self.ancres_parcours


# --------------------------------------------------------------------------- #
# Dessin
# --------------------------------------------------------------------------- #

def echapper(texte: str) -> str:
    return (texte.replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def decouper(texte: str, largeur: float, police: float) -> list[str]:
    """Coupe un libelle en lignes qui tiennent dans la boite. Glouton, donc stable."""
    par_ligne = max(1, int(largeur / (police * LARGEUR_CAR)))
    lignes: list[str] = []
    courante = ""
    for mot in texte.split():
        essai = f"{courante} {mot}".strip()
        if len(essai) <= par_ligne or not courante:
            courante = essai
        else:
            lignes.append(courante)
            courante = mot
    if courante:
        lignes.append(courante)
    return lignes


def boite(noeud: dict) -> tuple[float, float, float, float]:
    mesure = noeud.get("measured") or {}
    style = noeud.get("style") or {}
    x = noeud["position"]["x"]
    y = noeud["position"]["y"]
    w = mesure.get("width") or noeud.get("width") or style.get("width") or 200
    h = mesure.get("height") or noeud.get("height") or style.get("height") or 49
    return float(x), float(y), float(w), float(h)


def point_d_accroche(noeud: dict, poignee: str | None) -> tuple[float, float]:
    """La lettre de la poignee donne le cote : w haut, x bas, y gauche, z droite."""
    x, y, w, h = boite(noeud)
    cote = (poignee or "x")[0]
    return {
        "w": (x + w / 2, y),
        "x": (x + w / 2, y + h),
        "y": (x, y + h / 2),
        "z": (x + w, y + h / 2),
    }.get(cote, (x + w / 2, y + h / 2))


def chemin_arete(depart: tuple[float, float], arrivee: tuple[float, float],
                 cote_depart: str, cote_arrivee: str) -> str:
    """Une bezier qui sort et entre perpendiculairement au bord, comme roadmap.sh."""
    x1, y1 = depart
    x2, y2 = arrivee
    ecart = max(20.0, min(90.0, (abs(x2 - x1) + abs(y2 - y1)) / 3))
    normales = {"w": (0, -1), "x": (0, 1), "y": (-1, 0), "z": (1, 0)}
    dx1, dy1 = normales.get(cote_depart[0], (0, 1))
    dx2, dy2 = normales.get(cote_arrivee[0], (0, -1))
    c1 = (x1 + dx1 * ecart, y1 + dy1 * ecart)
    c2 = (x2 + dx2 * ecart, y2 + dy2 * ecart)
    return (f"M {x1:.1f} {y1:.1f} C {c1[0]:.1f} {c1[1]:.1f} "
            f"{c2[0]:.1f} {c2[1]:.1f} {x2:.1f} {y2:.1f}")


STYLE_SVG = """<style>
.carte-roadmap { display:block; font-family:var(--bodyFont, system-ui, sans-serif); }
.carte-roadmap .fond { fill:var(--light, #faf8f8); }
.carte-roadmap .arete { fill:none; stroke:var(--gray, #b8b8b8); stroke-width:2; stroke-linecap:round; }
.carte-roadmap .arete.pointille { stroke-dasharray:1 7; }
.carte-roadmap .filet { fill:none; stroke:var(--gray, #b8b8b8); stroke-width:3; stroke-linecap:round; }
.carte-roadmap .filet.pointille { stroke-dasharray:1 7; }
.carte-roadmap .cadre { fill:none; stroke:var(--lightgray, #e5e5e5); stroke-width:1.5; }
.carte-roadmap text { fill:var(--darkgray, #4e4e4e); }
.carte-roadmap .titre text { fill:var(--dark, #2b2b2b); font-weight:700; }
.carte-roadmap .section text { fill:var(--dark, #2b2b2b); font-weight:600; }
.carte-roadmap .section rect { fill:var(--highlight, rgba(143,159,169,.15)); stroke:none; }
.carte-roadmap .paragraphe text { fill:var(--gray, #b8b8b8); }
.carte-roadmap .noeud rect { fill:var(--lightgray, #e5e5e5); stroke:var(--darkgray, #4e4e4e); stroke-width:1.5; }
.carte-roadmap .noeud text { fill:var(--dark, #2b2b2b); font-weight:600; }
.carte-roadmap .sous-noeud rect { fill:var(--light, #faf8f8); stroke:var(--gray, #b8b8b8); stroke-width:1.5; }
.carte-roadmap .sous-noeud text { fill:var(--darkgray, #4e4e4e); font-weight:400; }
.carte-roadmap .renvoi rect { fill:none; stroke:var(--secondary, #284b63); stroke-width:1.5; }
.carte-roadmap .groupe rect { fill:none; stroke:var(--lightgray, #e5e5e5); stroke-width:1.5; }
.carte-roadmap .ressource rect { fill:none; stroke:var(--tertiary, #84a59d); stroke-width:1.5; }
.carte-roadmap .ressource text { fill:var(--gray, #b8b8b8); }
.carte-roadmap .tache text { fill:var(--darkgray, #4e4e4e); font-weight:600; }
.carte-roadmap .groupe > text { font-weight:600; }
.carte-roadmap .lien-groupe text { fill:var(--secondary, #284b63); }
.carte-roadmap .lien-groupe:hover text { text-decoration:underline; }
.carte-roadmap .renvoi text { fill:var(--secondary, #284b63); font-weight:500; }
.carte-roadmap a { text-decoration:none; }
.carte-roadmap a:hover rect { stroke:var(--secondary, #284b63); stroke-width:2.5; }
.carte-roadmap a:hover text { fill:var(--secondary, #284b63); }
.carte-roadmap .a-ecrire rect { stroke-dasharray:5 4; }
.carte-roadmap .a-ecrire text { font-style:italic; fill:var(--gray, #b8b8b8); }
.carte-roadmap a .external-icon { display:none; }
</style>"""


def dessiner_noeud(noeud: dict, href: str | None, existe: bool) -> str:
    x, y, w, h = boite(noeud)
    data = noeud.get("data") or {}
    style = data.get("style") or {}
    libelle = data.get("label") or ""
    type_ = noeud["type"]
    police = float(style.get("fontSize") or 17)

    if type_ in FILETS:
        if type_ == "vertical":
            d = f"M {x + w / 2:.1f} {y:.1f} L {x + w / 2:.1f} {y + h:.1f}"
        else:
            d = f"M {x:.1f} {y + h / 2:.1f} L {x + w:.1f} {y + h / 2:.1f}"
        pointille = "" if (style.get("strokeDasharray") or "") == "0" else " pointille"
        return f'<path class="filet{pointille}" d="{d}"/>'

    if type_ in CADRES:
        # Un cadre de regroupement : une boite vide posee derriere ses noeuds.
        return (f'<rect class="cadre" x="{x:.1f}" y="{y:.1f}" '
                f'width="{w:.1f}" height="{h:.1f}" rx="8"/>')

    classes = {
        "topic": "noeud", "subtopic": "sous-noeud", "button": "renvoi",
        "resourceButton": "ressource", "todo": "tache",
        "linksgroup": "groupe", "title": "titre", "label": "section",
        "paragraph": "paragraphe",
    }.get(type_, "sous-noeud")
    if href and not existe:
        classes += " a-ecrire"

    # Un conteneur -- paragraphe d'ambiance, groupe de renvois -- est bien plus
    # haut que son texte et abrite d'autres noeuds. Son libelle se cale en haut,
    # sinon il se centre au milieu de la boite et passe sous ce qu'elle contient.
    conteneur = type_ in ("paragraph", "linksgroup")
    aligne = style.get("textAlign") or ("left" if type_ == "paragraph" else "center")
    ancre_texte = {"left": "start", "right": "end"}.get(aligne, "middle")
    tx = {"start": x + 10, "end": x + w - 10}.get(ancre_texte, x + w / 2)

    lignes = decouper(libelle, w - 20, police)
    hauteur_ligne = police * 1.25
    if conteneur:
        depart = y + 10 + police * 0.85
    else:
        depart = y + h / 2 - (len(lignes) - 1) * hauteur_ligne / 2 + police * 0.35

    corps = []
    if type_ not in ("title", "paragraph", "todo"):
        corps.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="5"/>')
    for i, ligne in enumerate(lignes):
        corps.append(f'<text x="{tx:.1f}" y="{depart + i * hauteur_ligne:.1f}" '
                     f'text-anchor="{ancre_texte}" font-size="{police:.0f}">{echapper(ligne)}</text>')

    # Un groupe de renvois porte sa liste de liens dans ses donnees. La laisser
    # de cote donnerait une boite vide avec un titre.
    if type_ == "linksgroup":
        ligne_y = depart + len(lignes) * hauteur_ligne + 6
        for lien in data.get("links") or []:
            url = lien.get("url") or ""
            texte = lien.get("label") or url
            if not url or ligne_y > y + h - 4:
                continue
            corps.append(f'<a href="{echapper(url)}" class="lien-groupe">'
                         f'<text x="{x + 12:.1f}" y="{ligne_y:.1f}" text-anchor="start" '
                         f'font-size="{police * 0.85:.0f}">{echapper(texte)}</text></a>')
            ligne_y += police * 1.25

    interieur = "".join(corps)
    if href:
        titre = libelle if existe else f"{libelle} — page à écrire"
        return (f'<a href="{echapper(href)}" class="{classes}">'
                f'<title>{echapper(titre)}</title>{interieur}</a>')
    return f'<g class="{classes}">{interieur}</g>'


def dessiner(capture: dict, resolveur: Resolveur) -> tuple[str, list[tuple[str, str, bool]]]:
    noeuds = capture["nodes"]
    par_id = {n["id"]: n for n in noeuds}

    xs, ys = [], []
    for n in noeuds:
        x, y, w, h = boite(n)
        xs += [x, x + w]
        ys += [y, y + h]
    x0, y0 = min(xs) - MARGE, min(ys) - MARGE
    largeur = max(xs) - min(xs) + 2 * MARGE
    hauteur = max(ys) - min(ys) + 2 * MARGE

    morceaux = [f'<rect class="fond" x="{x0:.1f}" y="{y0:.1f}" '
                f'width="{largeur:.1f}" height="{hauteur:.1f}"/>']

    # Un cadre de regroupement se pose derriere tout le reste, sinon il masque
    # les noeuds qu'il entoure.
    for noeud in noeuds:
        if noeud.get("type") in CADRES:
            morceaux.append(dessiner_noeud(noeud, None, False))

    for arete in capture.get("edges", []):
        source, cible = par_id.get(arete["source"]), par_id.get(arete["target"])
        if not source or not cible:
            continue
        ps = arete.get("sourceHandle") or "x"
        pc = arete.get("targetHandle") or "w"
        d = chemin_arete(point_d_accroche(source, ps), point_d_accroche(cible, pc), ps, pc)
        style = " pointille" if (arete.get("data") or {}).get("edgeStyle") == "dashed" else ""
        morceaux.append(f'<path class="arete{style}" d="{d}"/>')

    journal: list[tuple[str, str, bool]] = []
    for noeud in noeuds:
        if noeud.get("type") in CADRES:
            continue
        href, existe = resolveur.pour(noeud)
        morceaux.append(dessiner_noeud(noeud, href, existe))
        if href:
            journal.append(((noeud.get("data") or {}).get("label") or "", href, existe))

    svg = (f'<svg class="carte-roadmap" xmlns="http://www.w3.org/2000/svg" '
           f'viewBox="{x0:.1f} {y0:.1f} {largeur:.1f} {hauteur:.1f}" '
           f'width="{largeur:.0f}" height="{hauteur:.0f}" role="img" '
           f'aria-label="Carte de la roadmap">{STYLE_SVG}{"".join(morceaux)}</svg>')
    return svg, journal


# --------------------------------------------------------------------------- #
# La meme carte en liste : la sortie de secours
# --------------------------------------------------------------------------- #

def en_liste(extrait: dict, resolveur: Resolveur, par_libelle: dict[str, dict]) -> str:
    blocs = []
    for section in extrait.get("sections", []):
        blocs.append(f'<p><strong>{echapper(section["heading"])}</strong></p><ul>')
        for noeud in section.get("nodes", []):
            libelle = noeud["label"]
            source = par_libelle.get(libelle) or {"type": noeud["type"], "data": {"label": libelle}}
            href, existe = resolveur.pour(source)
            marque = "" if existe else ' <em>(à écrire)</em>'
            if href:
                blocs.append(f'<li><a href="{echapper(href)}">{echapper(libelle)}</a>{marque}</li>')
            else:
                blocs.append(f"<li>{echapper(libelle)}</li>")
        blocs.append("</ul>")
    return ("<details class=\"carte-en-liste\"><summary>La même carte en liste</summary>"
            + "".join(blocs) + "</details>")


# --------------------------------------------------------------------------- #

def rendre(slug: str, parcours: str, liens: dict[str, dict[str, str]]) -> tuple[str, Resolveur, list]:
    capture_path = derniere_capture(slug)
    capture = charger(capture_path)
    extrait = charger(EXTRACT / f"{slug}.json")

    correspondances = dict(CORRESPONDANCES.get(slug, {}))
    correspondances.update(liens.get(slug, {}))
    resolveur = Resolveur(slug, parcours, correspondances)

    svg, journal = dessiner(capture, resolveur)
    par_libelle = {(n.get("data") or {}).get("label"): n for n in capture["nodes"]}
    liste = en_liste(extrait, resolveur, par_libelle)

    titre = extrait.get("title") or slug
    page = "\n".join([
        "---",
        f"title: Carte — {titre}",
        "tags: [carte, roadmap, genere]",
        f"date: {capture_path.stem}",
        "statut: actif",
        f"source: https://roadmap.sh/{slug}",
        "---",
        "",
        "> [!abstract] La disposition exacte de la roadmap amont, chaque nœud cliquable.",
        "> Les nœuds en pointillé mènent à une page qui reste à écrire.",
        "",
        f"**Source** : roadmap.sh/{slug}, capturée le {capture_path.stem} · "
        f"**Rendu** : `tools/roadmap_render.py`",
        "",
        "> [!warning] Fichier généré",
        "> Ne pas éditer à la main : regénérer avec "
        f"`python3 tools/roadmap_render.py {slug}`.",
        "",
        '<div class="carte-cadre">' + svg + "</div>",
        "",
        liste,
        "",
    ])
    return page, resolveur, journal


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("slug", help="le slug de la roadmap, ex. forward-deployed-engineer")
    parser.add_argument("--parcours", help="slug Quartz de la note de parcours (defaut parcours/<slug>)")
    parser.add_argument("--sortie", help="fichier a ecrire (defaut : stdout)")
    parser.add_argument("--liens", help="JSON de correspondances libelle -> slug de notion")
    parser.add_argument("--verifier", action="store_true",
                        help="ne rien ecrire, lister les cibles et leur etat")
    args = parser.parse_args()

    parcours = args.parcours or f"parcours/{args.slug}"
    liens = charger(pathlib.Path(args.liens)) if args.liens else {}

    page, resolveur, journal = rendre(args.slug, parcours, liens)

    if args.verifier:
        manquantes = 0
        for libelle, href, existe in journal:
            etat = "ok      " if existe else "a ecrire"
            manquantes += 0 if existe else 1
            print(f"{etat}  {libelle:34.34s} -> {href}")
        print(f"\n{len(journal)} noeuds cliquables, {manquantes} cibles a ecrire")
        for notion in sorted(set(resolveur.hors_registre)):
            print(f"HORS REGISTRE  notions/{notion}", file=sys.stderr)
        return 0

    if args.sortie:
        chemin = pathlib.Path(args.sortie)
        chemin.parent.mkdir(parents=True, exist_ok=True)
        chemin.write_text(page, encoding="utf-8")
        print(f"{chemin}  {len(journal)} noeuds cliquables")
    else:
        sys.stdout.write(page)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
