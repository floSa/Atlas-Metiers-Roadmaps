# Atlas Métiers Roadmaps

Un site de parcours d'apprentissage, en français, pour treize métiers de l'intelligence
artificielle et de la donnée. Pour chaque métier : une roadmap cliquable, ce qu'il faut
savoir faire et **à quel niveau on l'attend chez un profil confirmé**, et des ressources
de formation gratuites et vérifiées.

## Comment c'est organisé

Un arbre. À chaque étage, une carte cliquable de ce qu'il y a à apprendre ; on descend
d'un cran, on remonte par le fil d'Ariane ou par la barre de navigation en bas de page.

```
Accueil          les treize métiers
 └── Métier      la roadmap du métier
      └── Domaine        la carte des sous-domaines
           └── Sous-domaine   la carte des notions
                └── Notion    la feuille : explication et ressources
```

Une règle gouverne le tout : **une case dans un schéma mène toujours quelque part**. Si
un sujet n'a pas de page, il n'a pas de case.

Une seconde règle évite la redite : **une notion transverse est expliquée une seule
fois**. Le RAG, l'évaluation, SQL, les garde-fous ont chacun un fichier sous `notions/`
et un seul. Un parcours métier y renvoie et ajoute ce que la notion signifie pour lui.

## Le contenu

| | |
|---|---|
| Métiers | 13 |
| Pages | 364 |
| Notions transverses | 65 |
| Niveaux de séniorité | 241 feuilles graduées |

Les treize métiers : Forward Deployed Engineer, Data Scientist, Data Engineer,
AI Engineer, Data Analyst, BI Analyst, MLOps, Machine Learning, AI Agents,
AI Product Builder, AI Red Teaming, Prompt Engineering, Computer Science.

L'échelle de séniorité a quatre niveaux — **notion** (reconnaître le sujet, savoir qui
appeler), **usage** (s'en servir sur un chemin balisé), **autonomie** (concevoir,
déboguer sous pression, arbitrer), **référence** (faire autorité dans la salle).

## Faire tourner le site en local

```sh
bash quartz/build.sh      # clone Quartz au commit épinglé, applique la config, construit
python3 tools/servir.py   # sert public/ sur http://localhost:8080
```

`tools/servir.py` résout les adresses sans extension comme le fait GitHub Pages.
`python -m http.server` ne le fait pas et renvoie 404 sur toutes les pages.

## Rafraîchir depuis roadmap.sh

Le corpus part des roadmaps de [roadmap.sh](https://roadmap.sh), mais ce n'en est pas une
traduction : chaque notion est expliquée, située dans le métier, et assortie de l'erreur
qu'on voit en vrai.

```sh
python3 tools/roadmap_extract.py --sync --all-known   # recapture l'amont
python3 tools/roadmap_diff.py                          # mesure l'écart avec le corpus
python3 tools/verifier_liens.py                        # teste les liens des ressources
```

Les captures sont horodatées dans `data/raw/`, donc l'extraction est rejouable et les
écarts se mesurent d'une veille à l'autre.

## Organisation du dépôt

| Chemin | Contenu |
|---|---|
| `content/` | le corpus — la source unique, éditable dans Obsidian |
| `quartz/` | configuration, correctifs et composants du générateur de site |
| `tools/` | extraction, diff, vérification des liens, serveur local |
| `data/` | captures horodatées de roadmap.sh et rapports |
| `prompts/` | le gabarit de rédaction et les consignes de chaque chantier |

Le cadrage du projet est dans [PROJET.md](PROJET.md), le gabarit d'une fiche métier dans
[prompts/_gabarit-metier.md](prompts/_gabarit-metier.md).

## Licence

Le dépôt est sous [licence MIT](LICENSE). Les ressources citées restent la propriété de
leurs auteurs, et le générateur [Quartz](https://github.com/jackyzha0/quartz) est
lui aussi sous MIT.
