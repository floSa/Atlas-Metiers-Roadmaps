---
title: Tableur
tags: [notion, tableur, excel, analyse, outillage]
date: 2026-09-16
statut: actif
appelee-par: [data-analyst, bi-analyst]
---

Outil de manipulation de données en grille où la donnée, le calcul et la présentation occupent le même espace — ce qui fait à la fois sa rapidité et sa limite.

## À quoi ça sert

Le tableur reste l'outil le plus rapide qui existe pour regarder mille lignes, faire trois calculs et montrer le résultat à quelqu'un. Il n'a pas de rival sur ce terrain, et la posture qui consiste à le mépriser coûte du temps. C'est aussi le format dans lequel le métier vous rendra ses données, quoi qu'on en dise.

Sa limite n'est pas le volume, c'est la **traçabilité**. Dans un tableur, rien ne distingue une valeur saisie d'une valeur calculée, une formule d'une constante collée par erreur. Un résultat n'est donc reproductible que si personne n'a rien touché — hypothèse que la pratique dément systématiquement.

La bonne question n'est donc pas « quelles formules connaître » mais **« à quel moment je n'ai plus le droit de rester ici »**. Le seuil est net : dès qu'un résultat devra être régénéré, ou qu'une valeur a été saisie à la main dans un fichier de production.

## Ce qu'il faut savoir

- **Le socle utile** : références absolues et relatives, `RECHERCHEX` (ou `INDEX`/`EQUIV`), `SOMME.SI.ENS` et `NB.SI.ENS`, tableaux croisés dynamiques, mise en forme conditionnelle, tables structurées.
- **Les tableaux croisés dynamiques** répondent à la majorité des demandes d'agrégation réelles, plus vite que n'importe quelle requête, et se relisent sans formation.
- **Power Query** change la nature de l'outil : il rend l'étape de transformation rejouable et auditable, ce qui retire au tableur son principal défaut. C'est la compétence tableur la plus rentable aujourd'hui.
- **Les modes d'échec classiques** : dates converties automatiquement, identifiants avec zéros initiaux tronqués, séparateur décimal et séparateur de colonnes en contexte francophone, lignes masquées oubliées dans une somme, plage de formule qui ne suit pas l'ajout de lignes.
- **Le fichier partagé sur un lecteur réseau** finit en cinq versions concurrentes. Si un chiffre circule, il doit venir d'une source unique.
- **Le tableur comme format d'échange** est légitime et durable ; le tableur comme **système de production** est une dette qui grossit en silence.
- **Le CSV n'est pas un tableur** : c'est un format texte que le tableur interprète, parfois abusivement. Contrôler l'encodage et les types à l'import plutôt que de laisser l'inférence décider.

## Selon le métier

### Data Analyst

Le seuil de sortie est la seule chose à retenir : dès qu'un résultat devra être régénéré, ou qu'une valeur a été saisie à la main dans un fichier de production, on passe à un script ou à une requête. Avant ce seuil, le tableur est souvent la réponse la plus rapide, et le savoir évite de sur-outiller une demande d'une heure.

### BI Analyst

C'est l'outil qu'on n'évite pas, et c'est aussi le concurrent : un chiffre juste qu'on n'arrive pas à défendre est remplacé par celui d'un tableur. Plutôt que de lutter, l'angle qui fonctionne est de fournir un export propre et daté depuis la source gouvernée — les gens continueront d'utiliser leur tableur, mais à partir du bon chiffre.

> [!warning] Piège
> Le fichier qui devient un système. Il commence comme une analyse ponctuelle, quelqu'un le réutilise le mois suivant, une colonne est ajoutée à la main, puis une direction s'en sert pour piloter. Personne n'a décidé de bâtir un système ; il en existe un, sans propriétaire, sans test et sans sauvegarde. Le repérer tôt et le sortir du tableur coûte une semaine ; le faire après trois ans coûte un projet.

## Pour aller plus loin

- [Excel — formation officielle Microsoft](https://support.microsoft.com/en-us/office/excel-video-training-9bc05390-e94c-46af-a5b3-d7c22f6990bb) — le socle, par l'éditeur.
- [Master Data Cleaning Essentials on Excel in 10 Minutes](https://www.youtube.com/watch?v=jxq4-KSB_OA) — le nettoyage de base, rapide et applicable.
- [Exploratory Data Analysis in Excel](https://www.scaler.com/topics/exploratory-data-analysis-projects/) — jusqu'où on peut aller sans sortir de l'outil.

## Appelée par

- [[parcours/data-analyst|Data Analyst]]
- [[parcours/bi-analyst/index|BI Analyst]]

Voisines : [[notions/outils-decisionnels]], [[notions/pandas]], [[notions/collecte-de-donnees]].
