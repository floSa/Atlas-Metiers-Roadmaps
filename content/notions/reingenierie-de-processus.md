---
title: Réingénierie de processus
tags: [notion, bpr, processus, simplification, organisation]
date: 2026-09-16
statut: actif
appelee-par: [forward-deployed-engineer]
---

Démarche qui consiste à remettre en cause l'enchaînement des étapes d'un processus — les supprimer, les fusionner, les réordonner — avant d'envisager de les outiller.

## À quoi ça sert

Automatiser une étape inutile produit une étape inutile plus rapide. C'est le constat fondateur de la démarche, et il reste le plus rentable : la suppression est le seul gain qui ne coûte rien à exploiter, ne tombe jamais en panne et ne demande aucune maintenance.

L'ordre compte donc : **simplifier d'abord, outiller ensuite**. Un processus qui passe de onze à six jours par suppression d'attentes et connexion de deux systèmes est un résultat acquis sans risque technique — et il achète la confiance nécessaire à la partie incertaine du projet.

Le troisième intérêt est diagnostique. En cherchant pourquoi une étape existe, on découvre presque toujours qu'elle compense un défaut situé ailleurs : un contrôle manuel qui rattrape une saisie non validée, une ressaisie qui pallie deux systèmes non connectés. Traiter la cause vaut mieux qu'accélérer la compensation.

## Ce qu'il faut savoir

- **L'ordre des questions** : cette étape peut-elle être supprimée ? fusionnée avec une autre ? déplacée plus tôt ? faite par quelqu'un d'autre ? automatisée ? L'automatisation vient en dernier, pas en premier.
- **Chercher les attentes, les ressaisies et les contrôles.** Le temps d'un processus passe surtout entre les étapes ; les ressaisies signalent deux systèmes non connectés ; les contrôles signalent un défaut de qualité en amont.
- **Quantifier même grossièrement.** « Quatre-vingts dossiers par semaine, vingt minutes chacun, dont la moitié en ressaisie » suffit à trancher, et ces chiffres se collectent en phase d'audit ou jamais.
- **Une étape a toujours une raison**, même quand elle n'en a plus. Demander son origine avant de proposer sa suppression : la réponse révèle soit une cause à traiter, soit une contrainte réelle qu'on n'avait pas vue.
- **La suppression n'appartient pas à celui qui la propose** : elle appartient au propriétaire du processus. C'est le gain le plus rentable et le plus difficile à obtenir, parce qu'il est politique et non technique.
- **Les exceptions sont le vrai sujet.** Un processus décrit comme linéaire traite en réalité 60 % des cas de cette façon ; les 40 % restants passent par des chemins que personne n'a documentés et qui font l'essentiel de la charge.
- **La réingénierie sans mesure de départ ne prouve rien.** Établir la situation de référence avant d'intervenir, sinon aucun gain ne sera démontrable.

## Selon le métier

### Forward Deployed Engineer

La réingénierie n'est pas un projet séparé, c'est la première semaine du projet d'IA — et le FDE l'obtient parce qu'il est sur place, pas parce qu'il a un mandat pour cela. L'angle pratique : mesurer ce que vaut la simplification seule, avant toute IA, et l'annoncer. Un FDE qui commence par la démonstration la plus impressionnante dépense son capital de confiance au lieu de le constituer.

> [!info] Une seule appelante
> Notion appelée par le seul parcours Forward Deployed Engineer, qui délègue explicitement le cadre méthodologique pour ne garder que sa mise en œuvre de mission.

> [!warning] Piège
> Confondre réingénierie et remise en cause de l'organisation. Redessiner un processus déplace des responsabilités, et un intervenant sans mandat qui s'y engage se heurte à un refus légitime. Ce qui passe est toujours la même chose : montrer l'écart chiffré, proposer, et laisser le propriétaire du processus décider — y compris de ne rien changer.

## Pour aller plus loin

- [Business process re-engineering — Wikipédia](https://en.wikipedia.org/wiki/Business_process_re-engineering) — l'histoire de la démarche, ses excès des années 1990 et ce qui en reste.
- [Project management triangle — Asana](https://asana.com/resources/project-management-triangle) — le cadre d'arbitrage périmètre / délai / qualité qui encadre toute simplification.

## Appelée par

- [[parcours/forward-deployed-engineer/index|Forward Deployed Engineer]]

Voisines : [[notions/bpmn]], [[notions/arbitrage-deterministe-probabiliste]], [[notions/roi-des-projets-ia]], [[notions/conduite-du-changement]].
