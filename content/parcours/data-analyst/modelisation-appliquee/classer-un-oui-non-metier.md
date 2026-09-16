---
title: Classer un oui-non métier
---

Niveau attendu : **usage**. Une régression logistique sur un chemin balisé, documentation ouverte ; au-delà, c'est le data scientist qu'on appelle.

Résiliation, impayé, requalification, fraude : la classification binaire est l'usage de modélisation le plus courant du métier. La régression logistique reste le premier choix, parce qu'elle donne des coefficients qu'on peut expliquer à celui qui décidera.

```mermaid
flowchart LR
  E["Étiquette définie avec le métier<br/>quoi, sur quelle fenêtre"] --> V["Variables antérieures au fait<br/>aucune fuite"]
  V --> M["Modèle lisible<br/>logistique, ou arbre peu profond"]
  M --> S["Seuil choisi avec le métier<br/>faux positifs contre faux négatifs"]
  S --> A["Action associée<br/>sinon le score ne sert à rien"]
```

## Ce qu'il faut savoir faire

- Définir l'étiquette avec le métier avant tout : qu'est-ce qu'une résiliation exactement, sur quelle fenêtre, à partir de quel événement. Une étiquette floue produit un modèle qui apprend le flou.
- Vérifier qu'aucune variable n'est postérieure au fait à prédire. La fuite est le mode d'échec dominant, elle produit une performance spectaculaire, et elle se détecte en listant la date de production de chaque colonne.
- Choisir le seuil avec le métier, pas au milieu. Le seuil encode l'arbitrage entre déranger un client fidèle et rater un client qui part, et cet arbitrage n'est pas une décision technique.
- Associer une action à chaque score livré. Un score sans geste prévu n'est pas utilisé — c'est ce qui distingue une analyse utile d'un exercice.
- Rester sur un modèle lisible tant que l'écart de performance n'est pas décisif. Des coefficients qu'on peut commenter valent une amélioration marginale de score que personne ne sait expliquer.
- Vérifier la stabilité dans le temps : un modèle appris sur l'an dernier peut refléter une politique commerciale qui a changé depuis. Le réentraînement régulier est une charge, et elle se dit au moment de livrer.

## Les notions mobilisées

- [[notions/regression-logistique]] — la classification binaire et les rapports de cotes, et la façon de les traduire sans les trahir.
- [[notions/apprentissage-supervise]] — le cadre général : jeu étiqueté, séparation des données, généralisation.
- [[notions/metriques-evaluation-ml]] — précision, rappel et leur arbitrage, qui portent la discussion sur le seuil.
- [[notions/donnees-sensibles]] — classer des personnes engage : un score qui influence l'accès à un service se documente et s'explique.

> [!tip] La liste des dates
> Avant d'entraîner, écrire pour chaque variable la date à laquelle sa valeur est réellement disponible dans le système. Toute variable dont la date est postérieure à celle du fait à prédire sort du modèle. Cette liste de dix lignes évite le modèle à performance parfaite qui n'a rien appris.

## Pour apprendre

- [Google ML Crash Course — Classification](https://developers.google.com/machine-learning/crash-course/classification) — seuils, matrice de confusion, compromis : exactement le bon niveau.
- [scikit-learn — Modèles linéaires](https://scikit-learn.org/stable/modules/linear_model.html) — la régression logistique et sa régularisation, expliquées sobrement.
- [statsmodels](https://www.statsmodels.org/stable/index.html) — quand on veut lire les coefficients et leurs intervalles plutôt que d'optimiser un score.
- [SHAP](https://shap.readthedocs.io/en/latest/) — l'attribution de contribution la mieux fondée, et la documentation dit ses limites.
