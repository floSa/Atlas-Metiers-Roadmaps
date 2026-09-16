---
title: Régression linéaire
tags: [notion, statistiques, regression, moindres-carres, modelisation]
date: 2026-09-16
statut: actif
appelee-par: [data-analyst, bi-analyst]
---

Méthode qui estime une grandeur continue comme une combinaison pondérée de variables explicatives, en choisissant les poids qui minimisent la somme des carrés des écarts aux observations.

## À quoi ça sert

La régression fait deux choses qu'aucune des méthodes précédentes ne fait. Elle **quantifie** : au lieu de dire qu'un lien existe, elle dit de combien varie la sortie quand une entrée bouge d'une unité. Et elle **tient compte de plusieurs facteurs à la fois** : le coefficient d'une variable s'interprète « à autres variables constantes », ce qui est le seul moyen statistique de désamorcer un facteur de confusion qu'on a su mesurer.

C'est aussi le modèle le plus explicable qui existe. Dans un contexte où le résultat doit être défendu en réunion, un coefficient assorti de son intervalle de confiance vaut mieux qu'un score légèrement supérieur produit par un modèle qu'on ne sait pas raconter.

## Ce qu'il faut savoir

- **L'interprétation du coefficient** est « toutes choses égales par ailleurs **parmi les variables du modèle** ». Une variable omise qui influence à la fois l'entrée et la sortie biaise le coefficient, et rien dans la sortie du modèle ne le signale.
- **Les hypothèses** : linéarité de la relation, indépendance des résidus, homoscédasticité (variance constante des résidus), normalité des résidus pour l'inférence. Elles se vérifient sur les graphiques de résidus, pas sur le R².
- **Le R² n'est pas un critère de qualité.** Il augmente mécaniquement avec le nombre de variables. Regarder le R² ajusté, et surtout l'erreur sur des données non vues.
- **Multicolinéarité** : des variables explicatives fortement corrélées entre elles rendent les coefficients instables et parfois de signe inattendu, sans dégrader la prédiction. C'est un problème d'interprétation, pas de performance.
- **Les valeurs influentes** : un point peut à lui seul déplacer la droite. Distance de Cook et effet de levier les identifient.
- **Variables catégorielles** : encodage en indicatrices, avec une modalité de référence dont l'interprétation dépend. Choisir une référence qui a du sens métier.
- **Régularisation** (ridge, lasso) quand les variables sont nombreuses ou corrélées : elle stabilise les coefficients, et le lasso en annule certains, ce qui sert de sélection.
- **Au-delà du linéaire** : transformation des variables, termes d'interaction, modèles non linéaires. Souvent, une transformation logarithmique suffit à rendre une relation traitable.

## Selon le métier

### Data Analyst

La régression quantifie la relation en tenant compte de plusieurs facteurs à la fois — c'est sa place dans la chaîne du diagnostic, après la corrélation et le test. Pour une grandeur continue, régression linéaire ; pour un oui-non comme la résiliation ou la fraude, [[notions/regression-logistique]]. Le livrable n'est pas le modèle, c'est la phrase qu'il permet d'écrire, avec son incertitude.

### BI Analyst

L'usage courant est la mesure de contribution : quelle part d'une variation s'explique par quel facteur. Le risque propre au contexte BI est la diffusion — un coefficient publié dans un tableau de bord sera lu comme une règle d'action, sans les précautions qui l'accompagnaient. Si le modèle doit vivre, il doit être recalculé et documenté comme n'importe quelle mesure.

> [!warning] Piège
> Interpréter les coefficients d'un modèle qu'on n'a pas diagnostiqué. Le résultat s'affiche toujours, quelles que soient les données : une relation non linéaire, des résidus structurés ou une variable influente produisent des coefficients parfaitement lisibles et faux. Le graphique des résidus se regarde avant le tableau des coefficients, pas après.

## Pour aller plus loin

- [What Is Linear Regression? — IBM](https://www.ibm.com/think/topics/linear-regression) — le cadrage, sans formalisme excessif.
- [Linear Models — scikit-learn](https://scikit-learn.org/stable/modules/linear_model.html) — l'implémentation et la régularisation, avec la théorie en regard.
- [Sklearn Linear Regression: A Complete Guide with Examples](https://www.datacamp.com/tutorial/sklearn-linear-regression) — la mise en pratique bout en bout.
- [Nonlinear regression — Wikipédia](https://en.wikipedia.org/wiki/Nonlinear_regression) — quand la linéarité ne tient plus.

## Appelée par

- [[parcours/data-analyst/index|Data Analyst]]
- [[parcours/bi-analyst|BI Analyst]]

Voisines : [[notions/regression-logistique]], [[notions/analyse-correlation]], [[notions/tests-hypotheses]], [[notions/apprentissage-supervise]].
