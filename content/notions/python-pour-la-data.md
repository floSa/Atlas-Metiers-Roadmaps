---
title: Python pour la data
tags: [notion, python, environnement, notebooks, outillage]
date: 2026-09-16
statut: actif
appelee-par: [data-analyst]
---

L'environnement de travail Python d'un analyste : le langage, la gestion des dépendances, les carnets de calcul et les bibliothèques qui gravitent autour de la manipulation de données.

## À quoi ça sert

Python a gagné cette place moins par ses qualités de langage que par son rôle de point de rencontre : la manipulation tabulaire, la visualisation, le calcul scientifique, l'appel d'API et l'intégration au système d'information vivent dans le même environnement. C'est ce qui permet de passer d'une analyse ponctuelle à un traitement automatisé sans changer d'outil ni réécrire.

Cette notion couvre **l'environnement**, pas les bibliothèques : la manipulation tabulaire est dans [[notions/pandas]], la visualisation dans [[notions/visualisation-de-donnees]]. Ce qui reste ici est ce qui décide de la reproductibilité — comment les dépendances sont gérées, comment le code s'organise, et comment un carnet devient un script réutilisable.

## Ce qu'il faut savoir

- **Un environnement isolé par projet**, toujours. Un environnement global finit par contenir des versions incompatibles, et la résolution devient un chantier. Les outils récents (uv, conda, venv classique) font tous le travail ; le choix compte moins que la discipline.
- **Les dépendances sont figées dans un fichier versionné**, avec les versions exactes. C'est la condition minimale pour qu'un résultat soit reproductible par quelqu'un d'autre.
- **Le carnet de calcul est un outil d'exploration**, pas un format de production. L'exécution dans le désordre produit un état invisible : un carnet qui affiche un résultat juste peut ne plus le produire si on le rejoue de haut en bas.
- **La règle utile** : ce qui doit tourner plus d'une fois sort du carnet et devient une fonction dans un module, importée par le carnet. On garde l'exploration et on gagne la testabilité.
- **Redémarrer et tout réexécuter avant de livrer** un carnet. C'est le test le moins cher qui existe et il attrape la majorité des surprises.
- **Les bibliothèques utiles au-delà du socle** : `requests` pour les API, `pyarrow` pour Parquet, `duckdb` pour le SQL local sur fichiers, `great-expectations` ou équivalent pour les contrôles de qualité.
- **La lisibilité prime sur l'astuce.** Un script d'analyse sera relu par quelqu'un qui cherche une règle métier, pas par quelqu'un qui admire une compréhension de liste imbriquée.
- **Choisir un langage et aller au fond** : Python si l'on doit s'interfacer avec le reste du système d'information, R si l'environnement est statistique. Savoir bricoler dans les deux ne vaut rien.

## Selon le métier

### Data Analyst

Ce qui distingue l'usage analyste de l'usage développeur est la destination du code : il sert à établir un résultat, et sa qualité se mesure à la possibilité de le refaire. D'où deux exigences qui priment sur toutes les autres — le nettoyage est un script rejouable depuis la donnée brute, et l'environnement est reproductible par un collègue sans intervention de l'auteur.

> [!info] Une seule appelante
> Notion appelée par le seul parcours Data Analyst. Elle reste séparée de [[notions/pandas]] volontairement : l'une porte l'environnement et la reproductibilité, l'autre la bibliothèque et ses pièges. Voir la synthèse du chantier 07 pour la frontière retenue.

> [!warning] Piège
> Livrer un carnet comme résultat final. Il contient l'exploration, les essais abandonnés, les cellules exécutées dans le désordre et les chemins absolus du poste de son auteur. Le destinataire ne saura ni le rejouer ni distinguer ce qui compte. Le livrable est le résultat plus le script qui le produit ; le carnet reste un brouillon.

## Pour aller plus loin

- [Roadmap Python for Data Analysis](https://roadmap.sh/python-data-analysis) — le parcours amont dédié.
- [Kaggle Learn: Python](https://www.kaggle.com/learn/python) — le socle du langage, court et pratique.
- [Introduction to Data Science with Python — Harvard](https://pll.harvard.edu/course/introduction-data-science-python) — cours complet si les bases manquent.

## Appelée par

- [[parcours/data-analyst/index|Data Analyst]]

Voisines : [[notions/pandas]], [[notions/r-et-tidyverse]], [[notions/traitement-distribue]], [[notions/assistants-de-codage]].
