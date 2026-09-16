# Prompt Engineering Roadmap — plan extrait

- **Slug** : `prompt-engineering`
- **Description amont** : Step by step guide to learning Prompt Engineering in @currentYear@
- **Derniere modification amont** : 2026-04-29T07:36:03.435Z
- **Capture** : 2026-09-16
- **Volume** : 47 noeuds de contenu, 46 documentes, 90 ressources
- **Renvois vers d'autres roadmaps** : `https://roadmap.sh`, `https://roadmap.sh/ai-agents`, `https://roadmap.sh/ai-engineer`

---

## Prompt Engineering

#### LLMs and how they work?

LLMs function as sophisticated prediction engines that process text sequentially, predicting the next token based on relationships between previous tokens and patterns from training data. They don't predict single tokens directly but generate probability distributions over possible next tokens, which are then sampled using parameters like temperature and top-K. The model repeatedly adds predicted tokens to the sequence, building responses iteratively. This token-by-token prediction process, combined with massive training datasets, enables LLMs to generate coherent, contextually relevant text across diverse applications and domains.

- `@article` [What are large language models (LLMs)? - IBM](https://www.ibm.com/think/topics/large-language-models)
- `@article` [Large language model - Wikipedia](https://en.wikipedia.org/wiki/Large_language_model)
- `@article` [How Large Language Models Work: Explained Simply](https://justainews.com/applications/chatbots-and-virtual-assistants/how-large-language-models-work/)
- `@video` [How Large Language Models Work](https://youtu.be/5sLYAQS9sWQ)

#### What is a Prompt?

A prompt is an input provided to a Large Language Model (LLM) to generate a response or prediction. It serves as the instruction or context that guides the AI model's output generation process. Effective prompts are clear, specific, well-structured, and goal-oriented, directly affecting the accuracy and relevance of AI responses.

- `@article` [Basics of Prompting - DAIR.AI](https://www.promptingguide.ai/introduction/basics)
- `@article` [Prompt Elements - DAIR.AI](https://www.promptingguide.ai/introduction/elements)

### Introduction

Prompt engineering is the practice of designing effective inputs for Large Language Models to achieve desired outputs. This roadmap covers fundamental concepts, core techniques, model parameters, and advanced methods. It's a universal skill accessible to anyone, requiring no programming background, yet crucial for unlocking AI potential across diverse applications and domains.

- `@article` [What is Generative AI? - LearnPrompting](https://learnprompting.org/docs/basics/generative_ai)

#### What is Prompt Engineering?

Prompt engineering is the practice of designing effective inputs for large language models to achieve desired outputs. It covers techniques like few-shot prompting, chain-of-thought, and parameter tuning. No programming background is required, making it a universal skill for anyone working with AI.

- `@article` [Prompt engineering - Wikipedia](https://en.wikipedia.org/wiki/Prompt_engineering)
- `@article` [Introduction to Prompt Engineering - LearnPrompting](https://learnprompting.org/docs/basics/prompt_engineering)
- `@video` [RAG vs Fine-Tuning vs Prompt Engineering: Optimizing AI Models](https://youtu.be/zYGDpG-pTho?si=yov4dDrcsHBAkey-&t=522)

### Output Control

Output control encompasses techniques and parameters for managing LLM response characteristics including length, format, style, and content boundaries. Key methods include max tokens for length limits, stop sequences for precise boundaries, temperature for creativity control, and structured output requirements for format consistency. Effective output control combines prompt engineering techniques with model parameters to ensure responses meet specific requirements. This is crucial for production applications where consistent, appropriately formatted outputs are essential for user experience and system integration.

- `@official` [Increase Output Consistency - Anthropic](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/increase-consistency)
- `@article` [General Tips for Designing Prompts - DAIR.AI](https://www.promptingguide.ai/introduction/tips)

### Structured Outputs

Structured outputs involve prompting LLMs to return responses in specific formats like JSON, XML, or other organized structures rather than free-form text. This approach forces models to organize information systematically, reduces hallucinations by imposing format constraints, enables easy programmatic processing, and facilitates integration with applications. For example, requesting movie classification results as JSON with a specified schema ensures consistent, parseable responses. Structured outputs are particularly valuable for data extraction, API integration, and applications requiring reliable data formatting.

- `@official` [Structured Output - Google Gemini API](https://ai.google.dev/gemini-api/docs/structured-output)
- `@official` [Structured Outputs - Anthropic](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)
- `@opensource` [Instructor - Structured Output Library](https://github.com/jxnl/instructor)
- `@article` [Structured Outputs - LLM Parameter Guide - Vellum](https://www.vellum.ai/llm-parameters/structured-outputs)

#### Step-back Prompting

Step-back prompting improves LLM performance by first asking a general question related to the specific task, then using that answer to inform the final response. This technique activates relevant background knowledge before attempting the specific problem. For example, before writing a video game level storyline, first ask "What are key settings for engaging first-person shooter levels?" then use those insights to create the specific storyline. This approach reduces biases and improves accuracy by grounding responses in broader principles.

- `@article` [Step-Back Prompting - LearnPrompting](https://learnprompting.org/docs/advanced/thought_generation/step_back_prompting)

#### Zero-Shot Prompting

Zero-shot prompting provides only a task description without examples, relying on the model's training patterns. Simply describe the task clearly, provide input data, and optionally specify output format. Works well for simple classification, text generation, and Q&A, but may produce inconsistent results for complex tasks.

- `@article` [Zero-Shot Prompting - DAIR.AI](https://www.promptingguide.ai/techniques/zeroshot)
- `@article` [Introduction to Zero-Shot Techniques - LearnPrompting](https://learnprompting.org/docs/advanced/zero_shot/introduction)

#### Chain of Thought (CoT) Prompting

Chain of Thought prompting improves LLM reasoning by generating intermediate reasoning steps before providing the final answer. Instead of jumping to conclusions, the model "thinks through" problems step by step. Simply adding "Let's think step by step" to prompts often dramatically improves accuracy on complex reasoning tasks and mathematical problems.

- `@article` [Chain-of-Thought Prompting - DAIR.AI](https://www.promptingguide.ai/techniques/cot)
- `@article` [Chain-of-Thought Prompting - LearnPrompting](https://learnprompting.org/docs/intermediate/chain_of_thought)
- `@article` [Reasoning LLMs Guide - DAIR.AI](https://www.promptingguide.ai/guides/reasoning-llms)
- `@video` [Context Engineering vs. Prompt Engineering: Smarter AI with RAG & Agents](https://youtu.be/vD0E3EUb8-8?si=Y6MCLPzjmhMB4jSu&t=203)

#### One-Shot / Few-Shot Prompting

One-shot provides a single example to guide model behavior, while few-shot includes multiple examples (3-5) to demonstrate desired patterns. Examples show output structure, style, and tone, increasing accuracy and consistency. Use few-shot for complex formatting, specialized tasks, and when zero-shot results are inconsistent.

- `@article` [Few-Shot Prompting - DAIR.AI](https://www.promptingguide.ai/techniques/fewshot)
- `@article` [Few-Shot Prompting - LearnPrompting](https://learnprompting.org/docs/basics/few_shot)
- `@article` [Few-Shot Introduction - LearnPrompting](https://learnprompting.org/docs/advanced/few_shot/introduction)
- `@video` [Context Engineering vs. Prompt Engineering: Smarter AI with RAG & Agents](https://youtu.be/vD0E3EUb8-8?si=Fi2igdPTBUocqnX7&t=177)

### Automatic Prompt Engineering

Automatic Prompt Engineering (APE) uses LLMs to generate and optimize prompts automatically, reducing human effort while enhancing model performance. The process involves prompting a model to create multiple prompt variants, evaluating them using metrics like BLEU or ROUGE, then selecting the highest-scoring candidate. For example, generating 10 variants of customer order phrases for chatbot training, then testing and refining the best performers. This iterative approach helps discover effective prompts that humans might not consider, automating the optimization process.

- `@article` [Automatic Prompt Engineer - DAIR.AI](https://www.promptingguide.ai/techniques/ape)

#### Self-Consistency Prompting

Self-consistency prompting generates multiple reasoning paths for the same problem using higher temperature settings, then selects the most commonly occurring answer through majority voting. This technique combines sampling and voting to improve accuracy and provides pseudo-probability of answer correctness. While more expensive due to multiple API calls, it significantly enhances reliability for complex reasoning tasks by reducing the impact of single incorrect reasoning chains and leveraging diverse problem-solving approaches.

- `@article` [Self-Consistency - DAIR.AI](https://www.promptingguide.ai/techniques/consistency)
- `@article` [Self-Consistency - LearnPrompting](https://learnprompting.org/docs/intermediate/self_consistency)

## Common Terminology

#### LLM

Large Language Models (LLMs) are AI systems trained on vast text data to understand and generate human-like language. They work as prediction engines, analyzing input and predicting the next most likely token. LLMs perform tasks like text generation, translation, summarization, and Q&A. Understanding token processing is key to effective prompt engineering.

- `@official` [LLM - Anthropic Glossary](https://platform.claude.com/docs/en/about-claude/glossary)
- `@article` [Differences Between Chatbots and LLMs - LearnPrompting](https://learnprompting.org/docs/basics/chatbot_basics)

#### Tokens

Tokens are fundamental units of text that LLMs process, created by breaking down text into smaller components like words, subwords, or characters. Understanding tokens is crucial because models predict the next token in sequences, API costs are based on token count, and models have maximum token limits for input and output.

- `@article` [Understanding tokens - Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/ai/conceptual/understanding-tokens)
- `@article` [What Are Tokens in LLMs and Why They Matter - LLM Guides](https://llmguides.ai/learn/what-are-tokens/)

#### Context Window

Context window refers to the maximum number of tokens an LLM can process in a single interaction, including both input prompt and generated output. When exceeded, older parts are truncated. Understanding this constraint is crucial for prompt engineering—you must balance providing sufficient context with staying within token limits.

- `@official` [Context windows - Anthropic](https://platform.claude.com/docs/en/build-with-claude/context-windows)
- `@article` [What is a context window? - IBM](https://www.ibm.com/think/topics/context-window)

#### Hallucination

Hallucination in LLMs refers to generating plausible-sounding but factually incorrect or fabricated information. This occurs when models fill knowledge gaps or present uncertain information with apparent certainty. Mitigation techniques include requesting sources, asking for confidence levels, providing context, and always verifying critical information independently.

- `@official` [Reduce hallucinations - Anthropic](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)
- `@article` [What are AI hallucinations? - IBM](https://www.ibm.com/think/topics/ai-hallucinations)

#### Agents

AI agents are autonomous systems that use LLMs to reason, plan, and take actions to achieve specific goals. They combine language understanding with tool usage, memory, and decision-making to perform complex, multi-step tasks. Agents can interact with external APIs and services while maintaining context across interactions.

- `@official` [Tool use overview - Anthropic](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)
- `@article` [Introduction to AI Agents - DAIR.AI](https://www.promptingguide.ai/agents/introduction)

#### Prompt Injection

Prompt injection is a security vulnerability where malicious users manipulate LLM inputs to override intended behavior, bypass safety measures, or extract sensitive information. Attackers embed instructions within data to make models ignore original prompts and follow malicious commands. Mitigation requires input sanitization, injection-resistant prompt design, and proper security boundaries.

- `@official` [Mitigate jailbreaks and prompt injections - Anthropic](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks)
- `@official` [LLM01:2025 Prompt Injection - OWASP](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)
- `@course` [Prompt Injection: Hands-on Exercise Against a Live Assistant](https://ransomleak.com/exercises/clawdbot-prompt-injection/)
- `@video` [What Is a Prompt Injection Attack?](https://www.youtube.com/watch?v=jrHRe9lSqqA)

#### Model Weights / Parameters

Model weights and parameters are the learned values that define an LLM's behavior and knowledge. Parameters are the trainable variables adjusted during training, while weights represent their final values. Understanding parameter count helps gauge model capabilities - larger models typically have more parameters and better performance but require more computational resources.

- `@article` [What are LLM parameters? - IBM](https://www.ibm.com/think/topics/llm-parameters)

#### Fine-Tuning vs Prompt Engg.

Fine-tuning trains models on specific data to specialize behavior, while prompt engineering achieves customization through input design without model modification. Prompt engineering is faster, cheaper, and more accessible. Fine-tuning offers deeper customization but requires significant resources and expertise.

- `@article` [When to use prompt engineering vs. fine-tuning - TechTarget](https://www.techtarget.com/searchEnterpriseAI/tip/Prompt-engineering-vs-fine-tuning-Whats-the-difference)
- `@article` [Prompt Engineering vs Fine Tuning: When to Use Each - Codecademy](https://www.codecademy.com/article/prompt-engineering-vs-fine-tuning)

#### AI vs AGI

AI (Artificial Intelligence) refers to systems that perform specific tasks intelligently, while AGI (Artificial General Intelligence) represents hypothetical AI with human-level reasoning across all domains. Current LLMs are narrow AI - powerful at language tasks but lacking true understanding or general intelligence like AGI would possess.

- `@article` [Artificial general intelligence - Wikipedia](https://en.wikipedia.org/wiki/Artificial_general_intelligence)

#### RAG

Retrieval-Augmented Generation (RAG) combines LLMs with external knowledge retrieval to ground responses in verified, current information. RAG retrieves relevant documents before generating responses, reducing hallucinations and enabling access to information beyond the model's training cutoff. This approach improves accuracy and provides source attribution.

- `@opensource` [Introduction to RAG - LlamaIndex](https://developers.llamaindex.ai/python/framework/understanding/rag/)
- `@article` [Retrieval Augmented Generation (RAG) - DAIR.AI](https://www.promptingguide.ai/techniques/rag)

## Models offered by ____

#### OpenAI

OpenAI develops leading language models including GPT-5.4, o3, and Codex, setting industry standards for prompt engineering. Their API provides access to frontier models with configurable parameters, and their Agents SDK enables building autonomous AI systems. The OpenAI Cookbook and platform documentation are key references for prompt engineering best practices.

- `@official` [OpenAI API Documentation](https://developers.openai.com/api/docs)
- `@official` [OpenAI Cookbook (GitHub)](https://github.com/openai/openai-cookbook)

#### Google

Google develops Gemini, a family of multimodal AI models. The latest flagship, Gemini 3, supports text, image, video, and audio through the Gemini API and Google AI Studio. Google also offers specialized models including Imagen for image generation, Veo for video, and Lyria 3 for music. Their research has advanced many prompt engineering techniques, including Chain of Thought reasoning.

- `@official` [Google AI Studio](https://ai.google.dev/)
- `@official` [Gemini API Documentation](https://ai.google.dev/gemini-api/docs)

#### Anthropic

Anthropic develops Claude, a family of large language models focused on safety and helpfulness. The current lineup includes Claude Opus 4.7 (most capable, for complex reasoning and agentic coding), Claude Sonnet 4.6 (best speed-intelligence balance), and Claude Haiku 4.5 (fastest, near-frontier intelligence). All models support extended thinking, vision, and 1M token context windows.

- `@roadmap` [Visit the Dedicated Claude Code Roadmap](https://roadmap.sh/claude-code)
- `@official` [Claude API Documentation](https://docs.anthropic.com/en/docs/intro)
- `@official` [Anthropic Research](https://www.anthropic.com/research)

#### Meta

Meta develops the Llama family of open-source large language models. The latest release, Llama 4, comes in Maverick and Scout variants with strong multimodal and long-context capabilities. Llama models are freely available for research and commercial use, providing transparency in training data and architecture without vendor lock-in.

- `@official` [Llama](https://www.llama.com/)
- `@opensource` [Llama Models (GitHub)](https://github.com/meta-llama/llama-models)

#### xAI

xAI develops Grok, a conversational AI model with real-time web access and integration with X (Twitter). The latest model, Grok 4.20, features a 2M token context window, agentic tool calling, and industry-leading low hallucination rates. Grok focuses on delivering truthful, unfiltered responses with strict prompt adherence.

- `@official` [xAI Documentation](https://docs.x.ai/)
- `@official` [xAI API Console](https://console.x.ai)

### Sampling Parameters

Sampling parameters (temperature, top-K, top-P) control how LLMs select tokens from probability distributions, determining output randomness and creativity. These parameters interact: at extreme settings, one can override others (temperature 0 makes top-K/top-P irrelevant). A balanced starting point is temperature 0.2, top-P 0.95, top-K 30 for coherent but creative results. Understanding their interactions is crucial for optimal prompting—use temperature 0 for factual tasks, higher values for creativity, and combine settings strategically based on your specific use case.

- `@article` [LLM Settings (Temperature, Top-K, Top-P) - DAIR.AI](https://www.promptingguide.ai/introduction/settings)

#### Temperature

Temperature controls the randomness in token selection during text generation. Lower values (0-0.3) produce deterministic, factual outputs. Medium values (0.5-0.7) balance creativity and coherence. Higher values (0.8-1.0) generate creative, diverse outputs but may be less coherent. Use low temperature for math/facts, high for creative writing.

- `@article` [What is LLM Temperature? - IBM](https://www.ibm.com/think/topics/llm-temperature)
- `@article` [Temperature - LLM Parameter Guide - Vellum](https://www.vellum.ai/llm-parameters/temperature)

#### Top-K

Top-K restricts token selection to the K most likely tokens from the probability distribution. Low values (1-10) produce conservative, factual outputs. Medium values (20-50) balance creativity and quality. High values (50+) enable diverse, creative outputs. Use low K for technical tasks, high K for creative writing.

- `@official` [Gemini API Prompting Strategies - Google](https://ai.google.dev/gemini-api/docs/prompting-strategies)
- `@article` [Top K - LLM Parameter Guide - Vellum](https://www.vellum.ai/llm-parameters/top-k)

#### Top-P

Top-P (nucleus sampling) selects tokens from the smallest set whose cumulative probability exceeds threshold P. Unlike Top-K's fixed number, Top-P dynamically adjusts based on probability distribution. Low values (0.1-0.5) produce focused outputs, medium (0.6-0.9) balance creativity and coherence, high (0.9-0.99) enable creative diversity.

- `@article` [Top P - LLM Parameter Guide - Vellum](https://www.vellum.ai/llm-parameters/top-p)

#### Max Tokens

Max tokens setting controls the maximum number of tokens an LLM can generate in response, directly impacting computation cost, response time, and energy consumption. Setting lower limits doesn't make models more concise—it simply stops generation when the limit is reached. This parameter is crucial for techniques like ReAct where models might generate unnecessary tokens after the desired response. Balancing max tokens involves considering cost efficiency, response completeness, and application requirements while ensuring critical information isn't truncated.

- `@official` [Token Counting - Anthropic](https://platform.claude.com/docs/en/build-with-claude/token-counting)
- `@article` [Max Tokens - LLM Parameter Guide - Vellum](https://www.vellum.ai/llm-parameters/max-tokens)

#### Stop Sequences

Stop sequences are specific strings that signal the LLM to stop generating text when encountered, providing precise control over output length and format. Common examples include newlines, periods, or custom markers like "###" or "END". This parameter is particularly useful for structured outputs, preventing models from generating beyond intended boundaries. Stop sequences are essential for ReAct prompting and other scenarios where you need clean, precisely bounded responses. They offer more control than max tokens by stopping at logical breakpoints rather than arbitrary token limits.

- `@official` [Handling Stop Reasons - Anthropic](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons)
- `@article` [Stop Sequence - LLM Parameter Guide - Vellum](https://www.vellum.ai/llm-parameters/stop-sequence)

### Repetition Penalties

Repetition penalties discourage LLMs from repeating words or phrases by reducing the probability of selecting previously used tokens. This includes frequency penalty (scales with usage count) and presence penalty (applies equally to any used token). These parameters improve output quality by promoting vocabulary diversity and preventing redundant phrasing.

- `@article` [Tips for Writing Better Prompts - LearnPrompting](https://learnprompting.org/docs/basics/ai_prompt_tips)

#### Frequency Penalty

Frequency penalty reduces token probability based on how frequently they have appeared in the text, with higher penalties for more frequent tokens. This prevents excessive repetition and encourages varied language use. The penalty scales with usage frequency, making overused words less likely to be selected again, improving content diversity.

- `@article` [Frequency Penalty - LLM Parameter Guide - Vellum](https://www.vellum.ai/llm-parameters/frequency-penalty)

#### Presence Penalty

Presence penalty reduces the likelihood of repeating tokens that have already appeared in the text, encouraging diverse vocabulary usage. Unlike frequency penalty which considers how often tokens appear, presence penalty applies the same penalty to any previously used token, promoting varied content and creativity.

- `@article` [Presence Penalty - LLM Parameter Guide - Vellum](https://www.vellum.ai/llm-parameters/presence-penalty)

## System / Role / Contextual

#### System Prompting

System prompting sets the overall context, purpose, and operational guidelines for LLMs. It defines the model's role, behavioral constraints, output format requirements, and safety guardrails. System prompts provide foundational parameters that influence all subsequent interactions, ensuring consistent, controlled, and structured AI responses throughout the session.

- `@official` [Prompt Engineering Overview - Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)
- `@article` [Instructions - LearnPrompting](https://learnprompting.org/docs/basics/instructions)

#### Role Prompting

Role prompting assigns a specific character, identity, or professional role to the LLM to generate responses consistent with that role's expertise, personality, and communication style. By establishing roles like "teacher," "travel guide," or "software engineer," you provide the model with appropriate domain knowledge, perspective, and tone for more targeted, natural interactions.

- `@article` [Assigning Roles to Chatbots - LearnPrompting](https://learnprompting.org/docs/basics/roles)
- `@article` [Role Prompting - LearnPrompting](https://learnprompting.org/docs/advanced/zero_shot/role_prompting)
- `@video` [Context Engineering vs. Prompt Engineering: Smarter AI with RAG & Agents](https://youtu.be/vD0E3EUb8-8?si=9orzEniOGmRD7g-o&t=136)

#### Contextual Prompting

Contextual prompting provides specific background information or situational details relevant to the current task, helping LLMs understand nuances and tailor responses accordingly. Unlike system or role prompts, contextual prompts supply immediate, task-specific information that's dynamic and changes based on the situation. For example: "Context: You are writing for a blog about retro 80's arcade video games. Suggest 3 topics to write articles about." This technique ensures responses are relevant, accurate, and appropriately framed for the specific context provided.

- `@official` [Prompting Best Practices - Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- `@article` [Prompt Structure and Key Parts - LearnPrompting](https://learnprompting.org/docs/basics/prompt_structure)

## Use LLM to generate Prompts

#### Tree of Thoughts (ToT) Prompting

Tree of Thoughts (ToT) generalizes Chain of Thought by allowing LLMs to explore multiple reasoning paths simultaneously rather than following a single linear chain. This approach maintains a tree structure where each thought represents a coherent step toward solving a problem, enabling the model to branch out and explore different reasoning directions. ToT is particularly effective for complex tasks requiring exploration and is well-suited for problems that benefit from considering multiple solution approaches before converging on the best answer.

- `@article` [Tree of Thoughts - DAIR.AI](https://www.promptingguide.ai/techniques/tot)

#### ReAct Prompting

ReAct (Reason and Act) prompting enables LLMs to solve complex tasks by combining reasoning with external tool interactions. It follows a thought-action-observation loop: analyze the problem, perform actions using external APIs, review results, and iterate until solved. Useful for research, multi-step problems, and tasks requiring current data.

- `@article` [ReAct - DAIR.AI](https://www.promptingguide.ai/techniques/react)
- `@article` [ReAct: Synergizing Reasoning and Acting - LearnPrompting](https://learnprompting.org/docs/techniques/react)
- `@video` [4 Methods of Prompt Engineering](https://youtu.be/vD0E3EUb8-8?si=Y6MCLPzjmhMB4jSu&t=203)

#### Prompt Tuning

### AI Red Teaming

AI red teaming involves deliberately testing AI systems to find vulnerabilities, biases, or harmful behaviors through adversarial prompting. Teams attempt to make models produce undesired outputs, bypass safety measures, or exhibit problematic behaviors. This process helps identify weaknesses and improve AI safety and robustness before deployment.

- `@roadmap` [Visit the Dedicated AI Red Teaming Roadmap](https://roadmap.sh/ai-red-teaming)

## — Experiment with input formats and writing styles

#### Prompt Debiasing

Prompt debiasing involves techniques to reduce unwanted biases in LLM outputs by carefully crafting prompts. This includes using neutral language, diverse examples, and explicit instructions to avoid stereotypes or unfair representations. Effective debiasing helps ensure AI outputs are fairer, inclusive, and more representative across different groups and perspectives.

- `@article` [Prompt Debiasing - LearnPrompting](https://learnprompting.org/docs/reliability/debiasing)

## — Tune sampling (temperature, top-k, top-p) for determinism vs creativity

#### Prompt Ensembling

Prompt ensembling combines multiple different prompts or prompt variations to improve output quality and consistency. This technique involves running the same query with different prompt formulations and aggregating results through voting, averaging, or selection. Ensembling reduces variance and increases reliability by leveraging diverse prompt perspectives.

- `@article` [Introduction to Ensembling - LearnPrompting](https://learnprompting.org/docs/advanced/ensembling/introduction)

## — Automate evaluation; integrate unit tests for outputs

#### LLM Self Evaluation

LLM self-evaluation involves prompting models to assess their own outputs for quality, accuracy, or adherence to criteria. This technique can identify errors, rate confidence levels, or check if responses meet specific requirements. Self-evaluation helps improve output quality through iterative refinement and provides valuable feedback for prompt optimization.

- `@article` [LLM Self-Evaluation - LearnPrompting](https://learnprompting.org/docs/reliability/lm_self_eval)

## — Document and track prompt versions

#### Calibrating LLMs

Calibrating LLMs involves adjusting models so their confidence scores accurately reflect their actual accuracy. Well-calibrated models express appropriate uncertainty - being confident when correct and uncertain when likely wrong. This helps users better trust and interpret model outputs, especially in critical applications where uncertainty awareness is crucial.

- `@article` [Calibrating LLMs - LearnPrompting](https://learnprompting.org/docs/reliability/calibration)
