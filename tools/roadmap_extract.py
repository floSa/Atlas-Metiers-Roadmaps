#!/usr/bin/env python3
"""Extraction reproductible d'une roadmap roadmap.sh.

Deux sources, combinees :
  - l'API officielle  https://roadmap.sh/api/v1-official-roadmap/<slug>
    -> l'arbre complet : noeuds, aretes, positions (donc l'ordre visuel exact)
  - le depot de contenu github.com/nilbuild/developer-roadmap
    -> un markdown par noeud : le texte pedagogique et les ressources typees

Produit, pour chaque slug :
  data/raw/<slug>/<date>.json   la capture brute, versionnee, rejouable
  data/extract/<slug>.md        le plan lisible : sections, noeuds, ressources
  data/extract/<slug>.json      la forme normalisee, pour les scripts

Usage :
  python3 tools/roadmap_extract.py --sync                       # clone/maj du depot amont
  python3 tools/roadmap_extract.py forward-deployed-engineer ...
  python3 tools/roadmap_extract.py --all-known
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import re
import subprocess
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
EXTRACT = ROOT / "data" / "extract"
UPSTREAM = ROOT / "data" / "_upstream"
UPSTREAM_URL = "https://github.com/nilbuild/developer-roadmap.git"
API = "https://roadmap.sh/api/v1-official-roadmap/{slug}"

# Le perimetre IA / data science retenu pour ce projet.
KNOWN = [
    # deja transposees (capture du 15 mars 2026)
    "computer-science", "ai-data-scientist", "data-engineer", "machine-learning",
    "ai-engineer", "prompt-engineering", "ai-agents", "mlops",
    # manquantes, lot en cours
    "forward-deployed-engineer", "ai-red-teaming", "ai-product-builder",
    "data-analyst", "bi-analyst",
]

# Les types de noeuds qui portent du contenu pedagogique, par opposition
# au decor (fleches, encadres, boutons vers d'autres roadmaps).
# "todo" est le type de noeud des roadmaps au format historique (ai-data-scientist).
CONTENT_TYPES = {"topic", "subtopic", "todo"}
HEADING_TYPES = {"title", "label"}

RESOURCE_RE = re.compile(r"^\s*-\s*\[@(?P<kind>[a-z]+)@(?P<title>.+?)\]\((?P<url>\S+?)\)\s*$")


def fetch_api(slug: str) -> dict:
    url = API.format(slug=slug)
    req = urllib.request.Request(url, headers={"User-Agent": "roadmaps-extract/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        payload = json.load(resp)
    if payload.get("type") == "not_found" or "nodes" not in payload:
        raise SystemExit(f"{slug} : introuvable via l'API officielle")
    return payload


def sync_upstream() -> None:
    """Clone superficiel du depot de contenu, ou mise a jour s'il existe deja."""
    if (UPSTREAM / ".git").exists():
        subprocess.run(["git", "-C", str(UPSTREAM), "fetch", "--depth", "1", "origin"], check=True)
        subprocess.run(["git", "-C", str(UPSTREAM), "reset", "--hard", "origin/master"], check=True)
    else:
        UPSTREAM.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            ["git", "clone", "--depth", "1", "--quiet", UPSTREAM_URL, str(UPSTREAM)], check=True
        )


def load_node_contents(slug: str) -> dict[str, dict]:
    """Indexe le contenu markdown par id de noeud.

    Les fichiers amont sont nommes <slug-du-noeud>@<id-du-noeud>.md ; c'est l'id
    qui fait la jointure avec l'arbre renvoye par l'API.
    """
    directory = UPSTREAM / "roadmaps" / slug / "content"
    if not directory.is_dir():
        return {}
    by_id: dict[str, dict] = {}
    for path in sorted(directory.glob("*.md")):
        if "@" not in path.stem:
            continue
        node_id = path.stem.rsplit("@", 1)[1]
        text = path.read_text(encoding="utf-8")
        body, resources = split_resources(text)
        # Le fichier amont repete son propre titre en H1 ; le plan le porte deja.
        body = re.sub(r"^#\s+.*?\n+", "", body, count=1)
        by_id[node_id] = {"body": body, "resources": resources, "file": path.name}
    return by_id


