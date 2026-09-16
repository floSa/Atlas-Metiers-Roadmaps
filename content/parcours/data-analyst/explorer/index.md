---
title: Explorer
aliases:
  - parcours/data-analyst/explorer
---

Le moment où l'on découvre ce que la donnée contient réellement, par opposition à ce que le dictionnaire prétend. L'exploration ne sert pas à trouver la réponse : elle sert à vérifier que la question tient, et à produire la liste des hypothèses à tester.

## Les quatre sujets

```mermaid
flowchart TD
  O["L'ordre du premier regard<br/>volumétrie, remplissage, distributions, croisements"]
  D["La distribution avant la moyenne<br/>une moyenne décrit parfois personne"]
  S["Segmenter avant d'agréger<br/>l'agrégat masque deux populations"]
  H["La liste d'hypothèses<br/>ce qu'on s'attend à observer si elle est vraie"]

  click O "/parcours/data-analyst/explorer/l-ordre-du-premier-regard"
  click D "/parcours/data-analyst/explorer/la-distribution-avant-la-moyenne"
  click S "/parcours/data-analyst/explorer/segmenter-avant-d-agreger"
  click H "/parcours/data-analyst/explorer/la-liste-d-hypotheses"
```

**Porte de sortie** : une liste d'hypothèses écrite, et aucune conclusion tirée de l'exploration elle-même.

## Ma progression

- [ ] [[parcours/data-analyst/explorer/l-ordre-du-premier-regard|L'ordre du premier regard]] — la séquence qui fait gagner une journée
- [ ] [[parcours/data-analyst/explorer/la-distribution-avant-la-moyenne|La distribution avant la moyenne]] — médiane et quartiles par défaut sur montants et délais
- [ ] [[parcours/data-analyst/explorer/segmenter-avant-d-agreger|Segmenter avant d'agréger]] — le contrôle le moins cher et le plus rentable du métier
- [ ] [[parcours/data-analyst/explorer/la-liste-d-hypotheses|La liste d'hypothèses]] — ce qui rend l'étape suivante honnête
