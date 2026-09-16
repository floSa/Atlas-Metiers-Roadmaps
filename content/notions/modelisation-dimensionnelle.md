---
title: Modélisation dimensionnelle
tags: [notion, modelisation-dimensionnelle, faits, dimensions, granularite]
date: 2026-09-16
statut: actif
appelee-par: [bi-analyst]
---

Organisation des données analytiques en tables de faits — les événements mesurables — et tables de dimensions — les axes selon lesquels on les découpe — de manière à rendre les questions métier exprimables sans connaître le système source.

## À quoi ça sert

Le modèle dimensionnel est le contrat entre la donnée et ceux qui la consultent. Il traduit la structure des systèmes de production, faite pour écrire vite et sans redondance, en une structure faite pour répondre à « combien, par quoi, sur quelle période ».

Son intérêt est autant cognitif que technique : un modèle en étoile se comprend en une minute par quelqu'un qui n'est pas informaticien. C'est ce qui rend la discussion possible avec le métier sur ce que contient réellement un indicateur, et c'est cette conversation qui produit la qualité, pas le schéma.

Il porte enfin l'historisation : c'est là qu'on décide si l'analyse se lit avec les attributs d'aujourd'hui ou avec ceux du jour de l'événement — une décision dont personne ne parle et dont tout dépend.

## Ce qu'il faut savoir

- **Table de faits** : les événements, avec leurs mesures numériques et leurs clés vers les dimensions. Une ligne = un événement au grain choisi.
- **Table de dimensions** : les axes d'analyse — client, produit, date, magasin — avec leurs attributs descriptifs, dénormalisés pour rester lisibles.
- **Le grain se déclare en premier, et en une phrase.** « Une ligne par ligne de commande » ou « une ligne par commande » ne sont pas le même modèle et ne répondent pas aux mêmes questions. Un grain implicite produit des doubles comptages qu'on découvre en réunion.
- **Étoile contre flocon** : l'étoile dénormalise les dimensions, le flocon les éclate en sous-tables. L'étoile gagne presque toujours en analytique — plus lisible, moins de jointures, et le gain de stockage du flocon n'a plus d'importance.
- **Types de faits** : transactionnel (un événement), instantané périodique (un état à une date), instantané cumulé (un processus avec ses étapes). Choisir le mauvais type rend certaines questions impossibles.
- **Additivité** : une mesure additive se somme sur tous les axes, une mesure semi-additive ne se somme pas sur le temps (un solde), une mesure non additive ne se somme jamais (un taux). C'est la source d'erreur la plus fréquente dans les outils de restitution.
- **Dimensions à évolution lente** : conserver l'historique d'un attribut (type 2) ou l'écraser (type 1). Décision structurante, à prendre avec le métier, indicateur par indicateur.
- **La dimension de date mérite une vraie table** : jours ouvrés, semaines fiscales, jours fériés, saisons. C'est elle qui porte les effets de calendrier, et elle sert tous les jours.

## Selon le métier

### BI Analyst

La mécanique ci-dessus est mutualisée ; ce qui appartient au parcours BI Analyst, c'est **la conduite des quatre ou cinq décisions** qui font qu'un modèle tient dix ans ou se réécrit tous les dix-huit mois — le grain, les dimensions conformées, l'historisation, l'additivité des mesures, et qui a le mandat de trancher. Le parcours les traite avec leurs conséquences de terrain ; cette notion en porte les définitions.

> [!info] Une seule appelante
> Notion appelée par le seul parcours BI Analyst, conservée ici par décision du pilote : le partage proposé par le chantier 06 est retenu — la notion porte les définitions, le parcours porte les décisions et leurs conséquences.

> [!warning] Piège
> Changer le grain d'une table de faits en cours de route parce qu'un nouveau besoin l'exige. Tout ce qui a été construit dessus — mesures, rapports, définitions, historique — devient faux ou ambigu, et la migration coûte plus que la reconstruction. Un nouveau grain justifie une nouvelle table de faits, pas une modification de l'existante.

## Pour aller plus loin

- [What is a Data Warehouse? — Google Cloud](https://cloud.google.com/learn/what-is-a-data-warehouse) — le contexte dans lequel le modèle dimensionnel prend place.
- [What is Normalization in DBMS (SQL)?](https://www.guru99.com/database-normalization.html) — la normalisation transactionnelle, dont le modèle dimensionnel s'éloigne volontairement.
- [dbt — documentation](https://docs.getdbt.com/docs/build/documentation) — l'outillage qui met ce modèle sous contrôle de version.

## Appelée par

- [[parcours/bi-analyst|BI Analyst]]

Voisines : [[notions/entrepot-de-donnees]], [[notions/transformation-dbt]], [[notions/series-temporelles]], [[notions/sql]].
