---
tags: [notion, regression-logistique, classification, odds-ratio, statistiques]
date: 2026-09-16
statut: actif
appelee-par: [data-analyst]
---

# Régression logistique

Modèle qui estime la probabilité d'un événement binaire à partir de variables explicatives, en modélisant le logarithme de la cote (le rapport entre probabilité de survenue et de non-survenue) comme une combinaison linéaire.

## À quoi ça sert

C'est le premier choix pour toute question en oui/non : ce client va-t-il résilier, cette facture sera-t-elle impayée, ce dossier sera-t-il requalifié. Elle produit une probabilité — donc un score qu'on peut trier — et non une simple étiquette, ce qui est exactement ce dont on a besoin pour prioriser un traitement.

Son avantage décisif n'est pas la performance : sur beaucoup de jeux tabulaires, un gradient boosting fait mieux. C'est **l'explicabilité**. Chaque variable a un coefficient, interprétable en rapport de cotes, qu'on peut présenter et discuter. Dans un contexte où la décision affecte une personne — refus, relance, contrôle — c'est souvent une exigence et pas une préférence.

Elle sert enfin de référence honnête : un modèle sophistiqué qui ne bat pas une régression logistique bien construite ne mérite pas la dette qu'il apporte.

## Ce qu'il faut savoir

- **La sortie est une probabilité**, pas une classe. Le seuil de décision est un choix métier — il encode l'arbitrage entre faux positifs et faux négatifs, et il se fixe avec celui qui subira les conséquences.
- **Interprétation** : un coefficient positif augmente la cote de l'événement. Son exponentielle est un rapport de cotes, qu'on ne doit pas lire comme un rapport de probabilités quand l'événement est fréquent.
- **Le déséquilibre des classes** est la norme sur les cas intéressants. Il ne s'agit pas d'un défaut à corriger systématiquement : le rééchantillonnage déforme les probabilités prédites, ce qui gêne dès qu'on veut les interpréter.
- **La séparation complète** — une variable qui prédit parfaitement l'issue — fait diverger les coefficients. C'est presque toujours le signe d'une fuite de données.
- **Les variables catégorielles** s'encodent en indicatrices, avec une modalité de référence ; les modalités très rares se regroupent sous peine de coefficients absurdes.
- **Calibration** : un modèle peut bien classer et mal estimer les probabilités. Si le chiffre est utilisé comme probabilité — pour un calcul d'espérance, une provision —, la calibration se vérifie.
- **La régularisation** stabilise quand les variables sont nombreuses ou corrélées, au prix d'une interprétation un peu moins directe.
- **Évaluer avec les bonnes métriques** : aire sous la courbe ROC pour le classement, précision-rappel quand la classe positive est rare. Voir [[notions/metriques-evaluation-ml]].

## Selon le métier

### Data Analyst

Le premier choix, et souvent le dernier : elle donne des coefficients qu'on peut expliquer en réunion, ce qui vaut plus que quelques points de performance sur la plupart des demandes réelles. La métrique et le seuil se choisissent **avec le métier avant d'entraîner quoi que ce soit**, parce qu'ils encodent un arbitrage qui n'est pas une décision technique.

> [!info] Une seule appelante
> Notion appelée par le seul parcours Data Analyst ; le registre la rattache également au parcours Machine Learning du corpus.

> [!warning] Piège
> Prendre 0,5 comme seuil parce que c'est la valeur par défaut. Sur un phénomène rare, presque aucune observation ne dépasse 0,5 et le modèle « ne prédit jamais rien » — alors qu'il classe peut-être très bien. Le seuil se choisit sur la courbe, en fonction du volume que l'équipe peut réellement traiter.

## Pour aller plus loin

- [Everything you need to know about Logistic Regression](https://www.spiceworks.com/tech/artificial-intelligence/articles/what-is-logistic-regression/) — le cadrage complet, sans formalisme lourd.
- [Linear Models — scikit-learn](https://scikit-learn.org/stable/modules/linear_model.html) — l'implémentation, y compris la régularisation.
- [What is a Confusion Matrix in Machine Learning?](https://www.datacamp.com/tutorial/what-is-a-confusion-matrix-in-machine-learning) — pour choisir le seuil en connaissance de cause.

## Appelée par

- [[parcours/data-analyst|Data Analyst]]

Voisines : [[notions/regression-lineaire]], [[notions/metriques-evaluation-ml]], [[notions/apprentissage-supervise]].
