---
title: Tests d'hypothèses
tags: [notion, statistiques, tests, inference, p-value]
date: 2026-09-16
statut: actif
appelee-par: [data-analyst, bi-analyst]
---

Procédure qui évalue si un écart observé sur un échantillon est compatible avec l'hypothèse qu'il n'existe aucun écart réel dans la population — et rien de plus que cela.

## À quoi ça sert

Un test d'hypothèse répond à une question défensive : « ce que je vois peut-il n'être que du hasard d'échantillonnage ? ». Il ne dit pas qu'un effet existe, il dit que l'absence d'effet expliquerait mal ce qu'on observe. La nuance est capitale, parce que c'est elle qui est perdue dans la quasi-totalité des usages en entreprise.

Son utilité réelle est donc de **freiner**. Devant un écart de 3 % entre deux segments, le test empêche de construire une histoire sur du bruit. C'est un outil de prudence, pas un outil de preuve, et c'est précisément ce dont un tableau de bord a besoin.

## Ce qu'il faut savoir

- **Hypothèse nulle et alternative** : la nulle postule l'absence d'effet. On ne l'accepte jamais — on la rejette ou on échoue à la rejeter. « Non significatif » signifie « pas assez de preuve », pas « pas d'effet ».
- **La p-value** est la probabilité d'observer un écart au moins aussi grand **si la nulle est vraie**. Ce n'est ni la probabilité que la nulle soit vraie, ni la probabilité que le résultat se reproduise.
- **Les deux erreurs** : type I (conclure à un effet qui n'existe pas, contrôlée par le seuil α) et type II (rater un effet réel, contrôlée par la puissance). Baisser α augmente mécaniquement le risque de type II.
- **La puissance** dépend de la taille d'effet, de la variance et de l'effectif. Elle se calcule **avant** le recueil : un test sous-dimensionné ne démontre rien, un test surdimensionné rend significatif un écart sans portée pratique.
- **Significatif ≠ important.** Sur un million d'observations, une différence de 0,1 % est significative et sans intérêt. Publier la taille d'effet et son intervalle de confiance, pas la p-value seule.
- **L'intervalle de confiance dit plus** que le test : il donne l'ordre de grandeur de l'effet et son incertitude en une seule information.
- **Comparaisons multiples** : tester vingt segments au seuil de 5 % produit en moyenne un faux positif. Corriger (Bonferroni, Benjamini-Hochberg) ou annoncer que l'analyse est exploratoire.
- **Choisir le test selon la donnée** : comparaison de moyennes, de proportions, d'indépendance entre catégories, cas appariés. Le mauvais test sur les bonnes données donne un résultat propre et faux.

## Selon le métier

### Data Analyst

Le test dit si un écart observé est compatible avec le hasard, et c'est exactement le rôle qu'il doit garder dans le raisonnement : il vient après la corrélation, avant la régression, et il ne remplace ni l'une ni l'autre. Quand la question porte sur l'effet d'une action qu'on contrôle, le protocole expérimental reste la seule réponse propre — voir [[notions/ab-testing]].

### BI Analyst

L'usage n'est presque jamais un test formel publié, c'est une discipline de seuil : savoir quelle variation mérite une flèche sur un tableau de bord. La bande de variation habituelle d'un indicateur, calculée une fois, sert ensuite en permanence et évite de déclencher des réunions sur du bruit.

> [!warning] Piège
> Regarder les résultats en continu et s'arrêter dès que la p-value passe sous le seuil. C'est la façon la plus simple de fabriquer un résultat significatif à partir de rien : en testant assez souvent, le seuil finit toujours par être franchi par hasard. La règle d'arrêt se fixe avant, avec l'effectif cible.

## Pour aller plus loin

- [Hypothesis Testing en 4 étapes — Investopedia](https://www.investopedia.com/terms/h/hypothesistesting.asp) — la procédure, pas à pas.
- [What Is A P-Value? — Clearly Explained](https://www.youtube.com/watch?v=ukcFrzt6cHk) — dix minutes qui suffisent à ne plus se tromper sur son interprétation.
- [Confidence interval — Wikipédia](https://en.wikipedia.org/wiki/Confidence_interval) — la définition rigoureuse, utile parce que l'intervalle est mal interprété aussi souvent que la p-value.
- [Intro to Inferential Statistics — Udacity](https://www.udacity.com/course/intro-to-inferential-statistics--ud201) — cours complet si le socle manque.

## Appelée par

- [[parcours/data-analyst|Data Analyst]]
- [[parcours/bi-analyst/index|BI Analyst]]

Voisines : [[notions/statistiques-descriptives]], [[notions/ab-testing]], [[notions/analyse-correlation]].
