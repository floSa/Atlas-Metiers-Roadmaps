---
title: Exploration des données
---

Niveau attendu : **autonomie**. Aucune étape en aval ne rattrape une fuite laissée ici, et l'arbitrage sur ce qu'on écarte se défend devant le métier qui a produit la donnée.

L'étape où l'on découvre que le jeu de données ne contient pas ce que le cahier des charges affirme : colonnes remplies à 3 %, dates au format américain une année sur deux, variable qui prédit parfaitement la cible parce qu'elle est calculée après. C'est le temps investi qui rapporte le plus.

```mermaid
flowchart TD
  COL["Collecte de données<br/>d'où vient la table, et ce qu'elle a perdu"]
  QUA["Qualité des données<br/>manquants, doublons, incohérences, tests"]
  LIG["Lignage des données<br/>remonter à la source d'une anomalie"]
  COR["Analyse de corrélation<br/>structure, redondance, colinéarité"]
  NSU["Apprentissage non supervisé<br/>réduction de dimension et structure latente"]
  VIZ["Visualisation de données<br/>voir avant de résumer"]

  click COL "/notions/collecte-de-donnees"
  click QUA "/notions/qualite-des-donnees"
  click LIG "/notions/lignage-des-donnees"
  click COR "/notions/analyse-correlation"
  click NSU "/notions/apprentissage-non-supervise"
  click VIZ "/notions/visualisation-de-donnees"
```

## Ce qu'il faut savoir faire

- **Comprendre le mécanisme d'une valeur manquante avant de l'imputer.** Une absence aléatoire, une absence liée à une variable observée et une absence liée à la valeur elle-même n'appellent pas le même traitement. Souvent l'absence est un signal, et la bonne réponse est un indicateur de manque plutôt qu'une moyenne.
- **Distinguer une aberration de mesure d'une queue lourde légitime.** Écrêter une distribution de revenus ou de montants de sinistres détruit exactement l'information la plus utile. La question n'est pas « cette valeur est-elle extrême » mais « cette valeur est-elle possible ».
- **Choisir un encodage selon la cardinalité** : indicatrices pour les faibles, encodage par la cible avec validation croisée interne pour les fortes, ordinal seulement lorsque l'ordre existe réellement dans le métier.
- **Visualiser avant de résumer.** Le quartet d'Anscombe et le datasaurus rappellent que des distributions radicalement différentes partagent moyenne, variance et corrélation. Un nuage de points révèle des ruptures qu'aucun coefficient ne montre.
- **Construire des variables plutôt qu'empiler des modèles.** Agrégations temporelles, ratios, écarts à une référence de groupe, variables de calendrier : c'est la source de gain la plus rentable sur données tabulaires, et de loin.
- **Transformer un constat d'exploration en test exécuté à chaque exécution du pipeline.** Un intervalle de valeurs attendu, un taux de manquants maximal, une unicité de clé : l'hypothèse implicite devient une assertion qui échoue bruyamment quand la source change.
- **Chercher la fuite activement.** Colonne dérivée de la cible, agrégation calculée sur le jeu complet avant découpage, identifiant encodant l'ordre chronologique.

> [!tip] Ce qui a changé
> Le profilage automatisé fait gratuitement les deux premières heures d'exploration : un rapport complet des distributions, des manquants et des corrélations en une commande. L'apport réel n'est pas le gain de temps mais le passage à l'étape suivante — les bibliothèques de contrats de données transforment les constats en attentes vérifiées à chaque exécution, ce qui déplace la détection d'anomalie de la découverte tardive vers l'échec immédiat.

> [!warning] Piège
> La fuite par variable construite. Symptôme typique : une aire sous la courbe de 0,99 en validation, qui s'effondre en production. Toute statistique servant à transformer les variables — moyenne d'imputation, paramètres de mise à l'échelle, encodage par la cible — doit être ajustée sur le seul jeu d'entraînement, à l'intérieur du pipeline, et recalculée à chaque pli de validation.

## Les notions mobilisées

- [[notions/collecte-de-donnees]] — la provenance et les métadonnées d'extraction expliquent la plupart des anomalies qu'on croit intrinsèques à la donnée.
- [[notions/qualite-des-donnees]] — les propriétés à vérifier et la façon de les transformer en tests plutôt qu'en constats ponctuels.
- [[notions/lignage-des-donnees]] — ce qui permet de remonter d'une valeur suspecte à la transformation qui l'a produite, au lieu de la corriger à l'aveugle.
- [[notions/analyse-correlation]] — la lecture de la structure entre variables, et la détection de redondances qui déstabiliseront les coefficients.
- [[notions/apprentissage-non-supervise]] — l'analyse en composantes principales pour la structure, les projections non linéaires pour visualiser des représentations denses.
- [[notions/visualisation-de-donnees]] — ici comme outil de diagnostic, pas de communication : les deux usages n'appellent pas les mêmes graphiques.

## Pour apprendre

- [Data Preparation and Feature Engineering](https://developers.google.com/machine-learning/data-prep) — le guide court de Google sur la construction de variables et les pièges de préparation.
- [scikit-learn — Common pitfalls and recommended practices](https://scikit-learn.org/stable/common_pitfalls.html) — la page qui traite explicitement la fuite par préparation et le mauvais usage du découpage.
- [Data Leakage — Kaggle Learn](https://www.kaggle.com/code/alexisbcook/data-leakage) — la leçon courte et concrète, avec les deux formes classiques de fuite et leur détection.
- [ydata-profiling](https://docs.profiling.ydata.ai/latest/) — le profilage automatisé d'un jeu de données en une commande.
- [Pandera](https://pandera.readthedocs.io/en/stable/) et [Great Expectations](https://docs.greatexpectations.io/docs/home/) — deux façons de figer les hypothèses d'exploration en contrats vérifiés.
- [Tutoriel seaborn](https://seaborn.pydata.org/tutorial.html) — l'exploration graphique rapide, à compléter par [matplotlib](https://matplotlib.org/stable/users/index.html) pour le contrôle fin.
