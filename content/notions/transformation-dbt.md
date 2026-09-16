---
title: Transformation avec dbt
tags: [notion, dbt, transformation, elt, sql, tests]
date: 2026-09-16
statut: actif
appelee-par: [bi-analyst]
---

Outil qui organise les transformations d'un entrepôt en un graphe de modèles SQL versionnés, testés et documentés, exécutés par l'entrepôt lui-même.

## À quoi ça sert

dbt n'apporte pas une capacité technique nouvelle — tout ce qu'il fait pourrait s'écrire en SQL et en scripts. Il apporte une **discipline** : la logique métier cesse d'être éparpillée dans des rapports et des procédures, et devient un dépôt de code avec des dépendances explicites, des tests et un historique.

Son effet réel sur le métier est un déplacement de frontière. La transformation est passée d'un outil graphique administré par l'informatique à du SQL dans un dépôt Git, ce qui l'a mise à la portée du BI Analyst — et lui a imposé en retour des pratiques de développeur : branches, revue, tests, environnements séparés.

Le troisième apport est la documentation générée : le graphe de dépendances et la description des colonnes sortent du code plutôt que d'un document tenu à côté, donc ils ne se périment pas silencieusement.

## Ce qu'il faut savoir

- **Un modèle est un `SELECT`** ; dbt se charge de le matérialiser en vue, table, table incrémentale ou instantané. La matérialisation est un réglage, pas une réécriture.
- **Les dépendances sont déclarées par référence** (`ref` et `source`), ce qui produit automatiquement l'ordre d'exécution et le graphe de lignage.
- **Les tests sont natifs** : unicité, non-nullité, valeurs acceptées, intégrité référentielle, plus des tests écrits en SQL. Un test qui échoue arrête la chaîne — c'est ce qui fait la différence avec un contrôle de qualité décoratif.
- **Les couches restent nécessaires** : sources, modèles intermédiaires, modèles exposés. dbt n'impose pas d'architecture ; sans convention, on obtient un graphe de deux cents modèles sans structure.
- **Les modèles incrémentaux** évitent de tout recalculer, au prix d'une logique de reprise à écrire soigneusement. Pouvoir tout reconstruire depuis le brut reste la propriété la plus précieuse.
- **Les macros Jinja** factorisent le SQL répétitif. Elles deviennent vite illisibles : la règle utile est qu'un modèle doit rester compréhensible dans sa forme compilée.
- **dbt transforme, il n'orchestre pas.** L'ordonnancement, les dépendances externes et la reprise sur incident relèvent d'un orchestrateur — voir [[notions/orchestration-de-flux]].

## Selon le métier

### BI Analyst

Ce qui est propre au métier n'est pas l'outil mais le déplacement qu'il a provoqué : la transformation lui est revenue, avec les obligations qui l'accompagnent. Concrètement, cela veut dire qu'un changement de définition passe par une branche, une revue et un test, et non par une modification directe en production — la contrepartie exacte de l'autonomie gagnée.

> [!info] Une seule appelante
> Notion appelée par le seul parcours BI Analyst. Le parcours Data Engineer du corpus la recoupe ; elle reste ici pour cette raison.

> [!warning] Piège
> Migrer les rapports existants en modèles dbt sans arbitrer les définitions au passage. On obtient un graphe propre, versionné et testé, qui produit toujours trois chiffres d'affaires différents — en les rendant simplement plus difficiles à contester, puisqu'ils ont maintenant l'air rigoureux. L'outil ne tranche pas les désaccords, il les documente.

## Pour aller plus loin

- [Qu'est-ce que dbt — site officiel](https://www.getdbt.com/product/what-is-dbt) — le cadrage du produit et de son positionnement.
- [dbt — documentation](https://docs.getdbt.com/docs/build/documentation) — la référence, notamment sur les tests et la documentation générée.
- [dbt — cours officiels](https://learn.getdbt.com/catalog) — la prise en main guidée.

## Appelée par

- [[parcours/bi-analyst/index|BI Analyst]]

Voisines : [[notions/orchestration-de-flux]], [[notions/entrepot-de-donnees]], [[notions/qualite-des-donnees]], [[notions/lignage-des-donnees]].
