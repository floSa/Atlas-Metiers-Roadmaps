---
title: AI Product Builder
tags: [parcours, ai-product-builder, produit, vibe-coding, prototypage, deploiement, ia]
date: 2026-09-16
statut: actif
source: https://roadmap.sh/ai-product-builder
---

Livrer un produit logiciel en s'appuyant sur des outils de génération de code : cadrer, prototyper, générer, reprendre ce qui a été généré, tester avec de vrais utilisateurs, mettre en ligne. Le mot « AI » du titre désigne l'atelier, pas nécessairement le produit. Deux pré-requis non déclarés en amont mais réels : savoir lire du code qu'on n'a pas écrit, et savoir ce qu'est une requête HTTP.

## La roadmap

Chaque case mène à sa page. Cochez les étapes acquises en bas de page pour suivre votre progression.

```mermaid
flowchart TD
  C["Cadrage et arbitrage<br/>le problème, la pile, construire ou acheter"] --> P["Prototypage<br/>réduire l'incertitude avant de générer"]
  P --> G["Génération et reprise du code<br/>relire, corriger, régénérer"]
  G --> T["Tests et mesure d'usage<br/>deux boucles à ne pas confondre"]
  T --> M["Mise en ligne<br/>dépôt, intégration continue, hébergement"]
  M --> D["Du prototype au produit<br/>la liste de ce qui n'a jamais été conçu"]
  D -.-> MO["Quand le produit embarque un modèle<br/>l'autre moitié du titre"]
  T -.->|"boucle de retour"| C

  click C "/parcours/ai-product-builder/cadrage-et-arbitrage/index"
  click P "/parcours/ai-product-builder/prototypage/index"
  click G "/parcours/ai-product-builder/generation-et-reprise/index"
  click T "/parcours/ai-product-builder/tests-et-mesure-d-usage/index"
  click M "/parcours/ai-product-builder/mise-en-ligne/index"
  click D "/parcours/ai-product-builder/du-prototype-au-produit/index"
  click MO "/parcours/ai-product-builder/quand-le-produit-embarque-un-modele/index"

  classDef conditionnel stroke:#f9a825,stroke-width:1px,stroke-dasharray:4 3
  class MO conditionnel
```

## Ma progression

- [ ] [[parcours/ai-product-builder/cadrage-et-arbitrage/index|Cadrage et arbitrage]] — définir le problème, poser la pile, décider de construire ou pas
- [ ] [[parcours/ai-product-builder/prototypage/index|Prototypage]] — choisir l'outil, prototyper la bonne fonction, valider avec des gens
- [ ] [[parcours/ai-product-builder/generation-et-reprise/index|Génération et reprise du code]] — conduire une génération, la relire, la corriger sans la dénaturer
- [ ] [[parcours/ai-product-builder/tests-et-mesure-d-usage/index|Tests et mesure d'usage]] — la boucle technique et la boucle produit, et ce qu'on instrumente
- [ ] [[parcours/ai-product-builder/mise-en-ligne/index|Mise en ligne]] — dépôt, intégration continue, hébergement, base de données, droits d'accès
- [ ] [[parcours/ai-product-builder/du-prototype-au-produit/index|Du prototype au produit]] — ce qu'un prototype n'a jamais eu, et ce que coûte son report
- [ ] [[parcours/ai-product-builder/quand-le-produit-embarque-un-modele/index|Quand le produit embarque un modèle]] — la frontière avec l'AI Engineer, et ce qu'elle impose