def split_resources(text: str) -> tuple[str, list[dict]]:
    """Separe la prose des liens de ressources typees (@article@, @video@, ...)."""
    body_lines, resources = [], []
    for line in text.splitlines():
        match = RESOURCE_RE.match(line)
        if match:
            resources.append(match.groupdict())
        else:
            body_lines.append(line)
    body = re.sub(r"\n{3,}", "\n\n", "\n".join(body_lines)).strip()
    body = re.sub(r"\n*Visit the following resources to learn more:\s*$", "", body).strip()
    return body, resources


def box(node: dict) -> tuple[float, float, float, float]:
    """Boite englobante d'un noeud, en coordonnees absolues."""
    pos = node.get("positionAbsolute") or node.get("position") or {}
    x, y = pos.get("x", 0.0), pos.get("y", 0.0)
    return x, y, x + (node.get("width") or 0), y + (node.get("height") or 0)


def inside(node: dict, container: dict) -> bool:
    """Vrai si le centre du noeud tombe dans la boite du conteneur."""
    nx0, ny0, nx1, ny1 = box(node)
    cx0, cy0, cx1, cy1 = box(container)
    cx, cy = (nx0 + nx1) / 2, (ny0 + ny1) / 2
    return cx0 <= cx <= cx1 and cy0 <= cy <= cy1


def normalise(payload: dict, contents: dict[str, dict]) -> dict:
    """Reconstruit un plan ordonne a partir de la geometrie du schema.

    roadmap.sh ne stocke aucune hierarchie explicite : l'arbre n'existe qu'a
    l'ecran. Deux signaux le retablissent, par ordre de fiabilite :

      1. les noeuds de type "section" sont de vrais conteneurs, avec une boite
         englobante ; un noeud qui tombe dedans appartient a cette section, et
         le "label" qui tombe dedans lui donne son nom ;
      2. a defaut de section, on rattache chaque noeud au dernier label situe
         au-dessus de lui.

    Le point 1 est necessaire : un label est place en haut a gauche de sa bande,
    alors que les noeuds de la bande precedente peuvent descendre plus bas. Un
    simple tri par ordonnee fait donc deriver les titres d'une bande a l'autre.
    """
    def key(node):
        x0, y0, _, _ = box(node)
        return (round(y0, 1), round(x0, 1))

    nodes = payload.get("nodes", [])
    containers = sorted((n for n in nodes if n.get("type") == "section"), key=key)
    labels = [n for n in nodes if n.get("type") in HEADING_TYPES
              and ((n.get("data") or {}).get("label") or "").strip()]

    # Chaque conteneur prend le nom du label qui tombe dedans.
    named: dict[str, str] = {}
    claimed: set[str] = set()
    for container in containers:
        for label in labels:
            if label["id"] not in claimed and inside(label, container):
                named[container["id"]] = (label["data"]["label"]).strip()
                claimed.add(label["id"])
                break

    # Les labels hors conteneur restent des en-tetes de bande.
    free_labels = sorted((l for l in labels if l["id"] not in claimed), key=key)

    buckets: dict[str, dict] = {}
    order: list[str] = []

    def bucket(bid: str, heading):
        if bid not in buckets:
            buckets[bid] = {"heading": heading, "nodes": []}
            order.append(bid)
        return buckets[bid]

    for node in sorted(nodes, key=key):
        if node.get("type") not in CONTENT_TYPES:
            continue
        label_text = ((node.get("data") or {}).get("label") or "").strip()
        if not label_text:
            continue

        host = next((c for c in containers if inside(node, c)), None)
        if host is not None:
            target = bucket(host["id"], named.get(host["id"]))
        else:
            above = [l for l in free_labels if key(l) <= key(node)]
            heading_node = above[-1] if above else None
            target = bucket(heading_node["id"] if heading_node else "_racine",
                            (heading_node["data"]["label"]).strip() if heading_node else None)

        entry = {"id": node["id"], "type": node["type"], "label": label_text}
        entry.update(contents.get(node["id"], {"body": "", "resources": [], "file": None}))
        target["nodes"].append(entry)

    sections = [buckets[bid] for bid in order if buckets[bid]["nodes"]]

    # Les boutons renvoient vers d'autres roadmaps : c'est la carte des recouvrements.
    crossrefs = sorted({
        (node.get("data") or {}).get("href", "")
        for node in payload.get("nodes", [])
        if node.get("type") == "button" and (node.get("data") or {}).get("href")
    })

    return {
        "slug": payload.get("slug"),
        "title": (payload.get("title") or {}).get("page"),
        "description": payload.get("description"),
        "updatedAt": payload.get("updatedAt"),
        "capturedAt": dt.date.today().isoformat(),
        "counts": {
            "nodes": len(payload.get("nodes", [])),
            "topics": sum(len(s["nodes"]) for s in sections),
            "withContent": sum(1 for s in sections for n in s["nodes"] if n.get("body")),
            "resources": sum(len(n.get("resources", [])) for s in sections for n in s["nodes"]),
        },
        "crossrefs": crossrefs,
        "sections": sections,
    }


