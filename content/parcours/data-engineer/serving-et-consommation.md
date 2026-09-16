---
title: Serving et consommation
tags: [parcours, data-engineer, bi, couche-semantique, reverse-etl, rag, features]
date: 2026-09-16
statut: actif
source: https://roadmap.sh/data-engineer
---

Le moment où la donnée produit de la valeur — et où le travail du data engineer se juge : des tables documentées dont d'autres se servent sans venir demander comment les lire.

```mermaid
flowchart TD
  OD["Outils décisionnels<br/>ce qui consomme vos tables"]
  RA["RAG<br/>le corpus documentaire est un pipeline de plus"]
  VE["Embeddings et bases vectorielles<br/>l'index à maintenir frais"]
  ME["Mesure d'usage produit<br/>savoir quels rapports servent"]
  AB["A/B testing<br/>vous en fournissez la mesure"]

  click OD "/notions/outils-decisionnels"
  click RA "/notions/rag"
  click VE "/notions/embeddings-et-bases-vectorielles"
  click ME "/notions/mesure-d-usage-produit"
  click AB "/notions/ab-testing"
```

## Quatre consommateurs, quatre contrats

L'**analytique et la BI** attendent des tables propres, documentées et stables, pas des extractions à la demande. Le **reverse ETL** renverse la flèche habituelle : l'entrepôt redevient source et pousse des segments enrichis vers le CRM, l'outil de support ou la plateforme d'envoi — même mécanique qu'une ingestion, avec des contraintes plus dures côté destination, quotas d'API et effets métier immédiats en cas d'erreur. Le **machine learning** est un consommateur exigeant de features fraîches, versionnées et calculées de la même façon à l'entraînement et en ligne — voir [[parcours/mlops/donnees-et-features]]. Les **systèmes de récupération documentaire** ajoutent un quatrième contrat : un corpus versionné, une fraîcheur mesurée et un index qu'on sait reconstruire.

La **couche sémantique** est ce qui les tient ensemble : définir « chiffre d'affaires » une seule fois, à un seul endroit, plutôt que dans chaque rapport. C'est le meilleur remède connu aux réunions où deux équipes affichent deux chiffres différents pour la même chose.

## Ce qu'il faut savoir faire

- **Livrer une table avec son mode d'emploi** : grain, fraîcheur attendue, propriétaire, définition de chaque colonne. Une table non documentée finit recopiée trois fois avec trois interprétations.
- **Poser une définition partagée des indicateurs** avant de laisser fleurir les rapports, et la faire vivre dans un dépôt, pas dans une réunion.
- **Instrumenter l'usage** des tables et des rapports, puis supprimer sans état d'âme ce que personne ne consulte. Un catalogue de rapports orphelins interdit toute évolution du modèle.
- **Traiter un corpus documentaire comme un pipeline** : extraction, découpage, versionnement, idempotence, fraîcheur mesurée. Le choix du modèle vient après, et pèse moins.
- **Fournir la mesure des expérimentations** : affectation figée, métriques de ratio calculées de façon reproductible. La décision revient au produit, la justesse du chiffre revient à vous.

> [!tip] Ajout 2026
> Le data engineer est devenu un acteur central des systèmes à base de LLM : c'est lui qui construit l'ingestion documentaire, maintient les index et gère le versionnement des corpus. Deux ponts concrets. Pour l'accès en langage naturel à l'entrepôt, le modèle sémantique et la documentation des colonnes font davantage pour la qualité des réponses que le choix du modèle. Et l'hébergement des modèles de plongement est devenu une brique d'infrastructure comme une autre, à dimensionner et à superviser.

> [!warning] Piège
> Le tableau de bord sans propriétaire. Les outils décisionnels accumulent des centaines de rapports dont on ignore lesquels sont consultés ; chacun devient une contrainte invisible sur le modèle de données, et l'ensemble finit par geler la plateforme. Un rapport sans propriétaire nommé et sans usage mesuré se supprime.

## Les notions mobilisées

- [[notions/outils-decisionnels]] — ce qui consomme vos tables ; en connaître les contraintes évite de livrer un modèle inexploitable dans l'outil de l'entreprise.
- [[notions/rag]] — vu du data engineer, c'est un pipeline documentaire avec une exigence de fraîcheur et un index à reconstruire.
- [[notions/embeddings-et-bases-vectorielles]] — l'index de récupération, à sauvegarder, superviser et réindexer comme n'importe quel magasin.
- [[notions/mesure-d-usage-produit]] — l'instrumentation des rapports et des tables : la seule façon de savoir ce qu'on peut faire évoluer.
- [[notions/ab-testing]] — le data engineer n'arbitre pas l'expérimentation, il en garantit la mesure et la reproductibilité.

## Pour apprendre

- [Introduction to Data Analytics](https://www.coursera.org/learn/introduction-to-data-analytics) — pour comprendre ce que fait de vos tables celui qui les consomme.
- [Looker — plateforme et analytique embarquée](https://cloud.google.com/looker) — la couche sémantique comme produit, à lire pour le concept même si vous n'achetez rien.
- [Streamlit Docs](https://docs.streamlit.io/) — le chemin le plus court entre une table et une application interne utilisable.
- [Hightouch Docs](https://hightouch.com/docs) — le reverse ETL expliqué par un de ses outils, avec les contraintes de destination.
- [Power BI](https://www.microsoft.com/en-us/power-platform/products/power-bi) — l'outil décisionnel le plus répandu en entreprise, dont les limites conditionnent votre modélisation.
