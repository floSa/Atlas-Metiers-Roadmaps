---
tags: [notion, data-lake, lakehouse, stockage, formats]
date: 2026-09-16
statut: actif
appelee-par: [bi-analyst]
---

# Data lake et lakehouse

Stockage de fichiers bruts à bas coût, dans leur format d'origine et sans schéma imposé à l'écriture — et, dans sa forme récente, la couche de table qui lui rend les garanties d'une base.

## À quoi ça sert

Le data lake répond à un problème de coût et de délai : conserver tout ce qui arrive, y compris ce dont on ne sait pas encore quoi faire, sans payer le prix d'une modélisation préalable. Journaux applicatifs, fichiers semi-structurés, exports volumineux, images — des données qu'un entrepôt accepterait mal ou cher.

Sa contrepartie est connue : sans discipline, il devient un dépotoir où personne ne sait ce qui est à jour, ce qui est fiable, ni qui a le droit de le lire. Le schéma à la lecture déplace le coût, il ne le supprime pas — il le transfère à chaque personne qui consomme la donnée.

Le lakehouse est la réponse à ce dérapage : des formats de table ouverts — Delta Lake, Iceberg, Hudi — posés sur le stockage objet, qui rendent transactions, évolution de schéma, historique et suppression ciblée. On obtient le coût du lac avec une partie des garanties de l'entrepôt.

## Ce qu'il faut savoir

- **Schéma à l'écriture contre schéma à la lecture** : l'entrepôt valide à l'entrée, le lac au moment de lire. Le second est plus souple et déporte la charge de vérification sur le consommateur.
- **Le format de fichier compte plus que le stockage.** Parquet — colonnes, types conservés, compression — divise les temps de lecture et les coûts par rapport au CSV, et reste lisible par tout l'écosystème.
- **Le partitionnement** par date ou par domaine est ce qui rend les lectures abordables. Mal choisi, il produit des millions de petits fichiers et dégrade tout.
- **Les formats de table** ajoutent ce qui manquait : écriture transactionnelle, voyage dans le temps, évolution de schéma, suppression ciblée — cette dernière étant nécessaire pour honorer une demande d'effacement au titre du [[notions/rgpd]].
- **Un catalogue est indispensable** : sans inventaire de ce qui existe, de sa fraîcheur et de son propriétaire, le lac est illisible au bout de six mois. Voir [[notions/lignage-des-donnees]].
- **Les droits d'accès sont plus difficiles** qu'en base : ils portent sur des chemins et des préfixes, à une granularité rarement alignée sur le besoin métier.
- **Le lac ne remplace pas l'entrepôt** dans la plupart des organisations : il l'alimente, et sert les usages que l'entrepôt traite mal.

## Selon le métier

### BI Analyst

Le BI Analyst consomme le lac plus qu'il ne le construit, et son angle est la fiabilité : ce qui vient du lac n'a pas été validé à l'écriture, donc les contrôles de [[notions/qualite-des-donnees]] lui incombent avant publication. La question à poser devant toute source de lac : qui l'écrit, à quelle fréquence, et que se passe-t-il quand le format change en amont.

> [!info] Une seule appelante
> Notion appelée par le seul parcours BI Analyst. Conservée ici parce qu'elle est le pendant direct de [[notions/entrepot-de-donnees]] et qu'un lecteur qui arrive par l'un cherche l'autre.

> [!warning] Piège
> Traiter le lac comme un entrepôt sans modélisation. On y déverse les sources, on branche l'outil de restitution dessus, et chaque rapport refait à sa façon le nettoyage, les jointures et les règles métier. Six mois plus tard, trois rapports donnent trois chiffres, et aucun n'est démontrable. La couche exposée reste nécessaire, quel que soit le stockage.

## Pour aller plus loin

- [Data Lake Definition — Microsoft Azure](https://azure.microsoft.com/en-gb/resources/cloud-computing-dictionary/what-is-a-data-lake) — la définition et les cas d'usage.
- [Data Lake VS Data Warehouse](https://towardsdatascience.com/data-lake-vs-data-warehouse-2e3df551b800/) — la comparaison, avec les critères de choix.
- [What is a Data Lake?](https://www.youtube.com/watch?v=LxcH6z8TFpI) — l'introduction en vidéo courte.

## Appelée par

- [[parcours/bi-analyst|BI Analyst]]

Voisines : [[notions/entrepot-de-donnees]], [[notions/traitement-distribue]], [[notions/qualite-des-donnees]], [[notions/lignage-des-donnees]].
