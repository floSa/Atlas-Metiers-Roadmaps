#!/usr/bin/env python3
"""Mesure l'ecart entre une note deja redigee et l'etat courant de roadmap.sh.

On n'a pas conserve la capture HTML de mars 2026 qui a servi aux huit premieres
notes. La reference de comparaison est donc la note elle-meme : les schemas
Mermaid qu'elle contient enumerent, noeud par noeud, la roadmap telle qu'elle
etait au moment de la transposition.

Le rapport distingue trois cas :
  - AMONT SEUL   le noeud existe sur roadmap.sh et n'apparait dans aucun schema
                 -> candidat a l'ajout, c'est la mesure de l'obsolescence
  - NOTE SEULE   le noeud figure dans la note sans exister en amont
                 -> soit un "Ajout 2026" volontaire, soit un noeud retire amont
  - COUVERT      les deux concordent

Usage :
  python3 tools/roadmap_diff.py                 # tout le corpus deja redige
  python3 tools/roadmap_diff.py ai-engineer     # une roadmap
"""
from __future__ import annotations

import json
import pathlib
import re
import sys
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parent.parent
EXTRACT = ROOT / "data" / "extract"

# Les huit notes deja redigees, associees a leur slug amont.
NOTES = {
    "computer-science": "01 - Roadmap — Computer Science.md",
    "ai-data-scientist": "02 - Roadmap — AI and Data Scientist.md",
    "data-engineer": "03 - Roadmap — Data Engineer.md",
    "machine-learning": "04 - Roadmap — Machine Learning.md",
    "ai-engineer": "05 - Roadmap — AI Engineer.md",
    "prompt-engineering": "06 - Roadmap — Prompt Engineering.md",
    "ai-agents": "07 - Roadmap — AI Agents.md",
    "mlops": "08 - Roadmap — MLOps.md",
}

MERMAID_BLOCK = re.compile(r"```mermaid\n(.*?)```", re.DOTALL)
# Un libelle de noeud Mermaid : id["texte"], id("texte"), id{"texte"}...
MERMAID_LABEL = re.compile(r'[\[\(\{]+"([^"]+)"[\]\)\}]+')


def fold(text: str) -> str:
    """Normalise pour comparer : sans accents, sans ponctuation, en minuscules."""
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def note_labels(path: pathlib.Path) -> list[str]:
    """Tous les libelles de noeuds cites dans les schemas Mermaid de la note.

    Un noeud de schema regroupe souvent plusieurs noeuds amont sur une ligne
    ("Embeddings, Vector DBs, RAG") : on eclate sur les virgules et les tirets
    pour que la comparaison reste fine.
    """
    labels: list[str] = []
    for block in MERMAID_BLOCK.findall(path.read_text(encoding="utf-8")):
        for raw in MERMAID_LABEL.findall(block):
            labels.append(raw)
            for part in re.split(r"\s*[,;]\s*|\s+—\s+|\s+-\s+", raw):
                if len(part.strip()) > 2:
                    labels.append(part.strip())
    return labels


def covered(upstream: str, haystack: list[str]) -> bool:
    """Un noeud amont est couvert si son libelle apparait dans un libelle de note.

    La correspondance est inclusive dans les deux sens : la note abrege parfois
    ("RAG" pour "RAG and Dynamic Filters"), parfois elle developpe.
    """
    needle = fold(upstream)
    if not needle:
        return True
    return any(needle in h or (len(h) > 3 and h in needle) for h in haystack)


def report(slug: str) -> dict:
    doc = json.loads((EXTRACT / f"{slug}.json").read_text(encoding="utf-8"))
    path = ROOT / "content" / "roadmaps" / NOTES[slug]
    raw_labels = note_labels(path)
    folded = [fold(x) for x in raw_labels if fold(x)]

    upstream = [n["label"] for s in doc["sections"] for n in s["nodes"]]
    missing = [label for label in upstream if not covered(label, folded)]

    upstream_folded = [fold(x) for x in upstream]
    extra = sorted({
        raw for raw in raw_labels
        if fold(raw) and len(fold(raw)) > 4
        and not any(fold(raw) in u or u in fold(raw) for u in upstream_folded)
    })

    return {
        "slug": slug, "note": path.name, "upstreamUpdated": doc["updatedAt"][:10],
        "upstream": upstream, "missing": missing, "extra": extra,
    }


def main() -> int:
    slugs = sys.argv[1:] or list(NOTES)
    lines = ["# Rapport d'ecart — notes redigees vs roadmap.sh", "",
             f"Capture de reference : {json.loads((EXTRACT / 'ai-engineer.json').read_text())['capturedAt']}",
             "",
             "> La comparaison est lexicale : un noeud amont compte comme couvert si son",
             "> libelle se retrouve dans un schema de la note. Elle sous-estime donc la",
             "> couverture des roadmaps au format historique (`ai-data-scientist`), dont les",
             "> noeuds regroupent plusieurs notions sur une meme ligne. A lire comme un",
             "> signal a verifier, pas comme un verdict.",
             "", "| Note | Noeuds amont | Absents de la note | Couverture |",
             "|---|---:|---:|---:|"]
    details = []
    for slug in slugs:
        r = report(slug)
        total = len(r["upstream"]) or 1
        pct = 100 * (total - len(r["missing"])) / total
        lines.append(f"| {r['note'].replace('.md','')} | {len(r['upstream'])} | "
                     f"{len(r['missing'])} | {pct:.0f} % |")
        details += [f"\n## {r['note'].replace('.md','')}", "",
                    f"Slug `{r['slug']}` · derniere modification amont {r['upstreamUpdated']}", ""]
        if r["missing"]:
            details += [f"**{len(r['missing'])} noeuds amont absents de la note :**", ""]
            details += [f"- {m}" for m in r["missing"]] + [""]
        else:
            details += ["Aucun noeud amont manquant.", ""]
        if r["extra"]:
            details += [f"<details><summary>{len(r['extra'])} libelles de la note sans "
                        "equivalent amont (ajouts 2026 volontaires, ou noeuds retires)</summary>", ""]
            details += [f"- {e}" for e in r["extra"]] + ["", "</details>", ""]
        print(f"{r['slug']:22s} {len(r['upstream']):4d} amont  {len(r['missing']):4d} manquants  {pct:5.1f} % couvert")

    out = ROOT / "data" / "extract" / "_rapport-ecart.md"
    out.write_text("\n".join(lines + details).rstrip() + "\n", encoding="utf-8")
    print(f"\nRapport : {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
