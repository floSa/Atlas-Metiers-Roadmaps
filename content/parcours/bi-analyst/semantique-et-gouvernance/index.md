---
title: Sémantique et gouvernance
aliases:
  - parcours/bi-analyst/semantique-et-gouvernance
---

Le vrai travail du métier, auquel l'amont ne consacre qu'un nœud : l'endroit où « chiffre d'affaires » et « client actif » reçoivent **une** définition, et où un chiffre devient défendable en réunion sans préparation.

## Les six sujets

```mermaid
flowchart TD
  D["Définir une mesure<br/>formule et règle d'agrégation"]
  O["Où vit la couche sémantique<br/>trois emplacements, trois compromis"]
  E["Faire évoluer une définition<br/>comme une interface publique"]
  Q["La qualité instrumentée<br/>savoir avant que quelqu'un découvre"]
  L["Lignage et analyse d'impact<br/>d'où vient ce chiffre, qu'est-ce qui casse"]
  R["RGPD, périmètre et éthique<br/>ce qu'on publie et sur qui"]

  click D "/parcours/bi-analyst/semantique-et-gouvernance/definir-une-mesure"
  click O "/parcours/bi-analyst/semantique-et-gouvernance/ou-vit-la-couche-semantique"
  click E "/parcours/bi-analyst/semantique-et-gouvernance/faire-evoluer-une-definition"
  click Q "/parcours/bi-analyst/semantique-et-gouvernance/la-qualite-instrumentee"
  click L "/parcours/bi-analyst/semantique-et-gouvernance/lignage-et-analyse-d-impact"
  click R "/parcours/bi-analyst/semantique-et-gouvernance/rgpd-perimetre-et-ethique"
```

**Porte de sortie** : quinze mesures définies une seule fois, dont un ratio correct à tous les niveaux d'agrégation, et une réconciliation nocturne avec la source métier.

## Ma progression

- [ ] [[parcours/bi-analyst/semantique-et-gouvernance/definir-une-mesure|Définir une mesure]] — formule, agrégation, et le test du ratio de ratios
- [ ] [[parcours/bi-analyst/semantique-et-gouvernance/ou-vit-la-couche-semantique|Où vit la couche sémantique]] — dans l'outil, découplée, ou dans l'entrepôt
- [ ] [[parcours/bi-analyst/semantique-et-gouvernance/faire-evoluer-une-definition|Faire évoluer une définition]] — annonce, coexistence, dépréciation
- [ ] [[parcours/bi-analyst/semantique-et-gouvernance/la-qualite-instrumentee|La qualité instrumentée]] — six dimensions traduites en tests, et la fraîcheur affichée
- [ ] [[parcours/bi-analyst/semantique-et-gouvernance/lignage-et-analyse-d-impact|Lignage et analyse d'impact]] — les deux sens, et pourquoi le montant est le plus utile
- [ ] [[parcours/bi-analyst/semantique-et-gouvernance/rgpd-perimetre-et-ethique|RGPD, périmètre et éthique]] — minimisation, conservation, et le biais par le périmètre
