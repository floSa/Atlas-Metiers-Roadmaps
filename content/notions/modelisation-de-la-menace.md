---
title: Modélisation de la menace
tags: [notion, menace, threat-modeling, risque, securite]
date: 2026-09-16
statut: actif
appelee-par: [ai-red-teaming, forward-deployed-engineer]
---

Exercice structuré qui répond, dans cet ordre, à trois questions : qui attaque et avec quels moyens, par où il entre, et ce qu'il obtient s'il réussit.

## À quoi ça sert

Sans modèle de menace, un travail de sécurité dérive vers ce qui est intéressant à trouver plutôt que vers ce qui coûterait cher. La modélisation impose une priorisation par **impact métier**, pas par élégance technique — et c'est la seule chose qui parle à la direction qui finance.

Son second apport est une décision d'architecture. Devant un système qui cumule accès à des données privées, exposition à du contenu non maîtrisé et canal de sortie vers l'extérieur, la question n'est plus « comment le durcir » mais « laquelle de ces trois propriétés peut-on retirer ». C'est presque toujours plus simple, plus sûr et moins cher que de renforcer les deux autres.

Sur les systèmes à base de modèle, l'exercice a un effet de tri immédiat : il sépare ce qui relève de la sécurité applicative ordinaire — la grande majorité des constats — de ce qui est réellement propre aux modèles et n'a pas d'équivalent.

## Ce qu'il faut savoir

- **Cartographier les surfaces.** Sur un système d'IA, quatre entrées qui ne se défendent pas au même endroit : les données d'entraînement ou d'affinage, l'interface de prompt, le processus d'inférence, et les outils et API connectés. Sur un système bâti sur un modèle du commerce, la première est hors de portée et la quatrième concentre le risque réel.
- **Graduer les adversaires** : l'utilisateur curieux qui teste les limites, le client légitime qui veut voir les données d'un autre locataire, l'employé interne, le concurrent, l'attaquant qui vise l'infrastructure. Chacun a un budget de requêtes et un niveau d'accès différents — un scénario à dix millions de requêtes n'est pas le même risque qu'un scénario à trois.
- **La triade létale** : données privées, contenu non fiable, canal de sortie. Leur conjonction est le critère de priorisation le plus efficace en revue d'architecture.
- **Classer par ce que le constat permet** — lire les données d'un autre client, déclencher un virement, dégrader un service réglementé — et non par la sophistication de la technique.
- **Les méthodes existantes servent de liste de contrôle** : STRIDE pour les catégories de menace, le NIST AI Risk Management Framework pour le vocabulaire commun et la remontée dans un registre de risques existant. Voir [[notions/gouvernance-ia]].
- **Le modèle de menace se date et se révise.** Ajouter un outil à un agent, indexer une nouvelle source ou ouvrir une API le rend caduc.
- **Le modèle le plus utile aujourd'hui n'est pas centré sur le modèle** mais sur la couche de connexion aux outils, où se concentre une part croissante des incidents réels.

## Selon le métier

### AI Red Teaming

C'est ce qui donne un périmètre à l'engagement et une structure au rapport. Le troisième point — ce que l'attaquant obtient — est celui que les rapports négligent et le seul qui déclenche une décision. Le modèle de menace sert aussi à défendre le périmètre : ce qui n'y figure pas n'a pas été testé, et le dire explicitement évite qu'un audit partiel soit lu comme un quitus.

### Forward Deployed Engineer

L'exercice se mène avec le client, pas pour lui, et il produit un livrable que le contrôle interne sait lire. Son bénéfice principal en mission est de trancher tôt des questions d'architecture : quelles données entrent dans l'index, quelles actions l'agent peut réellement déclencher, et par où une sortie est possible. Posées au cadrage, ces questions coûtent une réunion ; posées à la recette, elles coûtent une réécriture.

> [!warning] Piège
> Traiter la sécurité de l'IA comme un domaine neuf en bloc. Dans un audit réel, la grande majorité des constats est de la sécurité applicative ordinaire — une clé dans le dépôt, un point d'accès sans authentification, une absence de limitation de débit, un contrôle d'accès manquant sur l'index. Ne pas savoir trier fait dépenser l'effort sur les attaques spectaculaires pendant que les portes ouvertes restent ouvertes.

## Pour aller plus loin

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — le vocabulaire commun et le cycle cartographier / mesurer / gérer / gouverner.
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) — le socle applicatif, qui reste la source de la majorité des constats.
- [OWASP API Security Project](https://owasp.org/www-project-api-security/) — la surface qui concentre le risque sur les systèmes agentiques.

## Appelée par

- [[parcours/ai-red-teaming/index|AI Red Teaming]]
- [[parcours/forward-deployed-engineer/index|Forward Deployed Engineer]]

Voisines : [[notions/injection-de-prompt]], [[notions/controle-d-acces]], [[notions/chaine-d-approvisionnement-logicielle]], [[notions/gouvernance-ia]].
