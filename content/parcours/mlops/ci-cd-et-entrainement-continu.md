---
title: CI/CD et entraînement continu
tags: [parcours, mlops, ci-cd, cml, continuous-training, tests-ml]
date: 2026-09-16
statut: actif
source: https://roadmap.sh/mlops
---

En logiciel, la chaîne d'intégration valide que le code compile et que les tests passent. En ML il faut ajouter deux portes, faute de quoi elle donne une fausse assurance : tout est vert et le modèle est pire.

```mermaid
flowchart TD
  CI["Intégration continue<br/>le socle qu'on étend"]
  TE["Tests logiciels<br/>plus trois tests propres au ML"]
  QU["Qualité des données<br/>la première porte ajoutée"]
  ME["Métriques d'évaluation ML<br/>la seconde porte : mieux que le modèle en place ?"]
  CT["Conteneurisation<br/>l'image construite à chaque passage"]

  click CI "/notions/integration-continue"
  click TE "/notions/tests-logiciels"
  click QU "/notions/qualite-des-donnees"
  click ME "/notions/metriques-evaluation-ml"
  click CT "/notions/conteneurisation"
```

## Les deux portes que le ML ajoute

La première : **les données entrantes sont-elles conformes au schéma attendu ?** Contrôle de schéma, de plages, de taux de nuls, de volumétrie, exécuté avant l'entraînement et bloquant.

La seconde : **le nouveau modèle est-il meilleur que celui en place, sur un jeu de référence figé ?** Pas meilleur que la veille, pas meilleur en moyenne sur un jeu qui bouge : meilleur sur le même jeu, avec un seuil décidé à l'avance et écrit dans la configuration.

L'enchaînement complet, dans l'ordre : contrôle de style et tests unitaires, construction de l'image, tests de données et de schéma, entraînement sur un exécuteur adapté, évaluation contre le modèle en place, publication au registre, déploiement progressif.

## Trois tests que seul le ML demande

**Non-régression** sur un jeu de référence annoté : la sortie ne doit pas se dégrader sur des cas dont on connaît la réponse. **Invariance** : une perturbation qui ne doit rien changer — une casse, un espace, un identifiant technique — ne change effectivement rien. **Directionnel** : une perturbation qui doit déplacer la prédiction dans un sens connu le fait bien. Ces trois-là attrapent des défauts qu'aucune métrique agrégée ne montre.

## Ce qu'il faut savoir faire

- **Rendre l'évaluation visible là où la décision se prend** : métriques, matrice de confusion et courbes publiées dans la demande de fusion, pas dans un tableau de bord que personne n'ouvre.
- **Brancher des exécuteurs auto-hébergés** dès qu'il faut un GPU, et borner leur coût — un entraînement déclenché à chaque commit sur une branche de travail vide un budget en une semaine.
- **Faire produire à l'entraînement continu un modèle candidat, jamais un modèle promu.** La promotion reste une décision explicite adossée à une évaluation comparative. C'est la règle qui évite les catastrophes automatisées.
- **Déclencher sur un signal, pas sur un commit** : dérive détectée, volume de nouvelles étiquettes atteint, ou calendrier. Le code d'un modèle ne change pas souvent ; ses données, tous les jours.
- **Utiliser l'authentification fédérée entre la chaîne d'intégration et le fournisseur cloud** plutôt que des clés statiques stockées en variables.

> [!tip] Ajout 2026
> Le troisième C — **Continuous Training** — s'est standardisé et c'est le principal écart avec le DevOps classique. Le pipeline d'entraînement devient un service déclenché par un signal, avec sa propre supervision et son propre budget. Deux garde-fous le rendent sûr : un candidat n'est jamais promu automatiquement, et chaque exécution enregistre l'identifiant du jeu de données qui l'a déclenchée, sans quoi on ne saura pas expliquer a posteriori pourquoi un modèle a changé.

> [!warning] Piège
> Entraîner dans la chaîne d'intégration avec un jeu de test régénéré à chaque passage. Les deux modèles comparés ne sont alors pas évalués sur la même chose, et l'écart mesuré est du bruit. Le jeu d'évaluation est un artefact versionné, au même titre que le code.

## Les notions mobilisées

- [[notions/integration-continue]] — le socle qu'on étend ; tout ce qui vaut pour le logiciel reste vrai, rien n'y suffit.
- [[notions/tests-logiciels]] — auxquels s'ajoutent non-régression, invariance et test directionnel, propres au ML.
- [[notions/qualite-des-donnees]] — sous sa forme de porte bloquante, exécutée avant l'entraînement.
- [[notions/metriques-evaluation-ml]] — le critère de promotion, et le seuil qui doit être écrit avant de voir le résultat.
- [[notions/conteneurisation]] — l'image construite à chaque passage est ce qui rendra l'entraînement rejouable ailleurs.

## Pour apprendre

- [Continuous Delivery for Machine Learning](https://martinfowler.com/articles/cd4ml.html) — la référence sur la CI/CD appliquée au ML, avec un exemple complet.
- [CML — Get Started](https://cml.dev/doc/start) — publier métriques et courbes directement dans la demande de fusion.
- [GitHub Actions Documentation](https://docs.github.com/en/actions) — la chaîne de livraison et ses exécuteurs auto-hébergés pour le GPU.
- [GitLab CI/CD Examples](https://docs.gitlab.com/ee/ci/examples/) — l'équivalent en environnement auto-hébergé, registre d'images inclus.
- [MLOps: Continuous delivery and automation pipelines in machine learning](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning) — l'article d'où vient l'échelle de maturité 0/1/2.
