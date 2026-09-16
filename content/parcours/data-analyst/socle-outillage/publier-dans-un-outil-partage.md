---
title: Publier dans un outil partagé
---

Power BI, Tableau, Looker, Metabase : l'analyste les consomme et y publie parfois. Les construire, les gouverner et y porter les définitions partagées est un autre métier — savoir où passe la frontière évite d'hériter d'un parc de rapports à maintenir.

```mermaid
flowchart TD
  C["Outils décisionnels<br/>ce qu'on achète : la distribution"]
  V["Visualisation de données<br/>le graphique se choisit avant l'outil"]
  S["Modélisation dimensionnelle<br/>la couche que l'analyste consomme"]
  B["BI Analyst<br/>le métier qui construit et gouverne"]

  click C "/notions/outils-decisionnels"
  click V "/notions/visualisation-de-donnees"
  click S "/notions/modelisation-dimensionnelle"
  click B "/parcours/bi-analyst/"
```

## Ce qu'il faut savoir faire

- Se connecter à une source, construire une vue et la publier pour un cercle restreint — le geste courant quand une analyse doit rester consultable quelques semaines.
- Lire un modèle existant avant d'y ajouter quoi que ce soit : quelles tables, quelle granularité, quelles mesures déjà définies. Recréer une mesure qui existe déjà est la première cause de deux chiffres divergents dans la même entreprise.
- Savoir reconnaître la demande qui n'est pas une analyse : « tout le monde doit pouvoir suivre ça » est une commande de suivi récurrent, elle se transmet, elle ne se bricole pas.
- Refuser d'être le mainteneur implicite d'un rapport publié à la hâte. Un rapport sans propriétaire dérive, et c'est celui qui l'a créé qu'on rappelle deux ans plus tard.
- Poser la question des droits avant la publication : qui voit quelles lignes. Un tableau de bord qui expose des données de paie ou de santé à un cercle mal défini est un incident, pas une maladresse.

## Les notions mobilisées

- [[notions/outils-decisionnels]] — ce qu'on achète n'est pas le graphique mais la distribution : un chiffre rafraîchi seul, identique pour tout le monde.
- [[notions/visualisation-de-donnees]] — le choix du graphique est indépendant de l'outil, et se décide avant d'ouvrir celui-ci.
- [[notions/modelisation-dimensionnelle]] — la couche que l'analyste consomme sans la construire : en comprendre la granularité suffit à ne pas la contourner.
- [[notions/controle-d-acces]] — la propagation des droits jusqu'à la ligne, le point que les publications rapides oublient.

> [!tip] Le test de la commande
> Demander qui consultera l'objet, à quelle fréquence, et qui le corrigera quand il cassera. Trois réponses nettes : c'est un produit décisionnel, il se commande à [[parcours/bi-analyst/index|Bi Analyst]]. Trois réponses floues : c'est une analyse ponctuelle, elle se livre en document et se range.

## Pour apprendre

- [Metabase](https://github.com/metabase/metabase) — le plus simple à mettre entre les mains d'un métier, déployable en une soirée : le meilleur cours sur le fonctionnement interne de ces outils.
- [Apache Superset](https://github.com/apache/superset) — le plus complet côté modélisation et droits, pour voir ce que les éditeurs facturent.
- [Visual Best Practices](https://help.tableau.com/current/blueprint/en-us/bp_visual_best_practices.htm) — la check-list avant publication, indépendante de l'outil malgré la source.
- [Power BI — Documentation](https://learn.microsoft.com/fr-fr/power-bi/) — l'outil le plus répandu en entreprise francophone ; lire la partie modèle sémantique avant la partie graphique.
