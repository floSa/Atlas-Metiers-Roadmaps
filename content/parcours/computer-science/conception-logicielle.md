---
title: Conception logicielle
tags: [parcours, computer-science, design-patterns, uml, injection-de-dependances, diagrammes]
date: 2026-09-16
statut: actif
source: https://roadmap.sh/computer-science
---

La valeur réelle des patterns n'est pas de les appliquer mais de les **reconnaître** : comprendre qu'un cadriciel impose une fabrique ou une stratégie fait gagner des heures de lecture.

```mermaid
flowchart TD
  CA["Conception d'API<br/>les frontières qui comptent"]
  TL["Tests logiciels<br/>ce que l'injection rend testable"]
  MCP["MCP<br/>stratégie plus registre, standardisés"]
  BP["BPMN<br/>le diagramme que lisent les métiers"]
  RT["Rédaction technique<br/>le diagramme dans le dépôt"]

  click CA "/notions/conception-d-api"
  click TL "/notions/tests-logiciels"
  click MCP "/notions/mcp"
  click BP "/notions/bpmn"
  click RT "/notions/redaction-technique"
```

## Cinq patterns qui reviennent, deux diagrammes qui servent

Sur le catalogue complet — création, structure, comportement — cinq patterns reviennent vraiment : fabrique, stratégie, adaptateur, observateur, décorateur. Côté architecture, le choix entre couches, hexagonal, piloté par les événements ou microservices se joue sur les **frontières de déploiement et de données**, jamais sur l'élégance. L'**injection de dépendances** — passer les dépendances au lieu de les construire — est la pratique qui rend un pipeline testable sans réseau, en substituant un faux client à l'appel réel.

Deux patterns moins cités méritent leur place. L'**objet nul** : un objet inerte plutôt qu'une valeur absente supprime les tests de nullité éparpillés — traceur désactivé, cache sans effet. L'**objet-type** : décrire les variantes en données plutôt qu'en classes, ce qui est exactement le mécanisme d'un registre d'outils ou de modèles chargé depuis un fichier de configuration. C'est aussi, précisément, ce que standardise un protocole d'outils : stratégie plus registre, déclarés en données et sélectionnés à l'exécution.

Côté modélisation, deux diagrammes justifient leur coût. Le **diagramme de séquence** raconte un flux — une chaîne de récupération avec reclassement et repli se documente en dix lignes là où la prose en demande une page. Le **diagramme d'états** rend explicite une machine à états avec reprise sur erreur, et fait apparaître les transitions qu'on avait oubliées. Les diagrammes de classes servent à cartographier un schéma de données, ceux de cas d'usage à parler à des interlocuteurs non techniques. Écrits en Mermaid dans le dépôt, ils se relisent dans le diff — c'est ce qui décide de leur survie.

## Ce qu'il faut savoir faire

- **Reconnaître les patterns d'un cadriciel** à la lecture, pour cesser de deviner pourquoi une classe existe.
- **Injecter les dépendances d'un pipeline** pour le rendre testable hors ligne, sans réseau ni service externe.
- **Documenter un flux par un diagramme de séquence** versionné dans le dépôt, plutôt que par une page de prose qui se périme en silence.
- **Modéliser une machine à états** avant de l'implémenter, en particulier quand elle doit reprendre après erreur.
- **Choisir une frontière de service** sur un critère de déploiement ou de propriété des données, et savoir énoncer ce critère.
- **Attendre le troisième cas concret avant de factoriser** : la sur-abstraction préventive coûte plus cher que la duplication assumée.

> [!warning] Piège
> Introduire une hiérarchie de classes abstraites pour un pipeline qui n'a qu'un seul cas d'usage. On paie immédiatement la complexité pour une flexibilité dont on ignore encore la forme, et la deuxième variante ne rentre presque jamais dans l'abstraction prévue.

## Les notions mobilisées

- [[notions/conception-d-api]] — l'angle *computer science* : un contrat d'interface est la seule frontière qui tienne dans le temps, les patterns internes changent.
- [[notions/tests-logiciels]] — l'injection de dépendances n'a d'intérêt que pour ce qu'elle rend testable ; sans tests, c'est de la cérémonie.
- [[notions/mcp]] — stratégie plus registre, standardisés : les outils déclarés en données et sélectionnés à l'exécution.
- [[notions/bpmn]] — quand le diagramme doit être lu par le métier plutôt que par l'équipe technique.
- [[notions/redaction-technique]] — un diagramme n'existe que s'il est dans le dépôt et relu dans le diff.

## Pour apprendre

- [Refactoring Guru — Design Patterns](https://refactoring.guru/design-patterns) — le catalogue illustré, avec le problème que chaque pattern résout et le code dans plusieurs langages.
- [Mermaid — sequence diagrams](https://mermaid.js.org/syntax/sequenceDiagram.html) et [state diagrams](https://mermaid.js.org/syntax/stateDiagram.html) — la syntaxe des deux diagrammes qui servent, rendus nativement dans un dépôt.
- [Architecture Decision Records](https://adr.github.io/) — le format court qui enregistre *pourquoi* une frontière a été tracée là.
- [The Twelve-Factor App](https://12factor.net/) — les contraintes de configuration et de dépendances qui rendent un service déployable ailleurs.
- [Domain-Driven Design Reference](https://www.domainlanguage.com/ddd/reference/), Eric Evans — le vocabulaire des frontières de domaine, en cinquante pages gratuites.
