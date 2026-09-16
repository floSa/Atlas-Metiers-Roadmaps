---
title: MLOps
tags: [parcours, mlops, llmops, deploiement, supervision, derive, infrastructure]
date: 2026-09-16
statut: actif
source: https://roadmap.sh/mlops
---

Mener un modèle du carnet où il marche jusqu'à la production où il tient : le versionner, le livrer, le servir, le surveiller — et savoir décider, sur des chiffres, quand il faut le refaire.

## La roadmap

Chaque case mène à sa page. Cochez les étapes acquises en bas de page pour suivre votre progression.

```mermaid
flowchart TD
  P["Principes et versionnement<br/>code, données, modèle : trois objets"] --> D["Données et features<br/>pipelines, lignage, correction temporelle"]
  D --> E["Évaluation et explicabilité<br/>mesurer, comparer, justifier"]
  E --> CI["CI/CD et entraînement continu<br/>les deux portes que le ML ajoute"]
  CI --> O["Orchestration et déploiement<br/>graphe de tâches, canari, ombre"]
  O --> S["Supervision et dérive<br/>système, données, qualité prédictive"]
  S -->|boucle de ré-entraînement| CI
  S --> L["LLMOps<br/>évaluation, traces, coût par requête"]
  I["Infrastructure et serving<br/>cloud, conteneurs, GPU, embarqué"] -.-> O
  I -.-> S

  click P "/parcours/mlops/principes-et-versionnement"
  click D "/parcours/mlops/donnees-et-features"
  click E "/parcours/mlops/evaluation-et-explicabilite"
  click CI "/parcours/mlops/ci-cd-et-entrainement-continu"
  click I "/parcours/mlops/infrastructure-et-serving"
  click O "/parcours/mlops/orchestration-et-deploiement"
  click S "/parcours/mlops/supervision-et-derive"
  click L "/parcours/mlops/llmops"

  classDef transverse stroke:#f9a825,stroke-width:1px,stroke-dasharray:4 3
  class I transverse
```

## Ma progression

- [ ] [[parcours/mlops/principes-et-versionnement|Principes et versionnement]] — l'échelle de maturité, la reproductibilité, et les trois objets à versionner
- [ ] [[parcours/mlops/donnees-et-features|Données et features]] — la plupart des incidents « modèle » sont des incidents « données »
- [ ] [[parcours/mlops/evaluation-et-explicabilite|Évaluation et explicabilité]] — découpage temporel, calibration, métriques par segment, attribution
- [ ] [[parcours/mlops/ci-cd-et-entrainement-continu|CI/CD et entraînement continu]] — tester les données, comparer au modèle en place, produire un candidat
- [ ] [[parcours/mlops/infrastructure-et-serving|Infrastructure et serving]] — cloud, conteneurs, GPU, mise à l'échelle, embarqué
- [ ] [[parcours/mlops/orchestration-et-deploiement|Orchestration et déploiement]] — graphe de tâches, bleu-vert, canari, ombre, retour arrière
- [ ] [[parcours/mlops/supervision-et-derive|Supervision et dérive]] — trois couches à surveiller, et la cadence de ré-entraînement qui se mesure
- [ ] [[parcours/mlops/llmops|LLMOps]] — ce qui change quand le modèle est appelé et non entraîné
