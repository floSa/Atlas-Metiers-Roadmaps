---
tags: [notion, embeddings, vecteurs, recherche-semantique, rag]
date: 2026-09-16
statut: actif
appelee-par: [forward-deployed-engineer, ai-product-builder]
---

# Embeddings et bases vectorielles

Représentation d'un texte, d'une image ou d'un son par un vecteur numérique tel que la proximité géométrique traduise une proximité de sens — et les bases de données conçues pour chercher rapidement les plus proches voisins dans cet espace.

## À quoi ça sert

Une recherche par mots-clés trouve ce qui contient les mêmes mots. Une recherche vectorielle trouve ce qui parle de la même chose, même formulé autrement — « résiliation anticipée » et « rompre le contrat avant terme » se retrouvent. C'est la brique qui rend possible la récupération dans un corpus rédigé par des humains qui n'emploient pas le vocabulaire de la question.

Le second usage, moins visible, est la comparaison de masse : regrouper des verbatims par thème, détecter des doublons quasi identiques, repérer une sortie inhabituelle. Tout ce qui demande « à quel point ces deux choses se ressemblent-elles » sur des dizaines de milliers d'éléments.

La limite est symétrique de la force : la similarité sémantique ignore le littéral. Un numéro de contrat, une référence réglementaire ou un nom propre rare se retrouvent mal par vecteur, et très bien par recherche lexicale — d'où la règle de combiner les deux.

## Ce qu'il faut savoir

- **Le modèle d'embedding détermine la qualité** de la récupération plus que la base. Critères : langue réellement couverte, longueur maximale acceptée, dimension, coût, et possibilité d'héberger le modèle si les données ne sortent pas.
- **Tout doit être vectorisé par le même modèle.** Changer de modèle impose de réindexer l'intégralité du corpus ; c'est une opération à planifier, pas un réglage.
- **La mesure usuelle est la similarité cosinus.** Elle compare des directions, pas des distances — normaliser les vecteurs évite des surprises.
- **La recherche approximative** (HNSW, IVF) échange un peu de rappel contre beaucoup de vitesse. Les paramètres se règlent, et les valeurs par défaut conviennent rarement à un corpus réel.
- **Le filtrage par métadonnées avant la recherche** est souvent plus déterminant que le réglage de l'index : chercher dans la bonne période, le bon service, le bon niveau de confidentialité.
- **Choix de base** : une extension sur une base déjà en place (pgvector sur PostgreSQL) couvre la majorité des besoins réels ; les bases dédiées se justifient à volume élevé ou pour des fonctionnalités précises.
- **La recherche hybride** — vectorielle plus lexicale, puis reclassement — est le réglage qui rapporte le plus pour le moins d'effort. Voir [[notions/rag]].
- **Un vecteur n'est pas anonyme.** On peut reconstruire une approximation du texte d'origine à partir de son embedding ; un index vectoriel de documents sensibles est un traitement de données sensibles.

## Selon le métier

### Forward Deployed Engineer

Choisir la base qui vit déjà dans l'infrastructure du client plutôt que la meilleure sur le papier. C'est une base de plus à sauvegarder, superviser et mettre à jour pour son équipe après le départ du FDE, et ce coût dépasse largement l'écart de performance entre deux solutions correctes.

### AI Product Builder

Nécessaires seulement si le produit a un corpus propre à interroger. Beaucoup de produits n'en ont pas et s'en passent très bien ; monter une base vectorielle par réflexe est un des surcoûts les plus fréquents du métier. Quand c'est justifié, l'extension sur la base existante suffit presque toujours au démarrage.

> [!warning] Piège
> Juger la qualité d'une récupération sur quelques requêtes tapées à la main. Elles sont formulées par quelqu'un qui connaît le corpus, donc avec le bon vocabulaire, et elles réussissent. Les requêtes réelles sont approximatives, mal orthographiées et parfois hors sujet. La mesure se fait sur un jeu de questions réelles avec les fragments attendus, pas à l'impression.

## Pour aller plus loin

- [What are embedding models? Benefits and best practices — Cohere](https://cohere.com/blog/embedding-models) — le cadrage pratique du choix de modèle.
- [Mastering RAG: How to Select an Embedding Model](https://www.rungalileo.io/blog/mastering-rag-how-to-select-an-embedding-model) — les critères de sélection, comparés.
- [Best Open-Source Embedding Models Benchmarked and Ranked](https://supermemory.ai/blog/best-open-source-embedding-models-benchmarked-and-ranked/) — utile quand le modèle doit être hébergé.

## Appelée par

- [[parcours/forward-deployed-engineer|Forward Deployed Engineer]]
- [[parcours/ai-product-builder|AI Product Builder]]

Voisines : [[notions/rag]], [[notions/traitement-langage-naturel]], [[notions/donnees-sensibles]].
