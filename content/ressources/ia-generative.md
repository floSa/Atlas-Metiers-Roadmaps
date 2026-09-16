---
tags: [ressources, ia-generative, llm, rag, agents, mcp, securite, reference]
date: 2026-09-16
statut: actif
source: https://roadmap.sh/ai-engineer
---

# Ressources — IA générative

> [!abstract] Les sources qui servent vraiment quand on construit sur des modèles de langage : documentation d'éditeur, spécifications, articles fondateurs, outillage d'évaluation et de red teaming. Sélection commentée, pas annuaire.

**Source** : capture roadmap.sh du 16 septembre 2026, complétée et vérifiée · **Rédaction** : 16 septembre 2026
La méthode de sélection et de vérification est dans [[ressources/sources]].

---

## Comment lire ce tableau

`officiel` = documentation de celui qui publie l'outil · `norme` = texte réglementaire ou
spécification · `article` = analyse ou publication de recherche · `code` = dépôt ·
`cours` = parcours structuré.

Le **niveau** est celui du lecteur attendu, pas celui de la ressource : `débutant`
suppose qu'on découvre le sujet, `confirmé` qu'on a déjà mis quelque chose en
production et qu'on cherche à le durcir.

---

## Les API de modèles

C'est la source la moins contournable du domaine, et la plus négligée. La documentation
d'un éditeur change plus vite que n'importe quel tutoriel, et elle seule dit ce que
l'API fait *ce mois-ci*. On la lit en sachant qui l'écrit : un éditeur documente ses
capacités, rarement ses limites.

