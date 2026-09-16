---
title: Data Scientist
tags: [parcours, data-scientist, statistiques, machine-learning, deep-learning, mlops, ia]
date: 2026-09-16
statut: actif
source: https://roadmap.sh/ai-data-scientist
---

Transformer une question métier incertaine en une réponse mesurée, puis en un modèle qui tient hors du carnet de calcul — avec, à chaque étage, la discipline d'évaluation qui décide si le chiffre annoncé vaut quelque chose.

## La roadmap

Chaque case mène à sa page. Cochez les étapes acquises en bas de page pour suivre votre progression.

```mermaid
flowchart TD
  CA["Cadrer et restituer<br/>du besoin flou à la question mesurable"] --> MA["Socle mathématique<br/>algèbre, gradient, probabilités"]
  MA --> ST["Statistique et inférence<br/>signal, bruit, intervalle"]
  ST --> EC["Économétrie et causalité<br/>l'effet plutôt que la prédiction"]
  CA --> CO["Code et outillage<br/>le pipeline reproductible"]
  CO --> EX["Exploration des données<br/>ce que le cahier des charges tait"]
  EX --> MO["Modélisation<br/>le protocole avant l'algorithme"]
  ST --> MO
  EC --> MO
  MO --> DL["Apprentissage profond<br/>le non structuré et son coût"]
  DL --> LM["Modèles de langage<br/>appeler, récupérer ou affiner"]
  MO --> PR["Mise en production<br/>servir, tracer, surveiller"]
  LM --> PR

  click CA "/parcours/data-scientist/cadrer-et-restituer"
  click MA "/parcours/data-scientist/socle-mathematique"
  click ST "/parcours/data-scientist/statistique-et-inference"
  click EC "/parcours/data-scientist/econometrie-et-causalite"
  click CO "/parcours/data-scientist/code-et-outillage"
  click EX "/parcours/data-scientist/exploration-des-donnees"
  click MO "/parcours/data-scientist/modelisation"
  click DL "/parcours/data-scientist/apprentissage-profond"
  click LM "/parcours/data-scientist/modeles-de-langage"
  click PR "/parcours/data-scientist/mise-en-production"

  classDef pivot stroke:#f9a825,stroke-width:1px
  class CA,MO pivot
```

## Ma progression

- [ ] [[parcours/data-scientist/cadrer-et-restituer|Cadrer et restituer]] — traduire une demande en question mesurable, et rendre le résultat décidable
- [ ] [[parcours/data-scientist/socle-mathematique|Socle mathématique]] — l'algèbre, le gradient et les probabilités, là où ils se voient vraiment
- [ ] [[parcours/data-scientist/statistique-et-inference|Statistique et inférence]] — séparer le signal du bruit et rapporter une marge
- [ ] [[parcours/data-scientist/econometrie-et-causalite|Économétrie et causalité]] — mesurer un effet quand on ne peut pas randomiser
- [ ] [[parcours/data-scientist/code-et-outillage|Code et outillage]] — un pipeline versionné, testé, relançable par un tiers
- [ ] [[parcours/data-scientist/exploration-des-donnees|Exploration des données]] — qualité, fuite, structure, variables construites
- [ ] [[parcours/data-scientist/modelisation|Modélisation]] — métrique, validation, calibration, interprétation
- [ ] [[parcours/data-scientist/apprentissage-profond|Apprentissage profond]] — quand le non structuré justifie le coût, et comment diagnostiquer
- [ ] [[parcours/data-scientist/modeles-de-langage|Modèles de langage]] — l'arbitrage prompt, récupération, affinage, et son évaluation
- [ ] [[parcours/data-scientist/mise-en-production|Mise en production]] — versionner, servir, surveiller la dérive, revenir en arrière
