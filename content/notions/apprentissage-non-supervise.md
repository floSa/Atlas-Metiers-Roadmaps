---
title: Apprentissage non supervisé
tags: [notion, machine-learning, apprentissage-non-supervise, clustering, segmentation]
date: 2026-09-16
statut: actif
appelee-par: [data-analyst, bi-analyst, ai-red-teaming]
---

Famille de méthodes qui cherchent une structure dans des données sans étiquette : regrouper les observations qui se ressemblent, réduire le nombre de dimensions, ou repérer ce qui s'écarte du reste.

## À quoi ça sert

Le non supervisé sert quand personne ne sait encore quelle est la bonne réponse. Il ne prédit rien : il **propose une lecture**. C'est utile pour explorer un jeu de données qu'on ne connaît pas, pour suggérer une segmentation à discuter avec le métier, ou pour signaler des points inhabituels qui méritent un regard humain.

Sa limite tient à l'absence de vérité de référence : il n'existe pas de bonne réponse contre laquelle mesurer le résultat. Un regroupement n'est ni juste ni faux, il est utile ou inutile — et ce jugement appartient à quelqu'un qui connaît le métier, pas à une métrique.

D'où la règle qui gouverne tout usage sérieux : **le clustering sert à proposer une segmentation, pas à la trancher**. Une segmentation statistique qu'aucun responsable métier ne reconnaît ne sera jamais utilisée, quelle que soit sa qualité mathématique.

## Ce qu'il faut savoir

- **Clustering** : k-means (rapide, suppose des groupes sphériques de taille comparable, exige de fixer k), hiérarchique (donne un arbre, lisible sur petits volumes), DBSCAN (trouve des formes quelconques et isole le bruit, sans fixer k).
- **Le nombre de groupes est une décision, pas un résultat.** Coude, silhouette et indices divers donnent une fourchette ; le choix final se fait sur l'interprétabilité des groupes obtenus.
- **La mise à l'échelle des variables est déterminante.** Toutes ces méthodes reposent sur une distance : une variable exprimée en euros et une autre en années ne pèsent pas pareil tant qu'elles n'ont pas été normalisées. C'est l'erreur d'implémentation la plus répandue.
- **Réduction de dimension** : ACP pour compresser en conservant la variance, t-SNE et UMAP pour visualiser. Attention — les distances et les tailles de groupes sur une projection t-SNE ou UMAP ne sont pas interprétables, seule la structure locale l'est.
- **Détection d'anomalie** : ce qui est statistiquement rare n'est pas nécessairement ce qui est problématique. Le taux d'alerte se calibre sur la capacité de traitement humaine, pas sur un seuil théorique.
- **Un regroupement se décrit avant d'être publié** : effectif, profil moyen, ce qui distingue chaque groupe des autres en une phrase. Un groupe qu'on ne sait pas nommer ne sera pas adopté.
- **La stabilité se vérifie** : relancer sur un échantillon différent, ou avec une autre initialisation. Des groupes qui changent complètement ne portent pas de structure réelle.

## Selon le métier

### Data Analyst

Le clustering propose une segmentation, il ne la tranche pas. La sortie utile n'est pas la partition mais la conversation qu'elle permet avec le métier : « voilà cinq groupes, en reconnaissez-vous trois ? ». La réduction de dimension sert surtout à visualiser un jeu large avant de choisir les variables à explorer.

### BI Analyst

L'usage courant est la segmentation de clientèle et la détection d'anomalie sur des séries. La question qui décide n'est pas la qualité du regroupement mais sa **persistance** : une segmentation utile doit devenir une dimension stable dans le modèle, avec une règle d'affectation reproductible, sinon elle vit le temps d'une présentation.

### AI Red Teaming

Deux angles opposés. Un regroupement révèle parfois ce que l'anonymisation était censée masquer : recouper des attributs quasi identifiants suffit à reconstituer des individus dans un jeu réputé anonyme. À l'inverse, une réduction de dimension peut effacer précisément le signal sur lequel repose une détection — ce qui en fait un vecteur d'évasion plutôt qu'une défense.

> [!warning] Piège
> Publier une segmentation sans règle d'affectation pour les nouveaux cas. Le modèle a partitionné les clients existants ; trois mois plus tard, personne ne sait dans quel groupe ranger un client arrivé depuis, et la segmentation est abandonnée. La règle d'affectation fait partie du livrable, pas du prolongement.

## Pour aller plus loin

- [Clustering — scikit-learn](https://scikit-learn.org/stable/modules/clustering.html) — le comparatif des méthodes, avec les cas où chacune échoue.
- [What is clustering? — Google Developers](https://developers.google.com/machine-learning/clustering/overview) — le cours court, orienté décisions pratiques.
- [Unsupervised Clustering: A Guide](https://builtin.com/articles/unsupervised-clustering) — panorama accessible des familles de méthodes.

## Appelée par

- [[parcours/data-analyst|Data Analyst]]
- [[parcours/bi-analyst|BI Analyst]]
- [[parcours/ai-red-teaming|AI Red Teaming]]

Voisines : [[notions/apprentissage-supervise]], [[notions/analyse-de-cohorte]], [[notions/donnees-sensibles]].
