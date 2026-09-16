---
title: Collecte de données
tags: [notion, collecte, extraction, api, csv, moissonnage]
date: 2026-09-16
statut: actif
appelee-par: [data-analyst, bi-analyst]
---

Opération consistant à rapatrier le bon sous-ensemble de données dans son environnement de travail en sachant précisément d'où il vient, de quand il date et ce qu'il exclut.

## À quoi ça sert

Les trois informations ci-dessus — provenance, date, périmètre exclu — conditionnent la validité de tout ce qui suit, et elles ne se retrouvent pas après coup. Une analyse dont on ne sait plus si elle portait sur les commandes ou sur les livraisons, sur le mois calendaire ou sur le mois comptable, n'est pas corrigeable : elle est à refaire.

La collecte est aussi le premier moment où les défauts des systèmes amont deviennent visibles, parce que c'est le premier moment où quelqu'un regarde réellement le contenu. Celui qui collecte n'a généralement pas construit les flux, mais il est le seul à en constater les effets.

Le troisième enjeu est la **rejouabilité**. Si un chiffre doit ressortir plus d'une fois, la collecte s'écrit en requête ou en script dès la première — sinon l'écart entre deux exécutions sera inexplicable.

## Ce qu'il faut savoir

- **Base de données** : la source de référence dans presque tous les contextes d'entreprise. Interroger l'entrepôt plutôt que le système de production quand il existe — mêmes données, historisées, sans charge sur un service vivant. Voir [[notions/sql]].
- **Fichiers CSV** : format d'échange universel et première source d'erreurs silencieuses — encodage (UTF-8 contre Latin-1 sur les accents), séparateur (le point-virgule en contexte francophone), séparateur décimal, dates en format américain une ligne sur deux. Imposer le type des colonnes à la lecture au lieu de laisser l'inférence décider.
- **API** : lire la pagination, les quotas et la politique de limitation **avant** d'écrire la boucle, et conserver la réponse brute avant tout traitement. Une extraction relancée trois jours plus tard ne renvoie pas les mêmes données.
- **Moissonnage de sites** : techniquement accessible, juridiquement encadré. Conditions d'utilisation, `robots.txt`, droit des bases de données, et [[notions/rgpd]] dès qu'il y a de la donnée personnelle — ce qui est le cas plus souvent qu'on ne le croit. En entreprise, faire valider avant, pas après.
- **Trois métadonnées à consigner systématiquement** : la requête ou l'URL exacte, l'horodatage, le nombre de lignes obtenu. C'est ce qui permet de rejouer et d'expliquer un écart entre deux versions du même chiffre.
- **Vérifier le volume attendu dès la collecte.** Une table de commandes qui rend 4 000 lignes là où le métier en annonce 40 000 signale un filtre implicite, un droit d'accès partiel ou une jointure fautive.
- **Parquet comme format de travail intermédiaire** dès que l'extraction dépasse quelques centaines de milliers de lignes : types conservés, compression, lecture par colonne. Le CSV reste le format d'échange entre humains, pas le format de stockage d'une analyse.

## Selon le métier

### Data Analyst

L'analyste ne construit pas les flux — c'est le métier du Data Engineer — mais il en dépend entièrement et il est le premier à en constater les défauts. Son angle est donc le diagnostic : vérifier le volume, la période et les métadonnées à l'extraction, avant toute analyse, parce que c'est le seul moment où un écart est encore attribuable.

### BI Analyst

La collecte est en principe industrialisée et ne relève pas de lui, sauf pour les sources qui échappent à la chaîne — un fichier reçu par courriel, un export d'un outil métier, une API sans connecteur. Ce sont précisément ces sources-là qui cassent les tableaux de bord, et l'angle du métier est de les faire rentrer dans la chaîne plutôt que de les traiter à la main tous les mois.

> [!warning] Piège
> L'extraction manuelle refaite à la main tous les mois — un export depuis une interface, un filtre cliqué, un fichier daté à la main. Elle n'est ni rejouable ni vérifiable, et l'écart entre deux mois est impossible à expliquer. Le coût d'écrire la collecte une fois est inférieur au coût de la première explication qu'on ne pourra pas donner.

## Pour aller plus loin

- [Data Collection Methods](https://www.questionpro.com/blog/data-collection-methods/) — le panorama des sources et de leurs biais.
- [What is a CSV file: a comprehensive guide](https://flatfile.com/blog/what-is-a-csv-file-guide-to-uses-and-benefits/) — le format et ses pièges, traités sérieusement.
- [Introduction to APIs — MDN](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Client-side_APIs/Introduction) — le socle pour lire une documentation d'API sans être développeur.

## Appelée par

- [[parcours/data-analyst|Data Analyst]]
- [[parcours/bi-analyst|BI Analyst]]

Voisines : [[notions/qualite-des-donnees]], [[notions/sql]], [[notions/traitement-distribue]], [[notions/rgpd]].
