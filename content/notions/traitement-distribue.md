---
title: Traitement distribué
tags: [notion, traitement-distribue, spark, duckdb, polars, parquet, volume]
date: 2026-09-16
statut: actif
appelee-par: [data-analyst, bi-analyst]
---

Répartition d'un calcul sur plusieurs machines quand les données ne tiennent plus sur une seule — et, avant cela, l'ensemble des moyens d'éviter d'en arriver là.

## À quoi ça sert

Le principe est simple : quand la donnée dépasse la capacité d'une machine, le calcul se distribue et l'ordre des opérations devient déterminant pour le coût. Ce qu'il faut surtout savoir, c'est **à partir de quand** le sujet se pose, et la réponse a beaucoup bougé — un poste de travail courant traite aujourd'hui plusieurs dizaines de millions de lignes en mémoire sans effort particulier.

Le premier réflexe n'est donc pas de distribuer, c'est de **ne pas rapatrier** : agréger, filtrer et joindre dans la base, puis descendre un résultat de quelques milliers de lignes. La plupart des problèmes de volume sont des problèmes de requête.

Le second est de changer d'outil avant de changer d'infrastructure. Les moteurs embarqués couvrent aujourd'hui une gamme de volumes qui exigeait un cluster il y a cinq ans, sans coût d'exploitation permanent.

## Ce qu'il faut savoir

- **Le seuil se mesure, il ne se suppose pas.** Charger les colonnes utiles au lieu de la table entière, convertir en Parquet, refaire le test. La grande majorité des « il faut du Spark » observés sur le terrain sont un `SELECT *` sur une table large, un type mal choisi, ou une jointure faite côté client alors que la base l'aurait faite.
- **DuckDB et Polars** couvrent l'essentiel des besoins intermédiaires : SQL ou manipulation tabulaire sur des fichiers de plusieurs gigaoctets, sur un seul poste, sans infrastructure. C'est la réponse par défaut quand pandas sature.
- **Spark** garde son intérêt sur des volumes réellement distribués ou quand c'est le socle imposé par l'entreprise, généralement via PySpark. L'écrire depuis rien n'arrive presque jamais dans les métiers d'analyse.
- **MapReduce n'a plus qu'un intérêt historique** ; MPI relève du calcul scientifique haute performance et non de l'analyse de données.
- **Le format compte plus que le moteur** : Parquet divise les temps de lecture et conserve les types. C'est le levier le moins coûteux de tout le sujet.
- **Le coût du calcul est désormais un coût facturé.** Sur un entrepôt infonuagique, une requête mal écrite se paie à l'octet scanné ; regarder ce que coûte une requête fait partie du métier.
- **Les trois V** (volume, vélocité, variété) sont un vocabulaire de réunion, utile pour se comprendre, sans conséquence technique directe.
- **L'infrastructure distribuée ajoute un coût permanent d'exploitation** pour résoudre un problème qui dure dix minutes. C'est l'arbitrage à poser explicitement.

## Selon le métier

### Data Analyst

Le périmètre de l'analyse n'est pas le volume de l'entreprise. Une table de logs de plusieurs téraoctets ne signifie pas que l'analyse porte sur des téraoctets : la question concerne le plus souvent trois mois, deux colonnes et un segment. Formuler le périmètre avant de regarder la taille de la table évite un chantier d'infrastructure entier.

### BI Analyst

L'angle est le coût récurrent plutôt que la faisabilité. Une requête de tableau de bord est rejouée des milliers de fois : partitionnement, regroupement des données et sélection des colonnes ne sont pas des optimisations mais des décisions budgétaires. Un rapport rafraîchi toutes les cinq minutes sur une table non partitionnée est une ligne de facture qui croît sans que personne la relie au rapport.

> [!warning] Piège
> Prendre le volume de données de l'entreprise pour le volume de son calcul. C'est l'erreur qui déclenche des projets d'infrastructure entiers pour des analyses qui tiendraient sur un poste. La démarche inverse coûte une heure : réduire le périmètre, convertir en Parquet, mesurer, et ne distribuer que si la mesure l'exige.

## Pour aller plus loin

- [Apache Spark — documentation](https://spark.apache.org/documentation.html) — la référence, si le socle est imposé.
- [What Is Hadoop? — Databricks](https://www.databricks.com/glossary/hadoop) — le contexte historique, utile pour lire des architectures existantes.
- [Batch and Streaming Demystified](https://towardsdatascience.com/batch-and-streaming-demystified-for-unification-dee0b48f921d/) — la distinction lot/flux, souvent confondue avec la question du volume.

## Appelée par

- [[parcours/data-analyst|Data Analyst]]
- [[parcours/bi-analyst|BI Analyst]]

Voisines : [[notions/pandas]], [[notions/sql]], [[notions/data-lake]], [[notions/collecte-de-donnees]].
