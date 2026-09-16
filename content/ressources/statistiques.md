---
tags: [ressources, statistiques, machine-learning, methode, causalite, reference]
date: 2026-09-16
statut: actif
source: https://roadmap.sh/ai-data-scientist
---

# Ressources — Statistiques et méthode

> [!abstract] Ce qu'il faut pour ne pas se tromper : distributions, tests, régression, causalité, protocole d'évaluation. C'est la famille où les sources les plus anciennes sont les meilleures — un manuel de statistique de 2019 n'a pas vieilli, un article sur les LLM de 2024 si.

**Source** : capture roadmap.sh du 16 septembre 2026, complétée et vérifiée · **Rédaction** : 16 septembre 2026
La méthode de sélection et de vérification est dans [[ressources/sources]].

---

## Pourquoi cette famille se sélectionne autrement

Ailleurs dans ce corpus, le critère « daté et maintenu » écarte l'intemporel
autoproclamé. Ici, il s'inverse. La loi des grands nombres n'a pas de version 2026, et
un manuel universitaire relu pendant vingt ans vaut mieux qu'un billet de blog récent.
Le critère qui trie devient : **l'ouvrage dit-il ses hypothèses ?** Une ressource qui
donne une formule sans dire quand elle cesse d'être valable est un piège, quelle que
soit sa date.

## Les manuels de fond

