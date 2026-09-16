---
title: RGPD
tags: [notion, rgpd, conformite, donnees-personnelles, droit]
date: 2026-09-16
statut: actif
appelee-par: [forward-deployed-engineer, ai-red-teaming, ai-product-builder, data-analyst, bi-analyst]
---

Le règlement général sur la protection des données encadre tout traitement de données se rapportant à une personne physique identifiée ou identifiable, et impose que chaque traitement ait une finalité déclarée, une base légale, une durée de conservation et un responsable nommé.

## À quoi ça sert

Le RGPD ne sert pas à empêcher les projets, il sert à rendre explicite une chose qu'une organisation fait de toute façon : décider qui a le droit de savoir quoi sur qui, et pour combien de temps. En pratique, dans un projet data ou IA, il joue trois rôles très concrets. Il tranche des questions d'architecture qui seraient autrement tranchées par défaut — où réside la base, quel sous-traitant reçoit quoi. Il fixe une échéance à la conservation, ce qui interdit le « on garde tout au cas où » qui transforme une fuite mineure en incident majeur. Et il donne un point de contrôle opposable : un traitement non déclaré peut être arrêté, y compris après la mise en service.

L'essentiel du coût de conformité vient du moment où l'on s'y prend. Posée au cadrage, la question est une contrainte de conception parmi d'autres ; découverte à la recette, c'est un projet à refaire.

## Ce qu'il faut savoir

- **Donnée personnelle** : toute donnée permettant d'identifier une personne, directement ou par recoupement. Un identifiant client, une adresse IP, un horodatage de connexion associé à un poste en font partie. La pseudonymisation reste du traitement de données personnelles ; seule l'anonymisation irréversible en sort, et elle est plus difficile à obtenir qu'on ne le croit.
- **Base légale** : consentement, contrat, obligation légale, intérêt légitime, mission d'intérêt public, sauvegarde des intérêts vitaux. Une seule suffit, mais il en faut une, et le consentement est la plus fragile — il se retire.
- **Finalité et minimisation** : une donnée est collectée pour une finalité déterminée, et seules les données nécessaires à cette finalité le sont. Réutiliser un jeu collecté pour autre chose est un nouveau traitement, pas une variante du premier.
- **Durée de conservation** : une durée chiffrée, par catégorie de donnée, avec une purge réellement exécutée. C'est l'obligation la plus souvent déclarée et la moins souvent implémentée.
- **Registre des traitements** et, au-delà d'un certain risque, **analyse d'impact** (AIPD). Le registre est tenu par le responsable de traitement ; un nouveau système y entre, ce n'est pas optionnel.
- **Sous-traitants et transferts** : chaque prestataire qui touche la donnée est un sous-traitant contractualisé. Un transfert hors Union européenne demande un mécanisme d'encadrement explicite — c'est la question que pose tout appel à une API de modèle hébergée ailleurs.
- **Droits des personnes** : accès, rectification, effacement, portabilité, opposition. Ils doivent être techniquement exécutables : savoir retrouver et supprimer toutes les occurrences d'une personne est une contrainte d'architecture, pas une procédure administrative.
- **Le délégué à la protection des données** est un allié, pas un obstacle. Il connaît les traitements existants, les précédents internes et ce qui passera. Le rencontrer tôt fait gagner des semaines.

## Selon le métier

### Forward Deployed Engineer

Rencontrer le délégué à la protection des données pendant la phase d'audit, pas avant la mise en service, et lui fournir quatre éléments : base légale, finalité, durée de conservation, localisation du traitement. Un traitement découvert en fin de mission peut être bloqué, et le FDE ne sera plus là pour le défendre. Voir aussi [[notions/donnees-sensibles]] pour la classification technique, qui est une autre question.

### AI Red Teaming

Le RGPD est le cadre qui transforme un constat technique en incident qualifiable. L'inférence d'appartenance — déterminer qu'un enregistrement donné faisait partie du corpus d'entraînement — suffit à créer une violation de données personnelles quand l'appartenance est elle-même une information sensible : la liste des patients d'un service, des clients en défaut de paiement, des salariés d'un plan social. C'est ce qui donne à une attaque techniquement modeste un impact réglementaire élevé.

### AI Product Builder

Le piège concret est la dorsale gérée dont les données résident hors Union européenne, choisie en trois clics au démarrage et impossible à déplacer ensuite. L'hébergement, les sous-traitants et la durée de conservation sont des décisions de la section déploiement, pas des formalités ultérieures. Et ne jamais brancher de données réelles sur un prototype hébergé publiquement.

### Data Analyst

Deux gestes quotidiens sont concernés. Le moissonnage de sites, dès qu'il ramène de la donnée personnelle — ce qui est le cas plus souvent qu'on ne le croit — se fait valider avant, pas après. Et un extrait de base client ne se colle pas dans un service grand public : vérifier ce que l'entreprise autorise, et à quel niveau de donnée.

### BI Analyst

La gouvernance et le RGPD se rejoignent sur un même objet : savoir d'où vient un chiffre, ce qu'il inclut, et qui a le droit de le voir. Les droits d'accès par ligne dans l'outil de restitution sont une obligation réglementaire autant qu'une fonctionnalité, et le lignage est ce qui permet de répondre à une demande d'effacement sans deviner.

> [!warning] Piège
> Traiter la conformité comme une case à cocher en fin de projet. Le RGPD produit des contraintes d'architecture — localisation, cloisonnement, effaçabilité — qui coûtent une heure au cadrage et une réécriture six mois plus tard. Le second piège, plus discret : croire qu'un jeu de données « anonymisé » l'est. Retirer le nom ne suffit pas quand le croisement code postal, date de naissance et sexe réidentifie l'essentiel d'une population.

## Pour aller plus loin

- [Texte du règlement, article par article](https://gdpr-info.eu/) — la source, consultable par article.
- [What is GDPR, the EU's new data protection law?](https://gdpr.eu/what-is-gdpr/) — la synthèse d'entrée, en anglais.
- [What is GDPR Compliance in Web Application and API Security?](https://probely.com/blog/what-is-gdpr-compliance-in-web-application-and-api-security/) — l'angle applicatif, utile pour traduire les obligations en contrôles.
- [Guidance on AI and data protection — ICO](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/how-do-we-ensure-fairness-in-ai/what-about-fairness-bias-and-discrimination/) — l'autorité britannique sur l'articulation IA / protection des données ; le cadre diffère mais le raisonnement est transposable.

## Appelée par

- [[parcours/forward-deployed-engineer/index|Forward Deployed Engineer]]
- [[parcours/ai-red-teaming/index|AI Red Teaming]]
- [[parcours/ai-product-builder|AI Product Builder]]
- [[parcours/data-analyst/index|Data Analyst]]
- [[parcours/bi-analyst|BI Analyst]]

Voisines : [[notions/donnees-sensibles]], [[notions/gouvernance-ia]], [[notions/controle-d-acces]], [[notions/lignage-des-donnees]].
