---
tags: [notion, metriques, evaluation, classification, machine-learning]
date: 2026-09-16
statut: actif
appelee-par: [data-analyst]
---

# Métriques d'évaluation en apprentissage automatique

Mesures qui résument la performance d'un modèle sur des données qu'il n'a pas vues, chacune privilégiant un type d'erreur différent.

## À quoi ça sert

Choisir une métrique, c'est déclarer quelle erreur on accepte de faire. Sur un modèle de détection de fraude, privilégier le rappel signifie accepter de contrôler des dossiers honnêtes pour ne rien laisser passer ; privilégier la précision signifie l'inverse. Ce n'est pas un réglage technique, c'est un arbitrage métier, avec un coût réel de chaque côté.

D'où la règle qui gouverne l'usage : **la métrique se choisit avec le métier avant d'entraîner quoi que ce soit**. Choisie après, elle sera celle qui donne le meilleur chiffre, et l'évaluation ne mesurera plus rien.

Le second usage est comparatif : une métrique n'a de sens que rapportée à une référence — la règle métier existante, le traitement actuel, ou un modèle naïf. Un score de 0,82 ne dit rien tant qu'on ne sait pas ce que faisait la solution précédente.

## Ce qu'il faut savoir

- **La matrice de confusion est la source de tout** : vrais et faux positifs, vrais et faux négatifs. Toutes les métriques de classification en dérivent, et la regarder directement évite beaucoup de contresens.
- **Exactitude** : proportion de prédictions correctes. Trompeuse dès que les classes sont déséquilibrées — sur 2 % de positifs, tout prédire négatif donne 98 %.
- **Précision** : parmi les cas prédits positifs, combien le sont. **Rappel** : parmi les cas réellement positifs, combien ont été trouvés. **F1** : leur moyenne harmonique, utile comme résumé, insuffisante comme critère de décision.
- **Aire sous la courbe ROC** : qualité du classement, indépendante du seuil. Optimiste quand la classe positive est rare — préférer alors l'aire sous la courbe précision-rappel.
- **Pour la régression** : erreur absolue moyenne (robuste, dans l'unité de la variable), erreur quadratique moyenne (pénalise les grands écarts), erreur relative (comparable entre échelles, instable près de zéro). R² pour la part de variance expliquée.
- **Calibration** : un modèle peut bien ordonner et mal estimer les probabilités. Si le chiffre sert de probabilité, elle se vérifie séparément.
- **Évaluer sur des données non vues**, et chronologiquement séparées quand la donnée est temporelle.
- **La métrique technique n'est pas la métrique de décision.** Ce qui compte au final est le gain métier : dossiers évités, euros recouvrés, temps économisé.

## Selon le métier

### Data Analyst

La métrique se choisit avec le métier avant d'entraîner, parce qu'elle encode un arbitrage entre faux positifs et faux négatifs qui n'est pas une décision technique. Corollaire pratique : la question à poser au commanditaire n'est pas « quelle précision voulez-vous » mais « combien de dossiers pouvez-vous traiter par semaine, et que coûte un dossier contrôlé pour rien ». Les réponses déterminent la métrique et le seuil.

> [!info] Une seule appelante
> Notion appelée par le seul parcours Data Analyst ; le registre la rattache aussi au parcours BI Analyst du corpus. Elle est distincte de [[notions/evaluation-llm]], qui traite d'objets non déterministes et de critères d'une autre nature.

> [!warning] Piège
> Comparer deux modèles sur une métrique et oublier le seuil. Deux modèles peuvent avoir la même aire sous la courbe et des comportements très différents à l'endroit où l'on travaille réellement — les cinq cents dossiers les mieux classés. Comparer au point de fonctionnement réel, pas sur la courbe entière.

## Pour aller plus loin

- [Metrics and scoring — scikit-learn](https://scikit-learn.org/stable/modules/model_evaluation.html) — la référence, exhaustive et précise sur les définitions.
- [What is a Confusion Matrix in Machine Learning?](https://www.datacamp.com/tutorial/what-is-a-confusion-matrix-in-machine-learning) — le socle, expliqué simplement.
- [Confusion matrix — scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html) — l'implémentation et ses conventions d'axes, source d'erreurs fréquente.

## Appelée par

- [[parcours/data-analyst|Data Analyst]]

Voisines : [[notions/apprentissage-supervise]], [[notions/regression-logistique]], [[notions/evaluation-llm]].
