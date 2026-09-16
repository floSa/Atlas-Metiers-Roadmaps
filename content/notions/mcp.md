---
title: MCP — Model Context Protocol
tags: [notion, mcp, protocole, agents, outils]
date: 2026-09-16
statut: actif
appelee-par: [forward-deployed-engineer, ai-product-builder, ai-red-teaming]
---

Protocole ouvert qui normalise la façon dont une application à base de modèle découvre et invoque des capacités extérieures — outils, ressources, invites — exposées par des serveurs indépendants.

## À quoi ça sert

Avant MCP, chaque intégration entre un assistant et un système interne était du câblage sur mesure : une description d'outil propre à un fournisseur, un schéma d'arguments réécrit, une authentification ad hoc. Le protocole remplace ce travail par un contrat commun — un serveur écrit une fois est consommable par n'importe quel client conforme.

L'intérêt pratique est surtout un intérêt de durée de vie. Un connecteur exposé en MCP survit au changement de modèle, de client et de fournisseur, parce qu'il ne dépend d'aucun des trois. C'est ce qui en fait la voie la plus rapide pour ouvrir proprement un système interne à un agent, et ce qui justifie d'y mettre du soin : c'est le composant qui restera.

La contrepartie est une surface d'attaque nouvelle et partagée. Un serveur d'outils est un point d'entrée qui exécute des actions avec des identifiants ; une faille dans la couche de protocole se propage d'un coup à tout l'écosystème au lieu de rester cantonnée à un produit.

## Ce qu'il faut savoir

- **Trois primitives** : les *tools* (des actions que le modèle peut invoquer), les *resources* (des données qu'il peut lire), les *prompts* (des gabarits proposés par le serveur). La distinction outil / ressource porte l'essentiel de la sémantique de sécurité : lire n'est pas agir.
- **Client et serveur** : l'application hôte embarque un client, qui se connecte à un ou plusieurs serveurs. Un serveur peut être local (lancé sur le poste) ou distant (joignable par le réseau) — les modèles de menace des deux n'ont rien à voir.
- **La description de l'outil est le prompt.** Le modèle choisit d'après le nom, la description et le schéma d'arguments. Une description vague produit des appels erratiques ; une description précise, des paramètres nommés explicitement et des exemples corrigent plus de comportements qu'un réglage de température.
- **Peu d'outils, bien nommés.** Au-delà d'une vingtaine d'outils exposés, la sélection se dégrade. Regrouper, filtrer par contexte, et retirer ce qui ne sert pas.
- **Autorisation** : la spécification traite explicitement la question. Le point critique est la propagation d'identité — un serveur ne doit pas transmettre à un service en aval des identifiants qui n'ont pas été émis pour lui, ni agir avec un compte de service qui voit plus que l'utilisateur.
- **La chaîne d'approvisionnement compte** : un serveur installé en deux minutes exécute du code avec les droits de son hôte. Inventorier ce qui est installé, d'où il vient, et en quelle version. Voir [[notions/chaine-d-approvisionnement-logicielle]].
- **Un résultat d'outil est du contenu non maîtrisé.** Il revient dans la fenêtre de contexte et peut contenir des instructions — c'est un vecteur d'injection indirecte à part entière.

## Selon le métier

### Forward Deployed Engineer

Le moyen le plus rapide d'exposer proprement un système interne à un agent, et un point d'entrée de sécurité à traiter comme tel. Le serveur MCP construit en mission est souvent le composant qui survivra le plus longtemps et sera repris par l'équipe du client : il mérite plus de soin que la partie IA, et une documentation qui se lit sans son auteur.

### AI Product Builder

L'usage courant de MCP n'est pas dans le produit livré mais dans l'atelier : brancher les assistants de codage sur le dépôt, la base et le suivi de tickets. C'est là que le gain est immédiat, alors qu'exposer son propre produit en MCP n'a de sens que s'il a des clients agentiques, ce qui est rarement le cas d'un premier produit.

### AI Red Teaming

La couche de connexion aux outils concentre une part croissante des incidents réels : serveur qui relaie les identifiants de son appelant à un service en aval — le cas d'école du délégué confus —, ou instruction dissimulée dans un contenu non maîtrisé qui fait exfiltrer des données par un outil parfaitement légitime. Tester un système agentique, c'est tester ses frontières d'outils et la confiance entre serveurs avec autant de rigueur que ses prompts.

> [!warning] Piège
> Exposer un serveur MCP avec un compte de service unique parce que c'est ce qui marche tout de suite. L'authentification de l'utilisateur est alors faite à la porte d'entrée et perdue avant la couche de données : tout utilisateur connecté obtient ce que voit le compte de service. C'est le constat le plus fréquent en audit, et il ne se corrige pas après coup sans réécrire la chaîne d'appel.

## Pour aller plus loin

- [Build an MCP server — documentation officielle](https://modelcontextprotocol.io/docs/develop/build-server#build-an-mcp-server) — le point de départ pour écrire un serveur.
- [Authorization Specification — MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) — la référence sur l'identité et les jetons, à lire avant toute exposition réseau.
- [Connect to remote MCP servers](https://modelcontextprotocol.io/docs/develop/connect-remote-servers) — le cas distant et ses implications.
- [GitHub MCP Exploited: Accessing Private Repositories via MCP](https://invariantlabs.ai/blog/mcp-github-vulnerability) — un incident réel sur cette couche, utile pour calibrer le risque.

## Appelée par

- [[parcours/forward-deployed-engineer/index|Forward Deployed Engineer]]
- [[parcours/ai-product-builder/index|AI Product Builder]]
- [[parcours/ai-red-teaming/index|AI Red Teaming]]

Voisines : [[notions/agents-llm]], [[notions/conception-d-api]], [[notions/controle-d-acces]], [[notions/chaine-d-approvisionnement-logicielle]].
