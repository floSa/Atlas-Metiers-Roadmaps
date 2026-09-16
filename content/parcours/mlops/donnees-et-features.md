---
title: Données et features
tags: [parcours, mlops, feature-store, point-in-time, pipelines, schema]
date: 2026-09-16
statut: actif
source: https://roadmap.sh/mlops
---

Niveau attendu : **autonomie**. Un confirmé débusque seul une fuite temporelle et un écart entre entraînement et service, sous pression et sans le data scientist ; la référence sur les pipelines eux-mêmes appartient au data engineer, avec qui ce domaine se partage en permanence.

La qualité d'un modèle est plafonnée par celle de ses données, et sa fiabilité par celle de ses pipelines : en pratique, la majorité des incidents « modèle » sont des incidents « données ».

```mermaid
flowchart TD
  QU["Qualité des données<br/>le contrôle bloque à l'ingestion"]
  SQ["SQL<br/>beaucoup de features se calculent dans l'entrepôt"]
  DL["Data lake<br/>le brut, et le lakehouse qui l'a rendu transactionnel"]
  TD["Traitement distribué<br/>et le seuil en dessous duquel s'en passer"]
  OR["Orchestration de flux<br/>le graphe qui produit les tables d'entraînement"]

  click QU "/notions/qualite-des-donnees"
  click SQ "/notions/sql"
  click DL "/notions/data-lake"
  click TD "/notions/traitement-distribue"
  click OR "/notions/orchestration-de-flux"
```

## La correction temporelle, et pourquoi elle coûte cher

Le calcul d'une feature à l'entraînement doit voir **exactement ce qui était connu à l'instant de la prédiction**, et rien de plus. Une jointure naïve sur un identifiant client ramène la valeur d'aujourd'hui pour un événement d'il y a six mois : le modèle apprend sur le futur, obtient un score magnifique hors ligne, et s'effondre en production.

Le problème se double d'un second : la même feature est généralement calculée deux fois, une fois en lot pour l'entraînement, une fois en ligne pour le service. Les deux implémentations divergent — c'est la cause numéro un de l'écart entraînement-service. Un magasin de features résout précisément ces deux points : une définition unique, servie en lot avec correction temporelle et en ligne avec la même logique.

Cela dit, un magasin de features est une infrastructure de plus à exploiter. Sur un ou deux modèles, une table d'entraînement construite avec des jointures horodatées explicites et une bibliothèque partagée entre lot et ligne suffit — et se débogue.

## Ce qu'il faut savoir faire

- **Écrire une jointure horodatée correcte** et savoir la relire : pour chaque exemple, la valeur retenue est la dernière connue **avant** l'instant de prédiction, avec le décalage réel de disponibilité de la donnée.
- **Poser les contrôles de données en amont**, à l'ingestion, et les rendre bloquants : schéma, plages, taux de nuls, volumétrie. Détecter une anomalie par les prédictions, c'est la détecter trois jours trop tard.
- **Choisir le mode d'ingestion sur la fraîcheur exigée** — lot, micro-lot, flux, capture de changements — et non sur la mode. Voir [[parcours/data-engineer/sources-et-ingestion]].
- **Ne pas dégainer un moteur distribué sous cent gigaoctets** : un moteur mono-nœud va plus vite pour un coût d'exploitation nul.
- **Exiger un registre de schémas** sur les flux d'événements qui alimentent les features : c'est ce qui empêche un producteur de casser tous ses consommateurs en un déploiement.
- **Documenter chaque feature** : source, transformation, fenêtre, disponibilité. Une feature dont personne ne sait quand elle est rafraîchie ne peut pas être débuguée.

> [!tip] Ajout 2026
> Le rapprochement avec le métier de data engineer est devenu total sur cette page. La charge de travail — contrats de schéma, idempotence, reprise, lignage — est la même, seule la consommation en aval diffère. Sur une petite équipe, c'est la même personne ; sur une grande, c'est la frontière où les incidents se perdent, et elle mérite un contrat écrit plutôt qu'une habitude. Voir [[parcours/data-engineer/index]].

> [!warning] Piège
> Considérer qu'une AUC de 0,99 sur un problème métier ordinaire est une bonne nouvelle. C'est presque toujours une fuite de données — une colonne qui contient la réponse, ou une feature calculée après coup. La personne qui met en production est souvent la seule à regarder le pipeline de bout en bout, donc la seule à pouvoir le voir.

## Les notions mobilisées

- [[notions/qualite-des-donnees]] — ici, un contrôle bloquant posé à l'entrée ; c'est le seul endroit où il empêche quelque chose.
- [[notions/sql]] — beaucoup de features se calculent mieux dans l'entrepôt que dans un traitement distribué, et se relisent mieux.
- [[notions/data-lake]] — le brut conservé à bas coût, et le lakehouse qui a rendu ces tables transactionnelles et rejouables.
- [[notions/traitement-distribue]] — utile au-delà d'un seuil, coûteux en dessous ; le savoir évite une plateforme entière inutile.
- [[notions/orchestration-de-flux]] — le graphe qui produit les tables d'entraînement, avec ses reprises et ses dépendances.

## Pour apprendre

- [What is a Feature Store](https://www.snowflake.com/guides/what-feature-store-machine-learning/) — la définition et le problème que ça résout, correction temporelle comprise.
- [Feast — Documentation](https://docs.feast.dev/) — le magasin de features libre de référence, à installer pour comprendre le service en ligne.
- [How to Build Data Pipelines for Machine Learning](https://towardsdatascience.com/how-to-build-data-pipelines-for-machine-learning-b97bbef050a5/) — la chaîne complète, vue depuis le modèle.
- [Data Ingestion Patterns](https://docs.aws.amazon.com/whitepapers/latest/aws-cloud-data-ingestion-patterns-practices/data-ingestion-patterns.html) — le catalogue des schémas d'ingestion et leurs garanties.
- [Apache Kafka Quickstart](https://kafka.apache.org/quickstart) — pour éprouver ce qu'un flux d'événements impose aux features temps réel.