| Type | Ressource | Ce qu'elle apporte | Niveau |
|---|---|---|---|
| officiel | [OpenAI — API Reference](https://developers.openai.com/api/reference/overview) | la référence de l'API la plus répandue, paramètre par paramètre | intermédiaire |
| officiel | [Claude — Messages API](https://platform.claude.com/docs/en/api/messages) | le format de conversation, les blocs de contenu, l'usage d'outils | intermédiaire |
| officiel | [Gemini API](https://ai.google.dev/gemini-api/docs) | la troisième famille à connaître, notamment sur le multimodal | intermédiaire |
| officiel | [Claude — Fenêtres de contexte](https://platform.claude.com/docs/en/build-with-claude/context-windows) | ce qui occupe réellement le contexte, et pourquoi il se remplit plus vite que prévu | intermédiaire |
| officiel | [Claude — Comptage de jetons](https://platform.claude.com/docs/en/build-with-claude/token-counting) | compter avant d'appeler : la base de tout budget d'inférence | débutant |
| officiel | [OpenAI — Appel de fonctions](https://developers.openai.com/api/docs/guides/function-calling) | le mécanisme qui transforme un modèle en pièce d'un système | intermédiaire |
| officiel | [Gemini — Sortie structurée](https://ai.google.dev/gemini-api/docs/structured-output) | contraindre la forme de la réponse, la seule façon de chaîner sans analyser du texte libre | intermédiaire |
| code | [OpenAI Cookbook](https://github.com/openai/openai-cookbook) | des exemples qui tournent, maintenus par l'éditeur — le meilleur point d'entrée pratique | débutant |
| officiel | [Hugging Face — Hub](https://huggingface.co/docs/hub/en/index) | comment sont distribués modèles, jeux de données et démonstrations | débutant |
| officiel | [Hugging Face — Modèles](https://huggingface.co/models) | le catalogue à consulter avant de supposer qu'il faut une API propriétaire | débutant |
| officiel | [Ollama](https://ollama.com/) | faire tourner un modèle ouvert en local. La façon la moins chère de tester une idée, et la seule quand les données ne sortent pas | intermédiaire |

Ce que ces pages veulent dire pour votre travail est expliqué une fois dans
[[notions/choix-de-modele]] et [[notions/cout-et-latence-inference]].

## Prompt et context engineering

Le domaine où le rapport bruit sur signal est le pire. La règle qui trie : une source
qui explique *pourquoi* une formulation change la sortie vaut dix listes d'astuces.

| Type | Ressource | Ce qu'elle apporte | Niveau |
|---|---|---|---|
| officiel | [Claude — Prompt engineering](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) | la présentation la plus structurée des techniques, par ordre d'effet réel | débutant |
| officiel | [Gemini — Stratégies de prompt](https://ai.google.dev/gemini-api/docs/prompting-strategies) | le même terrain vu par un autre éditeur ; les écarts sont instructifs | débutant |
| article | [Prompting Guide — Chain of Thought](https://www.promptingguide.ai/techniques/cot) | la technique et ses limites, sans promesse excessive | débutant |
| article | [Chain-of-Thought Prompting Elicits Reasoning in LLMs](https://arxiv.org/abs/2201.11903) | l'article d'origine (Wei et al., 2022) — à lire plutôt que ses résumés | confirmé |
| article | [Attention Is All You Need](https://arxiv.org/abs/1706.03762) | Vaswani et al., 2017. L'architecture dont tout le reste descend ; on gagne à l'avoir lue une fois | confirmé |
| cours | [Hugging Face — LLM Course](https://huggingface.co/learn/llm-course/chapter1/1) | le parcours gratuit le plus complet pour comprendre ce qu'il y a sous l'API | intermédiaire |
| cours | [Learn Prompting — Introduction](https://learnprompting.org/courses/introduction_to_prompt_engineering) | parcours gratuit et progressif, utile pour cadrer une montée en compétence d'équipe | débutant |

Détail de ce qui marche encore et de ce qui est devenu du folklore :
[[notions/ingenierie-de-prompt]].

## Embeddings, RAG et bases vectorielles

| Type | Ressource | Ce qu'elle apporte | Niveau |
|---|---|---|---|
| article | [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) | l'article fondateur du RAG (Lewis et al., 2020). Le lire évite de croire que le RAG est une idée de 2024 | confirmé |
| officiel | [OpenAI — Embeddings](https://developers.openai.com/api/docs/guides/embeddings) | ce qu'est un vecteur d'embedding et comment il se calcule, côté pratique | débutant |
| officiel | [LlamaIndex](https://developers.llamaindex.ai/python/framework/) | la bibliothèque la plus explicite sur le découpage, l'indexation et la récupération | intermédiaire |
| officiel | [LangChain](https://docs.langchain.com/oss/python/langchain/overview) | l'écosystème le plus répandu ; utile comme catalogue de motifs même si on n'adopte pas le cadre | intermédiaire |
| officiel | [Qdrant](https://qdrant.tech/) | base vectorielle libre, documentation honnête sur les compromis d'index | intermédiaire |
| officiel | [Chroma](https://www.trychroma.com/) | la plus simple pour un prototype local, sans infrastructure | débutant |
| officiel | [Weaviate](https://weaviate.io/) | recherche hybride vecteur et mot-clé ; la combinaison qui rattrape le plus d'échecs de récupération | intermédiaire |
| officiel | [FAISS](https://ai.meta.com/tools/faiss/) | la bibliothèque d'index de similarité de référence ; ce que les autres enveloppent | confirmé |

Le découpage, le reclassement et les échecs typiques de récupération sont traités dans
[[notions/rag]] et [[notions/embeddings-et-bases-vectorielles]].

## Agents, outils et MCP

| Type | Ressource | Ce qu'elle apporte | Niveau |
|---|---|---|---|
| norme | [Model Context Protocol](https://modelcontextprotocol.io/) | la spécification du protocole d'accès aux outils. La source, pas un commentaire | intermédiaire |
| norme | [MCP — Spécification d'autorisation](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) | la partie qui décide si votre agent devient une porte d'entrée. À lire avant d'exposer quoi que ce soit | confirmé |
| officiel | [MCP — Construire un serveur](https://modelcontextprotocol.io/docs/develop/build-server) | le tutoriel officiel, court et suffisant pour un premier serveur | intermédiaire |
| code | [modelcontextprotocol](https://github.com/modelcontextprotocol/modelcontextprotocol) | les SDK et la spécification en version suivie | confirmé |
| officiel | [Claude — Usage d'outils](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview) | comment un modèle décide d'appeler un outil, et ce que la description d'outil change | intermédiaire |
| officiel | [A practical guide to building agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf) | un guide d'éditeur, mais le plus sobre sur le découpage d'une boucle agentique | intermédiaire |
| officiel | [ReAct: Synergizing Reasoning and Acting](https://react-lm.github.io/) | le motif raisonner-agir dont presque toutes les boucles actuelles dérivent | confirmé |
| cours | [Hugging Face — MCP Course](https://huggingface.co/learn/mcp-course/en/unit0/introduction) | parcours gratuit, avec des exercices, sur le protocole et ses clients | débutant |
| cours | [Hugging Face — Agents Course, les outils](https://huggingface.co/learn/agents-course/en/unit1/tools) | la notion d'outil expliquée sans cadre propriétaire | débutant |

Voir [[notions/agents-llm]] et [[notions/mcp]].

## Évaluation et observabilité

La partie que les projets sautent, et celle qui décide s'ils tiennent. Une fonction à
base de modèle n'a pas d'état binaire : sans protocole d'évaluation, « ça marche » est
une opinion.

| Type | Ressource | Ce qu'elle apporte | Niveau |
|---|---|---|---|
| officiel | [Ragas](https://docs.ragas.io/en/stable/) | des métriques de RAG définies et calculables — fidélité, pertinence du contexte | intermédiaire |
| officiel | [DeepEval](https://www.deepeval.com/) | l'évaluation écrite comme des tests, donc exécutable en intégration continue | intermédiaire |
| code | [deepeval](https://github.com/confident-ai/deepeval) | le dépôt, pour lire comment les métriques sont réellement calculées | confirmé |
| officiel | [Langfuse](https://langfuse.com/docs) | traces, coûts et jeux d'évaluation ; le plus complet des outils libres | intermédiaire |
| code | [langfuse](https://github.com/langfuse/langfuse) | auto-hébergeable, ce qui compte dès que les prompts contiennent des données client | confirmé |
| code | [Instructor](https://github.com/567-labs/instructor) | sortie structurée validée et réessayée ; supprime une classe entière d'erreurs | intermédiaire |

Les trois angles — négociation client, fonction non binaire, corpus adverse — sont dans
[[notions/evaluation-llm]]. L'instrumentation générale est dans [[notions/observabilite]].

## Sécurité des systèmes à base de modèles

| Type | Ressource | Ce qu'elle apporte | Niveau |
|---|---|---|---|
| norme | [OWASP GenAI Security Project](https://genai.owasp.org/) | le Top 10 des risques des applications LLM. Le référentiel que les équipes sécurité connaissent déjà | intermédiaire |
| norme | [OWASP LLM01 — Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) | la fiche du risque n°1, avec scénarios et atténuations | intermédiaire |
| article | [Jailbroken: How Does LLM Safety Training Fail?](https://arxiv.org/abs/2307.02483) | pourquoi l'alignement échoue, plutôt qu'une liste de contournements qui périme en trois mois | confirmé |
| article | [Extracting Training Data from Large Language Models](https://arxiv.org/abs/2012.07805) | la démonstration fondatrice de la mémorisation et de l'extraction | confirmé |
| article | [SoK: Prompt Hacking of Large Language Models](https://arxiv.org/abs/2410.13901) | la taxonomie systématique. **Attention** : l'URL citée en amont pour ce titre désigne un tout autre article | confirmé |
| article | [Poisoning Web-Scale Training Datasets is Practical](https://arxiv.org/abs/2302.10149) | l'empoisonnement côté faisabilité — même remarque sur l'URL amont | confirmé |
| article | [Towards Evaluating the Robustness of Neural Networks](https://arxiv.org/abs/1608.04644) | Carlini et Wagner : la référence sur l'évaluation de robustesse, et sur les défenses qui n'en sont pas | confirmé |
| officiel | [Claude — Atténuer jailbreaks et injections](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks) | des contre-mesures concrètes, avec leurs limites reconnues | intermédiaire |
| officiel | [Claude — Réduire les hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations) | ce qui marche vraiment : ancrage, citation, autorisation de répondre « je ne sais pas » | intermédiaire |
| officiel | [OpenAI — Modération](https://developers.openai.com/api/docs/guides/moderation) | un filtre d'entrée et de sortie prêt à l'emploi, gratuit | débutant |
| article | [Adversarial Testing for Generative AI](https://developers.google.com/machine-learning/guides/adv-testing) | une méthode de test adverse structurée, orientée évaluation plutôt qu'exploit | intermédiaire |
| article | [Prompt Hacking — Mesures défensives](https://learnprompting.org/docs/prompt_hacking/defensive_measures/introduction) | le pendant défensif, structuré contre-mesure par contre-mesure | intermédiaire |
| article | [Model Inversion Attacks: A Survey](https://arxiv.org/html/2411.10023v1) | panorama des attaques par inversion et des parades, à jour | confirmé |
| article | [Detecting and Preventing Data Poisoning Attacks on AI Models](https://arxiv.org/abs/2503.09302) | l'empoisonnement vu du côté de la défense | confirmé |
| article | [GitHub MCP Exploited](https://invariantlabs.ai/blog/mcp-github-vulnerability) | un cas réel sur la couche de connexion aux outils. Le plus convaincant des arguments pour lire la spécification d'autorisation | intermédiaire |
| norme | [OWASP — Threat Modeling](https://community.owasp.org/Threat_Modeling) | la méthode de modélisation de la menace, applicable telle quelle à un système à base de modèles | intermédiaire |
| norme | [NIST SP 800-218 — Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final) | les pratiques de développement sécurisé que les marchés publics commencent à exiger | confirmé |
| article | [Weaknesses and Vulnerabilities in Modern AI](https://www.sei.cmu.edu/blog/weaknesses-and-vulnerabilities-in-modern-ai-why-security-and-safety-are-so-challenging/) | le SEI de Carnegie Mellon sur pourquoi sécurité et sûreté sont si difficiles ici. Sobre, et sans intérêt commercial | confirmé |

Voir [[notions/injection-de-prompt]], [[notions/garde-fous]] et
[[notions/modelisation-de-la-menace]].

## Outillage de red teaming

| Type | Ressource | Ce qu'elle apporte | Niveau |
|---|---|---|---|
| code | [PyRIT](https://github.com/Azure/PyRIT) | orchestration de campagnes adverses, rejouable | confirmé |
| officiel | [Promptfoo — Red team](https://www.promptfoo.dev/docs/red-team/) | des scénarios adverses intégrables à une chaîne d'intégration continue | intermédiaire |
| officiel | [HackAPrompt](https://www.hackaprompt.com/) | environnement d'entraînement autorisé à l'injection de prompt | débutant |
| officiel | [Lakera — Agent Breaker](https://play.lakera.ai/agent-breaker) | le successeur de Gandalf : attaquer un agent, légalement et sans conséquence | débutant |
| officiel | [0din.ai — Politique de divulgation](https://0din.ai/policy) | un cadre de divulgation responsable propre à l'IA générative | confirmé |

## Cadres, régulation et veille

| Type | Ressource | Ce qu'elle apporte | Niveau |
|---|---|---|---|
| norme | [Règlement (UE) 2024/1689 — texte intégral](https://publications.europa.eu/resource/celex/32024R1689) | le règlement sur l'IA, servi par l'Office des publications. Contrairement au portail EUR-Lex, cette adresse répond aux robots | confirmé |
| norme | [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) | le cadre de gestion du risque, et le vocabulaire commun avec les équipes conformité | intermédiaire |
| norme | [ISO/IEC 42001](https://www.iso.org/standard/81230.html) | la norme de système de management de l'IA, certifiable — donc opposable en appel d'offres. Payante, et le site refuse toute vérification automatique | confirmé |
| officiel | [EU AI Act Explorer](https://artificialintelligenceact.eu/ai-act-explorer/) | le règlement article par article, navigable. Un confort de lecture, pas une source de droit | intermédiaire |
| officiel | [Cadre réglementaire de l'IA — Commission européenne](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) | le calendrier d'application et les actes d'exécution, c'est-à-dire ce qui s'impose et quand | intermédiaire |
| officiel | [Anthropic Research](https://www.anthropic.com/research) | publications de recherche à suivre en continu | confirmé |
| officiel | [AI Security Institute](https://www.aisi.gov.uk/) | évaluations publiques de sécurité des modèles, par un organisme public | intermédiaire |
| officiel | [Center for AI Safety](https://www.safe.ai/) | l'autre pôle de publication à suivre sur le risque | confirmé |
| article | [AI Index Report — Stanford HAI](https://hai.stanford.edu/ai-index) | le rapport annuel chiffré. Le seul document à citer quand une réunion réclame des ordres de grandeur | débutant |

La lecture réglementaire côté projet est dans [[notions/gouvernance-ia]].

## Écarté, et pourquoi

- **Les pages produit des fournisseurs de bases vectorielles et de plateformes
  d'agents**, quand elles ne documentent rien d'autre que leur propre offre. Il en reste
  trois ci-dessus, retenues pour leur documentation technique, pas pour leur argumentaire.
- **Les articles à marqueur de campagne.** Cinquante-trois des quatre-vingt-trois
  articles d'un même éditeur arrivent dans le catalogue amont avec
  `utm_campaign=TDS+roadmap+integration`. Certains sont bons ; aucun n'a été choisi pour
  sa qualité, et ça se voit dans l'URL.
- **Les vidéos dont le titre est corrompu dans la capture amont.** Deviner ce que
  « laude Code Tutorial » voulait dire, c'est inventer. Détail dans [[ressources/sources]].
