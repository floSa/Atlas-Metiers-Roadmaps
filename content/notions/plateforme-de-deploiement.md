---
title: Plateforme de déploiement
tags: [notion, deploiement, hebergement, plateforme, infrastructure]
date: 2026-09-16
statut: actif
appelee-par: [ai-product-builder, forward-deployed-engineer]
---

Ce sur quoi une application tourne une fois livrée, caractérisé moins par la marque que par le **niveau de prise en charge** qu'on achète : plus la plateforme en fait, moins on configure et moins on contrôle.

## À quoi ça sert

Le catalogue de produits n'est pas une grille de décision. La question utile est de savoir quelle part de l'exploitation on délègue — construction, certificats, mise à l'échelle, sauvegarde, supervision — et ce qu'on renonce à maîtriser en échange.

La règle qui en découle est simple : **le bon choix est le niveau le plus élevé qui satisfait la contrainte la plus dure du cadrage**. Pour un premier produit, cette contrainte est presque toujours le budget ou le délai, jamais l'extensibilité qu'on imagine. Dans un contexte d'entreprise, c'est le plus souvent une contrainte imposée qu'on ne choisit pas.

Le troisième enjeu est la réversibilité. Plus le niveau de prise en charge est élevé, plus l'adhérence à la plateforme est forte — et c'est acceptable tant que la décision est prise en connaissance de cause.

## Ce qu'il faut savoir

- **Périphérie et fonctions** — code déployé sur un réseau mondial, facturé à l'invocation, sans serveur à maintenir. Adapté au front end et aux traitements courts et sans état. Limite structurelle : durée d'exécution bornée, pas de processus long.
- **Plateforme applicative** — on pousse un dépôt, la plateforme construit, héberge, gère les certificats et la mise à l'échelle. C'est la case par défaut d'un produit qui démarre. Limite : le coût cesse d'être compétitif à volume soutenu.
- **Infrastructure brute** — contrôle total, tout est possible, tout est à faire. À éviter pour un premier produit sauf contrainte imposée : l'écart de temps de mise en ligne se compte en semaines et l'écart de facture en surprises.
- **Chaîne d'entreprise** — on ne la choisit pas, on la subit parce que l'organisation l'impose. Ce n'est pas une critique, c'est une réalité à intégrer au cadrage.
- **Dorsale gérée** — base relationnelle, authentification, droits d'accès par ligne, API générée et temps réel dans un seul service. Ce qu'on achète, c'est de ne pas écrire l'authentification soi-même, ce qui est le meilleur rapport valeur sur risque pour un petit produit.
- **Regarder le plafond du palier gratuit**, pas la vitrine : bande passante, minutes de construction, heures de base de données. La facture qui suit le dépassement est brutale et sans préavis. Noter le seuil au cadrage et poser une alerte de dépense le jour de la mise en ligne.
- **La localisation des données est une décision de cette étape**, pas une formalité ultérieure. Un service dont les données résident hors Union européenne se choisit en trois clics et se déplace difficilement.
- **Le déploiement est automatisé dès le début.** Livrer depuis le poste local « le temps de démarrer » supprime la seule trace de ce qui tourne réellement.

## Selon le métier

### AI Product Builder

L'amont liste des produits sans donner de critère ; la grille utile est le niveau de prise en charge. Deux décisions à prendre au moment du déploiement et pas après : le plafond du palier gratuit avec son alerte de dépense, et la localisation des données si l'application traite des données personnelles — voir [[notions/rgpd]].

### Forward Deployed Engineer

Le choix n'existe généralement pas : la plateforme est celle du client, souvent une chaîne d'entreprise ou une infrastructure interne, avec ses contraintes de registre, de réseau filtré et d'homologation. L'enjeu est de le découvrir en phase d'audit et de construire dessus dès le premier jour. Une application déployée sur un service que le client n'utilise pas est inexploitable dès la fin de mission, quelle que soit sa qualité.

> [!warning] Piège
> Choisir la plateforme sur la promesse d'échelle. Le produit qui doit encaisser des millions de requêtes n'existe pas encore, et le coût du choix « prêt pour l'échelle » se paie immédiatement en semaines de configuration et en complexité d'exploitation. Le niveau se monte quand la contrainte apparaît, pas quand on l'imagine.

## Pour aller plus loin

- [What is software deployment? — Atlassian](https://www.atlassian.com/agile/software-development/software-deployment) — le cadrage, indépendant des produits.
- [Getting started with Cloudflare Pages](https://developers.cloudflare.com/pages/get-started/) — un exemple concret du niveau périphérie.
- [Continuous Integration vs Delivery vs Deployment](https://www.guru99.com/continuous-integration-vs-delivery-vs-deployment.html) — la distinction entre livrer et déployer, à trancher au cadrage.

## Appelée par

- [[parcours/ai-product-builder/index|AI Product Builder]]
- [[parcours/forward-deployed-engineer/index|Forward Deployed Engineer]]

Voisines : [[notions/conteneurisation]], [[notions/integration-continue]], [[notions/cout-et-latence-inference]], [[notions/controle-d-acces]].
