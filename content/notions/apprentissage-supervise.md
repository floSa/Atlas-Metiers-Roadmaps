---
title: Apprentissage supervisé
tags: [notion, machine-learning, apprentissage-supervise, classification, regression]
date: 2026-09-16
statut: actif
appelee-par: [data-analyst, bi-analyst, ai-red-teaming]
---

Famille de méthodes qui apprennent une fonction reliant des variables d'entrée à une étiquette connue, à partir d'exemples déjà étiquetés, dans le but de prédire cette étiquette sur des cas nouveaux.

## À quoi ça sert

Le supervisé répond à une question précise : « à partir de ce que je sais d'un cas, que vaut probablement la chose que je ne sais pas encore ? » — ce client va-t-il résilier, cette facture sera-t-elle impayée, ce dossier demande-t-il une requalification. Il ne sert qu'à cela, et la condition est dure : il faut des exemples historiques où la réponse est connue, en quantité et représentatifs de ce qu'on rencontrera.

Son intérêt réel en entreprise n'est presque jamais la performance brute. C'est la capacité à **prioriser** : un score qui classe correctement les mille dossiers les plus risqués sur cent mille produit de la valeur même s'il se trompe souvent dans l'absolu, parce qu'il remplace un traitement uniforme par un traitement ordonné.

Deux formes : la **classification** (l'étiquette est une catégorie) et la **régression** (l'étiquette est une grandeur continue). Le vocabulaire diffère, la méthode est la même.

## Ce qu'il faut savoir

- **La séparation entraînement / validation / test** est non négociable. Un modèle évalué sur les données qui l'ont entraîné donne un score sans signification. Sur des données temporelles, la séparation doit être chronologique — évaluer sur le passé ce qui a été appris sur le futur produit des résultats magnifiques et faux.
- **Surapprentissage** : le modèle mémorise le bruit du jeu d'entraînement au lieu d'en extraire la régularité. Il se détecte par l'écart entre la performance en entraînement et en validation, et se traite par la régularisation, la simplification ou plus de données.
- **La fuite de données** (*leakage*) est l'erreur la plus fréquente et la plus difficile à voir : une variable d'entrée contient, directement ou par ricochet, l'information qu'on cherche à prédire. Un score anormalement élevé est un signal de fuite avant d'être un succès.
- **Le déséquilibre des classes** change tout. Sur 2 % de fraudes, un modèle qui prédit toujours « pas de fraude » atteint 98 % d'exactitude et ne sert à rien. Voir [[notions/metriques-evaluation-ml]].
- **Les variables explicatives comptent plus que l'algorithme.** Sur données tabulaires, la construction de variables métier pertinentes fait plus de différence que le choix entre deux familles de modèles.
- **Sur tabulaire, les modèles à base d'arbres** (forêts aléatoires, gradient boosting) restent l'état de l'art pratique. Le réseau de neurones ne se justifie que sur texte, image ou son.
- **L'explicabilité est une exigence métier**, pas un supplément. La régression logistique reste souvent le premier choix parce qu'elle donne des coefficients discutables en réunion.
- **Un modèle se périme.** La population change, les processus changent, et la performance baisse silencieusement. Sans suivi, c'est l'utilisateur qui le découvre.

## Selon le métier

### Data Analyst

Prédire une étiquette connue — résiliation, impayé, requalification. La régression logistique est le premier choix, parce qu'elle donne des coefficients qu'on peut expliquer. La métrique se choisit **avec le métier avant d'entraîner quoi que ce soit** : elle encode un arbitrage entre faux positifs et faux négatifs qui n'est pas une décision technique.

### BI Analyst

L'usage réaliste est étroit, et ce n'est pas une faiblesse : scoring simple d'attrition, détection d'anomalie. La prévision qui sert vraiment en BI est celle des [[notions/series-temporelles]] sur l'activité, pas un modèle de classification. Dès que le modèle doit être réentraîné, surveillé et expliqué, ce n'est plus de la BI et il faut passer la main.

### AI Red Teaming

Une frontière de décision apprise est approximative, donc franchissable par une entrée légèrement perturbée. Et un modèle surajusté restitue des fragments de son jeu étiqueté. Les deux cibles sont donc la robustesse aux exemples adverses et la fuite par mémorisation — cette dernière suffisant à créer une violation de données personnelles quand l'appartenance au corpus est elle-même sensible.

> [!warning] Piège
> Optimiser l'exactitude parce que c'est la métrique par défaut. Elle est trompeuse dès que les classes sont déséquilibrées, c'est-à-dire dans la quasi-totalité des cas d'entreprise intéressants — fraude, attrition, incident. La métrique se décide au cadrage, à partir du coût réel d'un faux positif et d'un faux négatif.

## Pour aller plus loin

- [Supervised Learning Models — scikit-learn](https://scikit-learn.org/stable/supervised_learning.html) — la référence d'implémentation, avec la théorie en regard.
- [Supervised Machine Learning — DataCamp](https://www.datacamp.com/blog/supervised-machine-learning) — l'entrée en matière, sans prérequis mathématique.
- [What Is Semi-Supervised Learning? — IBM](https://www.ibm.com/think/topics/semi-supervised-learning) — le cas fréquent où l'étiquetage est partiel.

## Appelée par

- [[parcours/data-analyst/index|Data Analyst]]
- [[parcours/bi-analyst|BI Analyst]]
- [[parcours/ai-red-teaming/index|AI Red Teaming]]

Voisines : [[notions/metriques-evaluation-ml]], [[notions/regression-logistique]], [[notions/regression-lineaire]], [[notions/apprentissage-non-supervise]].
