---
title: Apprentissage profond
---

Niveau attendu : **usage**. Le confirmé entraîne et diagnostique à partir de modèles pré-entraînés, sur un chemin balisé ; concevoir une architecture relève d'un poste de recherche, pas d'un data scientist généraliste.

L'outil des données non structurées : texte, image, son, signal, séquences. La compétence critique n'est pas d'empiler des couches mais de diagnostiquer un entraînement, et de savoir quand un modèle plus petit et mieux régularisé bat un modèle plus gros.

```mermaid
flowchart TD
  RNE["Réseaux de neurones<br/>couches, activations, rétropropagation"]
  TAL["Traitement du langage naturel<br/>la première famille de tâches concernée"]
  EMB["Plongements et bases vectorielles<br/>ce que le modèle apprend à représenter"]
  AFF["Affinage de modèle<br/>partir d'un modèle pré-entraîné, et à quel coût"]
  RLF["Apprentissage par renforcement<br/>l'alignement et le raisonnement"]
  COU["Coût et latence d'inférence<br/>le budget qui décide de l'architecture"]

  click RNE "/notions/reseaux-de-neurones"
  click TAL "/notions/traitement-langage-naturel"
  click EMB "/notions/embeddings-et-bases-vectorielles"
  click AFF "/notions/affinage-de-modele"
  click RLF "/notions/apprentissage-par-renforcement"
  click COU "/notions/cout-et-latence-inference"
```

## Ce qu'il faut savoir faire

- **Expliquer le mécanisme d'attention en détail.** C'est le seul concept qui rend compte à la fois des modèles de langage, des modèles de vision récents et d'une grande partie de la recherche en cours. Chaque position agrège l'information des autres, pondérée par une similarité apprise ; le coût est quadratique en longueur de séquence, mais l'entraînement est entièrement parallélisable — la raison réelle de la victoire sur les architectures récurrentes.
- **Partir systématiquement d'un modèle pré-entraîné.** Entraîner depuis zéro n'a de sens que sur un domaine sans équivalent public. La question pratique n'est jamais « quelle architecture » mais « quel modèle existant, et quelle partie je réajuste ».
- **Diagnostiquer un entraînement à la courbe.** Perte qui stagne : taux d'apprentissage, initialisation, ou signal absent des données. Écart entraînement-validation qui explose : surapprentissage ou fuite. Perte qui devient non numérique : instabilité, gradient explosif, division par une variance nulle.
- **Maîtriser l'affinage à faible rang.** Adapter un modèle de plusieurs milliards de paramètres sur un seul processeur graphique grand public est devenu accessible, à condition d'accepter qu'on impose un format, un ton ou un domaine — pas des connaissances factuelles nouvelles.
- **Mesurer le coût de la précision numérique plutôt que le supposer.** Demi-précision à l'entraînement, quantification en huit ou quatre bits à l'inférence : le gain en mémoire est certain, la perte en qualité dépend du modèle et de la tâche et doit être évaluée sur le jeu de test réel.
- **Régler l'appétit en données.** Augmentation, régularisation, arrêt anticipé, normalisation : sur un jeu modeste, ces leviers rapportent davantage qu'une architecture plus profonde.

> [!warning] Piège
> Sortir l'artillerie profonde sur cinq mille lignes tabulaires. Un modèle d'arbres entraîné en quinze secondes fera mieux, s'expliquera plus facilement et se déploiera sans processeur graphique. L'apprentissage profond devient pertinent quand la donnée est non structurée, quand le volume dépasse largement ce qu'un modèle à variables explicites peut exploiter, ou quand un modèle pré-entraîné existe déjà pour le domaine.

## Les notions mobilisées

- [[notions/reseaux-de-neurones]] — la mécanique commune à toutes les architectures, et l'endroit où le diagnostic d'entraînement prend son sens.
- [[notions/traitement-langage-naturel]] — la famille de tâches où le passage aux modèles pré-entraînés a été le plus radical.
- [[notions/embeddings-et-bases-vectorielles]] — les représentations apprises, réutilisables bien au-delà de la tâche qui les a produites.
- [[notions/affinage-de-modele]] — quand il apporte réellement quelque chose, et la dette de ré-entraînement qu'il crée.
- [[notions/apprentissage-par-renforcement]] — le mécanisme d'alignement et d'entraînement au raisonnement des modèles récents, à connaître même sans l'implémenter.
- [[notions/cout-et-latence-inference]] — la contrainte qui tranche en pratique entre deux architectures de qualité comparable.

## Pour apprendre

- [Dive into Deep Learning](https://d2l.ai/) — le manuel libre avec code exécutable, la meilleure entrée pratique et théorique à la fois.
- [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) — la série d'Andrej Karpathy, qui construit la rétropropagation puis un transformeur depuis zéro.
- [A Recipe for Training Neural Networks](https://karpathy.github.io/2019/04/25/recipe/) — la méthode de diagnostic pas à pas, à relire à chaque entraînement qui refuse de converger.
- [Tutoriels PyTorch](https://docs.pytorch.org/tutorials/) — la documentation officielle, à traiter comme un cours d'entrée.
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) puis [Attention Is All You Need](https://arxiv.org/abs/1706.03762) — l'intuition visuelle, puis l'article fondateur.
- [Deep Learning](https://www.deeplearningbook.org/) — Goodfellow, Bengio et Courville, libre en ligne, pour les fondations théoriques.
