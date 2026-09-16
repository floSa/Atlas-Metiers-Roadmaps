---
title: Contraintes par secteur
---

Niveau attendu : **notion**. Reconnaître qu'un secteur impose ses propres règles suffit à ne pas se tromper de question ; le contenu s'acquiert sur place, en quelques jours.

La définition d'un taux de rotation des stocks s'apprend en trois jours dans l'entreprise concernée. Ce qui vaut d'être retenu, c'est que chaque domaine impose des **contraintes de modélisation** différentes, et ce sont elles qu'on doit reconnaître en arrivant sur un secteur nouveau.

| Secteur | Contrainte dominante | Ce qu'elle impose au modèle |
|---|---|---|
| Finance | immuabilité du passé | historisation stricte, calendrier fiscal, traçabilité jusqu'à la pièce |
| Commerce et e-commerce | multiplicité des grains | commande, ligne, expédition, retour, paiement : cinq faits distincts |
| Santé | sensibilité des données | pseudonymisation dès l'ingestion, cloisonnement, seuil d'agrégation |
| Industrie | volume et fréquence | agrégation à l'ingestion, conservation dégressive, temps réel découplé |

## Ce qu'il faut savoir faire

- En finance, garantir qu'un chiffre publié puisse être reproduit à l'identique dans deux ans. Une période comptable close ne bouge plus, et le reporting réglementaire ajoute une exigence d'auditabilité qui interdit les recalculs silencieux.
- Dans le commerce, ne jamais fusionner les cinq faits. Les fenêtres d'attribution — combien de jours après le clic — sont des décisions métier à documenter, pas des paramètres techniques, et la valeur vie client en dépend entièrement.
- En santé, traiter la donnée comme une catégorie particulière au sens du RGPD dès la conception. Les indicateurs d'efficience hospitalière sont par ailleurs très sensibles au codage des séjours, ce qui en fait un cas d'école de dépendance à la qualité de saisie.
- Dans l'industrie, séparer la surveillance temps réel — qui relève d'un autre outillage — de l'analyse décisionnelle. La maintenance prédictive est un projet d'apprentissage automatique, pas un tableau de bord ; le rôle du BI Analyst y est de fournir l'historique propre.
- Reconnaître le transverse : le reporting de conformité apparaît dans trois secteurs sur quatre, avec toujours la même exigence de reproductibilité et de piste d'audit.
- Situer la détection de fraude à part. Elle exige de la fraîcheur et un retour sur les cas confirmés, ce qui en fait un système opérationnel ; la BI y contribue par le suivi des taux et des faux positifs, pas par la détection.

## Les notions mobilisées

- [[notions/modelisation-dimensionnelle]] — les contraintes de secteur s'expriment toutes en décisions de modélisation.
- [[notions/rgpd]] — la donnée de santé et la donnée d'employé déplacent l'architecture entière.
- [[notions/donnees-sensibles]] — le seuil d'agrégation minimale et le cloisonnement des accès.
- [[notions/traitement-distribue]] — le volume de télémétrie industrielle, qui change la nature du stockage.
- [[notions/series-temporelles]] — la conservation dégressive suppose de savoir ce qu'on perd en agrégeant.

> [!warning] Piège
> Importer le modèle d'un secteur dans un autre. Les gabarits d'entrepôt sectoriels vendus comme accélérateurs imposent un grain et des dimensions conçus pour une autre organisation, et le temps passé à les tordre dépasse celui qu'aurait coûté un modèle conçu sur place. Ce qui se transfère, ce sont les **patrons** — grain fin, dimensions conformes, dimension de date, historisation — pas les schémas.

## Pour apprendre

- [Texte du RGPD](https://gdpr-info.eu/) — les catégories particulières de données, décisives en santé et en ressources humaines.
- [What is a Data Warehouse? — Google Cloud](https://cloud.google.com/learn/what-is-a-data-warehouse) — le cadre commun dans lequel ces contraintes s'expriment.
- [5 Principles of Data Ethics for Business](https://online.hbs.edu/blog/post/data-ethics) — sur le périmètre et l'usage, qui varient fortement selon le secteur.
