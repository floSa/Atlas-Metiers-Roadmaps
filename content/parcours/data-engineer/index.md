---
title: Data Engineer
tags: [parcours, data-engineer, pipelines, sql, entrepot, orchestration, cloud]
date: 2026-09-16
statut: actif
source: https://roadmap.sh/data-engineer
---

Construire et exploiter les systèmes qui rendent la donnée utilisable par d'autres : la faire arriver, la stocker là où elle sera interrogée, la transformer en tables dont on peut se servir — et garantir qu'elle est encore juste demain matin.

## La roadmap

Chaque case porte le niveau attendu d'un profil confirmé — de **notion** (reconnaître le sujet, savoir qui appeler) à **référence** (faire autorité dans la salle), en passant par **usage** (chemin balisé) et **autonomie** (concevoir, déboguer sous pression, arbitrer). Chaque case mène à sa page. Cochez les étapes acquises en bas de page pour suivre votre progression.

```mermaid
flowchart TD
  S["Socle et cycle de vie<br/>Autonomie<br/>Python, SQL, Linux, systèmes distribués"] --> I["Sources et ingestion<br/>Autonomie<br/>d'où vient la donnée, comment elle entre"]
  I --> ST["Stockage et modélisation<br/>Référence<br/>bases, entrepôt, lac, lakehouse"]
  ST --> O["Orchestration et transformation<br/>Référence<br/>ELT, DAG, dbt, reprise par date"]
  O --> C["Calcul et flux<br/>Usage<br/>Spark, mono-nœud, Kafka"]
  O --> SV["Serving et consommation<br/>Autonomie<br/>BI, reverse ETL, ML, RAG"]
  C --> SV
  P["Plateforme et exploitation<br/>Usage<br/>conteneurs, CI/CD, IaC, supervision"] -.-> O
  P -.-> C
  G["Sécurité et gouvernance<br/>Usage<br/>droits, qualité, lignage, RGPD"] -.-> ST
  G -.-> SV

  click S "/parcours/data-engineer/socle-et-cycle-de-vie"
  click I "/parcours/data-engineer/sources-et-ingestion"
  click ST "/parcours/data-engineer/stockage-et-modelisation"
  click O "/parcours/data-engineer/orchestration-et-transformation"
  click C "/parcours/data-engineer/calcul-et-flux"
  click SV "/parcours/data-engineer/serving-et-consommation"
  click P "/parcours/data-engineer/plateforme-et-exploitation"
  click G "/parcours/data-engineer/securite-et-gouvernance"

  classDef transverse stroke:#f9a825,stroke-width:1px,stroke-dasharray:4 3
  class P,G transverse
```

## Ma progression

- [ ] [[parcours/data-engineer/socle-et-cycle-de-vie|Socle et cycle de vie]] — les langages, le système, le réseau, et le fil rouge génération → stockage → ingestion → serving
- [ ] [[parcours/data-engineer/sources-et-ingestion|Sources et ingestion]] — bases, API, journaux, documents ; batch, temps réel, capture de changements
- [ ] [[parcours/data-engineer/stockage-et-modelisation|Stockage et modélisation]] — transactionnel contre analytique, familles de bases, entrepôt, lac, lakehouse
- [ ] [[parcours/data-engineer/orchestration-et-transformation|Orchestration et transformation]] — ELT, graphes de tâches, dbt, idempotence et reprise
- [ ] [[parcours/data-engineer/calcul-et-flux|Calcul et flux]] — quand distribuer, quand une machine suffit, et ce qu'un bus d'événements apporte
- [ ] [[parcours/data-engineer/plateforme-et-exploitation|Plateforme et exploitation]] — conteneurs, CI/CD, infrastructure déclarative, tests de données, supervision
- [ ] [[parcours/data-engineer/serving-et-consommation|Serving et consommation]] — couche sémantique, BI, reverse ETL, features de modèles, corpus documentaires
- [ ] [[parcours/data-engineer/securite-et-gouvernance|Sécurité et gouvernance]] — droits fins, chiffrement, qualité, lignage, catalogue, RGPD et AI Act
