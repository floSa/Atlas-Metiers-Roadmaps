---
tags: [notion, affinage, fine-tuning, llm, entrainement]
date: 2026-09-16
statut: actif
appelee-par: [forward-deployed-engineer, ai-red-teaming]
---

# Affinage de modèle

Poursuite de l'entraînement d'un modèle pré-entraîné sur un jeu d'exemples propres à un usage, de manière à en modifier le comportement par défaut.

## À quoi ça sert

L'affinage change **la forme** d'une réponse, pas la connaissance du modèle. Il sert quand un format, un style, un vocabulaire métier ou une convention de sortie résistent réellement au prompt — après qu'on ait essayé le prompt. Il sert aussi à faire tenir sur un petit modèle un comportement qu'un grand modèle obtenait avec un long prompt, ce qui est le cas d'usage économique le plus solide.

Il ne sert pas à apprendre des faits. Une information nouvelle ou changeante appartient au contexte, donc à la récupération ([[notions/rag]]) : un modèle affiné sur des documents les restituera de façon approximative, sans source, et deviendra faux dès que les documents évoluent.

Son coût réel n'est pas l'entraînement, c'est la **dette**. Chaque nouvelle version du modèle de base, chaque évolution du besoin relance le cycle — collecte, nettoyage, entraînement, évaluation, redéploiement — et il faut une équipe pour le porter dans la durée.

## Ce qu'il faut savoir

- **L'ordre d'essai** : prompt système soigné, puis exemples dans le contexte, puis récupération, puis affinage. Sauter directement à l'affinage est l'erreur la plus courante et la plus chère.
- **La qualité du jeu prime sur sa taille.** Quelques centaines d'exemples cohérents et vérifiés font mieux que des milliers d'exemples hétérogènes. Le jeu est le livrable, pas le modèle.
- **Les méthodes légères** (LoRA et apparentées) n'entraînent qu'un petit nombre de paramètres additionnels : coût réduit, adaptateurs interchangeables, modèle de base intact. C'est le point d'entrée raisonnable.
- **Oubli catastrophique** : un affinage trop agressif dégrade des capacités qui n'étaient pas visées. Il faut donc évaluer aussi ce qu'on ne cherchait pas à changer.
- **La dette de ré-entraînement** est le vrai coût. À poser au cadrage : qui refera cela dans dix-huit mois, avec quel jeu de données, et sur quel budget.
- **Toute donnée entrée dans un affinage doit être considérée comme publiable** dès lors que le modèle est exposé. La mémorisation n'est pas une hypothèse théorique.
- **Évaluer avant et après, sur le même jeu.** Un affinage sans mesure comparative est une conviction, pas un résultat.

## Selon le métier

### Forward Deployed Engineer

Presque jamais justifié en mission. Il crée une dette de ré-entraînement que le client ne saura pas porter, et il arrive en général au moment où l'équipe cherche à compenser une récupération médiocre. À réserver au cas où un format ou un vocabulaire métier résiste réellement au contexte — et à documenter comme une charge d'exploitation, pas comme une fonctionnalité.

### AI Red Teaming

Traiter un affinage comme une opération sans conséquence de sécurité est une erreur de fond. Un modèle affiné sur des tickets de support a mémorisé des noms, des adresses et des numéros de contrat, et il les restituera sur une formulation adéquate, sans qu'aucune attaque sophistiquée soit nécessaire. L'affinage est aussi la porte d'entrée de l'empoisonnement : les données d'entraînement sont une surface à auditer comme les autres.

> [!warning] Piège
> Affiner pour apprendre des faits. Le modèle produira des réponses du bon style, sans source, partiellement fausses, et impossibles à corriger autrement qu'en réentraînant. L'écart le plus coûteux du domaine : un bon prompt système plus une récupération correcte battent presque toujours un affinage bâclé sur cinq cents exemples, pour un centième de l'effort.

## Pour aller plus loin

- [What is fine-tuning? — IBM](https://www.ibm.com/think/topics/fine-tuning) — le cadrage, y compris les méthodes légères.
- [Prompt Engineering vs Fine Tuning: When to Use Each](https://www.codecademy.com/article/prompt-engineering-vs-fine-tuning) — l'arbitrage, avec des critères applicables.
- [RAG vs Fine-Tuning vs Prompt Engineering](https://www.youtube.com/watch?v=zYGDpG-pTho) — la comparaison des trois voies, en vidéo courte.

## Appelée par

- [[parcours/forward-deployed-engineer/index|Forward Deployed Engineer]]
- [[parcours/ai-red-teaming|AI Red Teaming]]

Voisines : [[notions/rag]], [[notions/choix-de-modele]], [[notions/donnees-sensibles]], [[notions/apprentissage-supervise]].
