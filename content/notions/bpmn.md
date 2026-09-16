---
title: BPMN
tags: [notion, bpmn, processus, notation, cartographie]
date: 2026-09-16
statut: actif
appelee-par: [forward-deployed-engineer]
---

Notation graphique normalisée pour représenter un processus métier : ce qui se fait, dans quel ordre, par qui, et ce qui déclenche ou interrompt chaque étape.

## À quoi ça sert

Une carte de processus est le seul document qu'une équipe métier lira réellement, et elle circule bien au-delà du projet qui l'a produite. Sa fonction n'est pas documentaire : c'est un **support de discussion**. Posée sur une table, elle fait apparaître en dix minutes les désaccords qu'aucun entretien ne révèle — deux personnes qui décrivent la même étape différemment, un contrôle que personne ne fait plus, une boucle de reprise que le responsable ignorait.

Son second usage est politique. Les couloirs de la carte montrent combien de services traverse un dossier, donc combien de personnes devront approuver le changement. C'est souvent l'information la plus utile qu'elle contient, et elle n'a rien à voir avec la technique.

Le troisième est un préalable à toute automatisation : on n'automatise pas un processus qu'on n'a pas su dessiner.

## Ce qu'il faut savoir

- **On n'utilise qu'une fraction du standard** : tâches, passerelles, événements, couloirs, objets de données. Le reste est de la virtuosité inutile devant une équipe métier — et une carte que le métier ne lit pas ne sert à rien.
- **Les couloirs (`pools` et `lanes`)** portent l'organisation : qui fait quoi. Chaque franchissement de couloir est une attente potentielle et un point d'approbation.
- **Les passerelles** expriment les branchements : exclusive (un seul chemin), parallèle (tous), inclusive (un ou plusieurs). Confondre exclusive et inclusive est l'erreur de lecture la plus fréquente.
- **Les événements** — début, fin, intermédiaire, d'erreur, de temporisation — sont ce qui distingue une carte BPMN d'un organigramme : ils disent ce qui déclenche et ce qui interrompt.
- **Dessiner le processus tel qu'il est**, pas tel qu'il devrait être. La version officielle est presque toujours différente de la pratique, et l'écart est l'information la plus précieuse.
- **Chercher les attentes plus que les tâches.** Dans la plupart des processus lents, le temps passe entre les étapes, pas dedans — et c'est là que se trouvent les gains les moins risqués.
- **Une carte se date et se fait valider** par ceux qui exécutent le processus, pas seulement par ceux qui le pilotent.
- **BPMN est exécutable** par un moteur de processus, mais c'est un autre métier. Dans un contexte de cartographie, la notation reste un langage de description.

## Selon le métier

### Forward Deployed Engineer

La carte est un livrable de la phase d'audit et le document qui survit le plus longtemps à la mission. L'angle propre au FDE : n'utiliser qu'une fraction du standard, parce que le lecteur visé est une équipe métier et non un analyste de processus. Elle alimente directement deux autres travaux — la cartographie des parties prenantes, dont les couloirs donnent le premier jet, et l'arbitrage déterministe/probabiliste, qui se rend **par étape** de cette carte.

> [!info] Une seule appelante
> Notion appelée par le seul parcours Forward Deployed Engineer. Elle reste mutualisée parce que c'est une notation standard indépendante du métier, que le parcours délègue explicitement pour ne garder que son angle.

> [!warning] Piège
> Produire une carte complète et juste que personne ne relira. Le signe est facile à reconnaître : si la carte ne tient pas sur une page lisible à l'écran, elle ne sera pas discutée, et une carte non discutée n'a rien validé. Mieux vaut trois cartes à trois niveaux de détail qu'un schéma exhaustif que seul son auteur comprend.

## Pour aller plus loin

- [BPMN Specification — OMG](https://www.omg.org/spec/BPMN/2.0/) — la norme elle-même, à consulter par élément plutôt qu'à lire.
- [bpmn.org](https://www.bpmn.org/) — le portail de la notation, avec les ressources d'introduction.
- [Business Process Model and Notation — Wikipédia](https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation) — le panorama des éléments et de leur usage réel.

## Appelée par

- [[parcours/forward-deployed-engineer/index|Forward Deployed Engineer]]

Voisines : [[notions/reingenierie-de-processus]], [[notions/cadrage-besoin]], [[notions/gestion-parties-prenantes]], [[notions/arbitrage-deterministe-probabiliste]].
