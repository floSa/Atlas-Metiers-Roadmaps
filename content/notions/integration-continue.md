---
title: Intégration continue
tags: [notion, integration-continue, ci-cd, livraison, ingenierie]
date: 2026-09-16
statut: actif
appelee-par: [forward-deployed-engineer, ai-product-builder, ai-red-teaming]
---

Pratique consistant à fusionner fréquemment le travail dans une branche commune, en faisant exécuter automatiquement, à chaque fusion, la chaîne de vérifications qui décide si le résultat est livrable.

## À quoi ça sert

L'intégration continue résout un problème de coût d'erreur : plus un défaut vit longtemps, plus il coûte cher à corriger, parce que d'autres travaux se sont construits dessus. En rapprochant la vérification de l'écriture, on ramène le coût de la correction à quelques minutes.

Son second effet est moins technique et plus décisif : elle déplace la définition de « fini ». Ce qui est fini n'est plus ce qui marche sur le poste de son auteur, c'est ce qui passe une chaîne que personne ne peut contourner. C'est ce qui rend une exigence — un seuil de qualité, une absence de vulnérabilité connue, un jeu d'évaluation au-dessus d'un score — réellement opposable, au lieu d'être une bonne intention.

Sur un système à base de modèle, elle prend un rôle supplémentaire : c'est le seul endroit où l'on peut rejouer automatiquement une évaluation à chaque changement de prompt, de modèle ou de corpus.

## Ce qu'il faut savoir

- **La chaîne minimale** : construction, tests, analyse statique, vérification des dépendances, construction de l'artefact, publication. Ajouter le reste ensuite, pas avant.
- **Rapide ou ignorée.** Au-delà de dix minutes, les gens contournent. Séparer une chaîne courte à chaque poussée d'une chaîne longue nocturne est le compromis usuel.
- **Déterministe.** Un test instable coûte plus qu'il ne rapporte : il apprend à l'équipe à relancer sans lire. Réparer ou supprimer, pas tolérer.
- **Intégration continue ≠ déploiement continu.** La première vérifie, la seconde met en production automatiquement. On adopte la première partout, la seconde quand le retour arrière est sûr.
- **Les secrets ne sont pas dans le dépôt.** Coffre à secrets, injection au moment de l'exécution, rotation. Une clé d'API dans l'historique reste dans l'historique.
- **L'environnement de prévisualisation par branche** est le gain le plus sous-estimé : il transforme une idée en lien cliquable à envoyer à trois personnes.
- **Ce qui bloque doit être justifié.** Un seuil bloquant a un propriétaire et une raison écrite, sinon il est désactivé à la première urgence et ne revient jamais.
- **Reproductibilité** : versions figées, image de base épinglée, construction qui ne dépend pas d'un service extérieur susceptible de disparaître.

## Selon le métier

### Forward Deployed Engineer

La chaîne de livraison doit tourner sur **l'outillage du client** — GitLab interne, Jenkins vieillissant ou autre — dès le premier jour. Une chaîne construite sur un service que le client n'utilise pas est inutilisable dès la fin de mission, quelle que soit sa qualité. C'est aussi là que le protocole d'évaluation est rejoué automatiquement, ce qui le rend durable au-delà de la présence du FDE.

### AI Product Builder

L'usage ici est moins la qualité que la **vitesse de retour** : un environnement de prévisualisation par branche transforme chaque idée en lien à envoyer à trois utilisateurs. Sur une base de code partiellement générée, la chaîne joue un second rôle — elle est le garde-corps qui empêche un assistant de casser en silence ce qu'il ne comprend pas.

### AI Red Teaming

Le corpus d'attaques tourne à chaque changement de prompt, de modèle, de version d'outil ou de politique de filtrage, avec un seuil bloquant. Même logique que les tests de non-régression fonctionnels : c'est ce qui transforme un audit ponctuel en posture de sécurité suivie, et ce qui détecte qu'une atténuation a été désactivée.

> [!warning] Piège
> Livrer en production depuis le poste local, « le temps de démarrer ». L'habitude ne se défait plus une fois prise, et elle supprime la seule trace qui permettrait de savoir ce qui tourne réellement. Le premier déploiement automatisé coûte une demi-journée au démarrage et une semaine six mois plus tard.

## Pour aller plus loin

- [What is CI/CD? — GitLab](https://about.gitlab.com/topics/ci-cd/) — le cadrage des trois notions et de leurs différences.
- [Continuous Integration vs Delivery vs Deployment](https://www.guru99.com/continuous-integration-vs-delivery-vs-deployment.html) — la distinction que tout le monde confond, expliquée simplement.
- [GitHub Actions — documentation](https://docs.github.com/en/actions) — la mise en œuvre la plus répandue.

## Appelée par

- [[parcours/forward-deployed-engineer/index|Forward Deployed Engineer]]
- [[parcours/ai-product-builder|AI Product Builder]]
- [[parcours/ai-red-teaming/index|AI Red Teaming]]

Voisines : [[notions/tests-logiciels]], [[notions/conteneurisation]], [[notions/evaluation-llm]], [[notions/plateforme-de-deploiement]].
