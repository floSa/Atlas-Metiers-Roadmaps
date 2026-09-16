# 02 — Métier : Forward Deployed Engineer

Lis d'abord `PROJET.md` puis `prompts/_commun.md`. Tu es le chantier
**02 — Métier : Forward Deployed Engineer**.

C'est la pièce maîtresse du projet. Les quatre autres chantiers métier produisent une
note ; toi, tu produis un dossier. Prends la mesure de l'écart.

## Zone d'écriture exclusive

`content/parcours/forward-deployed-engineer/` — le dossier entier, à toi seul.
**Rien ailleurs**, et en particulier rien dans `content/notions/`.

## Sources

- `data/extract/forward-deployed-engineer.md` — le plan amont. **20 nœuds seulement,
  30 ressources.** C'est la roadmap la plus maigre du catalogue : elle te donne un
  squelette, pas un plan. Ne te laisse pas borner par elle.
- Le brief de commande, reproduit intégralement en fin de prompt. C'est lui qui porte
  la valeur propre du dossier.

## Pourquoi ce dossier existe

La roadmap amont réduit le socle technique à sept renvois vers d'autres roadmaps, et ne
garde en propre qu'un bloc *Customer Delivery & Field Skills*. Elle ne dit rien de cinq
sujets qui font pourtant le métier au quotidien :

1. la réingénierie de processus et sa modélisation ;
2. l'arbitrage entre automatisation déterministe et IA générative ;
3. l'interfaçage avec les systèmes patrimoniaux ;
4. la dimension politique d'une mission en immersion ;
5. la sortie de mission et le transfert de compétences.

Ton travail consiste à traiter ces cinq sujets aussi sérieusement que l'amont traite
les siens, et à recoudre l'ensemble.

## Structure attendue

Un dossier multi-fichiers, navigable par clics successifs. Proposition de départ — tu
peux l'amender si tu argumentes le changement dans ta synthèse :

```
content/parcours/forward-deployed-engineer/
├── index.md                      la carte, le positionnement, les trajectoires d'accès
├── socle-technique.md            ce qu'il faut savoir faire, et à quelle profondeur
├── cycle-mission.md              audit → rationalisation → industrialisation → sortie
├── audit-et-cartographie.md      l'immersion terrain, l'observation, le BPMN
├── arbitrage-technologique.md    déterministe contre probabiliste, choix de modèle
├── industrialisation.md          livraison en environnement client, sécurité, reprise
└── competences-relationnelles.md parties prenantes, politique interne, changement
```

`index.md` est la porte d'entrée : il porte la carte et renvoie vers les autres pages.
Chaque page se tient seule et respecte le contrat de format du socle commun.

## Exigences particulières

**Le socle technique se traite par renvoi.** L'amont renvoie vers sept roadmaps ; toi
tu as déjà les notes correspondantes dans `content/roadmaps/`. Dis pour chaque domaine
**quelle profondeur est réellement attendue chez un FDE** — c'est là l'information utile,
bien plus que la liste des technologies — et renvoie vers la note existante.

**Le cycle d'intervention est la colonne vertébrale.** Le brief en donne trois phases ;
ajoute-en une quatrième, la sortie de mission, que le brief mentionne sans l'ériger en
phase alors que c'est là que la plupart des missions échouent à laisser quelque chose.

**La dimension politique doit être traitée sans euphémisme et sans cynisme.** Intérêts
divergents, résistance au changement, arbitrages à défendre devant une direction : c'est
une compétence professionnelle, décris-la comme telle.

**Distingue ce qui vient de l'amont, du brief, et de toi.** Les trois sont légitimes,
mais le lecteur doit pouvoir faire la part des choses. Les apports propres passent par
les encadrés `Ajout 2026`.

**Le métier est récent et son contenu est largement du témoignage.** Beaucoup de ce qui
circule dessus est promotionnel. Sois sévère sur les sources : préfère une source
primaire datée à un article de contenu, et signale explicitement quand une affirmation
relève de la pratique rapportée plutôt que d'un consensus établi.

## Recouvrements connus

Avec **AI Engineer** et **AI Agents** (notes existantes) sur RAG, agents, MCP,
évaluation. Avec **AI Red Teaming** (chantier 03) sur les garde-fous, l'injection de
prompt, les données sensibles, la gouvernance. Avec **AI Product Builder** (chantier 04)
sur l'arbitrage déterministe/probabiliste et le ROI. Avec **BI Analyst** (chantier 06)
sur le cadrage du besoin et la gestion des parties prenantes.

