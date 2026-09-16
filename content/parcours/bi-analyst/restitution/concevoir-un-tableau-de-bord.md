---
title: Concevoir un tableau de bord
---

Le choix du graphique se déduit de la question, pas du goût. Comparer des catégories appelle des barres, suivre dans le temps appelle une courbe, montrer une distribution appelle un histogramme, chercher une relation appelle un nuage de points.

```mermaid
flowchart TD
  VD["Visualisation de données<br/>choix du graphique, lisibilité, erreurs classiques"]
  ST["Statistiques descriptives<br/>ce qu'une moyenne cache"]
  TB["Tableur<br/>l'export qui suivra, à cadrer"]
  RT["Rédaction technique<br/>les libellés, qui font la moitié du travail"]

  click VD "/notions/visualisation-de-donnees"
  click ST "/notions/statistiques-descriptives"
  click TB "/notions/tableur"
  click RT "/notions/redaction-technique"
```

## Ce qu'il faut savoir faire

- Éliminer par principe les deux erreurs récurrentes : le camembert au-delà de trois parts, et le second axe vertical. Elles ne se justifient jamais assez pour valoir l'ambiguïté qu'elles introduisent.
- Ne jamais faire porter l'information par la seule couleur, vérifier les palettes contre les daltonismes et garder un contraste suffisant. Autour de 8 % des hommes sont concernés par une déficience de perception des rouges et des verts, ce qui est beaucoup dans une audience de direction.
- Structurer la page : trois à cinq chiffres en haut, le détail en dessous, un filtre par défaut qui correspond à l'usage dominant. Un tableau de bord qui exige six sélections avant d'afficher quelque chose ne sera pas utilisé.
- Afficher la médiane et un quantile haut plutôt que la moyenne seule sur toute distribution asymétrique. Le délai de livraison moyen de trois jours cache mal 20 % de livraisons à dix jours, et ce sont elles qui produisent les réclamations.
- Ne concevoir une version mobile que si l'usage est réellement mobile, et alors la concevoir séparément. Un tableau de bord dense rétréci sur un téléphone est illisible, et le compromis automatique donne le pire des deux.
- Refuser les graphiques trompeurs, y compris quand la demande vient d'en haut. Axe tronqué, échelles incohérentes entre deux graphiques côte à côte, période sélectionnée pour avantager une conclusion : c'est souvent le BI Analyst qu'on sollicite pour « mieux présenter » un chiffre décevant, et savoir dire non fait partie du métier.

## Les notions mobilisées

- [[notions/visualisation-de-donnees]] — la grammaire du graphique et les erreurs classiques, expliquées une fois pour tous les métiers.
- [[notions/statistiques-descriptives]] — la dispersion, sans laquelle une moyenne publiée est une information incomplète.
- [[notions/tableur]] — l'export est la suite naturelle de la consultation ; autant le prévoir propre.
- [[notions/redaction-technique]] — un libellé compréhensible par le métier fait plus pour la qualité perçue que trois tests.

> [!warning] Piège
> Afficher des flèches vertes et rouges sur des variations non significatives. « Les ventes ont baissé de 4 % » ne veut rien dire tant qu'on ne sait pas que la variation hebdomadaire courante est de plus ou moins 6 %. Le tableau de bord fabrique alors de la réaction là où il n'y a rien à décider, et finit par être ignoré — y compris le jour où la variation compte.

## Pour apprendre

- [Fundamentals of Data Visualization](https://clauswilke.com/dataviz/introduction.html) — libre et en ligne ; les parties sur les couleurs et les échelles sont les plus utiles.
- [The Data Visualisation Catalogue](https://datavizcatalogue.com/) — pour choisir un type de graphique en partant de la question posée.
- [10 Guidelines for DataViz Accessibility](https://www.highcharts.com/blog/best-practices/10-guidelines-for-dataviz-accessibility/) — la liste à passer avant publication.
- [How To Spot Misleading Charts](https://www.tableau.com/blog/how-spot-misleading-charts-check-axes) — utile dans les deux sens : détecter, et ne pas produire.