| Type | Ressource | Ce qu'elle apporte | Niveau |
|---|---|---|---|
| livre | [OpenIntro Statistics](https://www.openintro.org/book/os/) | le manuel d'introduction libre le mieux fait. Complet, exercices corrigés, sans prérequis | débutant |
| livre | [NIST/SEMATECH e-Handbook of Statistical Methods](https://www.itl.nist.gov/div898/handbook/) | rigoureux, gratuit, orienté mesure et industrie. La référence quand on veut être sûr | intermédiaire |
| livre | [Probability and Statistics: The Science of Uncertainty](https://utstat.utoronto.ca/mikevans/jeffrosenthal/book.pdf) | Evans et Rosenthal, libre. Le versant probabiliste, plus formel | confirmé |
| livre | [Linear Algebra Done Right](https://linear.axler.net/LADR4e.pdf) | Axler, 4ᵉ édition libre. L'algèbre linéaire par les espaces vectoriels plutôt que par les matrices — le bon ordre pour comprendre les décompositions | confirmé |
| livre | [Deep Learning](https://www.deeplearningbook.org/) | Goodfellow, Bengio, Courville. Libre en ligne. Daté sur les architectures, toujours juste sur les principes | confirmé |
| livre | [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) | Jake VanderPlas, libre. Le pont entre les manuels ci-dessus et le code qu'on écrit vraiment | débutant |
| livre | [Calculus (MIT OpenCourseWare)](https://ocw.mit.edu/courses/res-18-001-calculus-fall-2023/mitres_18_001_f17_full_book.pdf) | le manuel de Gilbert Strang, libre. Le rattrapage d'analyse quand les gradients cessent d'être une métaphore | intermédiaire |

Voir [[notions/statistiques-descriptives]] et [[notions/tests-hypotheses]].

## Comprendre avant de calculer

| Type | Ressource | Ce qu'elle apporte | Niveau |
|---|---|---|---|
| vidéo | [StatQuest](https://www.youtube.com/@statquest) | Josh Starmer. La meilleure vulgarisation statistique disponible, et la seule qui explique *pourquoi* la formule est celle-là | débutant |
| cours | [Khan Academy — Statistiques et probabilités](https://www.khanacademy.org/math/statistics-probability) | gratuit, progressif, avec exercices. Le rattrapage le plus efficace pour qui vient du métier | débutant |
| article | [Choosing the Right Statistical Test](https://www.scribbr.com/statistics/statistical-tests/) | l'arbre de décision qu'on relit avant chaque test. Court, correct | débutant |
| article | [Type I & Type II Errors](https://www.scribbr.com/statistics/type-i-and-type-ii-errors/) | la distinction qu'on croit connaître et qu'on inverse en réunion | débutant |
| article | [Population vs. Sample](https://www.scribbr.com/methodology/population-vs-sample/) | la question à poser en premier, et celle qu'on saute en premier | débutant |

## Causalité, tests et protocole

La section la plus rentable de cette page. Presque toutes les erreurs coûteuses d'une
analyse sont ici, pas dans le code.

| Type | Ressource | Ce qu'elle apporte | Niveau |
|---|---|---|---|
| article | [Correlation vs. Causation](https://www.scribbr.com/methodology/correlation-vs-causation/) | à garder sous la main pour les réunions, littéralement | débutant |
| article | [A Refresher on A/B Testing](https://hbr.org/2017/06/a-refresher-on-ab-testing) | le rappel de protocole à relire avant tout test, y compris le dixième | intermédiaire |
| article | [A Refresher on Regression Analysis](https://hbr.org/2015/11/a-refresher-on-regression-analysis) | ce qu'un coefficient dit, et surtout ce qu'il ne dit pas | intermédiaire |
| livre | [Introduction to Time Series Analysis (NIST)](https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc4.htm) | la décomposition tendance-saisonnalité-résidu, rigoureusement et gratuitement | intermédiaire |

Voir [[notions/analyse-correlation]], [[notions/ab-testing]],
[[notions/regression-lineaire]] et [[notions/series-temporelles]].

> [!warning] Piège
> Un test significatif sur un échantillon qu'on a choisi après avoir vu les données ne
> démontre rien. C'est l'erreur la plus fréquente et la plus difficile à faire admettre,
> parce que la sortie du logiciel est identique dans les deux cas : le chiffre ne sait
> pas dans quel ordre vous avez fait les choses.

## Apprentissage automatique

| Type | Ressource | Ce qu'elle apporte | Niveau |
|---|---|---|---|
| officiel | [scikit-learn](https://scikit-learn.org/stable/) | la documentation la plus pédagogique de tout l'écosystème. Le guide utilisateur est un cours de ML déguisé | débutant |
| officiel | [scikit-learn — Prétraitement](https://scikit-learn.org/stable/modules/preprocessing.html) | normalisation, encodage, et pourquoi l'ordre par rapport à la découpe compte | intermédiaire |
| officiel | [scikit-learn — Recherche d'hyperparamètres](https://scikit-learn.org/stable/modules/grid_search.html) | valider sans se mentir : la validation croisée imbriquée expliquée correctement | confirmé |
| cours | [Practical Deep Learning for Coders](https://course.fast.ai/) | fast.ai. L'approche descendante — on entraîne d'abord, on comprend ensuite | intermédiaire |
| cours | [mlcourse.ai](https://mlcourse.ai/) | cours libre et complet, avec devoirs corrigés. L'un des rares à traiter sérieusement l'analyse exploratoire avant la modélisation | intermédiaire |
| cours | [Google ML Crash Course — Classification](https://developers.google.com/machine-learning/crash-course/classification) | court, gratuit, et le passage sur les seuils et la matrice de confusion est le meilleur du lot | débutant |
| officiel | [PyTorch — Documentation](https://docs.pytorch.org/docs/stable/index.html) | le cadre devenu majoritaire en recherche comme en production | intermédiaire |
| officiel | [TensorFlow — Tutoriels](https://www.tensorflow.org/tutorials) | l'autre cadre, encore très présent dans les bases de code d'entreprise | intermédiaire |

Voir [[notions/apprentissage-supervise]], [[notions/apprentissage-non-supervise]],
[[notions/metriques-evaluation-ml]] et [[notions/reseaux-de-neurones]].

## Interprétabilité et suivi des modèles

| Type | Ressource | Ce qu'elle apporte | Niveau |
|---|---|---|---|
| officiel | [SHAP](https://shap.readthedocs.io/en/latest/) | l'attribution de contribution la mieux fondée théoriquement, et la documentation dit ses limites | confirmé |
| code | [LIME](https://github.com/marcotcr/lime) | l'explication locale par approximation ; plus simple, moins solide, utile quand même | intermédiaire |
| officiel | [MLflow](https://mlflow.org/docs/latest/) | suivi d'expériences, registre de modèles. Le standard de fait | intermédiaire |
| officiel | [DVC — Prise en main](https://doc.dvc.org/start) | versionner les données et les pipelines, pas seulement le code | intermédiaire |
| officiel | [Kubeflow](https://www.kubeflow.org/) | l'orchestration de chaînes de ML sur Kubernetes. Lourd, et justifié seulement quand plusieurs équipes partagent l'infrastructure | confirmé |

## Écarté, et pourquoi

- **Les cours de statistiques hébergés sur des plateformes à paywall**, quand un manuel
  libre couvre le même terrain. C'est le cas pour tout ce qui précède.
- **Les listes d'articles de blog sur les mathématiques du ML.** L'amont en propose
  plusieurs ; aucune ne remplace un chapitre de manuel, et toutes se périment.
- **Une vidéo de cours universitaire complet** dont le titre amont est tronqué
  (« tatistics - A Full University Course... »). Écartée par principe : on ne republie
  pas une référence dont on ne peut pas citer le titre exact.