def render_outline(doc: dict) -> str:
    counts = doc["counts"]
    out = [
        f"# {doc['title']} — plan extrait",
        "",
        f"- **Slug** : `{doc['slug']}`",
        f"- **Description amont** : {doc['description']}",
        f"- **Derniere modification amont** : {doc['updatedAt']}",
        f"- **Capture** : {doc['capturedAt']}",
        f"- **Volume** : {counts['topics']} noeuds de contenu, "
        f"{counts['withContent']} documentes, {counts['resources']} ressources",
    ]
    if doc["crossrefs"]:
        out += ["- **Renvois vers d'autres roadmaps** : "
                + ", ".join(f"`{h}`" for h in doc["crossrefs"])]
    out += ["", "---", ""]

    for section in doc["sections"]:
        if section["heading"]:
            out += [f"## {section['heading']}", ""]
        for node in section["nodes"]:
            marker = "###" if node["type"] == "topic" else "####"
            out += [f"{marker} {node['label']}", ""]
            if node["body"]:
                out += [node["body"], ""]
            for res in node["resources"]:
                out += [f"- `@{res['kind']}` [{res['title']}]({res['url']})"]
            if node["resources"]:
                out += [""]
    return "\n".join(out).rstrip() + "\n"


def extract(slug: str) -> dict:
    payload = fetch_api(slug)
    contents = load_node_contents(slug)
    doc = normalise(payload, contents)

    raw_dir = RAW / slug
    raw_dir.mkdir(parents=True, exist_ok=True)
    (raw_dir / f"{doc['capturedAt']}.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8"
    )
    EXTRACT.mkdir(parents=True, exist_ok=True)
    (EXTRACT / f"{slug}.json").write_text(
        json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8"
    )
    (EXTRACT / f"{slug}.md").write_text(render_outline(doc), encoding="utf-8")
    return doc


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("slugs", nargs="*", help="slugs roadmap.sh a extraire")
    parser.add_argument("--sync", action="store_true", help="cloner ou mettre a jour le depot de contenu amont")
    parser.add_argument("--all-known", action="store_true", help="extraire tout le perimetre IA / data science")
    args = parser.parse_args()

    if args.sync:
        sync_upstream()
    if not UPSTREAM.is_dir():
        print("Depot amont absent : lancer d'abord --sync", file=sys.stderr)
        return 1

    slugs = KNOWN if args.all_known else args.slugs
    if not slugs:
        parser.print_help()
        return 1

    for slug in slugs:
        doc = extract(slug)
        c = doc["counts"]
        print(f"{slug:32s} {c['topics']:4d} noeuds  {c['withContent']:4d} documentes  "
              f"{c['resources']:4d} ressources  (amont {doc['updatedAt'][:10]})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
