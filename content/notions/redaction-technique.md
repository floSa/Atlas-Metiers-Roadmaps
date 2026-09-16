---
title: Rédaction technique
tags: [notion, redaction, documentation, decision, communication]
date: 2026-09-16
statut: actif
appelee-par: [forward-deployed-engineer, ai-red-teaming]
---

Production d'écrits destinés à être utilisés — spécification, note de décision, documentation d'exploitation, constat d'audit — dont le critère de qualité est qu'ils permettent d'agir sans leur auteur.

## À quoi ça sert

Un écrit technique n'est pas un compte rendu de ce qu'on a fait : c'est un outil pour quelqu'un d'autre, plus tard. Cela change tout — le plan, la longueur, ce qu'on met en premier. Le lecteur cherche une réponse, il ne lit pas du début à la fin, et il abandonnera si elle n'arrive pas vite.

Trois genres reviennent, avec trois fonctions distinctes. La **note de décision** fige un arbitrage pour qu'il ne soit pas rejoué tous les mois. La **documentation d'exploitation** permet à quelqu'un de faire tourner le système sans son auteur. Le **constat** permet à un lecteur de juger une gravité et de décider s'il corrige.

L'effet le plus utile est défensif : un arbitrage écrit et validé protège d'un changement d'avis rétroactif — non par méfiance, mais parce que les souvenirs divergent de bonne foi.

## Ce qu'il faut savoir

- **La conclusion en premier.** Ce qui a été décidé, ou ce qui a été trouvé, dans les trois premières lignes. Le raisonnement vient après, pour ceux qui le veulent.
- **Une note de décision tient en une page** : la question, les options envisagées, ce qui a été retenu, par qui, à quelle date, et **ce qui invaliderait la décision**. La dernière ligne est la plus utile et la plus souvent absente.
- **Écrire pour le lecteur réel.** Une direction veut l'impact et le choix ; une équipe d'exploitation veut la procédure ; un successeur veut les pourquoi. Trois documents valent mieux qu'un document qui vise tout le monde.
- **Dater et versionner.** Un document sans date ne peut pas être évalué. Le stocker là où vit le code plutôt que dans un espace documentaire séparé qui se périme sans bruit.
- **Distinguer le fait, l'hypothèse et la décision.** Le mélange est la première cause de malentendu, et il se règle par le vocabulaire : « nous avons constaté », « nous supposons », « nous avons choisi ».
- **Le diagramme économise trois paragraphes** quand il montre un mécanisme, et en coûte deux quand il décore.
- **Court gagne.** Ce qui est long n'est pas lu, donc pas contesté, donc pas validé — et une validation obtenue faute de lecture ne protège de rien.

## Selon le métier

### Forward Deployed Engineer

Deux angles. Le registre de décisions sert d'abord à se protéger d'un changement d'avis rétroactif : une page par arbitrage, dans le dépôt, en Markdown, datée, validée par celui qui a le mandat — pas par la salle. Et pour la documentation, le lecteur n'est pas un pair : c'est quelqu'un qui reprendra le système dans six mois, sans contexte et sans pouvoir poser de question.

### AI Red Teaming

Le constat est le livrable du métier, et sa structure est fixe : ce qui a été obtenu, le chemin complet et reproductible, les **conditions requises** — niveau d'accès, nombre de requêtes, connaissance préalable —, l'impact métier chiffré si possible, et une atténuation réaliste avec son coût. Sans les conditions requises, un lecteur ne peut pas juger la gravité, et le rapport devient une liste d'anecdotes inquiétantes.

> [!warning] Piège
> Documenter le fonctionnement et pas les raisons. Le code dit déjà ce que fait le système ; ce qu'il ne dira jamais, c'est pourquoi cette base plutôt qu'une autre, pourquoi ce seuil, pourquoi ce contournement moche qui a l'air d'une erreur. C'est exactement l'information que cherche celui qui reprend, et la seule que personne ne peut reconstituer.

## Pour aller plus loin

- [Requirements Gathering in Software Engineering](https://www.jamasoftware.com/requirements-management-guide/requirements-gathering-and-management-processes/what-is-requirements-gathering/) — le versant spécification, avec ses formalismes.
- [Project Scope Statement en 4 étapes](https://www.youtube.com/watch?v=QDLk2QIuJkg) — comment écrire un périmètre qui tient.

## Appelée par

- [[parcours/forward-deployed-engineer/index|Forward Deployed Engineer]]
- [[parcours/ai-red-teaming/index|AI Red Teaming]]

Voisines : [[notions/cadrage-besoin]], [[notions/transfert-de-competences]], [[notions/gestion-parties-prenantes]].
