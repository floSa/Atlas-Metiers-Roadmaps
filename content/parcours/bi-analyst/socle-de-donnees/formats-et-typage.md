---
title: Formats et typage
---

Niveau attendu : **usage**. Une typologie qu'on applique sur un chemin balisé ; ce qui compte vraiment, la frontière dimension/mesure, se joue à l'étape suivante.

La typologie catégoriel/numérique, discret/continu a un seul usage vraiment utile en BI, et il est décisif : elle préfigure la séparation **dimension contre mesure** du modèle. Une variable catégorielle devient un attribut de dimension, une variable numérique additive devient une mesure.

```mermaid
flowchart TD
  EN["Entrepôt de données<br/>le format y est un choix de performance"]
  DL["Data lake<br/>où Parquet devient la norme de fait"]
  TD["Traitement distribué<br/>formats colonnes et moteurs embarqués"]
  MD["Modélisation dimensionnelle<br/>la frontière attribut / mesure"]
  QD["Qualité des données<br/>le typage élimine une classe d'erreurs"]

  click EN "/notions/entrepot-de-donnees"
  click DL "/notions/data-lake"
  click TD "/notions/traitement-distribue"
  click MD "/notions/modelisation-dimensionnelle"
  click QD "/notions/qualite-des-donnees"
```

## Ce qu'il faut savoir faire

- Choisir le format par usage : CSV et Excel pour l'échange avec des humains, JSON pour les APIs, **Parquet** pour tout ce qui est stocké en vue d'être analysé. Le format colonnaire compressé change le temps de lecture d'un ordre de grandeur et porte son schéma, ce qui élimine toute une classe d'erreurs de typage.
- Ne pas aplatir systématiquement le semi-structuré. Les entrepôts modernes interrogent le JSON en place ; un champ préservé tel quel permet de récupérer un attribut oublié sans rejouer l'ingestion.
- Identifier les cas ambigus dès l'entrée : un code postal, une note sur cinq, un identifiant numérique. Ce sont exactement ceux qui finissent additionnés par erreur dans un tableau croisé, et le typage explicite est la seule parade.
- Typer les dates au type date, jamais en chaîne, et fixer le fuseau une fois pour toutes à l'ingestion. Un décalage de fuseau non traité déplace silencieusement des ventes d'un jour à l'autre, et la clôture mensuelle le révèle.
- Fixer la précision des montants à l'entrée — décimal, jamais flottant. L'écart de centimes qui apparaît sur un total de plusieurs millions est un incident de réconciliation, pas une approximation acceptable.
- Documenter les valeurs admises des colonnes codifiées dès qu'on les découvre. Cette liste deviendra un test dans la chaîne, et plus tard une contrainte de la couche sémantique.

## Les notions mobilisées

- [[notions/entrepot-de-donnees]] — le stockage colonnaire y est la raison même des performances analytiques.
- [[notions/data-lake]] — Parquet y tient lieu de contrat de schéma en l'absence de schéma imposé à l'écriture.
- [[notions/traitement-distribue]] — formats colonnes et moteurs embarqués, et le seuil à partir duquel distribuer a un sens.
- [[notions/modelisation-dimensionnelle]] — la distinction attribut de dimension / mesure se décide ici, sur le typage.
- [[notions/qualite-des-donnees]] — un typage strict à l'ingestion est le test de qualité le moins coûteux qui existe.

> [!warning] Piège
> Accepter un fichier dont une colonne a changé de type entre deux livraisons. Le moteur convertira souvent en silence, la colonne deviendra du texte, et les agrégations retourneront zéro sans erreur. Un contrôle de type à l'ingestion qui rejette le lot coûte une alerte ; sa découverte trois semaines plus tard coûte la confiance.

## Pour apprendre

- [Apache Parquet](https://parquet.apache.org/) — la documentation du format, y compris ce que le stockage colonnaire change à la lecture.
- [Documentation DuckDB](https://duckdb.org/docs/) — la façon la plus rapide d'éprouver Parquet et le typage sur un jeu réel, sans infrastructure.
- [Delta Lake — Databricks](https://docs.databricks.com/aws/en/delta) — ce que l'évolution de schéma devient quand elle est gérée plutôt que subie.
