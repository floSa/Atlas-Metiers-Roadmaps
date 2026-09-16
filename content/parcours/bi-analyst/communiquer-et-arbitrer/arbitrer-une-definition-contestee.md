---
title: Arbitrer une définition contestée
---

Deux services affichent deux nombres différents pour la même chose. Le réflexe est de chercher l'erreur, et il est faux : dans la grande majorité des cas les deux calculs sont corrects et portent sur deux périmètres différents.

```mermaid
flowchart LR
  D["Deux chiffres divergents"] --> V["Vérifier : les deux sont justes"]
  V --> P["Expliciter les deux périmètres"]
  P --> C["Chiffrer l'écart"]
  C --> N["Deux noms distincts"]
  N --> A["Désigner celle qui sert au pilotage"]
  A --> J["Consigner au journal"]
```

## Ce qu'il faut savoir faire

- Commencer par établir que les deux chiffres sont justes. C'est contre-intuitif et c'est ce qui désamorce la réunion : personne n'a d'erreur à défendre, le sujet devient une question de convention.
- Donner **deux noms distincts** aux deux mesures. Tant qu'elles portent le même nom, le désaccord reviendra, quel que soit l'arbitrage rendu.
- Chiffrer l'écart avant la réunion, et le présenter comme une donnée du problème. « L'écart est de 3,2 %, dont 2,1 dus aux avoirs » transforme un conflit de principe en arbitrage documenté.
- Instruire, pas décider. Expliciter les deux périmètres, chiffrer l'écart, montrer les conséquences de chaque option, et faire prendre la décision au bon niveau — puis la documenter.
- Refuser d'arbitrer seul une définition à enjeu politique. Si le choix avantage une direction, celui qui tranche techniquement sera désavoué à la première réunion tendue. Instruire est une position solide ; décider à la place du métier ne l'est pas.
- Consigner la décision le jour même, avec la date, les deux positions, ce qui a été tranché et par qui. C'est ce qui empêche la réouverture six mois plus tard, quand les personnes auront changé.

## Les notions mobilisées

- [[notions/gestion-parties-prenantes]] — celui qui pilote et celui qui est évalué n'ont pas le même intérêt dans l'arbitrage.
- [[notions/conduite-du-changement]] — une définition tranchée contre l'avis d'un service produit un calcul parallèle, pas une adoption.
- [[notions/redaction-technique]] — la consignation vaut par sa concision et sa régularité, pas par son exhaustivité.
- [[notions/cadrage-besoin]] — l'arbitrage se prépare avec les mêmes questions que le cadrage initial, posées à deux parties au lieu d'une.

> [!warning] Piège
> Chercher qui a tort. La recherche de l'erreur transforme un désaccord de convention en mise en cause, la réunion se crispe, et le sujet réel — quelle définition sert au pilotage — n'est jamais abordé. Il ressurgira au comité suivant, avec les mêmes personnes et une confiance en moins.

## Pour apprendre

- [Stakeholder Management Guide](https://simplystakeholders.com/resources/guides/stakeholder-management/) — la cartographie d'influence à faire avant d'entrer dans la salle.
- [Roadmap Technical Writer](https://roadmap.sh/technical-writer) — écrire une décision de façon qu'elle tienne lieu de référence six mois plus tard.
- [5 Principles of Data Ethics for Business](https://online.hbs.edu/blog/post/data-ethics) — sur le fait d'expliciter un périmètre plutôt que de le laisser implicite.
