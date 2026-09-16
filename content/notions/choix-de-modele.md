---
tags: [notion, choix-de-modele, llm, arbitrage, cout]
date: 2026-09-16
statut: actif
appelee-par: [forward-deployed-engineer, ai-product-builder]
---

# Choix de modèle

Décision portant sur le modèle qui traitera une tâche donnée — famille, taille, mode de raisonnement, hébergement — à partir de contraintes qui ne sont presque jamais uniquement de qualité.

## À quoi ça sert

Le choix de modèle est une décision d'architecture déguisée en comparaison de produits. Ce qui est en jeu n'est pas « lequel est le meilleur » mais « lequel satisfait la contrainte la plus dure », et cette contrainte est rarement la qualité : c'est la confidentialité, le coût unitaire, la latence perçue, ou la disponibilité dans une région.

Le second intérêt est qu'il ne s'agit pas d'un choix unique. Un système sérieux utilise plusieurs modèles : un petit et rapide pour la classification et le routage, un grand pour la synthèse difficile, un modèle de raisonnement pour la planification. Traiter la question tâche par tâche fait souvent gagner un ordre de grandeur sur la facture sans perte mesurable.

## Ce qu'il faut savoir

- **Les contraintes se hiérarchisent avant la comparaison.** Si les données ne peuvent pas sortir, le débat sur la qualité des modèles propriétaires est clos. Si le budget par utilisateur est fixé, il élimine des familles entières.
- **Petit contre grand** : sur l'extraction, la classification, le routage et la reformulation, un petit modèle atteint une qualité indiscernable pour une fraction du coût et de la latence. Les grands modèles se justifient sur la synthèse longue, le raisonnement et les tâches ouvertes.
- **Les modèles de raisonnement facturent leur chaîne de pensée en jetons de sortie.** Sur de l'extraction, activer le raisonnement multiplie le coût sans rien améliorer ; sur la planification multi-étapes et le débogage, l'écart est net. À traiter comme un paramètre à mesurer.
- **Ouvert contre propriétaire** : la question n'est pas idéologique, elle est opérationnelle. Un modèle ouvert hébergé soi-même signifie des GPU, une équipe qui sait les exploiter, et la responsabilité des mises à jour. Le coût total est rarement inférieur en dessous d'un volume élevé.
- **Les classements publics vieillissent vite et ne mesurent pas votre tâche.** Ils servent à établir une liste courte, jamais à trancher. La décision se prend sur un jeu d'évaluation maison.
- **Épingler la version** quand c'est possible, et rejouer l'évaluation à chaque montée de version. Un modèle mis à jour est un système modifié.
- **La portabilité se prépare** : isoler l'appel derrière une interface, garder les prompts hors du code applicatif, éviter les fonctionnalités propriétaires sur le chemin critique. Le coût est faible au départ et rend le changement possible.

## Selon le métier

### Forward Deployed Engineer

La confidentialité tranche souvent avant la qualité. Si les données ne peuvent pas sortir du système d'information, le débat est clos et l'arbitrage porte sur les modèles hébergeables. Second point : le client paiera la facture après le départ du FDE, donc le coût unitaire est une contrainte de conception et non une optimisation ultérieure.

### AI Product Builder

Le critère dominant n'est pas la qualité de tête de gamme mais le **coût par utilisateur actif**. Un produit grand public ne survit pas à un gros modèle appelé à chaque interaction. Le réflexe utile est de commencer par le plus petit modèle plausible et de ne monter que là où l'évaluation le prouve nécessaire.

> [!warning] Piège
> Choisir le modèle le plus capable « pour ne pas se limiter », puis découvrir que la latence rend l'interface désagréable et que la facture croît avec l'usage. L'excès de capacité n'est pas neutre : il coûte à chaque appel, pour toujours, sur des tâches dont 80 % ne l'exigeaient pas.

## Pour aller plus loin

- [Open Source vs Closed LLMs: a guide](https://hatchworks.com/blog/gen-ai/open-source-vs-closed-llms-guide/) — l'arbitrage hébergement, traité par les coûts réels.
- [The LLM Inference Trilemma: Throughput, Latency, Cost — DigitalOcean](https://www.digitalocean.com/blog/llm-inference-tradeoffs) — les trois contraintes qu'on ne peut pas satisfaire ensemble.
- [Reasoning LLMs Guide — DAIR.AI](https://www.promptingguide.ai/guides/reasoning-llms) — quand le raisonnement sert et quand il coûte pour rien.

## Appelée par

- [[parcours/forward-deployed-engineer/index|Forward Deployed Engineer]]
- [[parcours/ai-product-builder|AI Product Builder]]

Voisines : [[notions/cout-et-latence-inference]], [[notions/affinage-de-modele]], [[notions/evaluation-llm]], [[notions/arbitrage-deterministe-probabiliste]].
