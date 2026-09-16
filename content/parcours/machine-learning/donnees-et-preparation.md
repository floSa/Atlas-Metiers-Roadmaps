---
title: Données et préparation
---

L'étape qui consomme le plus de temps et détermine le plus fortement la performance finale — et l'endroit précis où se produisent la majorité des fuites. Tout ce qui est décidé ici se paie deux fois : à l'évaluation, puis en production.

```mermaid
flowchart TD
  COL["Collecte de données<br/>bases, fichiers, interfaces, moissonnage"]
  SQL["SQL<br/>la source la plus fréquente en entreprise"]
  QUA["Qualité des données<br/>manquants, doublons, unités, incohérences"]
  PAN["pandas<br/>manipulation tabulaire et ses pièges"]
  DIS["Traitement distribué<br/>formats colonnes et moteurs embarqués"]
  NSU["Apprentissage non supervisé<br/>réduction de dimension et sélection"]

  click COL "/notions/collecte-de-donnees"
  click SQL "/notions/sql"
  click QUA "/notions/qualite-des-donnees"
  click PAN "/notions/pandas"
  click DIS "/notions/traitement-distribue"
  click NSU "/notions/apprentissage-non-supervise"
```

## Les formats, et à quoi chacun sert

| Format | Usage juste | Ce qu'il ne faut pas en attendre |
|---|---|---|
| CSV, tableur | échange entre humains et systèmes hétérogènes | un typage fiable — il n'y en a pas, et la date en est la première victime |
| JSON | réponses d'interfaces de programmation | une structure stable ; à aplatir tôt et à valider contre un schéma |
| Parquet | tout jeu intermédiaire ou final | un format lisible tel quel sans outil |
| Avro, ORC, Arrow | ingestion et échange en mémoire entre moteurs | un usage direct depuis un carnet de calcul |

## Ce qu'il faut savoir faire

- **Encapsuler tout le prétraitement dans un pipeline**, et passer le pipeline entier à la validation croisée. C'est la seule parade systématique à la fuite par préparation : l'ajustement du centrage, de l'imputation ou de la sélection se refait alors à chaque pli, sur le seul jeu d'entraînement.
- **Surveiller les types.** Une colonne laissée en type générique alors qu'elle devrait être numérique est la source classique de résultats faux qui ne déclenchent aucune erreur.
- **Documenter chaque décision de nettoyage.** Une imputation non tracée est une hypothèse cachée, et elle se retrouvera dans le modèle sans que personne puisse l'auditer.
- **Construire des variables plutôt que d'ajouter des couches.** Agrégations temporelles, ratios, encodages, variables de calendrier : c'est la source de gain la plus rentable en apprentissage tabulaire.
- **Mettre à l'échelle quand le modèle l'exige** — plus proches voisins, machines à vecteurs de support, régression régularisée, réseaux de neurones — et savoir que c'est sans effet sur les modèles à base d'arbres.
- **Faire la sélection de variables à l'intérieur de la validation croisée**, jamais avant : une sélection faite sur le jeu complet a déjà consulté le test.
- **Protéger contre la fuite temporelle** en ne joignant que les valeurs disponibles à l'instant de la prédiction. C'est la seule protection sérieuse sur des données transactionnelles, et elle se conçoit au moment de la jointure, pas après.

> [!warning] Piège
> Ajuster le centrage, l'imputation ou le sélecteur sur le jeu complet avant le découpage. Le modèle voit alors la moyenne et la variance du test, l'évaluation devient optimiste, et rien ne le signale. Corollaire en manipulation tabulaire : ne jamais ignorer un avertissement de copie sur tranche, il annonce des variables partiellement remplies qu'on découvrira bien plus tard.

## Les notions mobilisées

- [[notions/collecte-de-donnees]] — la provenance, la fiabilité et les métadonnées d'extraction, qui expliquent la plupart des anomalies constatées ensuite.
- [[notions/sql]] — la source la plus fréquente, et le moyen d'agréger côté serveur plutôt que de rapatrier des millions de lignes.
- [[notions/qualite-des-donnees]] — les propriétés à vérifier, transformées en tests exécutés à chaque passage du pipeline.
- [[notions/pandas]] — l'outil du quotidien, avec ses pièges de types, de copies et de performance.
- [[notions/traitement-distribue]] — les formats colonnes et les moteurs embarqués, et le seuil au-delà duquel distribuer devient justifié.
- [[notions/apprentissage-non-supervise]] — l'analyse en composantes principales et la réduction de dimension, employées ici comme prétraitement.

## Pour apprendre

- [scikit-learn — Common pitfalls and recommended practices](https://scikit-learn.org/stable/common_pitfalls.html) — la page qui traite explicitement la fuite par prétraitement et le mauvais usage du découpage.
- [scikit-learn — Pipelines et ColumnTransformer](https://scikit-learn.org/stable/modules/compose.html) — la mécanique exacte qui empêche la fuite, avec les exemples de composition par type de colonne.
- [Data Preparation and Feature Engineering](https://developers.google.com/machine-learning/data-prep) — le guide court de Google sur la construction de variables.
- [Python for Data Analysis](https://wesmckinney.com/book/) — libre en ligne, la référence sur la manipulation tabulaire par l'auteur de pandas.
- [Documentation DuckDB](https://duckdb.org/docs/) et [documentation Polars](https://docs.pola.rs/) — le SQL sur fichiers colonnes et le tableau de données multi-cœur, dès que la mémoire devient contraignante.
