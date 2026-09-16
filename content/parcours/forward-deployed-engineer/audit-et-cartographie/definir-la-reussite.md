---
title: Définir la réussite
---

La question qui décide de tout n'est pas « qu'est-ce qu'on construit » mais « à quoi saura-t-on que ça marche ». Un système d'IA n'a pas de réussite binaire : il a une distribution de qualité.

```mermaid
flowchart TD
  P["Le problème à résoudre<br/>reformulé, borné, écrit"]
  S["Un seuil chiffré<br/>et la mesure qui le produit"]
  H["La référence humaine<br/>le taux d'erreur actuel sur les mêmes cas"]
  M["Des unités métier<br/>délai, taux de reprise, dossiers par jour"]
  A["Accepté par celui qui décide<br/>pas par la salle"]

  click P "/notions/cadrage-besoin"
  click S "/notions/evaluation-llm"
  click H "/notions/metriques-evaluation-ml"
  click M "/notions/roi-des-projets-ia"
  click A "/notions/gestion-parties-prenantes"
```

## Ce qu'il faut savoir faire

- Comparer le seuil à quelque chose : la performance humaine actuelle sur les mêmes cas. Presque personne ne la connaît, et l'établir est souvent le constat le plus utile de la phase — le taux d'erreur humain sur une tâche répétitive est rarement celui qu'on imagine.
- Refuser un objectif en pourcentage tant que la mesure n'est pas définie : précision sur quel échantillon, jugée par qui, comparée à quoi.
- Formuler la réussite en termes métier, et pas seulement en métriques de modèle.
- Fixer aussi le critère d'échec, celui qui fait arrêter. Un projet sans critère d'arrêt ne s'arrête jamais, il s'éteint.
- Dire tôt et par écrit ce que l'IA ne fera pas, dans le même document que ce qu'elle fera.
- Faire nommer par le client les vingt cas qu'il veut voir passer, et les écrire. Ils deviendront le noyau du jeu d'évaluation, et leur rédaction fait apparaître les désaccords internes sur ce qu'est une bonne réponse.

## Les notions mobilisées

- [[notions/cadrage-besoin]] — l'angle FDE est que la définition de la réussite fait partie du cadrage, pas de la recette.
- [[notions/evaluation-llm]] — le protocole qui matérialisera ce seuil se construit en phase 2 ; ici on fixe ce qu'il devra mesurer.
- [[notions/metriques-evaluation-ml]] — la référence humaine se mesure comme une performance de modèle : sur un échantillon, avec une convention d'annotation.
- [[notions/roi-des-projets-ia]] — un seuil qui ne se traduit pas en gain métier ne sera défendu par personne.
- [[notions/gestion-parties-prenantes]] — un seuil accepté par la salle n'engage personne ; il faut celui qui a le mandat.

> [!warning] Piège
> Accepter « quatre-vingt-quinze pour cent de précision » sans définir la mesure. Le chiffre rassure tout le monde en réunion et se retourne contre le FDE en recette.
