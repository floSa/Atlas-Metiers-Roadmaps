---
title: Évaluation et fiabilité
tags: [parcours, prompt-engineering, evaluation, llm-as-judge, ci, calibration]
date: 2026-09-16
statut: actif
source: https://roadmap.sh/prompt-engineering
---

Niveau attendu : **référence**. C'est le cœur du métier et le seul endroit où personne ne rattrapera l'erreur à la place du prompt engineer : sans jeu de cas versionné ni juge calibré, toutes les autres décisions du parcours reposent sur des impressions, et c'est sur ce point qu'on doit faire autorité dans la salle.

C'est l'étape qui sépare le bricolage du travail d'ingénieur : sans évaluation, « améliorer un prompt » signifie « avoir essayé trois exemples qui marchent ».

```mermaid
flowchart TD
  EV["Évaluation LLM<br/>jeux de cas, juges, non-régression"]
  MM["Métriques d'évaluation ML<br/>précision, rappel, ce qu'on agrège"]
  CI["Intégration continue<br/>l'éval au même rang que les tests"]
  OB["Observabilité<br/>les traces de production alimentent l'éval"]
  TL["Tests logiciels<br/>les assertions déterministes d'abord"]

  click EV "/notions/evaluation-llm"
  click MM "/notions/metriques-evaluation-ml"
  click CI "/notions/integration-continue"
  click OB "/notions/observabilite"
  click TL "/notions/tests-logiciels"
```

## Trois niveaux de vérification, dans cet ordre

Les **assertions déterministes** d'abord, parce qu'elles sont gratuites et non ambiguës : schéma valide, champ présent, valeur dans l'énumération, contrainte métier respectée. Le **juge LLM** ensuite, pour les critères qui ne se vérifient pas mécaniquement — mais le juge doit être un appel **séparé**, sans l'historique qui a produit la réponse, sinon il ne fait que se confirmer. Et il doit lui-même être évalué : mesurer son accord avec l'annotation humaine sur un sous-ensemble avant de lui faire confiance, faute de quoi on optimise contre un juge biaisé. La **revue humaine par échantillonnage** enfin, qui reste l'étalon.

Le jeu d'évaluation vit dans le dépôt : cinquante à deux cents cas, dont une trentaine de cas limites issus d'incidents réels, versionnés au même titre que le prompt. Il tourne en intégration continue à chaque modification de prompt **ou de modèle**, et les traces de production l'alimentent en retour.

Restent les biais propres aux modèles, que la roadmap d'origine range sous « fiabilité ». Biais de position — préférence pour la première ou la dernière option —, biais de format, biais de majorité hérité des exemples fournis : on les combat en permutant l'ordre des options entre appels, en équilibrant les classes des exemples et en explicitant les critères. La **calibration**, c'est-à-dire l'écart entre la confiance affichée et l'exactitude réelle, mérite la même méfiance : une confiance verbalisée est peu fiable, les log-probabilités le sont davantage quand elles existent, et pas du tout sur une trace de raisonnement.

## Ce qu'il faut savoir faire

- **Constituer un jeu de cas qui fait mal au premier passage** : entrées vides, documents non pertinents, questions hors périmètre, texte adverse, formats inattendus. Un jeu qui donne 95 % dès le premier jour ne mesure rien.
- **Séparer train, dev et test** comme pour n'importe quel modèle, dès qu'on optimise quoi que ce soit contre la métrique.
- **Mesurer l'accord d'un juge LLM avec l'annotation humaine** avant de s'en servir, et le remesurer quand le juge change de version.
- **Brancher l'évaluation en intégration continue** avec un seuil de blocage, pour qu'une régression de prompt soit détectée comme une régression de code.
- **Refuser de bâtir un routage sur une confiance auto-déclarée** tant qu'elle n'a pas été vérifiée sur un jeu annoté.
- **Faire remonter les incidents de production dans le jeu de cas** : c'est le seul mécanisme qui empêche la même panne de revenir deux fois.

> [!warning] Piège
> Le jeu d'évaluation qui ne contient que des cas nominaux. Il donne un score élevé immédiatement, ne bouge plus jamais, et rate exactement ce qui casse en production.

## Les notions mobilisées

- [[notions/evaluation-llm]] — la notion transverse ; cette page en donne l'ordre d'application côté prompt.
- [[notions/metriques-evaluation-ml]] — précision, rappel et F1 restent les bons agrégats dès que la tâche est une classification déguisée.
- [[notions/integration-continue]] — l'angle prompt engineering : le run d'évaluation est une étape de pipeline, avec un seuil et un artefact.
- [[notions/observabilite]] — capturer prompt, contexte, sortie et coût en production, sans quoi le jeu de cas ne se renouvelle jamais.
- [[notions/tests-logiciels]] — les assertions déterministes sont la première couche, et la moins chère.

## Pour apprendre

- [Evaluating LLM systems](https://hamel.dev/blog/posts/evals/), Hamel Husain — le texte le plus utile du domaine : comment démarrer une éval sans outillage, et pourquoi regarder ses données d'abord.
- [Creating a LLM-as-a-Judge That Drives Business Results](https://hamel.dev/blog/posts/llm-judge/) — la méthode complète pour calibrer un juge contre l'annotation humaine, étape par étape.
- [OpenAI Evals](https://github.com/openai/evals) — un cadre lisible pour écrire ses premiers cas et les rejouer.
- [Promptfoo](https://www.promptfoo.dev/docs/intro/) — évaluation et tests de non-régression de prompts en ligne de commande, branchable en intégration continue en une journée.
- [A Survey on LLM-as-a-Judge](https://arxiv.org/abs/2411.15594) — l'état de l'art des biais du juge : position, verbosité, auto-préférence.
