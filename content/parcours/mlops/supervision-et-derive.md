---
title: Supervision et dérive
tags: [parcours, mlops, monitoring, drift, prometheus, evidently, finops]
date: 2026-09-16
statut: actif
source: https://roadmap.sh/mlops
---

**Référence.** Second domaine de référence, parce que personne d'autre ne regarde la dérive : l'exploitation surveille la latence, le data scientist est déjà sur le modèle suivant, et un service parfaitement sain peut répondre faux pendant des mois sans qu'une seule alerte se déclenche.

Un service de prédiction peut être parfaitement sain du point de vue de l'infrastructure — latence nominale, zéro erreur — tout en produisant des réponses devenues fausses. C'est la spécificité du sujet : trois couches à surveiller, et seule la troisième intéresse le métier.

```mermaid
flowchart TD
  OB["Observabilité<br/>métriques, journaux, traces"]
  ME["Métriques d'évaluation ML<br/>la couche que l'infra ne voit pas"]
  QU["Qualité des données<br/>la dérive commence presque toujours là"]
  ST["Séries temporelles<br/>lire une dérive sans crier au loup"]
  CO["Coût et latence d'inférence<br/>le coût par prédiction est une métrique de premier plan"]

  click OB "/notions/observabilite"
  click ME "/notions/metriques-evaluation-ml"
  click QU "/notions/qualite-des-donnees"
  click ST "/notions/series-temporelles"
  click CO "/notions/cout-et-latence-inference"
```

## Trois couches, et deux dérives à ne pas confondre

La couche **système** répond « est-ce que ça tourne » : latence, erreurs, saturation. La couche **données** répond « est-ce qu'on lui donne ce qu'il attend » : distribution des entrées, valeurs manquantes, nouvelles modalités. La couche **qualité prédictive** répond « est-ce que c'est encore juste ». Seule la dernière dit quelque chose au métier, et c'est celle qu'on instrumente en dernier.

La **dérive des données** est un changement de distribution des entrées : elle se détecte immédiatement, feature par feature, avec un indice de stabilité de population, un test de Kolmogorov-Smirnov ou une distance entre distributions. La **dérive de concept** est un changement de la relation entre entrées et cible : elle ne se détecte qu'avec la vérité terrain, souvent disponible avec des semaines de retard. En attendant, on surveille des substituts — taux d'acceptation, distribution des scores, taux d'appel à la procédure de secours, taux de correction manuelle.

## Ce qu'il faut savoir faire

- **Tenir un tableau de bord par modèle, avec quatre panneaux** : trafic, latence au 95e centile, distribution des prédictions, indicateur de dérive. Au-delà, personne ne regarde, et un tableau que personne ne regarde est pire qu'aucun tableau.
- **Instrumenter par version de modèle.** Sans cette étiquette, une comparaison avant-après est impossible et un déploiement progressif est aveugle.
- **N'alerter que sur les features à forte importance.** Tester la dérive sur deux cents colonnes produit deux cents alertes par semaine, dont l'astreinte apprend à ignorer la totalité.
- **Dériver la cadence de ré-entraînement de la vitesse de dérive mesurée**, pas d'une intuition. Beaucoup d'équipes réentraînent chaque nuit un modèle qui dérive sur six mois : elles paient du calcul et s'exposent à une régression à chaque itération.
- **Suivre le coût par prédiction à côté de la latence.** Une inférence qui coûte plus que la valeur qu'elle produit est un incident, même si tous les voyants sont verts.
- **Relier chaque alerte à une conséquence métier estimée.** Une alerte qui ne dit pas ce qu'elle coûte ne sera pas traitée.

> [!tip] Ajout 2026
> **Evidently** et **NannyML** sont devenus les outils par défaut sur la dérive, le second apportant l'estimation de performance sans vérité terrain — utile précisément quand les étiquettes arrivent tard. **OpenTelemetry** s'est imposé comme socle commun de traces, métriques et journaux, ce qui permet de suivre une requête depuis l'API jusqu'à l'inférence dans un seul système au lieu de recoller trois outils à la main.

> [!warning] Piège
> Alerter sur la dérive statistique brute. Sur des volumes importants, n'importe quel test de distribution devient significatif pour un écart sans effet pratique. Couplez systématiquement taille d'effet et impact estimé sur la métrique métier — sinon l'astreinte apprend à ignorer les alertes du modèle, et l'apprentissage est définitif.

## Les notions mobilisées

- [[notions/observabilite]] — métriques, journaux et traces ; la couche infrastructure est nécessaire et ne dit rien de la justesse.
- [[notions/metriques-evaluation-ml]] — recalculées en production dès que la vérité terrain arrive, et ventilées par segment.
- [[notions/qualite-des-donnees]] — la plupart des dérives détectées sont en réalité des ruptures d'une source en amont.
- [[notions/series-temporelles]] — tendance, saisonnalité et effets de calendrier : ce qui distingue une vraie dérive d'un lundi de janvier.
- [[notions/cout-et-latence-inference]] — le coût par prédiction, devenu un indicateur de supervision au même titre que la latence.

## Pour apprendre

- [Prometheus — Getting Started](https://prometheus.io/docs/tutorials/getting_started/) — instrumenter un service et écrire ses premières alertes.
- [Grafana Docs](https://grafana.com/docs/) — construire le tableau de bord à quatre panneaux et ses règles d'alerte.
- [Evidently — Documentation](https://docs.evidentlyai.com/) — les rapports de dérive et de qualité, en libre.
- [NannyML — Documentation](https://nannyml.readthedocs.io/en/stable/) — l'estimation de performance sans vérité terrain, et ses hypothèses.
- [OpenTelemetry — Documentation](https://opentelemetry.io/docs/) — le socle commun de traces et de métriques, à poser avant de choisir un outil de visualisation.
- [Difference Between Observability and Monitoring](https://aws.amazon.com/compare/the-difference-between-monitoring-and-observability/) — la distinction, courte, à avoir en tête avant d'outiller.
