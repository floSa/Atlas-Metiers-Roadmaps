---
title: Analyse de corrélation
tags: [notion, statistiques, correlation, causalite]
date: 2026-09-16
statut: actif
appelee-par: [data-analyst, bi-analyst]
---

Mesure de l'intensité et du sens du lien statistique entre deux variables — et de rien d'autre.

## À quoi ça sert

La corrélation est un outil de dégrossissage. Sur un jeu large, elle indique en quelques secondes quelles paires de variables méritent d'être regardées et lesquelles n'ont manifestement rien à voir. C'est un filtre, pas une conclusion.

Sa seconde utilité est défensive : elle sert à repérer la redondance. Deux variables fortement corrélées apportent presque la même information, ce qui déstabilise les coefficients d'une régression et fait croire à un effet réparti là où il n'y en a qu'un.

Tout le reste de son intérêt tient dans ce qu'elle ne dit pas. Un coefficient élevé est compatible avec quatre situations très différentes : A cause B, B cause A, un troisième facteur cause les deux, ou c'est une coïncidence d'échantillon. Rien dans le chiffre ne permet de choisir.

## Ce qu'il faut savoir

- **Pearson** mesure un lien **linéaire** entre deux variables continues. **Spearman** et **Kendall** mesurent un lien monotone à partir des rangs, et résistent aux valeurs extrêmes comme aux relations non linéaires.
- **Un coefficient nul n'est pas une absence de lien**, c'est une absence de lien de la forme testée. Une relation en U donne un Pearson proche de zéro.
- **Toujours regarder le nuage de points.** Le quartet d'Anscombe existe pour cette raison : quatre jeux, même corrélation, quatre formes incomparables.
- **Les valeurs extrêmes déplacent Pearson à elles seules.** Un seul point peut créer ou effacer une corrélation sur un petit effectif.
- **Facteur de confusion** : la troisième variable qui explique les deux autres. La saison explique la vente de glaces et les noyades ; le chiffre d'affaires du client explique à la fois le nombre de commandes et le nombre de réclamations.
- **Biais de sélection** : une corrélation peut naître de la façon dont l'échantillon a été constitué, sans exister dans la population.
- **Une matrice de corrélation sur cinquante variables produit des liens forts par hasard.** Elle sert à explorer, pas à conclure, et ses résultats se confirment sur un autre échantillon.
- **Pour aller vers la causalité**, il faut autre chose : une expérimentation contrôlée ([[notions/ab-testing]]), une variation exogène, ou au minimum un raisonnement explicite sur le mécanisme et les facteurs contrôlés.

## Selon le métier

### Data Analyst

La corrélation mesure qu'un lien existe et rien d'autre : c'est la première des trois étapes du diagnostic, avant le test d'hypothèse et la régression. Sa place dans le raisonnement est d'ouvrir des pistes, et l'erreur professionnelle est de la présenter comme un résultat — parce que le commanditaire, lui, l'entendra comme une cause.

### BI Analyst

L'enjeu est la diffusion. Les « informations automatiques » des plateformes décisionnelles — détection de pic, explication d'écart — remontent des corrélations sur les dimensions disponibles, sans aucune notion de causalité ni du fait qu'une dimension puisse être un effet plutôt qu'une cause. Utiles pour attirer l'attention, mauvaises pour conclure, et jamais à transmettre telles quelles à une direction.

> [!warning] Piège
> Chercher dans une matrice de corrélation la variable la plus liée à l'objectif et en faire un levier d'action. La variable la mieux corrélée à l'attrition est souvent une conséquence de l'attrition — baisse d'usage, appels au support — et agir dessus ne change rien. Distinguer ce qui précède de ce qui accompagne est la première question à poser.

## Pour aller plus loin

- [Correlation vs. Causation — Scribbr](https://www.scribbr.com/methodology/correlation-vs-causation/) — la distinction traitée sérieusement, avec les designs qui permettent de conclure.
- [Correlation Analysis — DATAtab](https://datatab.net/tutorial/correlation) — quel coefficient pour quel type de données.
- [Correlation does not imply causation — Wikipédia](https://en.wikipedia.org/wiki/Correlation_does_not_imply_causation) — la typologie des faux liens, avec des exemples célèbres.

## Appelée par

- [[parcours/data-analyst|Data Analyst]]
- [[parcours/bi-analyst|BI Analyst]]

Voisines : [[notions/tests-hypotheses]], [[notions/regression-lineaire]], [[notions/ab-testing]].
