---
title: Du besoin à la métrique
---

Entendre « je veux le chiffre d'affaires » et demander *hors taxes ou TTC, à la commande ou à la facturation, net des avoirs ou brut, à la date de signature ou de livraison*. Les quatre réponses définissent quatre métriques différentes, et les quatre existent déjà quelque part dans l'entreprise.

```mermaid
flowchart TD
  CA["Cadrage du besoin<br/>le recueil et la reformulation"]
  GP["Gestion des parties prenantes<br/>qui décide, qui subit, qui est évalué"]
  RO["ROI des projets<br/>quelle décision change selon le chiffre"]
  ST["Statistiques descriptives<br/>ce qu'une métrique dit et ne dit pas"]

  click CA "/notions/cadrage-besoin"
  click GP "/notions/gestion-parties-prenantes"
  click RO "/notions/roi-des-projets-ia"
  click ST "/notions/statistiques-descriptives"
```

## Ce qu'il faut savoir faire

- Distinguer une métrique d'un KPI. Le trafic d'un site est une métrique ; le taux de conversion adossé à un objectif trimestriel est un KPI. La différence n'est pas dans le calcul mais dans le fait qu'un KPI a un propriétaire et une cible. Une organisation avec quarante KPI n'en a aucun.
- Poser systématiquement la question qui élimine les tableaux de bord morts : « quelle décision prendras-tu différemment selon ce que tu y verras ». Si la réponse est « aucune », l'objet sera consulté trois fois, abandonné, et maintenu quand même.
- Reconnaître que chaque fonction métier a sa maille et son calendrier. La finance travaille en périodes comptables closes et refuse qu'un chiffre passé bouge ; le marketing travaille en fenêtres d'attribution glissantes et accepte que le chiffre d'hier soit révisé demain. Ces deux exigences sont contradictoires : elles se modélisent séparément, jamais en moyenne.
- Séparer le sponsor de l'utilisateur. Celui qui finance regarde trois chiffres par mois, celui qui s'en sert en regarde trente par jour. Concevoir pour le premier donne un tableau de bord que personne n'ouvre.
- Traduire une demande formulée en solution (« il me faut un tableau de bord des ventes ») en spécification de mesure. En BI, la spécification porte sur une **définition**, pas sur une fonctionnalité — c'est ce qui distingue ce cadrage de celui d'un projet logiciel.
- Repérer, avant la réunion, la ligne de fracture politique : celui qui pilote veut une définition stable, celui qui est évalué veut celle qui l'avantage. L'arbitrage se prépare, il ne s'improvise pas devant les deux parties.

## Les notions mobilisées

- [[notions/cadrage-besoin]] — le recueil et la reformulation, ici appliqués à une définition de mesure plutôt qu'à une fonctionnalité.
- [[notions/gestion-parties-prenantes]] — cartographier qui décide, qui subit et qui est évalué par le chiffre, avant de l'écrire.
- [[notions/roi-des-projets-ia]] — sans décision associée, une métrique n'a pas de valeur mesurable, seulement un coût de maintenance.
- [[notions/statistiques-descriptives]] — savoir ce qu'une moyenne, une médiane ou un taux racontent réellement du phénomène mesuré.

> [!warning] Piège
> Accepter la demande telle qu'elle est formulée. Une demande arrive presque toujours sous forme de solution supposée, et la reformuler n'est pas de la procédure : c'est la seule occasion de découvrir que trois services appellent « chiffre d'affaires » trois choses différentes, avant que le modèle ne grave l'une des trois.

## Pour apprendre

- [Requirements Gathering and Management — Jama](https://www.jamasoftware.com/requirements-management-guide/requirements-gathering-and-management-processes/what-is-requirements-gathering/) — la mécanique du recueil, transposable telle quelle à une définition de mesure.
- [Requirements Gathering in Business Analysis — Coursera](https://www.coursera.org/learn/requirements-gathering-in-business-analysis) — cours gratuit à l'audit, centré sur l'entretien et la reformulation.
- [Stakeholder Management Guide](https://simplystakeholders.com/resources/guides/stakeholder-management/) — la cartographie influence/intérêt, à faire avant d'arbitrer une définition.
