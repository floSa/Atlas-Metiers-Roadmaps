---
title: Choisir un outil de prototypage
---

Trois catégories qu'on confond, et un seul critère de choix qui compte : le prototype est-il jetable, ou est-il le début du produit ?

```mermaid
flowchart TD
  A["Les outils qui écrivent le code<br/>et ce qu'on en fait ensuite"]
  C["Le cadrage donné en entrée<br/>la qualité de sortie en dépend"]
  D["Les dépendances embarquées<br/>ce que le prototype traîne avec lui"]
  P["La destination du code<br/>exportable ou prisonnier"]

  click A "/notions/assistants-de-codage"
  click C "/notions/cadrage-besoin"
  click D "/notions/chaine-d-approvisionnement-logicielle"
  click P "/notions/plateforme-de-deploiement"
```

## Ce qu'il faut savoir faire

- Distinguer le **générateur d'application** — il part d'une description et produit une application complète et hébergée, front et dorsale, prête à cliquer — du **générateur d'interface**, qui produit un composant ou un écran à intégrer dans un projet existant. Le premier valide un parcours, le second accélère une intégration.
- Ne pas écarter la **maquette statique classique**. Dessiner reste plus rapide pour explorer dix dispositions d'écran ; générer est plus rapide pour valider un enchaînement. Ce sont deux usages, pas deux générations d'outils.
- Choisir sur la destination, pas sur la qualité du code produit : si le prototype est jetable, prendre le plus rapide ; s'il doit survivre, prendre celui dont on peut exporter le code dans son dépôt et le lire.
- Vérifier avant de s'engager que l'export existe réellement et donne un dépôt qui se construit hors de la plateforme. C'est la question qui décide si le prototype deviendra une dette ou une base.
- Donner le fichier de cadrage en contexte à l'outil plutôt que de le reformuler dans une conversation. Une description tapée à la volée produit un produit légèrement différent à chaque essai.
- Considérer les noms d'outils comme interchangeables et la catégorie comme stable : le produit qui remplacera celui d'aujourd'hui occupera la même case et se choisira avec le même critère.

## Les notions mobilisées

- [[notions/assistants-de-codage]] — l'angle de ce métier est que l'outil de prototypage et l'assistant de reprise ne se choisissent pas sur les mêmes critères, alors qu'ils font la même chose techniquement.
- [[notions/cadrage-besoin]] — la sortie d'un générateur vaut son énoncé ; c'est le seul levier de qualité réellement sous contrôle.
- [[notions/chaine-d-approvisionnement-logicielle]] — un prototype exporté arrive avec un jeu de dépendances choisi par la plateforme, qu'il faudra assumer ou remplacer.
- [[notions/plateforme-de-deploiement]] — un prototype hébergé par son générateur est un hébergement de fait, avec son plafond et sa facture.

## Pour apprendre

- [Lovable](https://docs.lovable.dev/introduction/welcome), [Bolt](https://support.bolt.new/) et [Replit](https://docs.replit.com/getting-started/intro-replit) — les trois générateurs d'application les plus utilisés ; lire la page sur l'export du code avant le reste.
- [v0](https://v0.app/docs) — le représentant de la catégorie générateur d'interface, à comparer avec les précédents pour sentir la différence d'usage.
- [Roadmap vibe-coding](https://roadmap.sh/vibe-coding) — le versant pratique du sujet, utile pour la mécanique d'itération sur un prototype.
