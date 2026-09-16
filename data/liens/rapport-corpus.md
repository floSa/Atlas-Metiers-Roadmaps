# Rapport de verification des liens

> Produit par `tools/verifier_liens.py` le 2026-09-16.
> Perimetre : **corpus redige (content/)** — 241 URL uniques, 241 verifiees.
> Ce rapport ne modifie rien. Il liste ce qu'il y a a decider.

## Vue d'ensemble

| Statut | Nombre | Part | Ce que ca veut dire |
|---|---:|---:|---|
| `introuvable` | 3 | 1.2 % | La page a disparu. A remplacer par un equivalent verifie, ou a retirer. |
| `redirection` | 16 | 6.6 % | Atteignable, mais l'URL citee n'est plus l'URL reelle. A mettre a jour. |
| `delai` | 1 | 0.4 % | Aucune reponse dans le temps imparti. A reverifier. |
| `bloque` | 11 | 4.6 % | Le serveur refuse les robots. Ne veut pas dire mort : verification humaine requise. |
| `ok` | 210 | 87.1 % | Atteignable a l'URL citee. |

## introuvable — 3

La page a disparu. A remplacer par un equivalent verifie, ou a retirer.

- `https://huntr.com/guidelines` `404`
  cite par : content/parcours/ai-red-teaming.md
- `https://owasp.org/www-project-api-security/` `404`
  cite par : content/parcours/ai-red-teaming.md
- `https://support.bolt.new/building/quickstart` `404`
  cite par : content/parcours/ai-product-builder.md

## redirection — 16

Atteignable, mais l'URL citee n'est plus l'URL reelle. A mettre a jour.

- `http://montecarlodata.com/blog-data-lineage/` `200` — -> https://montecarlo.ai/blog-data-lineage
  cite par : content/parcours/bi-analyst.md
- `https://community.tableau.com/s/` `200` — -> https://trailhead.salesforce.com/fr/trailblazer-community/neighborhoods/tableau
  cite par : content/parcours/bi-analyst.md
- `https://developers.openai.com/codex` `200` — -> https://learn.chatgpt.com/docs
  cite par : content/parcours/ai-product-builder.md
- `https://docs.github.com/en/get-started/quickstart` `200` — -> https://docs.github.com/en/get-started/start-your-journey
  cite par : content/parcours/ai-product-builder.md
- `https://docs.replit.com/getting-started/intro-replit` `200` — -> https://docs.replit.com/welcome (page generique : la ressource a probablement disparu)
  cite par : content/parcours/ai-product-builder.md
- `https://gandalf.lakera.ai/` `200` — -> https://play.lakera.ai/agent-breaker
  cite par : content/parcours/ai-red-teaming.md
- `https://mode.com/sql-tutorial/sql-performance-tuning` `200` — -> https://www.thoughtspot.com/sql-tutorial/sql-performance-tuning
  cite par : content/parcours/bi-analyst.md
- `https://mode.com/sql-tutorial/sql-window-functions` `200` — -> https://www.thoughtspot.com/sql-tutorial/sql-window-functions
  cite par : content/parcours/bi-analyst.md
- `https://modelcontextprotocol.io` `200` — -> https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro
  cite par : content/parcours/forward-deployed-engineer/industrialisation.md
- `https://modelcontextprotocol.io/` `200` — -> https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro
  cite par : content/ressources/ia-generative.md, content/ressources/index.md
- `https://modelcontextprotocol.io/docs/develop/build-server` `200` — -> https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server
  cite par : content/ressources/ia-generative.md
- `https://owasp.org/www-community/Threat_Modeling` `200` — -> https://community.owasp.org/Threat_Modeling
  cite par : content/parcours/ai-red-teaming.md
- `https://publications.europa.eu/resource/celex/32024R1689` `200` — -> http://publications.europa.eu/resource/cellar/dc8116a1-3fe6-11ef-865a-01aa75ed71a1.0009.03/DOC_1
  cite par : content/ressources/conseil-et-terrain.md, content/ressources/ia-generative.md, content/ressources/index.md
- `https://research.nccgroup.com/2023/12/01/mitigating-prompt-injection-attacks/` `200` — -> https://www.nccgroup.com/research/ (page generique : la ressource a probablement disparu)
  cite par : content/parcours/ai-red-teaming.md
- `https://trymata.com/blog/what-is-user-testing/` `200` — -> https://ux.questionpro.com/ (page generique : la ressource a probablement disparu)
  cite par : content/parcours/ai-product-builder.md
- `https://www.highcharts.com/blog/tutorials/10-guidelines-for-dataviz-accessibility/` `200` — -> https://www.highcharts.com/blog/best-practices/10-guidelines-for-dataviz-accessibility/
  cite par : content/parcours/bi-analyst.md

## delai — 1

Aucune reponse dans le temps imparti. A reverifier.

- `https://hevodata.com/learn/understanding-cohort-analysis-a-guide/` — pas de reponse
  cite par : content/parcours/bi-analyst.md

## bloque — 11

Le serveur refuse les robots. Ne veut pas dire mort : verification humaine requise.

- `https://community.fabric.microsoft.com/t5/Power-BI-forums/ct-p/powerbi` `403` — a verifier a la main dans un navigateur
  cite par : content/parcours/bi-analyst.md
- `https://dev.mysql.com/doc/` `403` — a verifier a la main dans un navigateur
  cite par : content/parcours/ai-product-builder.md
- `https://docs.getdbt.com/docs/build/documentation` `200` — interstitiel anti-robot, a verifier a la main
  cite par : content/parcours/bi-analyst.md, content/ressources/donnees.md
- `https://dplyr.tidyverse.org/` `200` — interstitiel anti-robot, a verifier a la main
  cite par : content/ressources/donnees.md
- `https://eur-lex.europa.eu/eli/reg/2024/1689/oj` `202` — reponse vide derriere un controle navigateur, a verifier a la main
  cite par : content/parcours/forward-deployed-engineer/industrialisation.md
- `https://ggplot2.tidyverse.org/` `200` — interstitiel anti-robot, a verifier a la main
  cite par : content/ressources/donnees.md
- `https://huggingface.co/learn/agents-course/en/unit1/tools` `200` — interstitiel anti-robot, a verifier a la main
  cite par : content/ressources/ia-generative.md, content/ressources/index.md
- `https://huggingface.co/learn/mcp-course/en/unit0/introduction` `200` — interstitiel anti-robot, a verifier a la main
  cite par : content/ressources/ia-generative.md
- `https://medium.com/free-code-camp/how-to-effectively-scope-your-software-projects-from-planning-to-execution-e96cbcac54b9` `403` — a verifier a la main dans un navigateur
  cite par : content/parcours/forward-deployed-engineer/arbitrage-technologique.md
- `https://uxdesign.cc/how-to-scope-your-ai-product-5b9885ef3851` `403` — a verifier a la main dans un navigateur
  cite par : content/parcours/ai-product-builder.md
- `https://www.iso.org/standard/81230.html` `403` — a verifier a la main dans un navigateur
  cite par : content/parcours/ai-red-teaming.md, content/ressources/ia-generative.md, content/ressources/index.md

## ok — 210

Non detaillees : la liste est dans `data/liens/cache.json`.
