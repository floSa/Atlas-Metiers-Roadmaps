---
tags: [notion, garde-fous, securite, llm, moderation]
date: 2026-09-16
statut: actif
appelee-par: [forward-deployed-engineer, ai-product-builder, ai-red-teaming]
---

# Garde-fous

Dispositifs placés autour d'un modèle pour contraindre ce qui entre, ce qui sort et ce que le système a le droit de faire, de manière à ce qu'une défaillance du modèle ne devienne pas une défaillance du système.

## À quoi ça sert

Un modèle est un composant non déterministe dont on ne peut pas garantir le comportement. Les garde-fous ne cherchent pas à le rendre fiable : ils bornent les conséquences de son manque de fiabilité. C'est la même logique qu'un disjoncteur — on n'empêche pas le court-circuit, on empêche l'incendie.

La distinction utile est entre garde-fous de **mots** et garde-fous d'**actions**. Filtrer une sortie toxique protège la réputation ; empêcher un agent d'effectuer un virement ou de supprimer une table protège l'entreprise. Les premiers sont ceux qu'on met en place spontanément, les seconds ceux qui comptent dès que le système agit.

Un garde-fou a aussi une fonction de dégradation : quand la confiance est insuffisante, il vaut mieux un système qui dit « je passe la main » qu'un système qui répond quand même. C'est une décision de conception, pas un cas d'erreur.

## Ce qu'il faut savoir

- **En entrée** : détection de contenu interdit, longueur et format, limitation de débit par utilisateur, balisage explicite des blocs non fiables, retrait ou masquage des données sensibles avant l'appel.
- **En sortie** : validation du format attendu — un schéma, pas une expression régulière optimiste —, vérification que les sources citées existent, filtrage de contenu, contrôle qu'aucune donnée hors périmètre n'apparaît.
- **Sur les actions** : allowlist d'outils, périmètre de données réduit au strict nécessaire, écriture réversible par défaut, confirmation humaine sur l'irréversible, budget de tours et de jetons plafonné dans le code.
- **Le moindre privilège est le garde-fou le plus efficace**, et le moins coûteux : une capacité non exposée n'a pas besoin d'être filtrée. Voir [[notions/controle-d-acces]].
- **Dégradation contrôlée** : définir ce que fait le système quand un garde-fou déclenche — refuser, demander une reformulation, escalader vers un humain, répondre en mode réduit. Un refus silencieux est le pire des cas.
- **Chaque déclenchement se journalise** avec son motif. Sans cela, on ne sait ni si le filtre sert ni s'il bloque des cas légitimes — et un garde-fou qui gêne sans qu'on le sache finit désactivé en urgence un vendredi soir.
- **Un garde-fou se teste comme le reste** : cas censés passer, cas censés bloquer, et vérification qu'il est **réellement actif en production** et pas seulement en préproduction.
- **Le coût est réel** : chaque filtre ajoute de la latence et parfois un appel de modèle. Les ordonner du moins cher au plus cher, et sortir dès qu'une décision est prise.

## Selon le métier

### Forward Deployed Engineer

Le garde-fou qui compte en environnement client est celui qui borne les **actions** de l'agent, pas seulement ses mots : écriture réversible, périmètre de données limité, confirmation humaine sur les opérations irréversibles. C'est aussi l'argument qui fait accepter le système par le contrôle interne — un dispositif qu'on peut décrire et auditer vaut mieux qu'une promesse de qualité.

### AI Product Builder

Nécessaires dès que le produit affiche une sortie de modèle à un utilisateur ou lui laisse déclencher une action. Le minimum utile tient en peu de choses : validation de schéma sur les sorties structurées, plafond de dépense par utilisateur, et vérification qu'aucun outil n'atteint la base au-delà de ce dont la fonction a besoin.

### AI Red Teaming

Ce qui est propre au red teaming, c'est de tester les garde-fous **dans l'ordre inverse de leur coût**, en commençant par vérifier qu'ils sont réellement activés en production — le constat le plus fréquent n'est pas un filtre contourné, c'est un filtre absent dans l'environnement réel. Ensuite viennent les contournements : reformulation, encodage, changement de langue, découpage de la charge sur plusieurs tours.

> [!warning] Piège
> Empiler les filtres de contenu et laisser les capacités ouvertes. Un système qui refuse poliment d'écrire une insulte mais dispose d'un outil d'envoi d'e-mail sans restriction de destinataire est protégé sur ce qui se voit et exposé sur ce qui coûte. Commencer par la liste des actions possibles, pas par la liste des mots interdits.

## Pour aller plus loin

- [How to Build Safe AI Agents: Best Practices for Guardrails](https://medium.com/@sahin.samia/how-to-build-safe-ai-agents-best-practices-for-guardrails-and-oversight-a0085b50c022) — le panorama côté agents, où la question des actions domine.
- [Moderation API — OpenAI](https://platform.openai.com/docs/guides/moderation) — un filtre de contenu prêt à l'emploi, et ses limites documentées.
- [Reduce hallucinations — Anthropic](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations) — les techniques de fiabilisation en amont du filtrage.
- [How to Bypass Azure AI Content Safety Guardrails](https://mindgard.ai/blog/bypassing-azure-ai-content-safety-guardrails) — à lire pour calibrer ce qu'un filtre commercial garantit réellement.

## Appelée par

- [[parcours/forward-deployed-engineer|Forward Deployed Engineer]]
- [[parcours/ai-product-builder|AI Product Builder]]
- [[parcours/ai-red-teaming|AI Red Teaming]]

Voisines : [[notions/injection-de-prompt]], [[notions/controle-d-acces]], [[notions/agents-llm]], [[notions/observabilite]].
