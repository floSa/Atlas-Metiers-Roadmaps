---
tags: [notion, entrepot, data-warehouse, data-mart, architecture-decisionnelle]
date: 2026-09-16
statut: actif
appelee-par: [bi-analyst]
---

# Entrepôt de données

Base de données organisée pour l'analyse plutôt que pour la transaction : elle conserve l'historique, agrège des sources multiples et sert des lectures massives sans perturber les systèmes de production.

## À quoi ça sert

L'entrepôt existe pour une raison précise : **découpler la lecture analytique de l'écriture transactionnelle**, et fixer un historique que personne ne peut réécrire par accident. Tout le reste — la performance, la modélisation, la gouvernance — en découle.

Interroger directement le système de production pose deux problèmes qu'aucune optimisation ne résout. On y met une charge imprévisible sur un service vivant, et on n'y trouve que l'état courant : quand une adresse change, l'ancienne disparaît, et toute analyse historique devient fausse rétroactivement.

Le troisième apport est la réconciliation : un entrepôt est l'endroit où l'on décide que « client » désigne la même chose dans le CRM, la facturation et le support. C'est un travail de définition avant d'être un travail technique.

## Ce qu'il faut savoir

- **Entrepôt, data mart, ODS** : l'entrepôt couvre l'entreprise, le data mart sert un domaine ou une direction, l'ODS conserve un état courant intégré à faible latence. Le data mart est souvent la bonne porte d'entrée, à condition qu'il dérive de l'entrepôt et ne le double pas.
- **Architecture en couches** : brut (copie fidèle de la source, jamais modifiée), intermédiaire (nettoyé, typé, conformé), exposé (modélisé pour la consultation). Pouvoir rejouer depuis le brut est ce qui rend les corrections possibles.
- **ELT plutôt qu'ETL** : charger d'abord, transformer dans l'entrepôt avec sa puissance de calcul. C'est ce qui a mis la transformation à portée du BI Analyst — du SQL versionné plutôt qu'un outil graphique administré ailleurs.
- **Le stockage en colonnes** explique la performance analytique : ne lire que les colonnes utiles, compresser fortement des valeurs homogènes.
- **Le coût est désormais à l'usage.** Sur un entrepôt infonuagique, une requête mal écrite se paie à l'octet scanné. Partitionner, regrouper les données, éviter la sélection de toutes les colonnes : le plan d'exécution est une ligne budgétaire.
- **L'historisation est une décision de conception**, pas une propriété automatique. Elle se traite par les dimensions à évolution lente — voir [[notions/modelisation-dimensionnelle]].
- **La fraîcheur se négocie.** « Temps réel » coûte cher et n'est presque jamais le besoin : la question est quelle décision serait différente avec une donnée d'il y a une heure plutôt que d'hier soir.

## Selon le métier

### BI Analyst

Ce qui est propre au métier, ce ne sont pas les définitions mais **le choix et ses conséquences quotidiennes** : où vivent les définitions, quelle latence est acceptée, quel est le coût d'une requête de tableau de bord rejouée mille fois par jour, et qui a le droit d'écrire dans la couche exposée. Ce sont ces décisions qui déterminent si l'entrepôt sert ou si chacun repart du tableur.

> [!info] Une seule appelante
> Cette notion n'est appelée que par le parcours BI Analyst. Elle reste ici parce qu'elle est structurellement transverse — le parcours Data Engineer du corpus la recoupe, et le Data Analyst l'interroge sans la construire. Voir la synthèse du chantier 07 pour l'arbitrage.

> [!warning] Piège
> Construire l'entrepôt avant d'avoir les définitions. La difficulté n'est jamais technique : elle est de faire accepter qu'il n'existe qu'un seul chiffre d'affaires. Un entrepôt techniquement parfait alimenté par des définitions non arbitrées reproduit fidèlement le désaccord qu'il devait résoudre, avec en plus un coût d'infrastructure.

## Pour aller plus loin

- [What is a Data Warehouse? — Google Cloud](https://cloud.google.com/learn/what-is-a-data-warehouse) — le cadrage, par un fournisseur mais sans jargon.
- [Data Mart vs Data Warehouse: a Detailed Comparison](https://www.datacamp.com/blog/data-mart-vs-data-warehouse) — la distinction et ses conséquences d'organisation.
- [Data Lake VS Data Warehouse VS Data Marts](https://www.youtube.com/watch?v=w9-WoReNKHk) — les trois en quinze minutes.

## Appelée par

- [[parcours/bi-analyst|BI Analyst]]

Voisines : [[notions/data-lake]], [[notions/modelisation-dimensionnelle]], [[notions/transformation-dbt]], [[notions/sql]].
