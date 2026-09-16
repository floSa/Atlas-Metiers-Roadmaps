---
title: Réseaux de neurones
tags: [notion, reseaux-de-neurones, deep-learning, machine-learning]
date: 2026-09-16
statut: actif
appelee-par: [data-analyst, ai-red-teaming]
---

Modèles composés de couches de transformations linéaires suivies de fonctions non linéaires, dont les paramètres sont ajustés par descente de gradient sur l'erreur observée.

## À quoi ça sert

Un réseau de neurones apprend une représentation au lieu de la recevoir. C'est tout l'écart avec les méthodes classiques : sur des données tabulaires, un humain construit les variables explicatives et le modèle les combine ; sur du texte, de l'image ou du son, personne ne sait écrire ces variables à la main, et c'est précisément là que les réseaux sont irremplaçables.

La contrepartie est un besoin massif de données, de calcul et de réglage, pour un résultat difficile à expliquer. D'où une règle qui tient toujours en 2026 : **sur données tabulaires, un modèle à base d'arbres bien réglé reste à l'état de l'art**. Le deep learning se justifie sur texte, image et son, pas sur un fichier de clients.

Il faut enfin connaître le mécanisme pour une raison indirecte : c'est l'architecture qui sous-tend les modèles de langage que tout le monde utilise, et elle explique leurs comportements — la sensibilité à de petites perturbations, la mémorisation d'exemples d'entraînement, l'absence de frontière nette entre fonctionnement normal et détourné.

## Ce qu'il faut savoir

- **Le mécanisme** : couches de poids, fonction d'activation non linéaire, fonction de perte, rétropropagation du gradient, descente de gradient stochastique. Sans la non-linéarité, un empilement de couches reste une régression linéaire.
- **Les familles** : les réseaux convolutifs pour l'image, les récurrents pour le séquentiel (largement supplantés), les transformeurs fondés sur l'attention pour le texte et, désormais, presque tout le reste.
- **Le surapprentissage est la norme**, pas l'exception. Régularisation, abandon de neurones (*dropout*), arrêt précoce, augmentation de données sont des composants du dispositif, pas des options.
- **Le coût est d'abord un coût de données étiquetées**, ensuite un coût de calcul. C'est ce qui rend l'affinage d'un modèle pré-entraîné presque toujours préférable à un entraînement depuis zéro.
- **L'explicabilité est faible et les méthodes post hoc sont fragiles.** Dans un contexte où la décision doit être justifiée à une personne concernée, c'est un critère de choix, pas un détail.
- **La mémorisation est réelle** : un réseau entraîné sur des données sensibles peut en restituer des fragments. Ce n'est pas un incident, c'est une propriété du surapprentissage.
- **La sensibilité aux perturbations** : une modification imperceptible de l'entrée peut changer la sortie. Elle découle du fait que la frontière de décision apprise est une approximation, pas une règle.

## Selon le métier

### Data Analyst

Sur données tabulaires, qui sont le quotidien du métier, le deep learning n'apporte rien qu'un modèle à base d'arbres ne fasse mieux, plus vite et de façon explicable. Le seul volet qui touche réellement l'analyste est le traitement du langage sur les verbatims clients — et depuis 2024, un appel à un modèle de langage fait ce travail sans entraînement préalable. Voir [[notions/traitement-langage-naturel]].

### AI Red Teaming

L'accès aux gradients change tout. En boîte blanche, on construit une perturbation ciblée par optimisation directe sur l'entrée ; en boîte noire, on se rabat sur la recherche et sur la transférabilité — une perturbation trouvée sur un modèle en trompe souvent un autre entraîné sur des données voisines. La mémorisation est l'autre surface : elle rend l'inférence d'appartenance et la reconstruction de données d'entraînement réalistes.

> [!warning] Piège
> Choisir un réseau de neurones pour un problème tabulaire parce que c'est ce dont on parle. Le résultat est un modèle plus long à entraîner, plus difficile à expliquer, plus fragile à la dérive et généralement moins performant qu'un gradient boosting réglé en une après-midi. La justification « on aura besoin de scalabilité plus tard » ne s'est presque jamais vérifiée.

## Pour aller plus loin

- [Introduction to Deep Learning — IBM](https://www.ibm.com/topics/deep-learning) — le cadrage, sans mathématiques.
- [Neural networks: Activation functions — Google Developers](https://developers.google.com/machine-learning/crash-course/neural-networks/activation-functions) — le point qui fait la différence entre un réseau et une régression.
- [Neural network models — scikit-learn](https://scikit-learn.org/stable/modules/neural_networks_supervised.html) — l'implémentation minimale, utile pour expérimenter sans infrastructure.

## Appelée par

- [[parcours/data-analyst|Data Analyst]]
- [[parcours/ai-red-teaming/index|AI Red Teaming]]

Voisines : [[notions/apprentissage-supervise]], [[notions/traitement-langage-naturel]], [[notions/affinage-de-modele]].
