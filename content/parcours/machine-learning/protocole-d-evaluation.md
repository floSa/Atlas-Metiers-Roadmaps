---
title: Protocole d'évaluation
---

Niveau attendu : **référence**. Le chiffre annoncé n'engage que celui qui l'a produit, et personne en aval ne saura dire qu'il est faux : c'est le domaine où il faut faire autorité dans la salle.

La section qui distingue un travail sérieux d'une démonstration. Un protocole faux produit un chiffre flatteur et un modèle qui s'effondre en production, sans qu'aucune alerte ne se déclenche. L'ordre correct est invariable : définir la métrique et la validation d'abord, entraîner ensuite.

```mermaid
flowchart TD
  MET["Métriques d'évaluation ML<br/>matrice de confusion, précision, rappel, AUC"]
  TES["Tests d'hypothèses<br/>l'écart entre deux modèles est-il réel"]
  QUA["Qualité des données<br/>l'audit de fuite commence ici"]
  SER["Séries temporelles<br/>pourquoi le découpage aléatoire est faux"]
  ABT["A/B testing<br/>la seule mesure qui vaut après mise en service"]

  click MET "/notions/metriques-evaluation-ml"
  click TES "/notions/tests-hypotheses"
  click QUA "/notions/qualite-des-donnees"
  click SER "/notions/series-temporelles"
  click ABT "/notions/ab-testing"
```

## Ce qu'il faut savoir faire

- **Lire la matrice de confusion avant toute métrique agrégée.** Elle montre quelles classes sont confondues avec quelles autres, information qu'aucun score unique ne restitue. L'exactitude, elle, est trompeuse dès que les classes sont déséquilibrées : à 1 % de positifs, prédire toujours « négatif » donne 99 %.
- **Choisir entre précision et rappel selon le coût des deux erreurs.** La précision mesure le coût des faux positifs, le rappel celui des faux négatifs. Leur moyenne harmonique est commode pour comparer, mais elle masque le compromis exact et suppose que les deux erreurs ont la même valeur, ce qui est rarement le cas.
- **Préférer l'aire sous la courbe précision-rappel quand les positifs sont rares.** L'aire sous la courbe ROC reste optimiste dans ce régime, les vrais négatifs abondants gonflant le score.
- **Utiliser la perte logarithmique quand la sortie sert à décider.** Elle pénalise les probabilités mal calibrées et pas seulement les erreurs de classe — indispensable dès qu'un seuil métier ou une espérance de gain repose sur le score.
- **Tracer une courbe de calibration** pour vérifier qu'une probabilité annoncée de 0,8 correspond bien à 80 % de cas positifs. Sans cette vérification, un score n'est qu'un classement.
- **Valider par découpage adapté à la structure des données** : croisé stratifié en classification déséquilibrée, temporel sur des séries, par groupe quand plusieurs lignes viennent d'une même entité. Le cas limite où chaque observation est un pli a un biais faible, une variance élevée et un coût prohibitif ; il est réservé aux très petits jeux.
- **Emboîter la validation quand on règle des hyperparamètres.** Sans cela, la performance rapportée intègre le réglage et devient optimiste, parfois de plusieurs points.
- **Rapporter un intervalle plutôt qu'un point**, par rééchantillonnage du jeu de test.

> [!warning] Piège
> La fuite de données, sous ses trois formes courantes : prétraitement ajusté avant le découpage ; variable calculée à partir d'informations postérieures à l'instant de prédiction ; lignes corrélées réparties entre entraînement et test. Le test de dépistage tient en une phrase — une performance nettement supérieure aux attentes du métier est presque toujours une fuite, pas une réussite. Chercher la fuite avant de célébrer, et considérer que le jeu de test est contaminé dès qu'une décision a été prise en le regardant.

## Les notions mobilisées

- [[notions/metriques-evaluation-ml]] — le catalogue des métriques et, surtout, le type d'erreur que chacune privilégie.
- [[notions/tests-hypotheses]] — pour transformer « mon modèle est meilleur » en affirmation défendable plutôt qu'en impression.
- [[notions/qualite-des-donnees]] — l'audit de fuite est un cas particulier de contrôle de qualité, et il se mène avec les mêmes outils.
- [[notions/series-temporelles]] — la structure temporelle interdit le découpage aléatoire et impose un backtest avec intervalle de disponibilité.
- [[notions/ab-testing]] — la performance hors échantillon ne dit rien de l'effet réel ; seule l'expérience contrôlée le mesure.

## Pour apprendre

- [scikit-learn — sélection et évaluation de modèle](https://scikit-learn.org/stable/model_selection.html) — la partie du guide utilisateur qui vaut d'être lue intégralement, une fois.
- [Validation croisée imbriquée — exemple commenté](https://scikit-learn.org/stable/auto_examples/model_selection/plot_nested_cross_validation_iris.html) — la démonstration chiffrée de l'écart entre validation simple et validation imbriquée.
- [Model Evaluation, Model Selection, and Algorithm Selection in Machine Learning](https://arxiv.org/abs/1811.12808) — la synthèse de référence sur les protocoles, leurs biais et leurs conditions d'emploi.
- [Calibration des probabilités](https://scikit-learn.org/stable/modules/calibration.html) — pourquoi un score n'est pas une probabilité, et comment le corriger.
- [ROC et AUC expliquées visuellement](https://mlu-explain.github.io/roc-auc/) — l'intuition géométrique du seuil et du classement, en quelques minutes.
- [Data Leakage — Kaggle Learn](https://www.kaggle.com/code/alexisbcook/data-leakage) — les deux formes classiques de fuite sur un cas concret.
