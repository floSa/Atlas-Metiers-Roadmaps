---
tags: [notion, legacy, erp, crm, interfacage, integration]
date: 2026-09-16
statut: actif
appelee-par: [forward-deployed-engineer]
---

# Systèmes patrimoniaux

Applications anciennes qui portent encore une activité réelle — ERP, CRM, bases métier, progiciels spécifiques — et qu'on doit intégrer sans pouvoir les remplacer.

## À quoi ça sert

Un système patrimonial n'est pas un système mal conçu : c'est un système qui a survécu, ce qui est une performance. Il contient des règles métier accumulées sur vingt ans, dont une partie n'est écrite nulle part ailleurs, et il est utilisé quotidiennement par des gens qui savent le faire fonctionner.

La question n'est donc jamais « comment le remplacer » mais **« comment m'y brancher sans le casser et sans dépendre de ses détails »**. Ce déplacement change tout : il transforme un projet de refonte, qui échoue souvent, en un projet d'interfaçage, qui aboutit.

Le connecteur qui en résulte est le composant qui survivra le plus longtemps. Il sera repris par l'équipe interne, il continuera de tourner après le départ de son auteur, et il mérite plus de soin que la partie visible du projet — ce qui est rarement la répartition d'effort observée.

## Ce qu'il faut savoir

- **L'inventaire d'abord** : quelles données, quelle fraîcheur, quels volumes, quelles fenêtres d'exploitation, qui administre, et surtout ce qui casse si l'on ajoute de la charge.
- **Les stratégies d'accès, par ordre de préférence** : une API existante, une base de lecture ou un réplica, un export de fichier programmé, une capture de changements, et en dernier recours le pilotage de l'interface graphique.
- **Ne jamais écrire directement dans la base d'un progiciel.** Les règles métier sont dans l'application, pas dans le schéma ; une écriture directe contourne des contrôles et produit des incohérences qui se découvrent des mois plus tard.
- **La couche anti-corruption** est le motif central : un module de traduction qui isole le vocabulaire et les bizarreries du système ancien du reste de l'architecture. Sans elle, les particularités du patrimonial contaminent tout le nouveau code.
- **L'étranglement progressif** (*strangler fig*) permet de remplacer par morceaux : on intercepte, on redirige une fonction à la fois, on retire l'ancien quand il ne sert plus. C'est la seule approche de remplacement qui aboutit régulièrement.
- **Les fenêtres d'exploitation contraignent le calendrier** : traitements de nuit, clôtures mensuelles, gels de fin d'année. À découvrir en phase d'audit, pas la veille d'une mise en service.
- **Les caractères, les dates et les identifiants** sont les trois sources d'incident classiques : encodages anciens, formats de date ambigus, identifiants réutilisés après purge.
- **Réconcilier plutôt que faire confiance** : un rapprochement périodique entre le système ancien et le nouveau détecte les divergences avant les utilisateurs.

## Selon le métier

### Forward Deployed Engineer

Le connecteur est le composant qui survivra le plus longtemps et sera repris par l'équipe du client ; il mérite plus de soin que la partie IA. Deux conséquences pratiques : il s'écrit avec les conventions du client et non celles de son auteur, et il est documenté pour quelqu'un qui le reprendra dans six mois sans pouvoir poser de question. L'exposition de ces systèmes à un agent via [[notions/mcp]] est aujourd'hui la voie la plus rapide — et un point d'entrée de sécurité à traiter comme tel.

> [!info] Une seule appelante
> Notion appelée par le seul parcours Forward Deployed Engineer, qui en est le principal consommateur dans le lot 1.

> [!warning] Piège
> Prendre la documentation du système pour son comportement. Elle décrit ce qui était prévu ; vingt ans de paramétrages, de correctifs et de contournements ont produit autre chose. La seule source fiable est l'observation : extraire, comparer avec ce que voient les utilisateurs, et demander pourquoi quand cela diverge.

## Pour aller plus loin

- [Strangler Fig Application — Martin Fowler](https://martinfowler.com/bliki/StranglerFigApplication.html) — le motif de remplacement progressif, par celui qui l'a nommé.
- [Anti-corruption Layer pattern — Microsoft](https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer) — la couche de traduction, avec ses conditions d'emploi.
- [Legacy system — Wikipédia](https://en.wikipedia.org/wiki/Legacy_system) — le panorama et le vocabulaire.

## Appelée par

- [[parcours/forward-deployed-engineer/index|Forward Deployed Engineer]]

Voisines : [[notions/conception-d-api]], [[notions/mcp]], [[notions/qualite-des-donnees]], [[notions/collecte-de-donnees]].
