---
title: Socle outillage
aliases:
  - parcours/data-analyst/socle-outillage
---

Les outils s'apprennent en quelques semaines et ne distinguent personne. Ce qui distingue, c'est de savoir à quel moment basculer de l'un à l'autre — et ce domaine est organisé autour de ces seuils.

## Les six sujets

```mermaid
flowchart TD
  T["Le tableur et son seuil<br/>à quel moment on n'a plus le droit d'y rester"]
  S["SQL, l'outil le plus rentable<br/>agrégation, jointure, fenêtrage"]
  L["Choisir un langage<br/>Python ou R, et aller au fond"]
  M["Manipuler des tables en code<br/>pandas, dplyr, la lisibilité d'abord"]
  P["Publier dans un outil partagé<br/>ce que l'analyste y fait et n'y fait pas"]
  V["Quand le volume déborde<br/>DuckDB, Polars, Parquet, Spark"]

  click T "/parcours/data-analyst/socle-outillage/le-tableur-et-son-seuil"
  click S "/parcours/data-analyst/socle-outillage/sql-pour-l-analyste"
  click L "/parcours/data-analyst/socle-outillage/choisir-un-langage"
  click M "/parcours/data-analyst/socle-outillage/manipuler-des-tables-en-code"
  click P "/parcours/data-analyst/socle-outillage/publier-dans-un-outil-partage"
  click V "/parcours/data-analyst/socle-outillage/quand-le-volume-deborde"
```

## Ma progression

- [ ] [[parcours/data-analyst/socle-outillage/le-tableur-et-son-seuil|Le tableur et son seuil]] — la question n'est pas quelles formules, c'est quand arrêter
- [ ] [[parcours/data-analyst/socle-outillage/sql-pour-l-analyste|SQL pour l'analyste]] — ce qu'il faut maîtriser, et ce qui n'est pas ton sujet
- [ ] [[parcours/data-analyst/socle-outillage/choisir-un-langage|Choisir un langage]] — Python ou R, un seul, jusqu'au bout
- [ ] [[parcours/data-analyst/socle-outillage/manipuler-des-tables-en-code|Manipuler des tables en code]] — l'enchaînement des transformations, lisible et rejouable
- [ ] [[parcours/data-analyst/socle-outillage/publier-dans-un-outil-partage|Publier dans un outil partagé]] — consommer et publier sans devenir l'équipe décisionnelle
- [ ] [[parcours/data-analyst/socle-outillage/quand-le-volume-deborde|Quand le volume déborde]] — ne pas rapatrier, puis DuckDB et Polars, puis seulement distribuer
