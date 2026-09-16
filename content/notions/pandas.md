---
title: pandas
tags: [notion, pandas, python, manipulation-tabulaire, outillage]
date: 2026-09-16
statut: actif
appelee-par: [data-analyst, bi-analyst]
---

Bibliothèque Python de manipulation de données tabulaires en mémoire, organisée autour du DataFrame — un tableau indexé dont les colonnes sont typées.

## À quoi ça sert

pandas occupe la place qu'occupait le tableur, avec ce que le tableur n'a pas : un enchaînement de transformations écrit, relisible et rejouable depuis la donnée brute. C'est ce qui en fait l'outil de nettoyage et d'exploration par défaut côté Python, bien plus que sa performance.

L'enjeu principal du code pandas est donc la **lisibilité de l'enchaînement**, pas la vitesse. Un script qu'on relit six mois plus tard doit laisser voir dans quel ordre les filtres, jointures et agrégations ont été appliqués — parce que c'est là que se cachent les décisions d'analyse.

Sa limite est l'échelle : tout tient en mémoire, avec un surcoût important par rapport à la taille du fichier. Quand elle est atteinte, la bonne réponse est rarement de distribuer. Voir [[notions/traitement-distribue]].

## Ce qu'il faut savoir

- **Sélection** : `loc` par étiquette, `iloc` par position. Mélanger les deux est la première source de bogues silencieux.
- **Le chaînage d'indexation** (`df[...][...] = ...`) produit l'avertissement de copie et parfois une modification perdue. Une affectation passe par `loc`.
- **Les types comptent.** Une colonne chargée en `object` au lieu de numérique fausse les agrégations et multiplie la mémoire. Imposer les types à la lecture plutôt que de laisser l'inférence décider ; utiliser le type catégoriel sur les colonnes à faible cardinalité.
- **`groupby` puis `agg`** couvre la majorité des besoins. `transform` renvoie une série alignée sur l'index d'origine, ce qui évite une jointure de retour.
- **`merge` est une jointure SQL** avec les mêmes pièges : vérifier le nombre de lignes avant et après, et utiliser `validate=` pour faire échouer une jointure dont la cardinalité n'est pas celle qu'on croit.
- **Les valeurs manquantes** ont plusieurs représentations (`NaN`, `NaT`, `pd.NA`) selon le type. Les agrégations les ignorent par défaut, ce qui est rarement neutre.
- **Éviter les boucles ligne par ligne** : `apply` sur les lignes est lent et souvent remplaçable par une opération vectorisée. Mais la lisibilité prime tant que le volume ne le justifie pas.
- **L'écosystème autour** : NumPy en dessous, Parquet comme format de travail dès quelques centaines de milliers de lignes, Polars et DuckDB quand pandas sature.

## Selon le métier

### Data Analyst

La bibliothèque de manipulation tabulaire côté Python, avec NumPy en dessous. L'enjeu est la lisibilité de l'enchaînement des transformations, pas la performance. La règle qui gouverne tout le reste : le nettoyage est un script rejouable depuis la donnée brute, jamais une suite de corrections manuelles sur une copie.

### BI Analyst

pandas reste utile pour ce que SQL fait mal — appeler une API, lire un format exotique, calculer une prévision. Dans la chaîne de transformation, préférer SQL pour tout ce qu'il sait faire : il est testable, lisible par l'équipe métier et exécuté par l'entrepôt. Le Python en BI est une exception assumée, pas un choix par défaut.

> [!warning] Piège
> Laisser pandas inférer les types à la lecture d'un CSV. Un identifiant client à zéros initiaux devient un entier tronqué, une colonne mixte devient du texte, une date au format américain est lue une ligne sur deux. Le dégât est silencieux et se propage jusqu'au résultat final. Les types se déclarent à `read_csv`, pas après.

## Pour aller plus loin

- [pandas — documentation officielle](https://pandas.pydata.org/docs/index.html) — la référence ; le guide utilisateur vaut mieux que les tutoriels tiers.
- [pandas User Guide: Essential Basic Functionality](https://pandas.pydata.org/docs/user_guide/basics.html) — le socle, à lire en entier une fois.
- [Python NumPy Array Tutorial — DataCamp](https://www.datacamp.com/tutorial/python-numpy-tutorial) — la couche en dessous, utile pour comprendre les types et la vectorisation.

## Appelée par

- [[parcours/data-analyst|Data Analyst]]
- [[parcours/bi-analyst|BI Analyst]]

Voisines : [[notions/python-pour-la-data]], [[notions/r-et-tidyverse]], [[notions/traitement-distribue]], [[notions/qualite-des-donnees]].
