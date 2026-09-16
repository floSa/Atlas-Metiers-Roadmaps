---
title: Évaluation et explicabilité
tags: [parcours, mlops, evaluation, calibration, shap, cartes-modele, mlflow]
date: 2026-09-16
statut: actif
source: https://roadmap.sh/mlops
---

**Usage.** Un confirmé se sert du protocole que le data scientist a défini, sait refuser un découpage qui fuit et lit une courbe de calibration ; concevoir la métrique et produire une explication opposable sont hors de son périmètre réel, et l'explicabilité s'y tient à la notion — reconnaître le besoin, savoir qui appeler.

Reconnaître un résultat trop beau pour être vrai, mesurer ce qui compte pour le métier, et pouvoir dire pourquoi une décision a été prise : trois exigences distinctes que la même page sert.

```mermaid
flowchart TD
  ME["Métriques d'évaluation ML<br/>exactitude, rappel, AUC, et leurs limites"]
  AS["Apprentissage supervisé<br/>ce qu'on mesure, et sur quoi"]
  AB["A/B testing<br/>la seule mesure qui parle au métier"]
  GO["Gouvernance IA<br/>cartes modèle et traçabilité réglementaire"]

  click ME "/notions/metriques-evaluation-ml"
  click AS "/notions/apprentissage-supervise"
  click AB "/notions/ab-testing"
  click GO "/notions/gouvernance-ia"
```

## Quatre règles d'évaluation qui évitent la majorité des déconvenues

**Découpage temporel** pour tout ce qui a une dimension chronologique, jamais aléatoire : un découpage aléatoire sur des données datées entraîne sur le futur et flatte le score. **Calibration** des probabilités dès que la sortie alimente une décision à seuil — un score bien classé n'est pas un score bien calibré, et c'est la calibration qui détermine le point de coupure. **Métriques ventilées par segment**, parce qu'un modèle peut être excellent en moyenne et inutilisable sur les cas rares qui comptent. **Jeu d'évaluation figé et versionné**, sans quoi comparer deux modèles n'a pas de sens.

## L'explicabilité répond à deux besoins qu'on confond

Le besoin **externe** est réglementaire ou contractuel : un client, un auditeur demande pourquoi une décision a été prise. Le besoin **interne** est du débogage : les contributions de features révèlent souvent une fuite de données qu'aucune métrique n'avait montrée.

Deux familles d'outils. L'approximation locale par un modèle linéaire autour d'un point est rapide et instable — deux exécutions sur le même point peuvent différer, donc on l'utilise pour explorer, pas pour justifier. Les valeurs de Shapley sont fondées théoriquement et additives, donc agrégables en importance globale ; exactes et rapides sur les modèles à base d'arbres, coûteuses et approchées ailleurs. Dans les deux cas, une attribution n'est pas une cause : elle dit ce à quoi le modèle réagit.

## Ce qu'il faut savoir faire

- **Poser la fonction de coût métier avant d'entraîner.** Un gain de trois points de F1 qui ne déplace ni le revenu ni le coût de traitement ne justifie pas un déploiement, mais crée un risque de régression.
- **Tracer chaque exécution** — paramètres, métriques, artefacts, commit — dans un registre qui survivra au départ de la personne qui a fait l'expérience.
- **Comparer un candidat au modèle en place**, sur le même jeu figé, avant toute promotion. C'est la porte que le logiciel classique n'a pas.
- **Ventiler les métriques par sous-population** et les publier, y compris quand le résultat est gênant : c'est ce que les auditeurs demandent désormais, et c'est ce qui prévient la mauvaise surprise.
- **Rédiger une carte modèle** : usage prévu, données d'entraînement, limites connues, métriques par segment, versions déployées.

> [!tip] Ajout 2026
> La sérialisation par `pickle` est un handicap opérationnel : fragile aux versions et exécutant du code arbitraire au chargement. L'export **ONNX** pour les modèles classiques et **safetensors** pour les poids de réseaux règlent les deux problèmes et découplent l'entraînement du moteur d'exécution qui sert les prédictions. Côté explicabilité, l'entrée en application de la réglementation européenne a déplacé la demande : les auditeurs réclament moins des attributions par prédiction que des cartes modèle et une traçabilité des versions.

> [!warning] Piège
> Changer le jeu d'évaluation entre deux entraînements. La comparaison n'a alors plus aucun sens, et personne ne s'en aperçoit parce que les chiffres restent plausibles. Le jeu d'évaluation se gèle, se versionne, et son renouvellement est une décision délibérée, datée et documentée.

## Les notions mobilisées

- [[notions/metriques-evaluation-ml]] — exactitude, précision, rappel, F1, AUC ; côté MLOps, ce qui compte est leur stabilité d'une exécution à l'autre.
- [[notions/apprentissage-supervise]] — le cadre dont dépendent le découpage, la fuite de données et le sens des métriques.
- [[notions/ab-testing]] — la mesure en ligne qui relie une amélioration de modèle à un effet métier constatable.
- [[notions/gouvernance-ia]] — cartes modèle, documentation technique et traçabilité des versions, devenues des livrables attendus.

## Pour apprendre

- [scikit-learn — Metrics and scoring](https://scikit-learn.org/stable/modules/model_evaluation.html) — le tour des métriques, de leurs hypothèses et de la calibration.
- [MLflow — Documentation](https://mlflow.org/docs/latest/index.html) — suivi d'exécutions, registre, signatures : le socle de la traçabilité.
- [SHAP — Documentation](https://shap.readthedocs.io/en/latest/) — les valeurs de Shapley en pratique, et leurs coûts de calcul.
- [When Shapley Values Break](https://towardsdatascience.com/when-shapley-values-break-a-guide-to-robust-model-explainability/) — les cas où l'attribution induit en erreur.
- [ONNX — Documentation](https://onnx.ai/onnx/) — le format d'échange qui découple entraînement et exécution.
