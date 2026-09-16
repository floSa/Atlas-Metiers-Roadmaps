---
tags: [notion, tests, qualite-logicielle, ingenierie]
date: 2026-09-16
statut: actif
appelee-par: [forward-deployed-engineer, ai-product-builder, ai-red-teaming]
---

# Tests logiciels

Code écrit pour vérifier automatiquement qu'un autre code fait ce qu'on attend de lui, et continuera de le faire après avoir été modifié.

## À quoi ça sert

Un test ne sert pas à prouver que le code est juste — il sert à rendre le changement possible. Sans tests, modifier un système revient à parier ; avec des tests, c'est une opération dont on connaît le résultat en quelques secondes. C'est pour cette raison que la valeur d'une suite de tests se mesure à la fréquence des modifications, pas à la criticité du code.

Le deuxième usage est documentaire, et il est sous-estimé : un test est la seule documentation qui échoue quand elle ment. Une spécification vieillit en silence, un test vieillit bruyamment.

Le troisième usage est récent : sur une base de code partiellement produite par une machine, les tests sont le seul retour d'exécution qui empêche un assistant de casser en silence ce qu'il ne comprend pas.

## Ce qu'il faut savoir

- **La pyramide reste valable** : beaucoup de tests unitaires rapides, moins de tests d'intégration, quelques tests de bout en bout. Inverser la proportion donne une suite lente et instable qu'on finit par ignorer.
- **Unitaire** : une fonction, sans base ni réseau, en millisecondes. **Intégration** : les composants réels ensemble, y compris la base. **Bout en bout** : le parcours complet, du point de vue de l'utilisateur.
- **Test de non-régression** : le test écrit en réponse à un défaut constaté. C'est le meilleur rapport valeur sur effort de tout le sujet, parce qu'il porte sur une défaillance avérée et non supposée.
- **Le test décrit un comportement, pas une implémentation.** Un test qui casse à chaque refactorisation sans qu'aucun comportement n'ait changé est un frein déguisé en filet.
- **La couverture est un indicateur, pas un objectif.** Cent pour cent de lignes couvertes par des tests qui n'assertent rien ne garantit rien. Regarder plutôt ce qui n'est pas couvert et décider si c'est acceptable.
- **Les données de test sont du code** : jeux figés, pas de dépendance à l'état d'une base partagée, pas de test qui passe le lundi et échoue le 31 du mois.
- **Sur les systèmes non déterministes**, les tests classiques restent valables pour tout ce qui entoure le modèle — parsing, routage, gestion d'erreur, contrats. Le comportement du modèle lui-même relève de [[notions/evaluation-llm]], qui est une autre discipline avec d'autres critères.

## Selon le métier

### Forward Deployed Engineer

Les tests sont la seule documentation que le client relira, parce qu'elle échoue quand elle ment. C'est l'argument à donner quand on demande du temps pour les écrire en mission : ils ne sont pas un luxe d'ingénieur, ils sont ce qui permet à l'équipe du client de modifier le système sans son auteur.

### AI Product Builder

Les tests ne servent pas d'abord à prouver la justesse, ils servent de garde-corps aux modifications automatisées. Cela change ce qu'il faut couvrir en priorité : **les parcours, pas les fonctions**. Trois tests de bout en bout sur les chemins critiques valent mieux que cinquante tests unitaires sur du code généré qui sera régénéré.

### AI Red Teaming

La simulation structurée — objectif, périmètre et règles d'engagement écrits — reste l'exercice le plus proche du réel, et une part du travail restera toujours du script maison : aucune plateforme ne connaît le schéma de données métier du client. Les tests d'attaque suivent les mêmes règles que les autres : reproductibles, versionnés, rejoués.

> [!warning] Piège
> Tester ce qui est facile à tester. Les fonctions pures et sans effet de bord se couvrent en dix minutes et ne tombent jamais en panne ; l'intégration avec le système patrimonial, la gestion du cas où le service externe ne répond pas, et la reprise après échec partiel sont ce qui casse en production et ce qui n'est presque jamais couvert.

## Pour aller plus loin

- [Automation Testing vs. Manual Testing](https://www.opkey.com/blog/automation-testing-vs-manual-testing-which-is-better) — où placer la frontière, question plus utile qu'il n'y paraît.
- [Adversarial Testing for Generative AI — Google](https://developers.google.com/machine-learning/guides/adv-testing) — la transposition des pratiques de test au non déterministe.
- [LLM red teaming guide — promptfoo](https://www.promptfoo.dev/docs/red-team/) — l'outillage de test adverse, documenté en open source.

## Appelée par

- [[parcours/forward-deployed-engineer|Forward Deployed Engineer]]
- [[parcours/ai-product-builder|AI Product Builder]]
- [[parcours/ai-red-teaming|AI Red Teaming]]

Voisines : [[notions/integration-continue]], [[notions/evaluation-llm]], [[notions/conception-d-api]].
