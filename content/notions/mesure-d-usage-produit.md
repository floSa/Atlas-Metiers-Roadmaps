---
tags: [notion, produit, instrumentation, entonnoir, retention, activation]
date: 2026-09-16
statut: actif
appelee-par: [ai-product-builder, data-analyst]
---

# Mesure d'usage produit

Instrumentation des actions réelles des utilisateurs dans un produit — entrée dans un parcours, abandon, complétion, retour — et les indicateurs qu'on en tire pour arbitrer ce qu'on construit ensuite.

## À quoi ça sert

Les gens répondent qu'une fonction leur est utile et ne l'ouvrent jamais. **La satisfaction déclarée sert à comprendre un comportement déjà observé, jamais à le prédire.** C'est la raison d'être de la mesure d'usage : elle est la seule donnée qui arbitre les priorités sans passer par l'opinion de celui qui parle le plus fort.

Son second intérêt est temporel. Rétablir des données d'usage a posteriori demande de re-livrer et d'attendre un mois, pendant lequel les arbitrages se prennent à l'opinion. L'instrumentation se branche donc **avant la première mise en ligne**, pas après le premier désaccord sur les priorités.

Le troisième est de cadrer les discussions de valeur : un entonnoir chiffré transforme « il faudrait améliorer l'inscription » en « 60 % abandonnent à l'écran de vérification d'e-mail ».

## Ce qu'il faut savoir

- **Peu d'événements, bien nommés.** Une dizaine d'événements dans un fichier unique suffisent au démarrage, et ce fichier est de ceux qu'on écrit soi-même. Une convention de nommage cohérente vaut mieux qu'une taxonomie exhaustive appliquée à moitié.
- **Un événement porte un nom stable et des propriétés**, pas l'inverse. Créer un événement par variante rend toute agrégation impossible six mois plus tard.
- **L'entonnoir** mesure le passage d'une étape à la suivante et localise l'abandon. C'est l'outil le plus rentable du domaine, et il demande simplement des étapes définies à l'avance.
- **L'activation** est le moment où l'utilisateur obtient pour la première fois la valeur promise. La définir explicitement est plus utile que toutes les métriques de vanité réunies.
- **La rétention se lit par cohorte**, jamais en agrégat — un taux global qui monte peut refléter un ralentissement du recrutement. Voir [[notions/analyse-de-cohorte]].
- **Distinguer les métriques de vanité des métriques actionnables** : le nombre total d'inscrits monte toujours ; la part des nouveaux inscrits qui atteignent l'activation dit quelque chose.
- **Les données d'usage sont des données personnelles** dès qu'elles sont rattachées à un identifiant. Finalité, durée de conservation et information des utilisateurs relèvent du [[notions/rgpd]].
- **Instrumenter côté serveur quand c'est possible** : les bloqueurs, les extensions et les défauts de réseau rendent la mesure côté client incomplète, et pas uniformément.

## Selon le métier

### AI Product Builder

Brancher l'instrumentation avant la première mise en ligne, pas après le premier désaccord sur les priorités. Une dizaine d'événements nommés proprement suffisent. L'angle propre au métier : sur un produit dont une part est générée, l'usage réel est le seul contrepoids à la tentation d'ajouter des fonctions parce qu'elles sont peu coûteuses à produire.

### Data Analyst

C'est une source de données comme une autre, avec ses défauts propres : événements manquants, définitions qui changent en cours de route, identifiants qui se dédoublent entre session anonyme et compte créé. L'angle analyste est le même que partout — vérifier la provenance, la période et le périmètre exclu avant de conclure, et se méfier d'une baisse qui coïncide avec une livraison.

> [!warning] Piège
> Instrumenter tout « pour l'avoir ». On obtient trois cents événements dont personne ne connaît la définition, une facture d'outil d'analyse qui croît, et aucune décision prise. La bonne démarche part de la question : quelle décision prendrai-je différemment selon la réponse — et que faut-il mesurer pour y répondre.

## Pour aller plus loin

- [What is a Funnel Chart? — Atlassian](https://www.atlassian.com/data/charts/funnel-chart-complete-guide) — l'entonnoir, sa construction et ses lectures fautives.
- [A software engineer's guide to A/B testing — PostHog](https://posthog.com/product-engineers/ab-testing-guide-for-engineers) — le lien entre instrumentation et expérimentation.
- [Understanding Cohort Analysis](https://hevodata.com/learn/understanding-cohort-analysis-a-guide/) — la lecture de la rétention, qui est l'usage principal de ces données.

## Appelée par

- [[parcours/ai-product-builder|AI Product Builder]]
- [[parcours/data-analyst|Data Analyst]]

Voisines : [[notions/analyse-de-cohorte]], [[notions/ab-testing]], [[notions/observabilite]], [[notions/roi-des-projets-ia]].
