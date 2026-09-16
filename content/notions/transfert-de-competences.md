---
tags: [notion, transfert, sortie-de-mission, autonomie, maintenance]
date: 2026-09-16
statut: actif
appelee-par: [forward-deployed-engineer]
---

# Transfert de compétences

Organisation de la reprise d'un système par ceux qui l'exploiteront, de manière à ce qu'il reste modifiable, corrigeable et compréhensible après le départ de celui qui l'a construit.

## À quoi ça sert

Le critère de réussite d'un projet livré chez quelqu'un d'autre n'est pas qu'il fonctionne à la recette : c'est qu'il fonctionne encore dans dix-huit mois, après trois changements de contexte et sans son auteur. Tout le reste est une démonstration.

Le transfert n'est donc pas une formation de fin de mission, c'est **une contrainte qui s'impose à toutes les décisions techniques depuis le premier jour**. Elle change des choix qu'on croirait purement techniques : quelle base, quel langage, quel outil de chaîne d'intégration, quel niveau d'abstraction. La bonne réponse est rarement la meilleure sur le papier, c'est celle que l'équipe en place sait déjà exploiter.

Son second effet est de révéler tôt ce qui ne sera pas repris. Si personne n'est identifié pour porter le système, mieux vaut le savoir pendant qu'on peut encore réduire son périmètre.

## Ce qu'il faut savoir

- **Identifier le repreneur dès le cadrage**, nommément. Un système sans propriétaire désigné est un système abandonné à la première réorganisation.
- **Construire avec l'outillage du repreneur** : son dépôt, sa chaîne d'intégration, son registre d'images, son coffre à secrets, ses conventions. Une chaîne construite sur un service qu'il n'utilise pas est inutilisable dès le départ de l'auteur.
- **Ce qui se transfère est plus large que le code** : les décisions et leurs raisons, le jeu d'évaluation et son usage, la procédure d'exploitation, les contacts, les limites connues, et ce qu'il ne faut surtout pas faire.
- **Le registre de décisions est le livrable le plus durable** : le code dit ce que fait le système, il ne dira jamais pourquoi ce seuil, cette base, ce contournement qui a l'air d'une erreur.
- **Transférer par la pratique.** Faire faire, pas montrer. Le repreneur doit avoir corrigé un incident réel et ajouté un cas au jeu d'évaluation avant la fin de la mission.
- **Prévoir les limites connues et les cas dégradés.** Ce qui décide de la confiance du repreneur est ce qui se passe quand le système se trompe, pas quand il fonctionne.
- **Une période de retrait progressif** vaut mieux qu'une date de fin : disponible en second niveau pendant quelques semaines, sans être aux commandes.
- **La documentation vit avec le code**, dans le dépôt, datée. Un espace documentaire séparé se périme sans bruit.

## Selon le métier

### Forward Deployed Engineer

C'est le cœur de la sortie de mission, et l'angle est temporel : le transfert n'est pas une phase finale mais une contrainte présente dès la première décision technique. Concrètement, tout ce qui a été construit avec les outils du client, tout ce qui a été écrit pour un lecteur sans contexte et tout ce qui a été rejoué automatiquement est du transfert déjà fait. Ce qui est reporté à la dernière semaine ne se fera pas.

> [!info] Une seule appelante
> Notion appelée par le seul parcours Forward Deployed Engineer. Elle reste mutualisée parce qu'elle s'applique à toute intervention livrée chez un tiers, y compris hors IA.

> [!warning] Piège
> Confondre transfert et formation. Une session de deux heures avec des diapositives ne transfère rien : elle informe. Ce qui transfère est d'avoir fait — une correction, un ajout, un déploiement — pendant que l'auteur est encore là pour rattraper. Une formation sans mise en pratique produit un repreneur qui croit savoir, et découvre qu'il ne sait pas le jour du premier incident.

## Pour aller plus loin

> [!note] Ressources
> Ce sujet n'a aucune ressource dans les captures amont : c'est un apport propre du dossier Forward Deployed Engineer, issu du brief de commande et non de roadmap.sh. Aucune ressource externe n'est citée ici plutôt qu'une référence non vérifiée. Voir [[parcours/forward-deployed-engineer/sortie-de-mission]] pour le déroulé détaillé.

## Appelée par

- [[parcours/forward-deployed-engineer/index|Forward Deployed Engineer]]

Voisines : [[notions/redaction-technique]], [[notions/conduite-du-changement]], [[notions/integration-continue]], [[notions/evaluation-llm]].
