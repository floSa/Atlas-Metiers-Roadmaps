# Rapport de verification des liens

> Produit par `tools/verifier_liens.py` le 2026-09-16.
> Perimetre : **selection commentee (content/ressources/)** — 201 URL uniques, 201 verifiees.
> Ce rapport ne modifie rien. Il liste ce qu'il y a a decider.

## Vue d'ensemble

| Statut | Nombre | Part | Ce que ca veut dire |
|---|---:|---:|---|
| `redirection` | 3 | 1.5 % | Atteignable, mais l'URL citee n'est plus l'URL reelle. A mettre a jour. |
| `bloque` | 9 | 4.5 % | Le serveur refuse les robots. Ne veut pas dire mort : verification humaine requise. |
| `ok` | 189 | 94.0 % | Atteignable a l'URL citee. |

## redirection — 3

Atteignable, mais l'URL citee n'est plus l'URL reelle. A mettre a jour.

- `https://modelcontextprotocol.io/` `200` — -> https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro
  cite par : content/ressources/ia-generative.md, content/ressources/index.md
- `https://modelcontextprotocol.io/docs/develop/build-server` `200` — -> https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server
  cite par : content/ressources/ia-generative.md
- `https://publications.europa.eu/resource/celex/32024R1689` `200` — -> http://publications.europa.eu/resource/cellar/dc8116a1-3fe6-11ef-865a-01aa75ed71a1.0009.03/DOC_1
  cite par : content/ressources/conseil-et-terrain.md, content/ressources/ia-generative.md, content/ressources/index.md

## bloque — 9

Le serveur refuse les robots. Ne veut pas dire mort : verification humaine requise.

- `https://dev.mysql.com/doc/` `403` — a verifier a la main dans un navigateur
  cite par : content/ressources/donnees.md
- `https://docs.getdbt.com/docs/build/documentation` `200` — interstitiel anti-robot, a verifier a la main
  cite par : content/ressources/donnees.md
- `https://dplyr.tidyverse.org/` `200` — interstitiel anti-robot, a verifier a la main
  cite par : content/ressources/donnees.md
- `https://ggplot2.tidyverse.org/` `200` — interstitiel anti-robot, a verifier a la main
  cite par : content/ressources/donnees.md
- `https://huggingface.co/docs/hub/en/index` `200` — interstitiel anti-robot, a verifier a la main
  cite par : content/ressources/ia-generative.md
- `https://huggingface.co/learn/agents-course/en/unit1/tools` `200` — interstitiel anti-robot, a verifier a la main
  cite par : content/ressources/ia-generative.md, content/ressources/index.md
- `https://huggingface.co/learn/mcp-course/en/unit0/introduction` `200` — interstitiel anti-robot, a verifier a la main
  cite par : content/ressources/ia-generative.md
- `https://huggingface.co/models` `200` — interstitiel anti-robot, a verifier a la main
  cite par : content/ressources/ia-generative.md
- `https://www.iso.org/standard/81230.html` `403` — a verifier a la main dans un navigateur
  cite par : content/ressources/ia-generative.md, content/ressources/index.md

## ok — 189

Non detaillees : la liste est dans `data/liens/cache.json`.
