---
title: Les quatre questions
---

Descriptif, diagnostic, prédictif, prescriptif ne sont pas quatre niveaux de sophistication qu'on gravit : ce sont quatre questions différentes. La seule chose utile qu'elles apportent est un test de cadrage — savoir laquelle des quatre on vous pose, avant de commencer.

```mermaid
flowchart TD
  D["Que s'est-il passé<br/>un chiffre, une évolution, une répartition"]
  P["Pourquoi<br/>là où se trouve la valeur du métier"]
  F["Que va-t-il se passer<br/>une régression suffit presque toujours"]
  A["Que faut-il faire<br/>une recommandation, pas un système"]

  click D "/notions/statistiques-descriptives"
  click P "/notions/analyse-correlation"
  click F "/notions/regression-lineaire"
  click A "/notions/roi-des-projets-ia"
```

## Ce qu'il faut savoir faire

- Nommer la question posée avant d'ouvrir quoi que ce soit. La confusion la plus fréquente et la plus coûteuse est de répondre au descriptif quand on attendait du diagnostic : livrer un tableau de bord des résiliations à quelqu'un qui demandait pourquoi elles ont augmenté. Le tableau est juste, il ne répond pas.
- Entendre la question diagnostique derrière la demande descriptive. « Donne-moi le chiffre d'affaires par région » veut presque toujours dire « explique-moi pourquoi une région décroche », et il vaut mieux le vérifier tout de suite que le découvrir en restitution.
- Assumer le descriptif. C'est la moitié des demandes réelles, ce n'est pas dévalorisant, et un chiffre juste livré vite vaut mieux qu'une analyse tardive que personne n'attendait plus.
- Reconnaître le prédictif qui sort du métier : à volume et à enjeu sérieux, une prédiction qui doit généraliser est un travail de data scientist, pas une analyse — le repère est dans [[ne-pas-confondre]].
- Traiter le prescriptif par une recommandation argumentée, jamais par un système automatisé. Moteurs de recommandation, tarification dynamique et optimisation sont des métiers d'ingénierie.
- Écrire la question retenue en une phrase, et la faire confirmer. C'est le premier des cinq éléments du cadrage.

## Les notions mobilisées

- [[notions/statistiques-descriptives]] — le socle du descriptif : ce qu'une moyenne, une répartition et une évolution disent honnêtement.
- [[notions/analyse-correlation]] — le diagnostic est le cœur du métier, et c'est aussi là qu'on se trompe le plus.
- [[notions/regression-lineaire]] — le prédictif d'analyste tient le plus souvent dans un modèle simple et lisible.
- [[notions/roi-des-projets-ia]] — le prescriptif se ramène pour l'analyste à chiffrer ce que la décision rapporte ou coûte.
- [[notions/cadrage-besoin]] — la méthode générale de recueil et de reformulation, dont ce qui suit est la déclinaison analyste.

> [!warning] Piège
> Répondre à la question littérale quand la question réelle est ailleurs. Elle se détecte en une phrase : « si je te donne ce tableau, qu'est-ce que tu en fais ? ». La réponse contient presque toujours la vraie question, et elle est rarement descriptive.

## Pour apprendre

- [What is Data Analytics?](https://www.ibm.com/think/topics/data-analytics) — la présentation des quatre types, correcte sur les définitions et sobre sur le reste.
- [Requirements Gathering in Business Analysis](https://www.coursera.org/learn/requirements-gathering-in-business-analysis) — accessible en audit libre : la discipline de recueil, applicable telle quelle à une demande d'analyse.
- [Population vs. Sample](https://www.scribbr.com/methodology/population-vs-sample/) — la question à poser en premier, et celle qu'on saute en premier.
