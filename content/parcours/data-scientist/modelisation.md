---
title: Modélisation
---

Le cœur opérationnel du métier. Sur données tabulaires — la très grande majorité des problèmes en entreprise — la difficulté n'est pas l'algorithme, disponible en trois lignes, mais le protocole : un jeu de validation représentatif, une métrique alignée sur la décision, et la discipline de ne pas optimiser sur le test.

```mermaid
flowchart TD
  SUP["Apprentissage supervisé<br/>la grande majorité des modèles déployés"]
  NSU["Apprentissage non supervisé<br/>segmentation et détection d'anomalie"]
  LOG["Régression logistique<br/>la référence à battre en classification"]
  MET["Métriques d'évaluation ML<br/>choisir l'erreur qu'on accepte"]
  TES["Tests d'hypothèses<br/>un écart entre deux modèles est-il réel"]

  click SUP "/notions/apprentissage-supervise"
  click NSU "/notions/apprentissage-non-supervise"
  click LOG "/notions/regression-logistique"
  click MET "/notions/metriques-evaluation-ml"
  click TES "/notions/tests-hypotheses"
```

## Ce qu'il faut savoir faire

- **Choisir la métrique avant le modèle.** L'exactitude sur classes déséquilibrées ne veut rien dire ; l'aire sous la courbe précision-rappel est plus informative que l'aire sous la courbe ROC quand les positifs sont rares ; l'erreur quadratique et l'erreur absolue n'ont pas la même sensibilité aux valeurs extrêmes. Choisir après, c'est choisir celle qui arrange.
- **Poser une référence triviale et la battre.** Classe majoritaire, moyenne, valeur de la veille. Un modèle qui ne dépasse pas significativement cette référence n'est pas un modèle, et le cas se présente plus souvent qu'on ne l'admet.
- **Calibrer quand le score sert à décider.** Un modèle mal calibré donne des scores inutilisables comme probabilités. Dès que le score alimente un seuil métier ou un calcul d'espérance de gain, une recalibration est nécessaire, et la courbe de calibration doit figurer dans le rapport.
- **Traiter le déséquilibre dans le bon ordre** : d'abord la métrique et le seuil, ensuite les poids de classes, en dernier recours seulement le rééchantillonnage synthétique — surutilisé, et qui dégrade généralement la calibration.
- **Ajuster le seuil de décision sur le coût métier.** Un faux négatif et un faux positif ont rarement le même prix ; cet ajustement rapporte presque toujours davantage que cent itérations de recherche d'hyperparamètres.
- **Fixer un budget d'optimisation à l'avance** et préférer une recherche bayésienne à une grille exhaustive, avec trois jeux séparés ou une validation croisée imbriquée.
- **Interpréter sans surinterpréter.** Les attributions de contribution expliquent la sortie du modèle, pas le monde : ce sont des décompositions de prédiction, jamais des effets causaux.
- **Valider la stabilité d'une segmentation** en la rejouant sur des sous-échantillons et en mesurant la concordance. Si les groupes changent d'un tirage à l'autre, la segmentation décrit du bruit.

> [!tip] Ce qui a changé
> Deux évolutions sur le tabulaire. Les modèles pré-entraînés par inférence en contexte atteignent, sur des jeux de taille petite à moyenne, des performances comparables à un gradient boosting réglé, sans entraînement — une excellente référence instantanée. Et les modèles de langage se sont révélés médiocres en prédiction tabulaire mais très bons en extraction d'attributs structurés depuis du texte libre. L'architecture pertinente devient souvent hybride : extraction par le modèle de langage, prédiction par un modèle d'arbres.

> [!warning] Piège
> Optimiser les hyperparamètres sur le jeu de test. Après vingt itérations, le score de test n'est plus une estimation de généralisation mais un score d'entraînement déguisé. Le test s'ouvre une seule fois, à la fin, et le chiffre qui en sort est celui qu'on annonce — même s'il est moins joli que celui de la validation.

## Les notions mobilisées

- [[notions/apprentissage-supervise]] — la famille qui couvre la quasi-totalité des modèles réellement mis en service, et ses conditions de validité.
- [[notions/apprentissage-non-supervise]] — segmentation et détection d'anomalie, où l'absence de métrique arbitre impose une validation externe.
- [[notions/regression-logistique]] — rapide, interprétable, naturellement calibrée : la référence qu'un modèle plus lourd doit justifier de dépasser.
- [[notions/metriques-evaluation-ml]] — le choix de métrique comme arbitrage métier explicite, pas comme réglage technique.
- [[notions/tests-hypotheses]] — pour dire si l'écart de performance entre deux modèles tient, ou s'il relève du hasard d'échantillonnage.

## Pour apprendre

- [Guide utilisateur scikit-learn](https://scikit-learn.org/stable/user_guide.html) — à lire comme un cours ; la partie [sélection et évaluation de modèle](https://scikit-learn.org/stable/model_selection.html) vaut d'être parcourue intégralement.
- [Calibration des probabilités](https://scikit-learn.org/stable/modules/calibration.html) — la page qui explique pourquoi un score n'est pas une probabilité, et comment le corriger.
- [An Introduction to Statistical Learning](https://www.statlearning.com/) — les chapitres sur les arbres, les méthodes d'ensemble et la régularisation, avec les intuitions géométriques.
- [Why do tree-based models still outperform deep learning on tabular data?](https://arxiv.org/abs/2207.08815) — l'article qui documente, sur un banc d'essai sérieux, pourquoi le gradient boosting reste la référence sur tabulaire.
- [Optuna](https://optuna.readthedocs.io/en/stable/) et [SHAP](https://shap.readthedocs.io/en/latest/) — la recherche d'hyperparamètres sous budget et les attributions de contribution, avec leurs limites documentées.
