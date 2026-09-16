---
tags: [notion, visualisation, graphique, restitution, lisibilite]
date: 2026-09-16
statut: actif
appelee-par: [data-analyst, bi-analyst]
---

# Visualisation de données

Représentation graphique de valeurs, choisie pour qu'une question précise se lise sans calcul mental — et non pour illustrer un propos déjà écrit.

## À quoi ça sert

Un graphique exploite la seule chose que l'œil fait mieux qu'un tableau : comparer des positions et des longueurs instantanément. Tout l'art consiste à faire porter la comparaison qui compte par l'encodage visuel le plus précis disponible, et à retirer tout ce qui capte l'attention sans porter d'information.

La conséquence pratique est qu'on ne choisit pas un graphique à partir des données, mais à partir de la **question**. Comparer des catégories, suivre une évolution, montrer une distribution, montrer une relation, montrer une composition : cinq questions, cinq familles de réponses. Le même jeu de données donne cinq graphiques différents selon ce qu'on veut faire voir, et un seul est le bon.

Il faut aussi distinguer deux usages qui n'ont pas les mêmes exigences : le graphique d'exploration, fait pour soi, vite et laid ; et le graphique de restitution, fait pour quelqu'un d'autre, qui doit tenir sans son auteur à côté.

## Ce qu'il faut savoir

- **Comparer des catégories** : barres, horizontales dès que les libellés sont longs, triées par valeur et non par ordre alphabétique. **Évolution** : courbe. **Distribution** : histogramme, boîte à moustaches, ou nuage de points quand l'effectif le permet. **Relation** : nuage de points. **Composition** : barres empilées, et rarement autre chose.
- **L'axe des ordonnées part de zéro sur des barres**, parce que la longueur porte la comparaison. Sur une courbe, ce n'est pas obligatoire — mais toute troncature doit être visible.
- **Le camembert ne sert qu'à une chose** : montrer qu'une part domine, sur trois catégories au plus. Au-delà, l'œil ne compare pas des angles.
- **La couleur porte du sens ou rien.** Une couleur par catégorie quand les catégories comptent, un dégradé pour une grandeur ordonnée, et un accent unique pour ce qu'on veut faire remarquer. Vérifier le rendu en cas de daltonisme et en niveaux de gris.
- **Écrire le message dans le titre.** « Les ventes du segment pro ont décroché au T3 » informe ; « Ventes par segment et par trimestre » décrit un axe.
- **Annoter plutôt que commenter à côté.** La rupture, le seuil, l'événement se posent sur le graphique — c'est là que le lecteur regarde.
- **Retirer avant d'ajouter** : grilles lourdes, effets de relief, doubles axes, libellés redondants. Le double axe est le plus trompeur de tous : il permet de faire coïncider n'importe quelles deux séries.
- **Un graphique honnête se lit en cinq secondes.** S'il faut expliquer comment le lire, c'est le mauvais graphique.

## Selon le métier

### Data Analyst

Deux régimes à ne pas confondre. Les graphiques d'exploration — histogramme, boîte à moustaches, nuage de points — sont faits pour soi, n'ont pas à être présentables et servent à voir ce que la donnée contient. Ceux de restitution sont faits pour mettre quelqu'un en position de décider : le critère de réussite est que la personne en face sache ce qu'elle doit faire et ce qu'elle risque en le faisant.

### BI Analyst

La contrainte est la durée de vie. Un graphique produit une fois s'accompagne de son auteur ; un tableau de bord vit des années sans lui, devant des lecteurs qui ne connaissent pas les définitions. Cela impose des libellés explicites, des unités affichées, une date de rafraîchissement visible, et une prudence particulière sur les variations non significatives.

> [!warning] Piège
> Afficher tout ce qui est disponible parce que l'outil le permet. Un tableau de bord de trente indicateurs ne se lit pas : le lecteur ne sait pas où regarder, donc il ne regarde nulle part, et finit par redemander le chiffre par courriel. Cinq indicateurs choisis, avec leur référence de comparaison, produisent plus de décisions que trente affichés.

## Pour aller plus loin

- [How to choose colors for data visualizations — Atlassian](https://www.atlassian.com/data/charts/how-to-choose-colors-data-visualization) — la couleur traitée comme un encodage, pas comme une décoration.
- [Visual storytelling 101 — principes de conception de tableaux de bord](https://medium.com/@mokkup/8-essential-dashboard-design-principles-for-effective-data-visualization-40653c5fd135) — les règles de mise en page d'un tableau de bord.
- [Data Visualization Society](https://www.datavisualizationsociety.org/) — la communauté professionnelle et ses ressources.

## Appelée par

- [[parcours/data-analyst|Data Analyst]]
- [[parcours/bi-analyst|BI Analyst]]

Voisines : [[notions/outils-decisionnels]], [[notions/statistiques-descriptives]], [[notions/tableur]].
