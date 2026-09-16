---
title: Modélisation dimensionnelle
aliases:
  - parcours/bi-analyst/modelisation-dimensionnelle
---

La mécanique — faits, dimensions, étoile, flocon — est mutualisée dans [[notions/modelisation-dimensionnelle]]. Ce qui appartient à ce poste, ce sont les cinq décisions qui font qu'un modèle tient dix ans ou se réécrit tous les dix-huit mois.

## Les cinq décisions

```mermaid
flowchart TD
  G["Déclarer le grain<br/>la décision qui engage tout le reste"]
  M["Mesures et additivité<br/>l'erreur la plus difficile à détecter"]
  C["Dimensions conformes<br/>ce qui rend une comparaison possible"]
  H["Historiser les dimensions<br/>reclasser le passé, ou pas"]
  D["La dimension de date<br/>la table la plus rentable de l'entrepôt"]

  click G "/parcours/bi-analyst/modelisation-dimensionnelle/declarer-le-grain"
  click M "/parcours/bi-analyst/modelisation-dimensionnelle/mesures-et-additivite"
  click C "/parcours/bi-analyst/modelisation-dimensionnelle/dimensions-conformes"
  click H "/parcours/bi-analyst/modelisation-dimensionnelle/historiser-les-dimensions"
  click D "/parcours/bi-analyst/modelisation-dimensionnelle/la-dimension-de-date"
```

**Porte de sortie** : un modèle en étoile dont le grain tient en une phrase, avec sa dimension de date et une dimension historisée.

## Ma progression

- [ ] [[parcours/bi-analyst/modelisation-dimensionnelle/declarer-le-grain|Déclarer le grain]] — une ligne de la table de faits représente quoi, exactement
- [ ] [[parcours/bi-analyst/modelisation-dimensionnelle/mesures-et-additivite|Mesures et additivité]] — additif, semi-additif, non additif, et le total plausible et faux
- [ ] [[parcours/bi-analyst/modelisation-dimensionnelle/dimensions-conformes|Dimensions conformes]] — le partage entre domaines, ou l'impossibilité de comparer
- [ ] [[parcours/bi-analyst/modelisation-dimensionnelle/historiser-les-dimensions|Historiser les dimensions]] — type 1, type 2, et qui a le mandat de trancher
- [ ] [[parcours/bi-analyst/modelisation-dimensionnelle/la-dimension-de-date|La dimension de date]] — le calendrier de l'entreprise, qui n'est pas le calendrier civil
