---
title: Orchestration de flux
tags: [notion, orchestration, airflow, dag, ordonnancement]
date: 2026-09-16
statut: actif
appelee-par: [bi-analyst]
---

Coordination des traitements d'un système de données : dans quel ordre ils s'exécutent, sous quelle condition, que faire quand l'un échoue, et comment rejouer ce qui n'a pas abouti.

## À quoi ça sert

Dès qu'une chaîne compte plus de trois traitements, l'ordre et les dépendances deviennent le problème principal. Un ordonnanceur horaire suffit tant que tout va bien ; il devient ingérable dès la première panne — parce que la question n'est plus « quand lancer » mais « qu'est-ce qui a échoué, qu'est-ce qui en dépendait, et à partir d'où reprendre ».

L'orchestrateur répond à cela en représentant la chaîne par un graphe de dépendances : chaque tâche connaît ses prédécesseurs, l'échec se propage, et la reprise repart du point exact. Il apporte en même temps la visibilité — un historique des exécutions, des durées et des échecs, qui est souvent le premier outil de diagnostic d'une équipe data.

## Ce qu'il faut savoir

- **Le graphe orienté acyclique (DAG)** est la structure de base : des tâches, des dépendances, pas de cycle. Il décrit l'ordre, pas le calendrier.
- **Idempotence** : une tâche rejouée sur la même période doit produire le même résultat, sans doublon. C'est la propriété qui rend la reprise sûre, et elle s'obtient par conception — écriture par partition, insertion avec remplacement.
- **Paramétrage par intervalle** : une exécution traite une fenêtre temporelle explicite, pas « maintenant ». C'est ce qui permet de rejouer le 12 du mois dernier sans réécrire le code.
- **Déclenchement par le temps ou par la donnée** : à heure fixe, ou lorsqu'une source est prête. Le second évite les chaînes qui tournent sur des données absentes et produisent des rapports vides.
- **Reprise et alerte** : nombre de tentatives, délai entre elles, alerte sur échec **et sur dépassement de durée**. Une chaîne qui ne finit jamais ne déclenche aucune alerte d'échec.
- **L'orchestrateur coordonne, il ne calcule pas.** Faire exécuter le traitement lourd par l'entrepôt ou le moteur adapté, et garder l'orchestrateur mince.
- **Le paysage** : Airflow reste la référence installée ; Dagster et Prefect proposent un modèle plus orienté données ; les ordonnanceurs intégrés aux plateformes infonuagiques suffisent souvent.
- **La documentation d'exploitation** — que faire quand telle tâche échoue — vaut autant que le graphe. C'est elle qui manque à trois heures du matin.

## Selon le métier

### BI Analyst

L'angle est la fiabilité perçue du rapport. Ce que voit le métier n'est pas la chaîne mais un tableau de bord vide ou périmé, et il en conclut que le chiffre n'est pas fiable. Deux conséquences pratiques : afficher la date et l'heure du dernier rafraîchissement sur le rapport lui-même, et préférer un rapport qui affiche explicitement « données du 14 » plutôt qu'un rapport qui affiche silencieusement d'anciennes valeurs.

> [!info] Une seule appelante
> Notion appelée par le seul parcours BI Analyst. Elle recoupe le parcours Data Engineer et le parcours MLOps du corpus, ce qui justifie qu'elle reste mutualisée.

> [!warning] Piège
> Enchaîner les traitements par des horaires décalés — « celui-ci à 2 h, celui-là à 3 h, il aura fini » — au lieu de déclarer des dépendances. Le jour où le premier prend deux heures de plus, le second s'exécute sur des données incomplètes, sans erreur et sans alerte : le rapport est faux et il a l'air normal. C'est le mode d'échec le plus coûteux du domaine parce qu'il est silencieux.

## Pour aller plus loin

- [Apache Airflow — documentation](https://airflow.apache.org/docs) — la référence, y compris sur les concepts d'intervalle et de reprise.
- [Building Pipelines In Apache Airflow – For Beginners](https://towardsdatascience.com/building-pipelines-in-apache-airflow-for-beginners-58f87a1512d5/) — la prise en main par l'exemple.
- [What is Apache Airflow? For beginners](https://www.youtube.com/watch?v=CGxxVj13sOs) — l'introduction en vidéo.

## Appelée par

- [[parcours/bi-analyst|BI Analyst]]

Voisines : [[notions/transformation-dbt]], [[notions/qualite-des-donnees]], [[notions/entrepot-de-donnees]], [[notions/observabilite]].
