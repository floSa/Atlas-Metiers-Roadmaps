---
title: Faut-il un corpus
---

Niveau attendu : **notion**. La récupération de contexte est hors périmètre réel du métier : ce qu'on attend d'un confirmé, c'est de reconnaître que la question se pose, de répondre non par défaut, et d'appeler un [[parcours/ai-engineer/index|AI Engineer]] le jour où c'est oui.

La récupération de contexte n'est nécessaire que si le produit a un corpus propre à interroger. Beaucoup de produits n'en ont pas et s'en passent très bien ; les monter par réflexe est un des surcoûts les plus fréquents du métier.

```mermaid
flowchart TD
  R["La récupération de contexte<br/>quand elle est justifiée"]
  E["L'index et sa mise à jour<br/>ce qu'il coûte à maintenir"]
  Q["La propreté du corpus<br/>l'essentiel du travail est là"]
  C["Le coût de l'ingestion<br/>récurrent, pas ponctuel"]

  click R "/notions/rag"
  click E "/notions/embeddings-et-bases-vectorielles"
  click Q "/notions/qualite-des-donnees"
  click C "/notions/cout-et-latence-inference"
```

## Ce qu'il faut savoir faire

- Vérifier d'abord qu'il existe un corpus propre au produit — des documents, des fiches, un historique — que le modèle ne connaît pas et que l'utilisateur veut interroger. Sans corpus, pas de récupération : la question est close.
- Essayer d'abord la solution simple. Sur un corpus de quelques dizaines de documents courts, les passer en contexte ou faire une recherche plein texte donne souvent le même résultat pour une fraction du coût et de la complexité.
- Regarder l'ingestion comme le vrai chantier. Le corpus d'un produit est toujours plus sale que prévu, et l'essentiel du travail est dans le nettoyage, le découpage et la mise à jour — pas dans la génération.
- Prévoir la fraîcheur : un index qui ne se met pas à jour donne des réponses justes sur des documents périmés, ce qui est pire qu'une absence de réponse.
- Compter le coût de l'indexation comme récurrent. Chaque modification du découpage ou du modèle d'embedding impose une réindexation complète.
- Appliquer les droits d'accès **à la récupération** et pas à l'affichage : filtrer les documents avant qu'ils n'entrent dans le contexte, sinon le cloisonnement n'existe pas.

## Les notions mobilisées

- [[notions/rag]] — pour ce métier, la question préalable est « ai-je un corpus », et la réponse est non plus souvent qu'on ne le croit.
- [[notions/embeddings-et-bases-vectorielles]] — l'index a un coût de construction, un coût de stockage et un coût de reconstruction ; les trois se découvrent rarement au bon moment.
- [[notions/qualite-des-donnees]] — la qualité des réponses est bornée par la propreté du corpus, et aucune amélioration de prompt ne franchit cette borne.
- [[notions/cout-et-latence-inference]] — la récupération ajoute une latence et des jetons de contexte à chaque requête, ce qui change le budget par utilisateur.

> [!warning] Piège
> Monter une récupération complète parce que c'est l'architecture qu'on voit partout, sur un produit dont le corpus tient en trente pages. On paie l'ingestion, l'index, la réindexation et la complexité de diagnostic pour un gain nul par rapport à un contexte passé directement.
