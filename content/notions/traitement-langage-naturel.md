---
title: Traitement du langage naturel
tags: [notion, nlp, texte, verbatim, classification]
date: 2026-09-16
statut: actif
appelee-par: [data-analyst]
---

Ensemble des méthodes qui permettent d'extraire de l'information exploitable à partir de texte écrit en langue naturelle : classer, résumer, extraire des entités, mesurer une proximité de sens.

## À quoi ça sert

Dans une entreprise, une part importante de l'information utile n'est pas dans des colonnes : elle est dans les verbatims clients, les motifs de réclamation, les commentaires d'enquête, les descriptions libres de tickets. Ces champs sont ignorés par la plupart des analyses précisément parce qu'ils ne se somment pas — et ils contiennent souvent l'explication qu'on cherche ailleurs.

Le domaine a été bouleversé deux fois. La première par les plongements lexicaux et les transformeurs, qui ont remplacé les approches par règles. La seconde, plus radicale pour un analyste : **depuis 2024, un appel à un modèle de langage fait sans entraînement préalable ce qui demandait auparavant un corpus annoté et un modèle spécifique**. Classification thématique, détection de sujets, analyse de sentiment, extraction structurée sont devenues accessibles en quelques lignes.

Cela ne rend pas les méthodes classiques inutiles — sur des volumes élevés et des tâches stables, elles restent moins chères et plus rapides — mais cela déplace le point de départ.

## Ce qu'il faut savoir

- **Le prétraitement classique** — tokenisation, normalisation de casse, lemmatisation, retrait des mots vides — reste utile pour les approches statistiques, et devient inutile voire nuisible avec les modèles récents.
- **Représentations** : sac de mots et TF-IDF (simples, interprétables, efficaces sur des corpus homogènes), plongements contextuels (capturent le sens, coûtent plus cher). Voir [[notions/embeddings-et-bases-vectorielles]].
- **Les tâches courantes pour un analyste** : classification thématique, extraction d'entités, détection de sujets émergents, regroupement de verbatims proches, résumé.
- **L'analyse de sentiment est plus fragile qu'elle n'en a l'air** : ironie, négation, jargon métier et contexte sectoriel la mettent en défaut. Un score de sentiment publié sans validation humaine sur un échantillon est un chiffre inventé.
- **La langue compte.** Beaucoup d'outils et de modèles sont nettement meilleurs en anglais. Vérifier sur son propre corpus plutôt que sur un classement.
- **Avec un modèle de langage**, la tâche se spécifie par un prompt et une sortie structurée validée. Cela impose la même exigence que partout ailleurs : un jeu de cas annotés à la main pour mesurer, sans quoi on ne sait rien de la qualité.
- **Le coût change de nature** : classer un million de verbatims par appel de modèle a un prix. Sur ces volumes, entraîner un petit classifieur à partir d'un échantillon annoté par le modèle redevient rentable.

## Selon le métier

### Data Analyst

C'est le seul volet issu de l'apprentissage profond qui touche vraiment le métier, par ce qu'il permet sur les verbatims clients. L'usage réaliste est modeste et utile : transformer un champ libre en une variable catégorielle exploitable, pour pouvoir enfin le croiser avec le reste. La règle de prudence reste la même que partout — un échantillon relu à la main avant de publier quoi que ce soit.

> [!info] Une seule appelante
> Notion appelée par le seul parcours Data Analyst ; le registre la rattache aussi au parcours Machine Learning du corpus.

> [!warning] Piège
> Publier une répartition thématique produite par un modèle sans avoir relu un échantillon. Les catégories seront nettes, les pourcentages précis, et la classification peut être systématiquement biaisée sur une formulation fréquente — un motif de réclamation rangé au mauvais endroit dans 30 % des cas. Rien dans le résultat ne le signale.

## Pour aller plus loin

- [A Guide on Word Embeddings in NLP — Turing](https://www.turing.com/kb/guide-on-word-embeddings-in-nlp) — la représentation du texte, socle de tout le reste.
- [Text Embeddings, Classification, and Semantic Search](https://www.youtube.com/watch?v=sNa_uiqSlJo) — la mise en pratique avec du code.
- [[roadmaps/04 - Roadmap — Machine Learning]] — le cadre méthodologique, si la tâche doit être traitée par un modèle entraîné.

## Appelée par

- [[parcours/data-analyst/index|Data Analyst]]

Voisines : [[notions/embeddings-et-bases-vectorielles]], [[notions/reseaux-de-neurones]], [[notions/apprentissage-supervise]].
