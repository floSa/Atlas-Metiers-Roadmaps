---
title: Coût et latence d'inférence
tags: [notion, cout, latence, inference, llm, budget]
date: 2026-09-16
statut: actif
appelee-par: [forward-deployed-engineer, ai-product-builder]
---

Ce que coûte et ce que prend de temps un appel à un modèle, en fonction du nombre de jetons traités, du modèle choisi et de la façon dont les appels sont organisés.

## À quoi ça sert

Sur un système classique, la performance est un problème d'ingénierie. Sur un système à base de modèle, c'est un problème de **modèle économique** : le coût est variable, proportionnel à l'usage, et il se découvre sur la facture si personne ne l'a instrumenté. Une fonction dont le coût unitaire dépasse la valeur qu'elle crée reste rentable en démonstration et devient une perte à l'échelle.

La latence, elle, est un problème d'acceptation. Un traitement de fond peut prendre trente secondes ; une interface conversationnelle qui répond en huit secondes est abandonnée. Ce qui se mesure n'est pas la durée totale mais le délai avant le premier jeton, parce que c'est lui que l'utilisateur ressent.

Les deux se traitent au moment de la conception, pas de l'optimisation : ils déterminent le modèle, la taille du contexte, et l'architecture de l'appel.

## Ce qu'il faut savoir

- **La facturation est en jetons, entrée et sortie séparément**, la sortie étant plus chère. Compter avec le tokenizer du fournisseur, jamais en mots divisés par 0,75 — le français accentué, le code et les chiffres se découpent mal.
- **L'unité qui compte est le coût par transaction métier** : par dossier traité, par utilisateur actif et par mois. C'est ce chiffre qu'on extrapole au volume annuel réel, pas le prix pour mille jetons.
- **Le contexte est le premier levier.** Un prompt système de deux mille jetons envoyé à chaque appel est une dépense récurrente. Réduire ce qui est envoyé bat presque toujours le changement de fournisseur.
- **La mise en cache de prompt** rend quasi gratuit un préfixe stable réutilisé. Cela impose de structurer le prompt avec l'invariant en tête et le variable en queue — une contrainte d'écriture, pas un réglage.
- **Le traitement par lots** offre des réductions substantielles quand la réponse peut attendre. Beaucoup de traitements présentés comme temps réel ne le sont pas.
- **Latence** : délai avant le premier jeton, puis débit. Le streaming ne réduit pas la durée totale mais change complètement la perception. Les appels d'outils en série multiplient la latence — paralléliser ce qui est indépendant.
- **Plafonner dans le code**, par requête et par session, et poser une alerte de dépense le jour de la mise en ligne. Une boucle d'agent découverte le lendemain matin coûte plus que le reste du projet.
- **Le compromis qualité/coût se mesure** sur le même jeu d'évaluation : une amélioration obtenue en triplant la facture est une décision, pas un progrès.

## Selon le métier

### Forward Deployed Engineer

Calculer le coût unitaire par dossier traité et l'extrapoler au volume annuel réel **avant de construire**. Un coût par requête acceptable en démonstration devient insoutenable au volume de production, et c'est le client qui recevra la facture après le départ du FDE — ce qui en fait une contrainte de conception, pas une optimisation.

### AI Product Builder

Le budget par utilisateur et par mois est une contrainte de modèle économique, pas une ligne d'infrastructure. Il se calcule avant de livrer, pas sur la première facture. C'est aussi ce qui doit arbitrer la tentation d'ajouter un assistant conversationnel : la fonction la plus demandée est aussi celle dont le coût croît le plus vite avec l'usage.

> [!warning] Piège
> Estimer le coût sur les appels réussis. La facture réelle inclut les tentatives, les reprises après erreur de format, les tours d'agent improductifs et le contexte renvoyé à chaque itération. Sur un système agentique, l'écart entre le coût théorique et le coût observé se compte en multiples, pas en pourcentages.

## Pour aller plus loin

- [The LLM Inference Trilemma: Throughput, Latency, Cost — DigitalOcean](https://www.digitalocean.com/blog/llm-inference-tradeoffs) — les trois contraintes et leurs arbitrages.
- [LLM Cost Optimization: 5 Levers](https://www.morphllm.com/llm-cost-optimization) — les leviers concrets, dans l'ordre de rentabilité.
- [Long-Context LLM Infrastructure](https://introl.com/blog/long-context-llm-infrastructure-million-token-windows-guide) — ce que coûte réellement une fenêtre très large.

## Appelée par

- [[parcours/forward-deployed-engineer/index|Forward Deployed Engineer]]
- [[parcours/ai-product-builder/index|AI Product Builder]]

Voisines : [[notions/choix-de-modele]], [[notions/observabilite]], [[notions/roi-des-projets-ia]], [[notions/agents-llm]].