Dans tous les cas : lien vers le slug canonique, plus une ou deux phrases d'angle FDE.

Slugs à utiliser : `rag`, `embeddings-et-bases-vectorielles`, `agents-llm`, `mcp`,
`evaluation-llm`, `garde-fous`, `injection-de-prompt`, `donnees-sensibles`,
`gouvernance-ia`, `cout-et-latence-inference`, `choix-de-modele`, `affinage-de-modele`,
`conteneurisation`, `integration-continue`, `observabilite`, `tests-logiciels`,
`conception-d-api`, `systemes-patrimoniaux`, `rgpd`, `cadrage-besoin`, `bpmn`,
`reingenierie-de-processus`, `arbitrage-deterministe-probabiliste`,
`gestion-parties-prenantes`, `conduite-du-changement`, `roi-des-projets-ia`,
`redaction-technique`, `transfert-de-competences`.

---

## Le brief de commande, verbatim

> **Le métier de Forward Deployed Engineer (FDE) en Intelligence Artificielle**
>
> **Définition et positionnement**
>
> Le Forward Deployed Engineer (FDE) est un profil hybride à la croisée du conseil en
> stratégie opérationnelle et de l'ingénierie logicielle avancée. Historiquement
> démocratisé par des entreprises comme Palantir, ce rôle consiste à s'immerger
> directement au sein des équipes clientes pour auditer les flux opérationnels,
> concevoir sur mesure et déployer en production des solutions logicielles et
> d'intelligence artificielle adaptées aux contraintes réelles de l'organisation.
>
> **Domaines d'expertise requis**
>
> - **Ingénierie logicielle et intégration de systèmes** : Maîtriser le développement
>   backend robuste (Python, TypeScript, Go), la conception d'API, la manipulation de
>   bases de données relationnelles et vectorielles, ainsi que l'interfaçage avec des
>   systèmes patrimoniaux (ERP, CRM, bases legacy).
> - **Architecture IA, LLMs et systèmes agents** : Concevoir des architectures RAG
>   (Retrieval-Augmented Generation), orchestrer des agents autonomes et maîtriser les
>   techniques de prompting avancé, de fine-tuning ciblé et de sélection de modèles
>   (SLM vs LLM).
> - **LLMOps, sécurité et fiabilité** : Établir des protocoles d'évaluation rigoureux
>   (métriques de fidélité, de pertinence et de non-hallucination), implémenter des
>   garde-fous (guardrails, prévention des injections de prompts, filtrage des données
>   sensibles) et gérer la scalabilité, les coûts d'inférence et la latence.
> - **Business Process Re-engineering (BPR)** : Savoir décortiquer un processus métier
>   complexe, identifier les redondances et distinguer les besoins d'automatisation
>   déterministe (scripts, webhooks, RPA) des besoins probabilistes nécessitant de l'IA
>   générative.
>
> **Compétences clés (Hard et Soft Skills)**
>
> - **Compétences techniques** : Maîtrise des pipelines CI/CD, conteneurisation (Docker,
>   Kubernetes), frameworks d'orchestration IA, observabilité et logging des modèles en
>   production.
> - **Compétences d'audit et de conseil** : Capacité d'immersion terrain, modélisation
>   des processus (BPMN), reformulation des besoins métiers en spécifications techniques.
> - **Compétences relationnelles et politiques** : Intelligence situationnelle pour
>   naviguer dans la politique interne d'une entreprise, aligner des parties prenantes
>   aux intérêts divergents, surmonter la résistance au changement et vulgariser des
>   arbitrages techniques auprès de directions exécutives.
>
> **Cycle d'intervention type**
>
> 1. **Audit et cartographie in situ** : Observer directement les tâches exécutées par
>    les équipes opérationnelles, documenter exhaustivement chaque étape du cycle de
>    travail et cartographier les goulets d'étranglement ainsi que les silos
>    d'information.
> 2. **Rationalisation et sélection technologique** : Simplifier le processus avant
>    toute écriture de code en supprimant les étapes superflues, puis arbitrer
>    rigoureusement entre programmation classique et intégration de modèles de fondation.
> 3. **Développement, intégration et industrialisation** : Livrer des briques
>    logicielles résilientes directement dans l'infrastructure client, valider la
>    sécurité des données, exécuter les tests de performance et assurer le support, le
>    transfert de compétences et la maintenance opérationnelle.
