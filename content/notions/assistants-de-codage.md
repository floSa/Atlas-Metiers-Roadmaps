---
title: Assistants de codage
tags: [notion, assistants-de-codage, generation-de-code, outillage, productivite]
date: 2026-09-16
statut: actif
appelee-par: [data-analyst, ai-product-builder]
---

Outils qui écrivent, modifient ou expliquent du code à partir d'instructions en langage naturel, en disposant du contexte du projet — Claude Code, Cursor, Codex et leurs équivalents.

## À quoi ça sert

Le gain principal n'est pas d'écrire du code neuf plus vite : c'est de **réduire le coût d'entrée dans du code qu'on ne connaît pas**. Comprendre une base existante, localiser où une règle est appliquée, produire une première version d'une transformation fastidieuse, écrire les tests d'un comportement déjà défini — c'est là que le rapport effort/résultat est le plus net.

Le second gain, plus discret, est la baisse du coût de l'essai. Quand produire une version jetable coûte dix minutes, on en produit deux et on compare, au lieu de débattre. Utiliser la génération pour **décider de ne pas construire** est son usage le plus rentable et le moins pratiqué.

La règle de partage qui tient à l'usage : **générer ce qu'on saurait écrire, écrire ce qu'on ne saurait pas juger**. Inverser cette règle est la définition courte du problème, et elle se vérifie fichier par fichier en revue.

## Ce qu'il faut savoir

- **Le contexte fourni détermine le résultat.** Un modèle qui ne connaît pas le schéma de la base invente des noms de colonnes plausibles ; le même modèle à qui on donne le schéma produit du code correct la plupart du temps.
- **Relire est non négociable**, et le coût de relecture croît avec la taille du diff. Demander des changements petits et vérifiables plutôt qu'une refonte.
- **Les tests sont le garde-corps.** Sur une base partiellement générée, ils sont le seul retour d'exécution qui empêche l'assistant de casser en silence ce qu'il ne comprend pas.
- **Changement local dans le code, changement d'architecture par régénération.** Rapiécer manuellement une modification qui touche le modèle de données produit une base où la moitié suit la logique du générateur et l'autre celle du correcteur.
- **L'historique devient la mémoire des décisions.** Quand une part du code est produite par une machine, le dépôt est le seul endroit où répondre à « qui a décidé ça, et pourquoi ».
- **Confidentialité** : un extrait de base client ne se colle pas dans un service grand public. Vérifier ce que l'organisation autorise, et à quel niveau de donnée.
- **Le défaut typique n'est pas le bug, c'est l'absence silencieuse** : pas de limitation de débit, pas de vérification d'autorisation, pas de journalisation, pas de gestion de l'indisponibilité d'un service externe. Le code livré fonctionne ; ce qui manque ne produit aucune erreur jusqu'au jour où.
- **Brancher l'assistant sur les sources de vérité** — dépôt, base, suivi de tickets — via [[notions/mcp]] change plus le résultat que le choix de l'outil.

## Selon le métier

### Data Analyst

Le gain le plus net est la génération de requêtes et de code, à condition de fournir le schéma et de relire. Un modèle à qui on donne les tables produit du SQL correct la plupart du temps ; sans schéma, il produit des noms de colonnes vraisemblables et faux. La contrainte de confidentialité s'applique intégralement à ce geste-là — voir [[notions/rgpd]].

### AI Product Builder

L'usage dominant n'est pas d'écrire du code neuf mais de **comprendre et modifier du code qu'on n'a pas écrit**, ce qui inverse complètement les critères de choix d'outil : ce qui compte est la qualité de l'exploration du dépôt et du raisonnement sur l'existant, pas la vitesse de complétion. Deux catégories à ne pas confondre en amont : le générateur d'application, qui produit une application complète et hébergée à partir d'une description, et le générateur d'interface, qui produit un écran à intégrer dans un projet existant.

> [!warning] Piège
> Accepter une modification qu'on ne saurait pas écrire soi-même. Elle passera les tests, elle aura l'air raisonnable, et elle deviendra impossible à corriger le jour où elle échouera — parce que personne dans l'équipe ne sait ce qu'elle fait. Le critère n'est pas « est-ce que ça marche », c'est « est-ce que je peux en répondre ».

## Pour aller plus loin

- [Prompt Engineering Guide — DAIR.AI](https://www.promptingguide.ai/) — les techniques de formulation, transposables à la demande de code.
- [What are Tools in AI Agents? — Hugging Face](https://huggingface.co/learn/agents-course/en/unit1/tools) — comprendre ce que l'assistant peut faire quand il est branché sur des outils.

## Appelée par

- [[parcours/data-analyst/index|Data Analyst]]
- [[parcours/ai-product-builder/index|AI Product Builder]]

Voisines : [[notions/mcp]], [[notions/tests-logiciels]], [[notions/integration-continue]], [[notions/agents-llm]].
