---
tags: [notion, cadrage, besoin, specification, conseil]
date: 2026-09-16
statut: actif
appelee-par: [forward-deployed-engineer, ai-product-builder, data-analyst, bi-analyst]
---

# Cadrage du besoin

Travail de transformation d'une demande formulée en langage courant en un énoncé vérifiable : ce qui doit être produit, pour qui, à partir de quoi, et à quel seuil on considère que c'est réussi.

## À quoi ça sert

Une demande arrive presque toujours sous une forme inexploitable — « les clients sont moins actifs », « il nous faudrait de l'IA sur les devis », « je veux le chiffre d'affaires ». Ce n'est pas de la négligence : celui qui demande décrit une gêne, pas une spécification. Le cadrage est le travail qui rend la demande exécutable, et c'est le seul moment où corriger une erreur de direction coûte une heure.

Son effet le plus utile est de faire apparaître les désaccords tant qu'ils sont gratuits. « Chiffre d'affaires » recouvre quatre métriques différentes selon qu'on parle hors taxes ou TTC, à la commande ou à la facturation, net des avoirs ou brut. Les quatre existent quelque part dans l'entreprise, et deux directions qui ne parlent pas de la même s'affronteront en réunion trois mois plus tard sur un écart qu'aucune des deux ne saura expliquer.

Le cadrage est aussi ce qui autorise à dire non. Un périmètre écrit rend visible ce qu'on ajoute en cours de route, et transforme un glissement silencieux en décision assumée.

## Ce qu'il faut savoir

- **Partir de la décision, pas de la donnée.** La question utile est « qu'est-ce que tu feras différemment selon la réponse ? ». Si personne ne fait rien différemment, le besoin n'en est pas un — et le savoir tôt économise le travail entier.
- **Rendre chaque terme opérationnel.** Chaque mot de l'énoncé doit devenir une colonne, un filtre, un seuil ou une date. « Client actif » n'est pas une définition tant que la fenêtre et l'événement déclencheur ne sont pas fixés.
- **Observer avant de rédiger.** La façon dont le travail se fait réellement diffère de la façon dont il est décrit, toujours. Une demi-journée passée à regarder quelqu'un faire vaut plus que trois entretiens.
- **Nommer le commanditaire**, c'est-à-dire celui qui arbitre quand deux personnes veulent deux choses. La salle ne valide pas ; une personne valide.
- **Écrire les contraintes non fonctionnelles** au même moment : volume, fraîcheur attendue, données personnelles manipulées, budget. Trois lignes qui déterminent l'architecture et qu'on découvre sinon le jour de la mise en ligne.
- **Fixer le critère de réussite avec un chiffre**, même approximatif, et avec la conduite à tenir si on ne l'atteint pas. Un critère sans conséquence n'est pas un critère.
- **Le cadrage se termine par un écrit court**, relu par le commanditaire. Une page vaut mieux que vingt : ce qui est long n'est pas lu, donc pas contesté, donc pas validé.

## Selon le métier

### Forward Deployed Engineer

Le cadrage est d'abord un travail d'observation, pas de rédaction. Il se fait sur place, en regardant le processus réel, et il produit deux artefacts qui circuleront bien au-delà de la mission : la carte du processus (voir [[notions/bpmn]]) et le registre de décisions. Le rythme compte autant que le contenu — une démonstration hebdomadaire, même minuscule, fait remonter les objections tant qu'elles sont peu coûteuses.

### AI Product Builder

Le livrable de cadrage n'est pas un cahier des charges mais un paragraphe et une liste de dix fonctions maximum, dont la moitié est barrée. La raison est propre au métier : puisqu'on ne dessine plus d'architecture avant de coder, la précision de l'énoncé porte toute la charge. Un générateur ne comble pas un flou, il l'amplifie — il produira une application cohérente qui résout un problème légèrement différent, et l'écart ne se verra qu'au premier utilisateur réel.

### Data Analyst

Ce qui est propre à l'analyse : chaque terme de la question doit devenir une colonne, un filtre ou un seuil **avant d'écrire la première requête**. Le cadrage prend rarement plus d'une heure et détermine l'essentiel de la valeur du livrable. C'est ce qui sépare un analyste d'un exécutant de requêtes.

### BI Analyst

La spécification porte sur une **définition de mesure**, pas sur une fonctionnalité. Entendre « je veux le chiffre d'affaires » et poser les quatre questions qui le désambiguïsent est le cœur du métier. La définition retenue a un propriétaire nommé, et c'est ce qui permettra plus tard d'arbitrer un désaccord sur un chiffre sans rejouer le débat.

> [!warning] Piège
> Cadrer avec celui qui demande et pas avec celui qui fait. Le commanditaire décrit le processus tel qu'il devrait être ; l'opérationnel connaît les exceptions, les contournements et le fichier parallèle qui fait tourner la moitié de l'activité. Un cadrage qui ne rencontre que le niveau qui finance produit une solution pour un processus qui n'existe pas.

## Pour aller plus loin

- [Requirements Gathering in Software Engineering](https://www.jamasoftware.com/requirements-management-guide/requirements-gathering-and-management-processes/what-is-requirements-gathering/) — le cadre classique, à prendre pour ses techniques d'entretien plus que pour son formalisme.
- [How to effectively scope your software projects](https://www.freecodecamp.org/news/how-to-effectively-scope-your-software-projects-from-planning-to-execution-e96cbcac54b9/) — le versant délimitation de périmètre.
- [Requirements Gathering in Business Analysis — Coursera](https://www.coursera.org/learn/requirements-gathering-in-business-analysis) — cours complet si le sujet doit être travaillé en profondeur.

## Appelée par

- [[parcours/forward-deployed-engineer/index|Forward Deployed Engineer]]
- [[parcours/ai-product-builder|AI Product Builder]]
- [[parcours/data-analyst|Data Analyst]]
- [[parcours/bi-analyst|BI Analyst]]

Voisines : [[notions/gestion-parties-prenantes]], [[notions/reingenierie-de-processus]], [[notions/roi-des-projets-ia]], [[notions/redaction-technique]].
