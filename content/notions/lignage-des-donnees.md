---
title: Lignage des données
tags: [notion, lignage, catalogue, tracabilite, gouvernance]
date: 2026-09-16
statut: actif
appelee-par: [bi-analyst]
---

Traçabilité du chemin parcouru par une donnée, de sa source jusqu'à l'indicateur affiché : par quelles tables elle passe, quelles transformations lui sont appliquées, et ce qui dépend d'elle en aval.

## À quoi ça sert

Le lignage répond à deux questions qu'on se pose toujours dans l'urgence. En amont : **d'où vient ce chiffre** — question posée en réunion, à laquelle il faut répondre sans préparation. En aval : **qu'est-ce qui casse si je change ceci** — question posée avant une modification, et dont la réponse conditionne le risque.

Sans lignage, les deux se traitent par la mémoire de la personne la plus ancienne dans l'équipe. C'est une dépendance connue, silencieuse, et qui se découvre le jour de son départ.

Le troisième usage est réglementaire : honorer une demande d'effacement ou documenter un traitement suppose de savoir où la donnée d'une personne a été recopiée. Sans traçabilité, la réponse est une supposition.

## Ce qu'il faut savoir

- **Deux granularités** : au niveau des tables (suffisant pour l'analyse d'impact) et au niveau des colonnes (nécessaire pour expliquer un calcul et pour la conformité). La seconde coûte plus cher à obtenir.
- **Le lignage se déduit du code**, pas d'un document tenu à la main. Un lignage documenté manuellement est faux au bout de trois mois — c'est la règle, pas l'exception.
- **Les outils de transformation le produisent automatiquement** quand les dépendances sont déclarées. C'est un des arguments les plus concrets en faveur de [[notions/transformation-dbt]].
- **Le catalogue est le complément** : inventaire de ce qui existe, propriétaire, définition métier, fraîcheur, niveau de confidentialité. Le lignage dit d'où ça vient, le catalogue dit ce que c'est et qui en répond.
- **Le point de rupture est l'outil de restitution.** Le lignage s'arrête souvent à la table exposée, alors que les calculs continuent dans les mesures du rapport. C'est exactement là que les définitions divergent.
- **Le propriétaire nommé fait plus que l'outil.** Un catalogue sans propriétaires est un annuaire ; avec eux, c'est un mécanisme de décision.
- **L'analyse d'impact est le retour sur investissement immédiat** : avant de modifier une source, savoir quels rapports en dépendent évite la panne de rentrée.

## Selon le métier

### BI Analyst

L'angle est la charge de la preuve. Un chiffre défendable est un chiffre dont on peut dire, en réunion et sans préparation, d'où il vient, ce qu'il inclut, quand il a été calculé, et ce qui se passerait s'il était faux. Le lignage répond à la première question ; les tests de [[notions/qualite-des-donnees]] à la dernière. C'est ce qui empêche qu'un chiffre juste soit remplacé par celui d'un tableur.

> [!info] Une seule appelante
> Notion appelée par le seul parcours BI Analyst, dont le registre indique qu'elle recoupe aussi le parcours MLOps du corpus.

> [!warning] Piège
> Acheter un catalogue avant d'avoir des propriétaires. L'outil recense automatiquement quinze mille objets, personne n'en documente aucun, et l'inventaire devient une preuve supplémentaire que rien n'est gouverné. Commencer par les vingt tables qui portent les indicateurs de direction, avec un nom de propriétaire sur chacune, produit plus d'effet que le déploiement complet.

## Pour aller plus loin

- [What Is Data Lineage? — IBM](https://www.ibm.com/think/topics/data-lineage) — le cadrage et les niveaux de granularité.
- [The Ultimate Guide To Data Lineage — Monte Carlo](http://montecarlodata.com/blog-data-lineage/) — l'angle opérationnel, orienté incidents.
- [dbt — documentation](https://docs.getdbt.com/docs/build/documentation) — le lignage produit automatiquement à partir des dépendances déclarées.

## Appelée par

- [[parcours/bi-analyst/index|BI Analyst]]

Voisines : [[notions/qualite-des-donnees]], [[notions/transformation-dbt]], [[notions/rgpd]], [[notions/entrepot-de-donnees]].
