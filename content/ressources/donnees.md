---
title: Ressources — Données
tags: [ressources, donnees, sql, entrepot, bi, visualisation, gouvernance, reference]
date: 2026-09-16
statut: actif
source: https://roadmap.sh/data-engineer
---

> [!abstract] SQL, entrepôt, transformation, orchestration, restitution et gouvernance. Les sources qui tiennent sur la durée — documentation de moteur, manuels de référence, projets libres qu'on peut déployer soi-même — plutôt que les comparatifs d'éditeurs.

## SQL

Le langage qui conditionne l'accès à tout le reste. La meilleure ressource n'est pas un
tutoriel mais la documentation du moteur qu'on utilise vraiment : c'est la seule qui
dise ce que *votre* base fait, dialecte compris.

| Type | Ressource | Ce qu'elle apporte | Niveau |
|---|---|---|---|
| officiel | [Documentation PostgreSQL](https://www.postgresql.org/docs/) | la documentation de moteur la plus complète et la mieux écrite du domaine, toutes bases confondues | intermédiaire |
| officiel | [SQLite](https://www.sqlite.org/index.html) | le moteur le plus déployé au monde, et le plus facile à lire de bout en bout | débutant |
| officiel | [DuckDB](https://duckdb.org/docs/) | l'analytique en colonnes sur un poste de travail : la réponse à la plupart des « il faut un cluster » | intermédiaire |
| officiel | [Documentation MySQL](https://dev.mysql.com/doc/) | le moteur qu'on trouve derrière la moitié des applications existantes, dialecte compris | intermédiaire |
| article | [SQL Window Functions](https://www.thoughtspot.com/sql-tutorial/sql-window-functions) | la meilleure page courte sur le fenêtrage, le sujet SQL qui sépare l'analyste du débutant | intermédiaire |
| article | [Performance Tuning SQL Queries](https://www.thoughtspot.com/sql-tutorial/sql-performance-tuning) | le pendant sur l'optimisation, concret et sans folklore | intermédiaire |

Le détail des jointures, du fenêtrage et de l'optimisation est dans [[notions/sql]].

> [!warning] Piège
> Les deux tutoriels ci-dessus ont longtemps été publiés sous `mode.com` ; l'éditeur a
> été racheté et le contenu republié à l'identique ailleurs. Les liens amont vers
> `mode.com` répondent encore, par redirection — ce qui fonctionne aujourd'hui et
> cassera un jour sans prévenir. Les adresses données ici sont les adresses actuelles.

## Entrepôt et modélisation

| Type | Ressource | Ce qu'elle apporte | Niveau |
|---|---|---|---|
| article | [What is a Data Warehouse?](https://cloud.google.com/learn/what-is-a-data-warehouse) | la présentation la plus sobre du concept, sans argumentaire produit malgré l'origine | débutant |
| article | [Star Schema vs Snowflake Schema](https://www.thoughtspot.com/data-trends/data-modeling/star-schema-vs-snowflake-schema) | mise au point courte et correcte, suffisante pour démarrer | débutant |
| article | [Normalization vs Denormalization](https://codilime.com/blog/normalization-vs-denormalization-in-databases/) | pourquoi le bon réflexe transactionnel est le mauvais réflexe décisionnel | intermédiaire |
| officiel | [BigQuery — Introduction](https://docs.cloud.google.com/bigquery/docs/introduction) | le modèle d'un entrepôt sans serveur : stockage et calcul séparés, facturation à la donnée lue | intermédiaire |
| officiel | [Snowflake in 20 minutes](https://docs.snowflake.com/en/user-guide/tutorials/snowflake-in-20minutes) | la prise en main la plus rapide de l'autre entrepôt qu'on croise en entreprise | débutant |
| officiel | [Apache Parquet](https://parquet.apache.org/) | le format colonne qui sous-tend tout le reste. Comprendre pourquoi il est rapide change les choix d'architecture | intermédiaire |
| officiel | [Delta Lake](https://docs.databricks.com/aws/en/delta) | les transactions sur un lac de données, et le problème qu'elles résolvent vraiment | confirmé |

Voir [[notions/entrepot-de-donnees]], [[notions/modelisation-dimensionnelle]] et
[[notions/data-lake]].

## Transformation et orchestration

| Type | Ressource | Ce qu'elle apporte | Niveau |
|---|---|---|---|
| officiel | [dbt — Documentation](https://docs.getdbt.com/docs/build/documentation) | à lire comme un catalogue de pratiques — tests, matérialisations, documentation générée — autant que comme une documentation d'outil | intermédiaire |
| officiel | [What is dbt](https://www.getdbt.com/product/what-is-dbt) | le cadrage du modèle ELT en dix minutes | débutant |
| cours | [dbt — Cours officiels](https://learn.getdbt.com/catalog) | gratuits, courts, et les seuls à traiter le versionnement des modèles sérieusement | débutant |
| officiel | [Apache Airflow — Documentation](https://airflow.apache.org/docs) | DAG, dépendance, reprise sur incident : les notions à comprendre même si l'outil retenu est un autre | intermédiaire |
| officiel | [Prefect](https://docs.prefect.io/v3/get-started) | l'alternative dont le modèle mental est plus proche de Python ordinaire | intermédiaire |
| officiel | [Apache Spark](https://spark.apache.org/documentation.html) | la référence du traitement distribué, à ouvrir seulement quand le volume l'impose | confirmé |
| officiel | [Apache Kafka — Quickstart](https://kafka.apache.org/quickstart) | le flux d'événements, monté en trente minutes sur un poste | intermédiaire |

Voir [[notions/transformation-dbt]], [[notions/orchestration-de-flux]] et
[[notions/traitement-distribue]].

> [!tip] Ajout 2026
> Le seuil à partir duquel distribuer a un sens a nettement monté. Un fichier de
> plusieurs dizaines de gigaoctets se traite aujourd'hui sur un portable avec DuckDB ou
> Polars, sans cluster et sans les frais d'exploitation qui vont avec. Monter Spark pour
> un jeu de données qui tient sur un disque est devenu une erreur de dimensionnement,
> pas une précaution.

## Restitution et visualisation

| Type | Ressource | Ce qu'elle apporte | Niveau |
|---|---|---|---|
| livre | [Fundamentals of Data Visualization](https://clauswilke.com/dataviz/introduction.html) | Claus Wilke, libre et en ligne. La partie sur les couleurs et les échelles est la plus directement rentable | intermédiaire |
| article | [The Data Visualisation Catalogue](https://datavizcatalogue.com/) | choisir un type de graphique en partant de la question posée, et non de l'inverse | débutant |
| article | [Visual Best Practices](https://help.tableau.com/current/blueprint/en-us/bp_visual_best_practices.htm) | indépendant de l'outil malgré la source ; la check-list avant publication | débutant |
| article | [10 Guidelines for DataViz Accessibility](https://www.highcharts.com/blog/best-practices/10-guidelines-for-dataviz-accessibility/) | l'accessibilité traitée concrètement — contraste, redondance de l'encodage, taille | intermédiaire |
| article | [How To Spot Misleading Charts](https://www.tableau.com/blog/how-spot-misleading-charts-check-axes) | utile dans les deux sens : détecter, et ne pas produire | débutant |
| officiel | [Matplotlib](https://matplotlib.org/) | la bibliothèque de tracé de référence en Python ; verbeuse, mais rien ne lui échappe | intermédiaire |
| officiel | [seaborn](https://seaborn.pydata.org/) | la couche statistique par-dessus, pour explorer vite | débutant |
| officiel | [ggplot2](https://ggplot2.tidyverse.org/) | la grammaire des graphiques, côté R. Le modèle mental le plus solide du domaine | intermédiaire |

Voir [[notions/visualisation-de-donnees]] et [[notions/outils-decisionnels]].

## Plateformes décisionnelles libres

| Type | Ressource | Ce qu'elle apporte | Niveau |
|---|---|---|---|
| code | [Metabase](https://github.com/metabase/metabase) | la plus simple à mettre entre les mains d'un métier ; déployable en une soirée | intermédiaire |
| code | [Apache Superset](https://github.com/apache/superset) | la plus complète côté modélisation et droits | confirmé |

Les déployer soi-même reste le meilleur cours sur le fonctionnement interne d'un outil
décisionnel — cache, couche sémantique, propagation des droits — et ce que les éditeurs
facturent pour le faire à votre place.

## Qualité, lignage et gouvernance

| Type | Ressource | Ce qu'elle apporte | Niveau |
|---|---|---|---|
| article | [What Is Data Lineage?](https://www.ibm.com/think/topics/data-lineage) | la définition de référence. Contenu d'éditeur, correct sur le concept, muet sur le coût | débutant |
| article | [The Ultimate Guide To Data Lineage](https://montecarlo.ai/blog-data-lineage) | le versant pratique du précédent : ce que ça coûte à maintenir, et ce que ça rapporte quand une table casse | intermédiaire |
| norme | [Texte du RGPD](https://gdpr-info.eu/) | la source, à consulter plutôt que les résumés commerciaux | intermédiaire |
| norme | [California Consumer Privacy Act](https://oag.ca.gov/privacy/ccpa) | l'équivalent californien, utile dès qu'un client a des utilisateurs aux États-Unis | intermédiaire |
| article | [5 Principles of Data Ethics for Business](https://online.hbs.edu/blog/post/data-ethics) | court et exploitable, notamment sur la question du périmètre de collecte | débutant |

Voir [[notions/qualite-des-donnees]], [[notions/lignage-des-donnees]], [[notions/rgpd]]
et [[notions/donnees-sensibles]].

## Manipulation de données en Python et en R

| Type | Ressource | Ce qu'elle apporte | Niveau |
|---|---|---|---|
| officiel | [pandas — Documentation](https://pandas.pydata.org/docs/) | la référence. Le guide utilisateur vaut mieux que la plupart des tutoriels qui le paraphrasent | débutant |
| livre | [Python for Data Analysis](https://wesmckinney.com/book/) | Wes McKinney, l'auteur de pandas. Libre en ligne, et la meilleure entrée en matière | débutant |
| officiel | [NumPy — Documentation](https://numpy.org/doc/stable/) | ce sur quoi tout repose ; comprendre la diffusion évite des boucles inutiles | intermédiaire |
| livre | [R for Data Science](https://r4ds.hadley.nz/) | Wickham et al., libre en ligne. La deuxième édition, celle qui couvre le tidyverse actuel | débutant |
| officiel | [dplyr](https://dplyr.tidyverse.org/) | la grammaire de manipulation côté R, plus lisible que son équivalent Python | débutant |
| officiel | [The R Manuals (CRAN)](https://cran.r-project.org/manuals.html) | la référence du langage, quand la question devient précise | confirmé |

Voir [[notions/pandas]], [[notions/python-pour-la-data]] et [[notions/r-et-tidyverse]].

## Écarté, et pourquoi

- **Les comparatifs « X vs Y » publiés par X.** Il y en a beaucoup dans le catalogue
  amont. Quand un tel article est retenu ici, c'est pour sa définition, et la réserve est
  écrite dans la colonne d'à côté.
- **Les quinze flux d'agrégateur** repris en amont avec `ref=roadmapsh`. Un flux n'est pas
  une ressource : il ne dit pas ce qu'on va y trouver ni quand.
- **Les tutoriels de plateformes payantes sans accès libre.** À qualité égale, le
  gratuit et accessible l'emporte ; à qualité inégale, ça se discute, mais ce n'était pas
  le cas ici.
