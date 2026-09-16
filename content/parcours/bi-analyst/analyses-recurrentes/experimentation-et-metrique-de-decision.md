---
title: Expérimentation
---

Le BI Analyst est rarement celui qui conçoit le test, souvent celui qui produit la mesure sur laquelle il sera tranché. C'est une position qui a ses exigences propres, et elles se posent avant le début du test.

```mermaid
flowchart LR
  D["Métrique de décision<br/>définie avant le test"] --> U["Une seule métrique primaire"]
  U --> T["Test lancé<br/>durée fixée à l'avance"]
  T --> L["Lecture à l'échéance<br/>pas de relecture quotidienne"]
  L --> R["Décision"]
```

## Ce qu'il faut savoir faire

- Définir la métrique de décision **avant** le début du test, et la consigner. Une métrique choisie après coup transforme une expérience en recherche de justification.
- N'admettre qu'une seule métrique primaire. Les autres sont des garde-fous — on vérifie qu'elles ne se dégradent pas — mais elles ne décident pas, sinon toute expérience finit par trouver un chiffre favorable.
- Refuser la relecture quotidienne avec arrêt dès que l'écart est favorable. C'est la pratique qui fabrique le plus de conclusions fausses, et elle est presque toujours proposée de bonne foi.
- Fixer la durée à l'avance en tenant compte des cycles : une semaine complète au minimum, pour ne pas mesurer un effet de jour de semaine, et davantage si l'activité est saisonnière.
- Fournir le protocole de mesure autant que le chiffre : population incluse, exclusions, période, mode d'affectation. Sans ces quatre éléments, le résultat n'est pas reproductible, donc pas défendable.
- Distinguer une expérimentation d'une comparaison avant/après. La seconde est presque toujours polluée par la saisonnalité et par les autres actions menées en même temps ; le dire au moment où on la demande est plus utile qu'après.

## Les notions mobilisées

- [[notions/ab-testing]] — le protocole, les métriques de ratio et la sensibilité ; ici, le rôle de celui qui produit la mesure.
- [[notions/tests-hypotheses]] — la p-value, la puissance et les deux types d'erreur, indispensables pour dire ce qui est conclu.
- [[notions/analyse-correlation]] — la différence entre un écart observé et un effet attribuable à l'action.
- [[notions/statistiques-descriptives]] — la dispersion, qui détermine la taille d'échantillon nécessaire.

> [!tip] La phrase qui protège tout le monde
> « La métrique primaire est celle-ci, le test dure jusqu'à cette date, et nous la lirons à ce moment-là. » Écrite avant le lancement et envoyée aux parties prenantes, elle évite la conversation où chacun relit les résultats à sa convenance — et elle évite surtout d'avoir à la refuser sur le moment.

## Pour apprendre

- [A Refresher on A/B Testing — HBR](https://hbr.org/2017/06/a-refresher-on-ab-testing) — le rappel de protocole à relire avant tout test.
- [Type I and Type II Errors — Scribbr](https://www.scribbr.com/statistics/type-i-and-type-ii-errors/) — ce que l'arrêt anticipé fait exactement aux taux d'erreur.
- [Statistical Tests — Scribbr](https://www.scribbr.com/statistics/statistical-tests/) — comment choisir le test correspondant à la métrique retenue.
