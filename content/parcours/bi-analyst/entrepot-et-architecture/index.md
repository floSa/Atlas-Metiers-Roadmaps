---
title: Entrepôt et architecture
aliases:
  - parcours/bi-analyst/entrepot-et-architecture
---

L'entrepôt existe pour une raison précise : découpler la lecture analytique de l'écriture transactionnelle, et fixer un historique que personne ne peut réécrire par accident. Tout le reste en découle.

## Les quatre sujets

```mermaid
flowchart TD
  C["Entrepôt, lac ou moteur embarqué<br/>qui porte le coût du schéma"]
  Z["L'architecture à zones<br/>atterrissage, intermédiaire, présentation"]
  S["Stockage, calcul, formats ouverts<br/>la vraie rupture du cloud"]
  P["Le coût de la plateforme<br/>instrumenté avant d'ouvrir l'accès"]

  click C "/parcours/bi-analyst/entrepot-et-architecture/entrepot-lac-ou-moteur-embarque"
  click Z "/parcours/bi-analyst/entrepot-et-architecture/l-architecture-a-zones"
  click S "/parcours/bi-analyst/entrepot-et-architecture/stockage-calcul-et-formats-ouverts"
  click P "/parcours/bi-analyst/entrepot-et-architecture/le-cout-de-la-plateforme"
```

**Porte de sortie** : savoir justifier entrepôt contre lac contre moteur embarqué sur un cas chiffré, coût mensuel compris.

## Ma progression

- [ ] [[parcours/bi-analyst/entrepot-et-architecture/entrepot-lac-ou-moteur-embarque|Entrepôt, lac ou moteur embarqué]] — l'arbitrage et ses conséquences quotidiennes
- [ ] [[parcours/bi-analyst/entrepot-et-architecture/l-architecture-a-zones|L'architecture à zones]] — trois zones, trois responsabilités, une règle de rejeu
- [ ] [[parcours/bi-analyst/entrepot-et-architecture/stockage-calcul-et-formats-ouverts|Stockage, calcul, formats ouverts]] — Iceberg, Delta, et ce que ça change pour la BI
- [ ] [[parcours/bi-analyst/entrepot-et-architecture/le-cout-de-la-plateforme|Le coût de la plateforme]] — la dépense par tableau de bord, mesurée dès le premier jour
