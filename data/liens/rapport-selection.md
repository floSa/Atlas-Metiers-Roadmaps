# Rapport de verification des liens

> Produit par `tools/verifier_liens.py` le 2026-09-16.
> Perimetre : **verification ponctuelle** — 171 URL uniques, 171 verifiees.
> Ce rapport ne modifie rien. Il liste ce qu'il y a a decider.

## Vue d'ensemble

| Statut | Nombre | Part | Ce que ca veut dire |
|---|---:|---:|---|
| `redirection` | 3 | 1.8 % | Atteignable, mais l'URL citee n'est plus l'URL reelle. A mettre a jour. |
| `bloque` | 6 | 3.5 % | Le serveur refuse les robots. Ne veut pas dire mort : verification humaine requise. |
| `ok` | 162 | 94.7 % | Atteignable a l'URL citee. |

## redirection — 3

Atteignable, mais l'URL citee n'est plus l'URL reelle. A mettre a jour.

- `https://modelcontextprotocol.io/` `200` — -> https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro
  cite par : --url
- `https://modelcontextprotocol.io/docs/develop/build-server` `200` — -> https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server
  cite par : --url
- `https://publications.europa.eu/resource/celex/32024R1689` `200` — -> http://publications.europa.eu/resource/cellar/dc8116a1-3fe6-11ef-865a-01aa75ed71a1.0009.03/DOC_1
  cite par : --url

## bloque — 6

Le serveur refuse les robots. Ne veut pas dire mort : verification humaine requise.

- `https://docs.getdbt.com/docs/build/documentation` `200` — interstitiel anti-robot, a verifier a la main
  cite par : --url
- `https://dplyr.tidyverse.org/` `200` — interstitiel anti-robot, a verifier a la main
  cite par : --url
- `https://ggplot2.tidyverse.org/` `200` — interstitiel anti-robot, a verifier a la main
  cite par : --url
- `https://huggingface.co/learn/agents-course/en/unit1/tools` `200` — interstitiel anti-robot, a verifier a la main
  cite par : --url
- `https://huggingface.co/learn/mcp-course/en/unit0/introduction` `200` — interstitiel anti-robot, a verifier a la main
  cite par : --url
- `https://www.iso.org/standard/81230.html` `403` — a verifier a la main dans un navigateur
  cite par : --url

## ok — 162

Non detaillees : la liste est dans `data/liens/cache.json`.
