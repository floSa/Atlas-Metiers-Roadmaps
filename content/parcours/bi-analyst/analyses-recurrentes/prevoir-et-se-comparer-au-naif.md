---
title: Prévoir et se comparer au naïf
---

La référence à battre est toujours la prévision naïve : la même valeur que la même période l'an dernier, ou la dernière valeur connue. Beaucoup de modèles sophistiqués ne la battent pas, et le savoir évite de porter une dette de maintenance pour rien.

```mermaid
flowchart LR
  N["Prévision naïve<br/>même période l'an dernier"] --> C["Comparaison d'erreur"]
  M["Modèle candidat"] --> C
  C --> D{"Gain significatif ?"}
  D -->|non| A["Garder le naïf"]
  D -->|oui| B["Assumer la maintenance"]
```

## Ce qu'il faut savoir faire

- Publier l'erreur de la prévision contre la référence naïve, systématiquement et au même endroit que la prévision elle-même. Une prévision sans cette comparaison n'est pas évaluable.
- Établir la référence naïve **avant** de construire quoi que ce soit. Elle prend une heure, elle est parfois suffisante, et elle fixe le seuil au-dessous duquel un modèle ne se justifie pas.
- Chiffrer le coût de maintenance d'une prévision avant de s'y engager. Un modèle à réentraîner, à surveiller et à expliquer n'est plus de la BI, et sa maintenance coûte généralement plus que sa construction.
- Prévoir l'activité plutôt que classer. Depuis ce poste, la prévision qui sert réellement porte sur des séries d'activité — volume, chiffre d'affaires, charge — pas sur un modèle de classification.
- Publier une prévision avec son intervalle, jamais comme un nombre unique. Un point de prévision présenté seul sera traité comme un engagement, et la conversation suivante portera sur l'écart plutôt que sur la décision.
- Savoir passer la main. Dès que le modèle doit être réentraîné, surveillé et expliqué, le sujet change de métier ; le rôle du BI Analyst devient de fournir l'historique propre et de restituer les résultats.

## Les notions mobilisées

- [[notions/series-temporelles]] — la prévision, sa référence naïve, et la façon de mesurer l'écart.
- [[notions/apprentissage-supervise]] — ce qu'implique réellement un modèle prédictif, avant de promettre d'en livrer un.
- [[notions/metriques-evaluation-ml]] — les mesures d'erreur, et ce qu'elles disent réellement d'une prévision.
- [[notions/roi-des-projets-ia]] — la maintenance d'un modèle se chiffre au même titre que sa construction.

> [!tip] La comparaison qui tranche la discussion
> Afficher côte à côte l'erreur du modèle et celle du naïf sur les douze derniers mois. Dans un grand nombre de cas, l'écart ne justifie pas la maintenance — et ce constat, montré plutôt qu'affirmé, met fin à la demande de prévision sophistiquée sans conflit.

## Pour apprendre

- [Engineering Statistics Handbook, séries temporelles — NIST](https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc4.htm) — les modèles classiques et leur évaluation.
- [A Refresher on Regression Analysis — HBR](https://hbr.org/2015/11/a-refresher-on-regression-analysis) — le rappel court, utile avant de discuter d'une extrapolation.
- [Machine Learning Crash Course — Google](https://developers.google.com/machine-learning/crash-course/classification) — pour mesurer ce qu'un vrai modèle prédictif exige.
