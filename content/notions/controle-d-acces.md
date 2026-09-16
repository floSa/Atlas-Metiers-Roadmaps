---
title: Contrôle d'accès
tags: [notion, controle-d-acces, authentification, autorisation, moindre-privilege]
date: 2026-09-16
statut: actif
appelee-par: [ai-red-teaming, forward-deployed-engineer, ai-product-builder, bi-analyst]
---

Ensemble des mécanismes qui établissent qui est l'appelant (authentification), ce qu'il a le droit de faire (autorisation), et qui garantissent que cette identité est conservée jusqu'à la couche où la donnée est réellement lue.

## À quoi ça sert

Le contrôle d'accès est la mesure de sécurité dont la défaillance est la plus fréquente et la plus visible. Elle est aussi celle qui protège le mieux quand elle tient : une capacité qui n'est pas exposée à un appelant n'a pas besoin d'être filtrée, surveillée ni corrigée.

La distinction qui compte est simple et constamment confondue : **l'authentification dit qui vous êtes, l'autorisation dit ce que vous pouvez faire**. Une application qui authentifie parfaitement et n'autorise nulle part laisse n'importe quel utilisateur connecté lire les données de tous les autres. C'est la faille la plus banale et la plus facile à introduire.

Le troisième volet, propre aux architectures distribuées et agentiques, est la **propagation d'identité** : l'utilisateur est identifié à la porte d'entrée, puis la requête traverse trois services et un serveur d'outils, et l'identité se perd en route au profit d'un compte technique qui voit tout.

## Ce qu'il faut savoir

- **Authentifier une fois, autoriser partout.** L'autorisation se vérifie à chaque opération, y compris sur les routes internes — supposer qu'un appelant interne est légitime est une hypothèse qui tombe au premier composant compromis.
- **Autorisation au niveau de l'objet**, pas seulement de la route. « Cet utilisateur peut lire des factures » ne dit pas « cet utilisateur peut lire **cette** facture ».
- **Moindre privilège** : chaque composant reçoit les droits strictement nécessaires à sa fonction, et pour la durée nécessaire. C'est ce qui borne les conséquences d'une compromission.
- **Les modèles** : par rôle (RBAC, simple, suffisant dans la plupart des cas), par attributs (ABAC, plus fin, plus difficile à auditer), par ligne dans les outils de données.
- **Les comptes de service** sont le point faible structurel : puissants, partagés, rarement tournés, et souvent le moyen par lequel l'identité de l'utilisateur disparaît.
- **La propagation d'identité** doit descendre jusqu'à la couche de données et jusqu'aux serveurs d'outils distants. Un serveur qui transmet à un service en aval des identifiants qui n'ont pas été émis pour lui est un cas d'école de délégué confus.
- **Les secrets se gèrent**, ils ne se collent pas : coffre, injection à l'exécution, rotation, révocation. Une clé dans un dépôt reste dans l'historique.
- **Le contrôle d'accès se teste comme une fonctionnalité** : un test par rôle et par ressource, exécuté à chaque livraison, et vérifié **en production** et pas seulement en préproduction.

## Selon le métier

### AI Red Teaming

Le constat le plus fréquent en mission : l'application authentifie correctement l'utilisateur, puis interroge l'index de récupération avec un compte de service unique qui voit tout. Vérifier la propagation de l'identité de bout en bout, y compris jusqu'aux serveurs d'outils distants, est un test simple et presque toujours concluant. Le référentiel applicable est l'OWASP API Security Top 10, sans adaptation particulière.

### Forward Deployed Engineer

Le contrôle d'accès du client existe déjà et fait autorité : s'y raccorder plutôt qu'en construire un parallèle. Le point de vigilance propre à la mission est l'index de récupération, qui aplatit par construction des droits documentaires souvent fins — un corpus indexé sans filtrage par identité rend lisibles à tous des documents qui ne l'étaient pas.

### AI Product Builder

C'est le point où une application générée est le plus souvent fausse. Une route qui vérifie l'identité mais pas l'autorisation laisse n'importe quel utilisateur connecté lire les données des autres : à vérifier à la main, sur chaque route qui renvoie des données d'utilisateur. C'est aussi le principal argument en faveur d'une dorsale gérée, dont les droits d'accès par ligne évitent d'écrire soi-même la partie la plus facile à rater.

### BI Analyst

Les droits d'accès par ligne dans l'outil de restitution sont à la fois une fonctionnalité et une obligation réglementaire. Ils sont typiquement configurés une fois et jamais revérifiés, alors que le modèle de données évolue : un nouvel axe d'analyse ajouté six mois plus tard peut contourner le filtrage sans que rien ne le signale.

> [!warning] Piège
> Contrôler l'accès à l'écran et pas à la donnée. Masquer un bouton, filtrer une liste dans l'interface ou retirer un menu ne protège rien : l'appel de l'API reste possible. Toute vérification faite côté client est un confort d'affichage, jamais un contrôle de sécurité.

## Pour aller plus loin

- [OWASP API Security Project (Top 10)](https://owasp.org/www-project-api-security/) — les défaillances d'autorisation y occupent les premières places, mesurées sur des incidents réels.
- [Principle of least privilege — Wikipédia](https://en.wikipedia.org/wiki/Principle_of_least_privilege) — le principe et ses implications d'architecture.
- [Authorization Specification — MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) — la propagation d'identité dans une architecture agentique.

## Appelée par

- [[parcours/ai-red-teaming/index|AI Red Teaming]]
- [[parcours/forward-deployed-engineer/index|Forward Deployed Engineer]]
- [[parcours/ai-product-builder|AI Product Builder]]
- [[parcours/bi-analyst/index|BI Analyst]]

Voisines : [[notions/conception-d-api]], [[notions/donnees-sensibles]], [[notions/garde-fous]], [[notions/mcp]].
