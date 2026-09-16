---
title: Processus, threads et matériel
tags: [parcours, computer-science, concurrence, memoire, cache, gil, vram]
date: 2026-09-16
statut: actif
source: https://roadmap.sh/computer-science
---

**Autonomie.** L'incident de production d'un pipeline ou d'un entraînement est presque toujours ici, et il faut le diagnostiquer seul, la nuit — la référence restant chez qui écrit les noyaux de calcul, pas chez qui les fait tourner.

Le chapitre qui transforme les incidents mystérieux en diagnostics : un chargeur de données qui bloque, une mémoire qui explose au *fork*, un travail qui n'utilise que quinze pour cent des cœurs.

```mermaid
flowchart TD
  TD["Traitement distribué<br/>quand une machine ne suffit plus"]
  CT["Conteneurisation<br/>les limites que voit le processus"]
  OB["Observabilité<br/>mesurer avant de supposer"]
  CL["Coût et latence<br/>la VRAM partagée entre poids et cache"]

  click TD "/notions/traitement-distribue"
  click CT "/notions/conteneurisation"
  click OB "/notions/observabilite"
  click CL "/notions/cout-et-latence-inference"
```

## De la concurrence à la hiérarchie mémoire

Un **processus** a sa mémoire isolée, un **thread** la partage. En Python, le verrou global rend les threads utiles pour l'attente d'entrée-sortie et inutiles pour le calcul pur. Le *fork* en copie sur écriture paraît gratuit jusqu'à ce que chaque enfant touche les pages partagées — et le simple comptage de références y suffit. Côté **mémoire**, pile, tas, mémoire virtuelle et pagination expliquent le cas le plus déroutant : le fichier d'échange qui s'active et rend un traitement cent fois plus lent sans lever la moindre erreur.

Verrou, mutex et sémaphore sont les trois primitives à connaître, le sémaphore étant l'outil naturel pour plafonner le nombre d'appels simultanés à un service. Le parallélisme sur plusieurs cœurs est réel, mais la **sur-souscription** guette : une bibliothèque de calcul lance déjà autant de threads que de cœurs, et empiler du multiprocessing par-dessus dégrade tout. L'ordonnanceur, lui, explique la variabilité de latence sur machine partagée, et les interruptions sont le mécanisme matériel derrière les entrées-sorties asynchrones.

La **hiérarchie mémoire** est ce qui explique le plus de choses pour le moins d'effort. La latence croît de plusieurs ordres de grandeur du registre à la mémoire vive, et parcourir une matrice dans le mauvais ordre multiplie le temps par cinq à opérations identiques : c'est toute la justification du calcul vectorisé. La même hiérarchie se retrouve sur processeur graphique — registres, mémoire partagée par bloc, puis mémoire à haute bande passante — et c'est le cœur de l'optimisation d'inférence : les noyaux fusionnés ne changent pas la complexité, ils évitent des allers-retours. Concrètement, la mémoire vidéo se partage entre poids du modèle et cache d'attention, et ce partage fixe le nombre de requêtes simultanées possibles.

## Ce qu'il faut savoir faire

- **Diagnostiquer une fuite mémoire, une sur-souscription de threads ou un dépassement de mémoire**, et distinguer les trois à partir des symptômes.
- **Choisir entre threads, processus et asynchrone** selon que la tâche attend ou calcule, et savoir énoncer pourquoi.
- **Plafonner une concurrence** avec un sémaphore plutôt qu'avec une temporisation empirique.
- **Repérer un accès mémoire dans le mauvais ordre** et le corriger : c'est souvent le gain le plus important d'un profilage.
- **Estimer une occupation de mémoire vidéo** — poids plus cache — et en déduire le nombre de requêtes simultanées tenables.
- **Vérifier les limites vues par le processus** dans un conteneur : le nombre de cœurs visible n'est pas toujours celui qui est alloué.

> [!warning] Piège
> Lancer un chargeur de données avec beaucoup de processus de travail sur un jeu qui référence un gros objet Python : le comptage de références touche les pages et déclenche la copie sur écriture, multipliant la mémoire par le nombre de processus. Passer par des tableaux NumPy ou une projection mémoire règle le problème.

## Les notions mobilisées

- [[notions/traitement-distribue]] — l'angle *computer science* : on ne distribue qu'après avoir épuisé une machine, et la sur-souscription est le symptôme qu'on ne l'a pas fait.
- [[notions/conteneurisation]] — limites de mémoire et de processeur, espaces de noms : ce que le processus croit voir n'est pas ce qu'il a.
- [[notions/observabilite]] — un diagnostic de concurrence sans métriques d'occupation est une conjecture.
- [[notions/cout-et-latence-inference]] — le partage de la mémoire vidéo entre poids et cache est ce qui fixe le débit, donc le coût unitaire.

## Pour apprendre

- [Operating Systems: Three Easy Pieces](https://pages.cs.wisc.edu/~remzi/OSTEP/) — le manuel libre de référence ; les parties virtualisation et concurrence suffisent.
- *Computer Systems: A Programmer's Perspective*, Bryant et O'Hallaron — représentation binaire, cache, processus, mémoire virtuelle, du point de vue de celui qui écrit le code.
- [What Every Programmer Should Know About Memory](https://people.freebsd.org/~lstewart/articles/cpumemory.pdf), Ulrich Drepper — long, mais les trois premières parties expliquent définitivement le cache.
- [py-spy](https://github.com/benfred/py-spy) — profiler un processus Python en production sans le modifier ; l'outil qui répond le plus vite à « pourquoi c'est lent ».
- [Efficiently Scaling Transformer Inference](https://arxiv.org/abs/2211.05102) — comment la mémoire vidéo se partage réellement, et ce que cela impose au dimensionnement.
