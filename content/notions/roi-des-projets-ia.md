---
tags: [notion, roi, valeur, cout-complet, decision]
date: 2026-09-16
statut: actif
appelee-par: [forward-deployed-engineer, ai-product-builder]
---

# Retour sur investissement des projets d'IA

Mise en regard de la valeur réellement créée par un système et de son coût complet, y compris ce qu'il coûtera à faire vivre une fois que son auteur sera parti.

## À quoi ça sert

Le calcul de retour sur investissement ne sert pas à justifier un projet après coup : il sert à **choisir quoi construire**, et surtout quoi ne pas construire. Sa vertu principale est de rendre visible la partie du coût que personne ne compte — la maintenance, la reprise, la montée de version, l'astreinte, le successeur quand l'auteur part.

Sur les projets d'IA, deux particularités déforment le calcul. Le coût de fabrication a baissé au point de ne plus être structurant, ce qui pousse à construire des choses qu'on aurait achetées. Et le coût d'exploitation est **variable** : il croît avec l'usage, donc avec le succès, ce qui est l'inverse du logiciel classique.

Le second usage est politique : un chiffre partagé permet de trancher une priorité sans que ce soit le plus insistant qui l'emporte.

## Ce qu'il faut savoir

- **Quantifier même grossièrement bat ne pas quantifier.** « Quatre-vingts dossiers par semaine, vingt minutes chacun, dont la moitié en ressaisie » suffit à décider. La précision vient après, si elle vient.
- **Ces chiffres se collectent tôt ou jamais.** Une fois le développement commencé, plus personne n'a le temps d'établir la situation de référence — et sans référence, aucun gain n'est démontrable.
- **Le coût complet** : construction, hébergement, appels de modèle au volume réel, supervision, correction, mise à jour des dépendances, formation, et le temps de reprise du code par quelqu'un d'autre.
- **Le gain se formule en termes métier** — délai de traitement, taux de reprise, dossiers traités par jour — et pas seulement en métriques de modèle. Une précision de 92 % ne dit rien à un directeur financier.
- **Distinguer le gain de temps du gain d'argent.** Vingt minutes économisées par personne et par jour ne deviennent une économie que si elles sont réaffectées ou si un poste ne se remplace pas. Le dire honnêtement vaut mieux que de se faire contredire.
- **Mesurer la simplification seule, avant toute IA.** Un processus qui passe de onze à six jours par suppression d'attentes et connexion de deux systèmes est un résultat acquis sans risque technique.
- **Le calcul se fait avec le contrôle de gestion**, avec ses conventions. Un chiffre produit par le seul prestataire est toujours suspect, et il a souvent raison de l'être.
- **Prévoir la mesure a posteriori**, à trois et six mois, avec les indicateurs définis au départ. C'est ce qui justifiera — ou non — la suite.

## Selon le métier

### Forward Deployed Engineer

Deux angles. La collecte se fait en phase d'audit ou jamais, parce qu'après le début du développement plus personne ne reconstitue la situation de référence. Et le calcul se fait **avec le contrôle de gestion du client**, avec ses conventions, sinon il ne sera pas repris — un chiffre produit par le prestataire seul ne survit pas à la première contestation.

### AI Product Builder

Le calcul se fait sur trois ans et inclut le **temps de reprise du code généré**, qui est la ligne systématiquement oubliée. La génération a tellement baissé le prix du premier jour qu'on construit désormais des choses qu'on aurait achetées, et dont on paiera la maintenance pendant cinq ans. Construire se justifie quand la fonction est le cœur de l'offre, quand les données ne peuvent pas sortir, ou quand le prix de l'abonnement croît plus vite que l'usage — trois raisons, pas quatre.

> [!warning] Piège
> Compter le gain sur le cas nominal et ignorer le traitement des exceptions. Un système qui traite correctement 80 % des dossiers laisse les 20 % restants à des humains qui doivent désormais aussi vérifier les 80 % automatisés. Le gain net peut être nul, voire négatif, tant que la sortie du système n'est pas fiable sans relecture.

## Pour aller plus loin

- [Project management triangle: Triple constraint guide — Asana](https://asana.com/resources/project-management-triangle) — le cadre d'arbitrage périmètre / délai / qualité, applicable tel quel.
- [The LLM Inference Trilemma: Throughput, Latency, Cost](https://www.digitalocean.com/blog/llm-inference-tradeoffs) — le versant coût variable, propre aux systèmes à base de modèle.

## Appelée par

- [[parcours/forward-deployed-engineer|Forward Deployed Engineer]]
- [[parcours/ai-product-builder|AI Product Builder]]

Voisines : [[notions/cadrage-besoin]], [[notions/cout-et-latence-inference]], [[notions/reingenierie-de-processus]], [[notions/mesure-d-usage-produit]].
