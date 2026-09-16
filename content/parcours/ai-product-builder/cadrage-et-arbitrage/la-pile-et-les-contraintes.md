---
title: La pile et les contraintes
---

Niveau attendu : **usage**. On prend la pile la plus répandue et on écrit trois contraintes : le chemin est balisé, et s'en écarter coûte plus cher que le gain espéré.

Une contrainte se pose **avant** de générer, jamais après. Trois lignes écrites au cadrage — volume attendu, données personnelles manipulées, budget mensuel — déterminent l'hébergement et évitent de découvrir le problème le jour de la mise en ligne.

```mermaid
flowchart TD
  P["Le niveau de prise en charge visé<br/>ce qu'on n'aura pas à configurer"]
  D["Les dépendances de la pile<br/>ce qu'on exécute sans l'avoir écrit"]
  R["Les données personnelles<br/>elles décident de l'hébergement"]
  S["La sensibilité des données<br/>ce qui n'a pas le droit de sortir"]

  click P "/notions/plateforme-de-deploiement"
  click D "/notions/chaine-d-approvisionnement-logicielle"
  click R "/notions/rgpd"
  click S "/notions/donnees-sensibles"
```

## Ce qu'il faut savoir faire

- Choisir une pile **très répandue**, pas la meilleure. Le générateur reproduit ce qu'il a vu massivement ; sur une pile de niche il invente des APIs qui n'existent pas, avec le même aplomb.
- Distinguer « pile populaire » de « pile que je connais ». Ce sont deux critères différents et le premier prime quand on délègue la génération : le coût de relecture d'une pile très documentée est plus faible que le coût de débogage d'un code plausible et inexistant.
- Écrire le volume attendu en ordre de grandeur, pas en ambition. Douze utilisateurs le premier mois n'appellent pas la même infrastructure que douze mille, et c'est presque toujours le premier chiffre.
- Recenser les données personnelles manipulées dès le cadrage : lesquelles, pour quelle finalité, combien de temps. C'est la ligne qui interdira certaines dorsales gérées et qui est impossible à rattraper après migration.
- Poser un budget mensuel d'hébergement chiffré. Il sert de critère de sélection à l'étage mise en ligne, et d'alerte de dépense le jour de la mise en production.
- Fixer la pile dans le fichier de cadrage et la rappeler à chaque outil. Sans cela, deux générations successives produisent deux piles et un assemblage impossible à maintenir.

## Les notions mobilisées

- [[notions/plateforme-de-deploiement]] — la contrainte la plus dure du cadrage décide du niveau de prise en charge, et pour un premier produit c'est presque toujours le budget ou le délai.
- [[notions/chaine-d-approvisionnement-logicielle]] — une pile très répandue est aussi une pile dont les dépendances sont maintenues ; l'inverse se paie en correctifs qu'on écrit soi-même.
- [[notions/rgpd]] — pour ce métier le piège concret est la dorsale gérée dont les données résident hors Union européenne, choisie en trois clics et impossible à déplacer ensuite.
- [[notions/donnees-sensibles]] — la classification décide de ce qui peut passer par un service tiers, et par un générateur hébergé.

> [!warning] Piège
> Dimensionner sur la charge imaginée. Le « au cas où ça décolle » fait perdre des semaines à un produit qui aura douze utilisateurs, et la migration vers une infrastructure plus lourde — quand elle devient nécessaire — se fait en connaissant enfin le profil de charge réel. C'est plus rapide dans cet ordre.

## Pour apprendre

- [The Best Tech Stack in the Age of AI](https://thebootstrappedfounder.com/the-best-tech-stack-in-the-age-of-ai/) — l'argument complet en faveur de la pile très répandue plutôt que de la pile élégante.
