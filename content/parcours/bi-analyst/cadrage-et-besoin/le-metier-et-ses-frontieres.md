---
title: Le métier et ses frontières
---

Niveau attendu : **référence**. Énoncer ce que ce poste livre en propre — un accord sur les chiffres — et ce qui revient au Data Analyst ou au Data Engineer est la première chose qu'on attend de lui en réunion.

Le seul rôle de la data dont le livrable est *un accord sur les chiffres* : un modèle, des définitions, des tableaux de bord que plusieurs services acceptent comme référence commune. Un Data Analyst produit une réponse ; un BI Analyst produit un socle qui produira des réponses sans lui.

```mermaid
flowchart TD
  SQ["SQL<br/>le niveau réel attendu : fenêtrage, CTE, plans"]
  OD["Outils décisionnels<br/>un maîtrisé en profondeur, pas trois survolés"]
  TB["Tableur<br/>le poste de travail qu'on n'évite pas"]
  ST["Statistiques descriptives<br/>assez pour ne pas publier une moyenne trompeuse"]
  GP["Gestion des parties prenantes<br/>la sixième responsabilité, absente de l'amont"]

  click SQ "/notions/sql"
  click OD "/notions/outils-decisionnels"
  click TB "/notions/tableur"
  click ST "/notions/statistiques-descriptives"
  click GP "/notions/gestion-parties-prenantes"
```

## Ce qu'il faut savoir faire

- Situer sa frontière avec le Data Engineer sur l'objet manipulé : lui garantit que la donnée **arrive** — fraîche, complète, à l'heure — et raisonne en pipelines et en SLA ; le BI Analyst garantit qu'elle **veut dire quelque chose**, et raisonne en grain, en dimension conforme et en définition métier. Les deux se rencontrent sur les tables de l'entrepôt.
- Situer sa frontière avec le Data Analyst sur la nature de la question. « Combien » demande un modèle partagé et se mesure en réutilisation ; « pourquoi » demande une exploration et se mesure en délai de réponse.
- Situer sa frontière avec le Data Scientist sur le droit à l'approximation. Le second prédit et assume une incertitude quantifiée ; le premier restitue le réalisé, où un écart de 2 % sur un chiffre d'affaires publié est un incident, pas un intervalle de confiance.
- Reconnaître la responsabilité que l'amont oublie et qui est la plus lourde : **arbitrer une définition**. Décider que « client actif » veut dire ceci et pas cela, et le faire tenir dans le temps.
- Lire une offre d'emploi par son périmètre et non par son intitulé. BI Analyst, BI Developer, Analytics Engineer et Data Analyst senior recouvrent souvent le même poste ; l'indice fiable est la mention d'un dépôt et d'une couche de transformation versionnée.
- Décliner une demande ponctuelle en chiffrant ce qu'elle coûte, et le comparer au coût du modèle qui l'absorberait — c'est la seule sortie du rôle de guichet à rapports.

## Les notions mobilisées

- [[notions/sql]] — l'angle BI est que la requête n'est pas une réponse mais une définition, écrite une fois et exécutée dix mille fois.
- [[notions/outils-decisionnels]] — un seul outil connu jusqu'à ses droits d'accès et ses modes de rafraîchissement vaut trois démonstrations.
- [[notions/tableur]] — il reste le poste de travail du métier, et la moitié des consultations finissent par un export.
- [[notions/statistiques-descriptives]] — assez de dispersion pour ne pas publier une moyenne qui cache 20 % de cas extrêmes.
- [[notions/gestion-parties-prenantes]] — en BI, celui qui pilote veut une définition stable et celui qui est évalué veut celle qui l'avantage.

> [!tip] Le titre qui décrit le mieux le poste
> **Analytics engineer** : le BI Analyst qui a pris les outils du développeur — dépôt, revue de code, tests, documentation générée, environnements séparés — pour construire le modèle de l'entrepôt. Ce n'est pas un intitulé de la roadmap amont, c'est celui qui décrit le cœur du travail depuis cinq ans.

> [!warning] Piège
> Se laisser réduire au guichet de rapports. Celui qui accepte toutes les demandes ponctuelles n'a jamais le temps de construire le modèle qui les rendrait inutiles, et se retrouve au bout de deux ans à maintenir quatre cents rapports dont il ne sait plus lesquels sont lus. La sortie est politique, pas technique.

## Pour apprendre

- [Roadmap BI Analyst](https://roadmap.sh/bi-analyst) — l'arbre amont, utile pour voir ce que le marché attend et ce qu'il délègue ailleurs.
- [Roadmap Data Engineer](https://roadmap.sh/data-engineer) — la frontière amont, à parcourir pour savoir où s'arrête sa propre responsabilité.
- [What is a Data Warehouse? — Google Cloud](https://cloud.google.com/learn/what-is-a-data-warehouse) — la présentation la plus sobre de l'objet central du métier, sans argumentaire produit.
- [What is dbt](https://www.getdbt.com/product/what-is-dbt) — l'outil qui a fait basculer le poste vers l'analytics engineering ; à lire comme un manifeste de pratiques.
