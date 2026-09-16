---
title: Génération et reprise du code
aliases:
  - parcours/ai-product-builder/generation-et-reprise
---

La génération ne supprime pas le travail, elle le déplace de l'écriture vers la relecture et la décision. C'est le cœur du métier, et la discipline la moins exercée.

## Les six sujets

```mermaid
flowchart TD
  C["Conduire une génération<br/>entrées, sortie brute, journal de l'énoncé"]
  R["Relire le code généré<br/>le schéma de données avant tout le reste"]
  D["Changement local ou régénération<br/>la question préalable au choix d'outil"]
  O["Les outils de codage assisté<br/>terminal, éditeur augmenté, complétion"]
  V["Les limites du vibe coding<br/>l'absence silencieuse, pas le bug"]
  S["Le socle à lire soi-même<br/>pour localiser la panne, pas pour écrire"]

  click C "/parcours/ai-product-builder/generation-et-reprise/conduire-une-generation"
  click R "/parcours/ai-product-builder/generation-et-reprise/relire-le-code-genere"
  click D "/parcours/ai-product-builder/generation-et-reprise/changement-local-ou-regeneration"
  click O "/parcours/ai-product-builder/generation-et-reprise/les-outils-de-codage-assiste"
  click V "/parcours/ai-product-builder/generation-et-reprise/les-limites-du-vibe-coding"
  click S "/parcours/ai-product-builder/generation-et-reprise/le-socle-a-lire-soi-meme"
```

## Ma progression

- [ ] [[parcours/ai-product-builder/generation-et-reprise/conduire-une-generation|Conduire une génération]] — ce qu'on donne en entrée, et ce qu'on commite avant de toucher
- [ ] [[parcours/ai-product-builder/generation-et-reprise/relire-le-code-genere|Relire le code généré]] — schéma, dépendances, secrets, dans cet ordre
- [ ] [[parcours/ai-product-builder/generation-et-reprise/changement-local-ou-regeneration|Changement local ou régénération]] — la règle qui évite la base de code à deux logiques
- [ ] [[parcours/ai-product-builder/generation-et-reprise/les-outils-de-codage-assiste|Les outils de codage assisté]] — trois catégories, un critère de choix, un facteur de qualité
- [ ] [[parcours/ai-product-builder/generation-et-reprise/les-limites-du-vibe-coding|Les limites du vibe coding]] — ce qu'il fait bien, ce qu'il fait mal, et pourquoi
- [ ] [[parcours/ai-product-builder/generation-et-reprise/le-socle-a-lire-soi-meme|Le socle à lire soi-même]] — HTML, CSS, JS, React, Node et les outils du navigateur
