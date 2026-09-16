---
title: Socle de données
aliases:
  - parcours/bi-analyst/socle-de-donnees
---

Ce qui entre dans l'entrepôt, et surtout ce qui va casser : chaque source a un mode de défaillance propre et prévisible, et un modèle se conçoit pour les absorber.

## Les quatre sujets

```mermaid
flowchart TD
  S["Connaître ses sources<br/>et leur mode de défaillance"]
  E["Extraire sans casser la source<br/>incrémental, découplage, quotas"]
  F["Formats et typage<br/>ce qui préfigure dimension et mesure"]
  Q["SQL de production<br/>une requête exécutée dix mille fois"]

  click S "/parcours/bi-analyst/socle-de-donnees/connaitre-ses-sources"
  click E "/parcours/bi-analyst/socle-de-donnees/extraire-sans-casser-la-source"
  click F "/parcours/bi-analyst/socle-de-donnees/formats-et-typage"
  click Q "/parcours/bi-analyst/socle-de-donnees/sql-de-production"
```

**Porte de sortie** : un inventaire des sources où chacune porte son propriétaire, sa fréquence, son mode de rechargement, et la réponse à « cette source peut-elle réécrire le passé ».

## Ma progression

- [ ] [[parcours/bi-analyst/socle-de-donnees/connaitre-ses-sources|Connaître ses sources]] — l'inventaire qui dit ce qui cassera, et quand
- [ ] [[parcours/bi-analyst/socle-de-donnees/extraire-sans-casser-la-source|Extraire sans casser la source]] — incrémental, découplage, et pourquoi jamais en production
- [ ] [[parcours/bi-analyst/socle-de-donnees/formats-et-typage|Formats et typage]] — Parquet, semi-structuré, et la frontière dimension/mesure
- [ ] [[parcours/bi-analyst/socle-de-donnees/sql-de-production|SQL de production]] — fenêtrage, plans d'exécution, réduction du volume lu
