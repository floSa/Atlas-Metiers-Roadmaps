---
title: Gestion des parties prenantes
tags: [notion, parties-prenantes, politique, arbitrage, conseil]
date: 2026-09-16
statut: actif
appelee-par: [forward-deployed-engineer, bi-analyst]
---

Travail d'identification des personnes que le projet affecte ou qui peuvent l'affecter, de leurs intérêts réels, et d'organisation des arbitrages entre ces intérêts quand ils divergent.

## À quoi ça sert

Un projet techniquement juste échoue régulièrement, et presque toujours pour la même raison : quelqu'un dont l'intérêt était contrarié n'a pas été identifié, ou l'a été trop tard. Ce n'est pas de la malveillance — c'est que les intérêts divergent réellement, et qu'aucune solution ne les satisfait tous.

Le travail consiste donc à rendre ces divergences visibles et à les traiter comme des arbitrages, pas comme des malentendus à dissiper par la pédagogie. Un désaccord de fond ne se résout pas par une meilleure explication.

L'autre fonction est de savoir **qui décide**. Une salle ne valide pas ; une personne valide. Confondre l'approbation générale d'une réunion avec une décision est la façon la plus courante de découvrir trois mois plus tard que rien n'était acté.

## Ce qu'il faut savoir

- **Cartographier tôt** : qui subit le changement, qui le finance, qui l'exploitera, qui perd quelque chose. La dernière catégorie est celle qu'on oublie et celle qui décide du sort du projet.
- **Distinguer influence et intérêt.** Beaucoup d'influence et peu d'intérêt : à informer, pas à impliquer. Beaucoup des deux : à associer aux décisions. Peu des deux : à ne pas surcharger.
- **L'intérêt réel n'est pas l'intérêt déclaré.** Ce que quelqu'un demande en réunion et ce qu'il protège ne coïncident pas toujours, et ce n'est pas de la duplicité — c'est ce qu'il peut dire publiquement.
- **Identifier le mandat.** Faire valider explicitement par celui qui a le pouvoir d'arbitrer, nommément, par écrit.
- **Préparer l'arbitrage avant la réunion**, pas pendant. Une réunion sert à acter, pas à découvrir un désaccord de fond entre deux directions.
- **Rythme régulier et écrit court** : ce qui a avancé, ce qui est bloqué, ce qui est décidé. Le silence entre deux jalons se remplit d'interprétations.
- **Le porteur du changement doit être interne.** Un intervenant extérieur peut démontrer et outiller ; il ne peut pas imposer. Identifier tôt qui portera.

## Selon le métier

### Forward Deployed Engineer

La cartographie se fait pendant la phase d'audit, en même temps que celle du processus, et les couloirs du schéma BPMN en donnent le premier jet : ils montrent combien de services traverse un dossier, donc combien de personnes devront approuver le changement. C'est l'information politique de la carte, et c'est souvent la plus utile. Voir [[notions/bpmn]].

### BI Analyst

La ligne de fracture est presque toujours la même : celui qui pilote veut une définition stable, celui qui est évalué veut la définition qui l'avantage. Ce n'est pas un problème de données, c'est un arbitrage à préparer avant la réunion. La situation revient tous les mois, sous la forme d'un désaccord sur un chiffre, et elle se traite par une définition écrite, datée et dotée d'un propriétaire.

> [!warning] Piège
> Cadrer avec celui qui finance et pas avec celui qui fait. Le premier décrit le processus tel qu'il devrait être ; le second connaît les exceptions, les contournements et le fichier parallèle qui fait tourner la moitié de l'activité. Un projet construit sur la seule vision du sommet arrive en production sur un processus qui n'existe pas.

## Pour aller plus loin

- [Stakeholder Management Guide](https://simplystakeholders.com/resources/guides/stakeholder-management/) — les méthodes de cartographie, à prendre pour leur grille plus que pour leur formalisme.
- [4 Most Common Stakeholders in Business Intelligence](https://www.youtube.com/watch?v=iPfwEjRhm7w) — la typologie côté BI, appliquée.
- [Business acumen — Wikipédia](https://en.wikipedia.org/wiki/Business_acumen) — le socle de compréhension des enjeux qui rend la cartographie possible.

## Appelée par

- [[parcours/forward-deployed-engineer/index|Forward Deployed Engineer]]
- [[parcours/bi-analyst|BI Analyst]]

Voisines : [[notions/conduite-du-changement]], [[notions/cadrage-besoin]], [[notions/redaction-technique]].
