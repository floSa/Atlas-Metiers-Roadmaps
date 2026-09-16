---
title: Données sensibles
tags: [notion, donnees-sensibles, classification, anonymisation, cloisonnement]
date: 2026-09-16
statut: actif
appelee-par: [forward-deployed-engineer, ai-red-teaming]
---

Données dont la divulgation, l'altération ou l'usage détourné causerait un préjudice — à une personne, à l'organisation ou à un tiers — et qui appellent pour cette raison un traitement technique distinct des autres.

## À quoi ça sert

La classification des données sert à ne pas protéger tout de la même façon. Une organisation qui applique le même niveau de contrôle partout finit par l'abaisser partout, parce que le coût devient insupportable. Distinguer permet de concentrer l'effort là où le préjudice est réel.

C'est aussi ce qui rend les décisions d'architecture possibles. « Ces données peuvent-elles sortir du système d'information ? » est la question qui tranche le choix de modèle, l'hébergement et parfois l'existence du projet. Sans classification, elle se pose au cas par cas, tard, et par la personne la moins bien placée.

Il faut distinguer la sensibilité **juridique** — les catégories particulières du RGPD, le secret professionnel, les données de santé — de la sensibilité **métier** : un carnet de commandes, une grille tarifaire, une liste de clients en difficulté. La seconde n'est pas encadrée par un texte et coûte parfois plus cher.

## Ce qu'il faut savoir

- **La classification existe déjà dans la plupart des organisations.** S'y conformer plutôt qu'en inventer une : une classification concurrente n'est pas appliquée et affaiblit celle qui existe.
- **Le cloisonnement est le mécanisme principal** : séparer les environnements, restreindre les accès à ce qui est nécessaire, éviter que des données de niveaux différents se retrouvent dans le même index ou le même journal.
- **Pseudonymisation ≠ anonymisation.** La première remplace un identifiant par un autre et reste réversible — donc reste du traitement de données personnelles. La seconde doit résister au recoupement, ce qui est difficile : code postal, date de naissance et sexe suffisent souvent à réidentifier.
- **Le masquage avant l'appel** à un service extérieur est une pratique efficace, à condition de savoir ce qu'on masque. Les détecteurs d'entités manquent les identifiants métier, les numéros de dossier et les noms rares.
- **Les journaux et les traces sont un angle mort.** Les données sensibles y entrent par défaut et y restent plus longtemps que dans la base. À décider au moment de la conception de l'observabilité.
- **Les données d'entraînement sont publiables de fait** dès que le modèle est exposé : la mémorisation permet la restitution. Voir [[notions/affinage-de-modele]].
- **Le filtrage par identité descend jusqu'à la couche de données.** Contrôler l'accès à l'écran et interroger l'index avec un compte qui voit tout ne protège rien.
- **La durée de conservation fait partie de la protection.** Ce qui a été supprimé ne fuit pas.

## Selon le métier

### Forward Deployed Engineer

La classification existe déjà chez le client et fait autorité. S'y conformer plutôt qu'en inventer une, et rencontrer tôt les personnes qui la tiennent. L'exercice pratique de la phase d'audit : pour chaque étape du processus cartographié, dire quelles catégories de données la traversent — c'est ce qui révèle les contraintes d'architecture avant qu'elles ne coûtent cher.

### AI Red Teaming

La conséquence la plus fréquente en entreprise n'est pas la génération de contenu interdit, c'est la **lecture transversale** : faire remonter par la récupération un document auquel l'utilisateur courant n'a pas droit. Le point de contrôle est le filtrage de l'index par identité, appliqué à la requête et non après coup. Le test correspondant est simple et presque toujours concluant.

> [!warning] Piège
> Croire qu'un jeu de données a été anonymisé parce que les noms ont été retirés. La réidentification par recoupement est bien documentée et ne demande pas de moyens particuliers. Si le jeu doit réellement sortir du périmètre protégé, l'anonymisation se conçoit et se teste — sinon, il faut le traiter comme des données personnelles et en assumer les contraintes.

## Pour aller plus loin

- [A Complete Guide on PII Redaction](https://enthu.ai/blog/what-is-pii-redaction/) — les techniques de masquage et leurs limites.
- [What Is Data Privacy? — IBM](https://www.ibm.com/think/topics/data-privacy) — le cadrage général, utile pour le vocabulaire.
- [What about fairness, bias and discrimination? — ICO](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/how-do-we-ensure-fairness-in-ai/what-about-fairness-bias-and-discrimination/) — l'angle protection des données appliqué aux systèmes d'IA.

## Appelée par

- [[parcours/forward-deployed-engineer/index|Forward Deployed Engineer]]
- [[parcours/ai-red-teaming/index|AI Red Teaming]]

Voisines : [[notions/rgpd]], [[notions/controle-d-acces]], [[notions/gouvernance-ia]], [[notions/observabilite]].
