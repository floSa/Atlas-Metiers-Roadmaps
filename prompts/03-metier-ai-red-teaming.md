# 03 — Métier : AI Red Teaming

Lis d'abord `PROJET.md` puis `prompts/_commun.md`. Tu es le chantier
**03 — Métier : AI Red Teaming**.

## Zone d'écriture exclusive

`content/parcours/ai-red-teaming.md`. Un seul fichier.

## Source

`data/extract/ai-red-teaming.md` — 64 nœuds documentés, 209 ressources.
Amont : `roadmap.sh/ai-red-teaming`, dernière modification 20 mars 2026.

## Mission

Produire la note de parcours du métier, au format du corpus. Elle doit tenir la
comparaison avec `content/roadmaps/05 - Roadmap — AI Engineer.md` en densité et en
qualité d'explication.

### Le sujet est sensible : cadre-le comme tel

Le red teaming IA est une discipline **défensive**. La note doit donner de quoi
comprendre les classes d'attaque, les évaluer et s'en protéger — pas un mode d'emploi
opérationnel pour attaquer des systèmes tiers.

En pratique : tu expliques les mécanismes, leurs conditions de réussite et leurs
atténuations ; tu ne fournis pas de charges utiles prêtes à l'emploi ni de procédures
de contournement pour un modèle nommé. Cette limite est une exigence de qualité
professionnelle, pas une pudeur — un contenu opérationnel se périme en semaines, alors
que le mécanisme et la parade restent vrais. Signale ce cadrage dans l'abstract.

### Ce qui compte particulièrement

- **La frontière avec la sécurité applicative classique** : ce qui relève de l'OWASP
  habituel et ce qui est propre aux modèles. C'est la confusion la plus fréquente.
- **L'injection de prompt indirecte** — la charge arrive par une page, un document, un
  résultat d'outil. C'est ce qui rend les agents structurellement exposés.
- **Le lien avec l'évaluation** : un red team sans jeu d'évaluation ni mesure de
  régression produit des anecdotes, pas de la sécurité.
- **La gouvernance** : AI Act, documentation, responsabilité. L'amont l'effleure.

### Recouvrements connus, à traiter par lien et non par réécriture

Avec **Prompt Engineering** sur l'injection de prompt, et avec **FDE** (chantier 02)
sur les garde-fous, les données sensibles et la gouvernance. Slugs canoniques à
utiliser : `injection-de-prompt`, `garde-fous`, `evaluation-llm`, `gouvernance-ia`,
`donnees-sensibles`, `ingenierie-de-prompt`, `apprentissage-supervise`,
`apprentissage-non-supervise`, `apprentissage-par-renforcement`, `reseaux-de-neurones`.

Une note existante couvre déjà le voisinage : `content/roadmaps/07 - Roadmap — AI Agents.md`
traite sécurité et évaluation des agents. Lis-la, et renvoie vers elle plutôt que de la
répéter.
