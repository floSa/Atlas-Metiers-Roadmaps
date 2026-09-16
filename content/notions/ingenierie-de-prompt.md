---
title: Ingénierie de prompt
tags: [notion, prompt, llm, instruction, contexte]
date: 2026-09-16
statut: actif
appelee-par: [ai-product-builder, ai-red-teaming]
---

Pratique consistant à écrire les instructions et à organiser le contexte fournis à un modèle de manière à obtenir un comportement fiable et reproductible.

## À quoi ça sert

Le prompt est l'interface de programmation d'un modèle : c'est là que se déclarent le rôle, le format attendu, les contraintes, les exemples et les limites. Bien écrit, il remplace la plupart des raisons qu'on aurait d'affiner, pour un coût et un délai sans commune mesure.

Le domaine s'est largement décanté. Ce qui reste vrai relève de la spécification claire — dire précisément ce qu'on veut, dans quel format, avec quoi faire en cas de doute. Ce qui relève du folklore — formules magiques, politesse supposée efficace, menaces ou promesses de pourboire — n'a jamais eu d'effet stable et n'en a pas davantage aujourd'hui.

La bascule récente est celle de l'**ingénierie de contexte** : sur les systèmes qui récupèrent des documents et appellent des outils, la question n'est plus « comment formuler » mais « qu'est-ce qui occupe la fenêtre, dans quel ordre, et qu'est-ce qu'on en retire ».

## Ce qu'il faut savoir

- **Être spécifique bat tout le reste.** Rôle, tâche, format de sortie, contraintes, conduite à tenir en cas d'information manquante. La majorité des mauvais résultats viennent d'une consigne qui n'a jamais été donnée.
- **Les exemples (few-shot)** sont le levier le plus efficace sur le format et le style. Deux ou trois exemples bien choisis, couvrant un cas limite, valent une page de description.
- **Sortie structurée** : exiger un schéma et le valider côté code. Ne jamais analyser une sortie libre en espérant qu'elle tienne.
- **Le raisonnement explicite** (chaîne de pensée) aide sur les tâches à plusieurs étapes et coûte pour rien sur l'extraction. Sur les modèles de raisonnement récents, il est intégré et se règle par un budget.
- **Le prompt système porte les invariants**, le message utilisateur porte le variable. Cette séparation conditionne aussi la mise en cache, donc le coût.
- **Un prompt est un actif versionné et testé**, pas une chaîne modifiée en production. Chaque modification se rejoue sur le jeu d'évaluation.
- **Position dans le contexte** : une fenêtre large ne garantit pas une attention uniforme, et la performance chute au milieu des longs contextes. Ce qui compte va en tête ou en queue.
- **Températeur 0 ne rend pas l'appel reproductible** : le traitement par lots côté fournisseur et le routage entre machines introduisent de la variance. Écrire des tests tolérants.

## Selon le métier

### AI Product Builder

Le prompt est un actif produit, versionné et testé comme du code, pas une chaîne dans un fichier de configuration modifiée en production. La conséquence pratique : il vit dans le dépôt, il passe en revue, et tout changement rejoue le jeu d'évaluation avant livraison.

### AI Red Teaming

C'est à la fois l'outil du test et son objet : les mêmes leviers qui font suivre une consigne au modèle sont ceux qui permettent d'en imposer une autre. Comprendre ce qui fait obéir un modèle est exactement ce qui permet de le faire désobéir — d'où l'inutilité des défenses fondées sur la seule formulation. Voir [[notions/injection-de-prompt]].

> [!warning] Piège
> Corriger un prompt à l'aveugle, cas par cas, jusqu'à ce que l'exemple montré en réunion passe. On obtient un prompt long, contradictoire, qui a régressé sur des cas qu'on ne teste plus. Sans jeu d'évaluation rejoué, chaque amélioration est un pari — voir [[notions/evaluation-llm]].

## Pour aller plus loin

- [Prompt Engineering Guide — DAIR.AI](https://www.promptingguide.ai/) — la référence du domaine, tenue à jour et sourcée.
- [Chain-of-Thought Prompting Elicits Reasoning in LLMs](https://arxiv.org/abs/2201.11903) — l'article d'origine, utile pour savoir ce que la technique démontre réellement.
- [Context Engineering vs. Prompt Engineering](https://www.youtube.com/watch?v=vD0E3EUb8-8) — le déplacement récent du sujet, expliqué simplement.
- [[roadmaps/06 - Roadmap — Prompt Engineering]] — la note de fond du corpus.

## Appelée par

- [[parcours/ai-product-builder/index|AI Product Builder]]
- [[parcours/ai-red-teaming/index|AI Red Teaming]]

Voisines : [[notions/injection-de-prompt]], [[notions/evaluation-llm]], [[notions/affinage-de-modele]], [[notions/choix-de-modele]].
