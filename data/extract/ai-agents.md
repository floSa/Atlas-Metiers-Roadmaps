# AI Agents — plan extrait

- **Slug** : `ai-agents`
- **Description amont** : Learn to design, build and ship AI agents in @currentYear@
- **Derniere modification amont** : 2026-03-09T11:24:39.307Z
- **Capture** : 2026-09-16
- **Volume** : 101 noeuds de contenu, 101 documentes, 305 ressources
- **Renvois vers d'autres roadmaps** : `https://roadmap.sh`, `https://roadmap.sh/ai-data-scientist`, `https://roadmap.sh/ai-engineer`, `https://roadmap.sh/api-design`, `https://roadmap.sh/backend?r=backend-beginner`, `https://roadmap.sh/git-github?r=git-github-beginner`, `https://roadmap.sh/prompt-engineering`

---

## Learn the Pre-requisites

### Basic Backend Development

Before you start learning how to build AI agents, we would recommend you to have a basic knowledge of Backend development. This includes, programming language knowledge, interacting with database and basics of APIs at minimum.

- `@article` [Introduction to the server-side](https://developer.mozilla.org/en-US/docs/Learn/Server-side/First_steps/Introduction)
- `@article` [What is a REST API? - Red Hat](https://www.redhat.com/en/topics/api/what-is-a-rest-api)
- `@article` [What is a Database? - Oracle](https://www.oracle.com/database/what-is-database/)

### Git and Terminal Usage

Git and the terminal are key tools for AI agents and developers. Git lets you track changes in code, work with branches, and collaborate safely with others. It stores snapshots of your work so you can undo mistakes or merge ideas. The terminal (command line) lets you move around files, run programs, set up servers, and control tools like Git quickly without a GUI.

- `@official` [Git Basics](https://git-scm.com/doc)
- `@official` [Introduction to the Terminal](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview)
- `@video` [Git and Terminal Basics Crash Course (YouTube)](https://www.youtube.com/watch?v=HVsySz-h9r4)

### Streamed vs Unstreamed Responses

An unstreamed response waits until the model finishes generating the entire output before returning anything to the caller. A streamed response sends tokens back as they are generated, so the caller can start displaying or processing output immediately. Streaming improves perceived responsiveness in user facing applications, while unstreamed responses are simpler to handle when the full output is needed before continuing.

- `@article` [Streaming Responses in AI: How AI Outputs Are Generated in Real Time](https://dev.to/pranshu_kabra_fe98a73547a/streaming-responses-in-ai-how-ai-outputs-are-generated-in-real-time-18kb)
- `@article` [AI for Web Devs: Faster Responses with HTTP Streaming](https://austingil.com/ai-for-web-devs-streaming/)
- `@article` [Master the OpenAI API: Stream Responses](https://www.toolify.ai/gpts/master-the-openai-api-stream-responses-139447)

### REST API Knowledge

REST APIs serve as a standardized way for different software systems to communicate with each other over the internet using HTTP requests. They allow an application to send data or request specific actions from a web server by using common methods like GET, POST, PUT, and DELETE. Understanding these protocols is essential for enabling an agent to interact with external tools, fetch real-time information, and perform tasks across various web-based services.

- `@article` [What is RESTful API? - RESTful API Explained - AWS](https://aws.amazon.com/what-is/restful-api/)
- `@article` [What Is a REST API? Examples, Uses & Challenges](https://blog.postman.com/rest-api-examples/)

### Reasoning vs Standard Models

Standard models generate a response directly from a prompt, while reasoning models are trained or prompted to work through intermediate steps before producing a final answer. This extra reasoning process tends to improve performance on complex tasks like math or multi-step planning, but it usually costs more tokens and takes longer to respond. Choosing between the two depends on whether the task needs deep step by step reasoning or a fast, direct answer.

- `@official` [ReAct: Synergizing Reasoning and Acting in Language Models](https://react-lm.github.io/)
- `@article` [ReAct Systems: Enhancing LLMs with Reasoning and Action](https://learnprompting.org/docs/agents/react)

### Fine-tuning vs Prompt Engineering

Fine-tuning and prompt engineering are two ways to get better outputs from a language model. Fine-tuning means training an existing model further with your own examples so it adapts to specific tasks. It needs extra data, computing power, and time but creates deeply specialized models. Prompt engineering, in contrast, leaves the model unchanged and focuses on crafting better instructions or examples in the prompt itself. It is faster, cheaper, and safer when no custom data is available. Fine-tuning suits deep domain needs; prompt engineering fits quick control and prototyping.

- `@article` [OpenAI Fine Tuning](https://platform.openai.com/docs/guides/fine-tuning)
- `@article` [Prompt Engineering Guide](https://www.promptingguide.ai/)
- `@article` [Prompt Engineering vs Prompt Tuning: A Detailed Explanation](https://medium.com/@aabhi02/prompt-engineering-vs-prompt-tuning-a-detailed-explanation-19ea8ce62ac4)
- `@video` [RAG vs Fine-Tuning vs Prompt Engineering: Optimizing AI Models](https://youtu.be/zYGDpG-pTho?si=pFeWqbjSN1RM4WiZ)

### Transformer Models and LLMs

Transformers are a neural network architecture that process sequences of tokens using a mechanism called attention, which lets the model weigh the relevance of different parts of the input to each other. Large language models (LLMs) are transformers trained on massive amounts of text to predict the next token in a sequence. This next token prediction, repeated many times, is what lets an LLM generate coherent text, answer questions, and follow instructions.

- `@article` [Exploring Open Source AI Models: LLMs and Transformer Architectures](https://llmmodels.org/blog/exploring-open-source-ai-models-llms-and-transformer-architectures/)
- `@article` [How Transformer LLMs Work](https://www.deeplearning.ai/short-courses/how-transformer-llms-work/)

### Embeddings and Vector Search

Embeddings turn words, pictures, or other data into lists of numbers called vectors. Each vector keeps the meaning of the original item. Things with similar meaning get vectors that sit close together in this number space. Vector search scans a large set of vectors and finds the ones nearest to a query vector, even if the exact words differ. This lets AI agents match questions with answers, suggest related items, and link ideas quickly.

- `@official` [OpenAI Embeddings API Documentation](https://platform.openai.com/docs/guides/embeddings/what-are-embeddings)
- `@article` [Understanding Embeddings and Vector Search (Pinecone Blog)](https://www.pinecone.io/learn/vector-embeddings/)

### Open Weight Models

Open weight models are language models whose trained parameters are published for anyone to download, run, and fine-tune, examples include Llama and Mistral. Because the weights are available, developers can self host these models, modify them, and avoid relying on a third party API. This gives more control over cost, data privacy, and customization, at the expense of needing your own infrastructure.

- `@official` [BLOOM BigScience](https://bigscience.huggingface.co/)
- `@official` [Falcon LLM – Technology Innovation Institute (TII)](https://falconllm.tii.ae/)
- `@official` [Llama 2 – Meta's Official Announcement](https://ai.meta.com/llama/)
- `@official` [Hugging Face – Open LLM Leaderboard (Top Open Models)](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
- `@official` [EleutherAI – Open Research Collective (GPT-Neo, GPT-J, etc.)](https://www.eleuther.ai/)

### Understand the Basics of RAG

Retrieval Augmented Generation (RAG) is a technique where relevant documents or data are fetched from an external source and added to a model's prompt before it generates a response. This lets the model answer questions using information it was not originally trained on, such as private documents or recent data. RAG typically combines a retrieval step, often using vector search, with a generation step handled by the LLM.

- `@article` [What Is RAG in AI and How to Use It?](https://www.v7labs.com/blog/what-is-rag)
- `@article` [An Introduction to RAG and Simple & Complex RAG](https://medium.com/enterprise-rag/an-introduction-to-rag-and-simple-complex-rag-9c3aa9bd017b)
- `@video` [Learn RAG From Scratch](https://www.youtube.com/watch?v=sVcwVQRHIc8)
- `@video` [What is Retrieval-Augmented Generation (RAG)?](https://www.youtube.com/watch?v=T-D1OfcDW1M)

### Closed Weight Models

Closed weight models are language models accessed only through an API, with the underlying weights kept private by the provider, examples include GPT-4 and Claude. Developers send requests and receive outputs without ever handling the model itself. This approach removes the need to manage infrastructure but ties usage to the provider's pricing, rate limits, and terms of service.

- `@official` [Open AI's GPT-4](https://openai.com/gpt-4)
- `@official` [Claude](https://www.anthropic.com/claude)
- `@official` [Gemini](https://deepmind.google/technologies/gemini/)
- `@article` [Open-Source LLMs vs Closed LLMs](https://hatchworks.com/blog/gen-ai/open-source-vs-closed-llms-guide/)
- `@article` [2024 Comparison of Open-Source Vs Closed-Source LLMs](https://blog.spheron.network/choosing-the-right-llm-2024-comparison-of-open-source-vs-closed-source-llms)

### Pricing of Common Models

Different LLM providers charge different rates per million input and output tokens, and prices vary widely between model sizes and capability tiers. Comparing pricing across common models like GPT, Claude, and Gemini helps in picking a model that fits both the task's quality requirements and the project's budget. Costs can shift quickly as providers release new models, so pricing should be checked against current rate cards rather than assumed.

- `@official` [OpenAI Pricing](https://openai.com/api/pricing/)
- `@article` [Executive Guide To AI Agent Pricing](https://www.forbes.com/councils/forbesbusinesscouncil/2025/01/28/executive-guide-to-ai-agent-pricing-winning-strategies-and-models-to-drive-growth/)
- `@article` [AI Pricing: How Much Does Artificial Intelligence Cost In 2025?](https://www.internetsearchinc.com/ai-pricing-how-much-does-artificial-intelligence-cost/)

#### Perception / User Input

Perception, also called user input, is the first step in an agent loop. The agent listens and gathers data from the outside world. This data can be text typed by a user, spoken words, camera images, sensor readings, or web content pulled through an API. The goal is to turn raw signals into a clear, usable form. The agent may clean the text, translate speech to text, resize an image, or drop noise from sensor values. Good perception means the agent starts its loop with facts, not guesses. If the input is wrong or unclear, later steps will also fail. So careful handling of perception keeps the whole agent loop on track.

- `@article` [Perception in AI: Understanding Its Types and Importance](https://marktalks.com/perception-in-ai-understanding-its-types-and-importance/)
- `@article` [What Is AI Agent Perception? - IBM](https://www.ibm.com/think/topics/ai-agent-perception)

## Model Mechanis

#### Tokenization

Tokenization is the process of breaking text into smaller units called tokens, which can be whole words, parts of words, or individual characters depending on the tokenizer. A language model does not read raw text, it reads a sequence of token IDs mapped from these units. The choice of tokenizer affects how many tokens a piece of text uses, which in turn affects cost and context limits.

- `@article` [Explaining Tokens — the Language and Currency of AI](https://blogs.nvidia.com/blog/ai-tokens-explained/)
- `@article` [What is Tokenization? Types, Use Cases, Implementation](https://www.datacamp.com/blog/what-is-tokenization)

#### Context Windows

 
The context window is the maximum number of tokens a model can process in a single request, including both the input and the generated output. Anything beyond this limit gets truncated or causes an error, so long conversations or documents need to be managed carefully. A larger context window lets an agent keep more history, tool outputs, or retrieved documents in view at once.

- `@article` [What is a Context Window in AI?](https://www.ibm.com/think/topics/context-window)
- `@article` [Scaling Language Models with Retrieval-Augmented Generation (RAG)](https://arxiv.org/abs/2005.11401)
- `@article` [Long Context in Language Models - Anthropic's Claude 3](https://www.anthropic.com/news/claude-3-family)

#### Token Based Pricing

Token-based pricing is how many language-model services charge for use. A token is a small chunk of text, roughly four characters or part of a word. The service counts every token that goes into the model (your prompt) and every token that comes out (the reply). It then multiplies this total by a listed price per thousand tokens. Some plans set one price for input tokens and a higher or lower price for output tokens. Because the bill grows with each token, users often shorten prompts, trim extra words, or cap response length to spend less.

- `@article` [Explaining Tokens — the Language and Currency of AI](https://blogs.nvidia.com/blog/ai-tokens-explained/)
- `@article` [What Are AI Tokens?](https://methodshop.com/what-are-ai-tokens/)
- `@article` [Pricing - OpenAI](https://openai.com/api/pricing/)

## Generation Controls

#### Temperature

Temperature is a setting that changes how random or predictable an AI model’s text output is. The value usually goes from 0 to 1, sometimes higher. A low temperature, close to 0, makes the model pick the most likely next word almost every time, so the answer is steady and safe but can feel dull or repetitive. A high temperature, like 0.9 or 1.0, lets the model explore less-likely word choices, which can give fresh and creative replies, but it may also add mistakes or drift off topic. By adjusting temperature, you balance reliability and creativity to fit the goal of your task.

- `@article` [What Temperature Means in Natural Language Processing and AI](https://thenewstack.io/what-temperature-means-in-natural-language-processing-and-ai/)
- `@article` [LLM Temperature: How It Works and When You Should Use It](https://www.vellum.ai/llm-parameters/temperature)
- `@article` [What is LLM Temperature? - IBM](https://www.ibm.com/think/topics/llm-temperature)
- `@article` [How Temperature Settings Transform Your AI Agent's Responses](https://docsbot.ai/article/how-temperature-settings-transform-your-ai-agents-responses)

#### Top-p

Top-p, also called nucleus sampling, is a setting that guides how an LLM picks its next word. The model lists many possible words and sorts them by probability. It then finds the smallest group of top words whose combined chance adds up to the chosen p value, such as 0.9. Only words inside this group stay in the running; the rest are dropped. The model picks one word from the kept group at random, weighted by their original chances. A lower p keeps only the very likely words, so output is safer and more focused. A higher p lets in less likely words, adding surprise and creativity but also more risk of error.

- `@article` [Nucleus Sampling](https://nn.labml.ai/sampling/nucleus.html)
- `@article` [Sampling Techniques in Large Language Models (LLMs)](https://medium.com/@shashankag14/understanding-sampling-techniques-in-large-language-models-llms-dfc28b93f518)
- `@article` [Temperature, top_p and top_k for chatbot responses](https://community.openai.com/t/temperature-top-p-and-top-k-for-chatbot-responses/295542)

#### Frequency Penalty

Frequency penalty reduces the likelihood of the model repeating tokens it has already used, with the penalty growing the more often a token appears. This discourages repetitive phrases and loops in longer generations. It is commonly tuned when a model produces text that gets stuck repeating the same words or ideas.

- `@article` [Understanding Frequency Penalty and Presence Penalty](https://medium.com/@the_tori_report/understanding-frequency-penalty-and-presence-penalty-how-to-fine-tune-ai-generated-text-e5e4f5e779cd)

#### Presence Penalty

Presence penalty is a setting you can adjust when you ask a large language model to write. It pushes the model to choose words it has not used yet. Each time a word has already appeared, the model gets a small score cut for picking it again. A higher penalty gives bigger cuts, so the model looks for new words and fresh ideas. A lower penalty lets the model reuse words more often, which can help with repeats like rhymes or bullet lists. Tuning this control helps you steer the output toward either more variety or more consistency.

- `@article` [Understanding Presence Penalty and Frequency Penalty](https://medium.com/@pushparajgenai2025/understanding-presence-penalty-and-frequency-penalty-in-openai-chat-completion-api-calls-2e3a22547b48)
- `@article` [Difference between Frequency and Presence Penalties?](https://community.openai.com/t/difference-between-frequency-and-presence-penalties/2777)
- `@article` [LLM Parameters Explained: A Practical Guide with Examples](https://learnprompting.org/blog/llm-parameters)

#### Stopping Criteria

Stopping criteria tell the language model when to stop writing more text. Without them, the model could keep adding words forever, waste time, or spill past the point we care about. Common rules include a maximum number of tokens, a special end-of-sequence token, or a custom string such as `“\n\n”`. We can also stop when the answer starts to repeat or reaches a score that means it is off topic. Good stopping rules save cost, speed up replies, and avoid nonsense or unsafe content.

- `@article` [Defining Stopping Criteria in Large Language Models](https://www.metriccoders.com/post/defining-stopping-criteria-in-large-language-models-a-practical-guide)

#### Max Length

Max Length sets the maximum number of tokens a language model can generate in one reply. Tokens are pieces of text—roughly 100 tokens equals a short paragraph. A small limit saves time and cost but risks cutting answers short. A large limit allows full, detailed replies but needs more compute and can lose focus. Choose limits based on the task: short limits for tweets, longer ones for articles. Tuning Max Length carefully helps balance clarity, speed, and cost.

- `@article` [Utilising Max Token Context Window of Anthropic Claude](https://medium.com/@nampreetsingh/utilising-max-token-context-window-of-anthropic-claude-on-amazon-bedrock-7377d94b2dfa)
- `@article` [Controlling the Length of OpenAI Model Responses](https://help.openai.com/en/articles/5072518-controlling-the-length-of-openai-model-responses)
- `@article` [Max Model Length in AI](https://www.restack.io/p/ai-model-answer-max-model-length-cat-ai)
- `@video` [Understanding ChatGPT/OpenAI Tokens](https://youtu.be/Mo3NV5n1yZk)

## 1

#### Reason and Plan

Reason and Plan is the moment when an AI agent thinks before it acts. The agent starts with a goal and the facts it already knows. It looks at these facts and asks, “What do I need to do next to reach the goal?” It breaks the goal into smaller steps, checks if each step makes sense, and orders them in a clear path. The agent may also guess what could go wrong and prepare backup steps. Once the plan feels solid, the agent is ready to move on and take the first action.

- `@official` [ReAct: Synergizing Reasoning and Acting in Language Models](https://react-lm.github.io/)
- `@article` [ReAct Systems: Enhancing LLMs with Reasoning and Action](https://learnprompting.org/docs/agents/react)

## 2

#### Acting / Tool Invocation

Acting, also called tool invocation, is the step where the AI chooses a tool and runs it to get real-world data or to change something. The agent looks at its current goal and the plan it just made. It then picks the best tool, such as a web search, a database query, or a calculator. The agent fills in the needed inputs and sends the call. The external system does the heavy work and returns a result. Acting ends when the agent stores that result so it can think about the next move.

- `@article` [What are Tools in AI Agents?](https://huggingface.co/learn/agents-course/en/unit1/tools)
- `@article` [What is Tool Calling in Agents?](https://www.useparagon.com/blog/ai-building-blocks-what-is-tool-calling-a-guide-for-pms)

## 3

#### Observation & Reflection

Observation and reflection form the thinking pause in an AI agent’s loop. First, the agent looks at the world around it, gathers fresh data, and sees what has changed. It then pauses to ask, “What does this new information mean for my goal?” During this short check, the agent updates its memory, spots errors, and ranks what matters most. These steps guide wiser plans and actions in the next cycle. Without careful observation and reflection, the agent would rely on old or wrong facts and soon drift off course.

- `@official` [Best Practices for Prompting and Self-checking](https://platform.openai.com/docs/guides/prompt-engineering)
- `@article` [Self-Reflective AI: Building Agents That Learn by Observing Themselves](https://arxiv.org/abs/2302.14045)

## 4

#### What are AI Agents?

An AI agent is a computer program or robot that can sense its surroundings, think about what it senses, and then act to reach a goal. It gathers data through cameras, microphones, or software inputs, decides what the data means using rules or learned patterns, and picks the best action to move closer to its goal. After acting, it checks the results and learns from them, so it can do better next time. Chatbots, self-driving cars, and game characters are all examples.

- `@article` [What are AI Agents? - Agents in Artificial Intelligence Explained](https://aws.amazon.com/what-is/ai-agents/)
- `@article` [AI Agents Explained in Simple Terms for Beginners](https://www.geeky-gadgets.com/ai-agents-explained-for-beginners/)
- `@video` [What are AI Agents?](https://www.youtube.com/watch?v=F8NKVhkZZWI)

### Agent Loop

An agent loop is the cycle that lets an AI agent keep working toward a goal. First, the agent gathers fresh data from its tools, sensors, or memory. Next, it updates its internal state and decides what to do, often by running a planning or reasoning step. Then it carries out the chosen action, such as calling an API, writing to a file, or sending a message. After acting, it checks the result and stores new information. The loop starts again with the latest data, so the agent can adjust to changes and improve over time. This fast repeat of observe–decide–act gives the agent its power.

- `@article` [What is an Agent Loop?](https://huggingface.co/learn/agents-course/en/unit1/agent-steps-and-structure)
- `@article` [Let's Build your Own Agentic Loop](https://www.reddit.com/r/AI_Agents/comments/1js1xjz/lets_build_our_own_agentic_loop_running_in_our/)

#### What are Tools?

Tools are extra skills or resources that an AI agent can call on to finish a job. A tool can be anything from a web search API to a calculator, a database, or a language-translation engine. The agent sends a request to the tool, gets the result, and then uses that result to move forward. Tools let a small core model handle tasks that would be hard or slow on its own. They also help keep answers current, accurate, and grounded in real data. Choosing the right tool and knowing when to use it are key parts of building a smart agent.

- `@article` [Compare 50+ AI Agent Tools in 2025 - AIMultiple](https://research.aimultiple.com/ai-agent-tools/)
- `@article` [AI Agents Explained in Simple Terms for Beginners](https://www.geeky-gadgets.com/ai-agents-explained-for-beginners/)

### What is Prompt Engineering

Prompt engineering is the skill of writing clear questions or instructions so that an AI system gives the answer you want. It means choosing the right words, adding enough detail, and giving examples when needed. A good prompt tells the AI what role to play, what style to use, and what facts to include or avoid. By testing and refining the prompt, you can improve the quality, accuracy, and usefulness of the AI’s response. In short, prompt engineering is guiding the AI with well-designed text so it can help you better.

- `@roadmap` [Visit Dedicated Prompt Engineering Roadmap](https://roadmap.sh/prompt-engineering)
- `@article` [What is Prompt Engineering? - AI Prompt Engineering Explained - AWS](https://aws.amazon.com/what-is/prompt-engineering/)
- `@article` [What is Prompt Engineering? A Detailed Guide For 2025](https://www.datacamp.com/blog/what-is-prompt-engineering-the-future-of-ai-communication)

### Tree-of-Thought

Tree-of-Thought is a way to organize an AI agent’s reasoning as a branching tree. At the root, the agent states the main problem. Each branch is a small idea, step, or guess that could lead to a solution. The agent expands the most promising branches, checks if they make sense, and prunes paths that look wrong or unhelpful. This setup helps the agent explore many possible answers while staying focused on the best ones. Because the agent can compare different branches side by side, it is less likely to get stuck on a bad line of thought. The result is more reliable and creative problem solving.

- `@article` [Tree of Thoughts (ToT) | Prompt Engineering Guide](https://www.promptingguide.ai/techniques/tot)
- `@article` [What is tree-of-thoughts? - IBM](https://www.ibm.com/think/topics/tree-of-thoughts)
- `@article` [The Revolutionary Approach of Tree-of-Thought Prompting in AI](https://medium.com/@WeavePlatform/the-revolutionary-approach-of-tree-of-thought-prompting-in-ai-eb7c0872247b)

### Chain of Thought (CoT)

Chain of Thought (CoT) is a way for an AI agent to think out loud. Before giving its final answer, the agent writes short notes that show each step it takes. These notes can list facts, name sub-tasks, or do small bits of math. By seeing the steps, the agent stays organized and is less likely to make a mistake. People who read the answer can also check the logic and spot any weak points. The same written steps can be fed back into the agent so it can plan, reflect, or fix itself. Because it is easy to use and boosts trust, CoT is one of the most common designs for language-based agents today.

- `@article` [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903)
- `@article` [Evoking Chain of Thought Reasoning in LLMs - Prompting Guide](https://www.promptingguide.ai/techniques/cot)

### Tool Definition

A tool definition describes a function an agent can call, including its name, purpose, and the parameters it accepts, usually specified in a structured format like JSON schema. The language model reads this definition to decide when the tool is relevant and how to fill in its arguments. Clear, well documented tool definitions directly affect how reliably an agent chooses and uses the right tool.

- `@article` [What are Tools? - Hugging Face](https://huggingface.co/learn/agents-course/en/unit1/tools)
- `@article` [Understanding the Agent Function in AI: Key Roles and Responsibilities](https://genezio.com/blog/ai-agents-101-understanding-their-role-and-functionality/)

## Example Usecases

#### Personal assistant

A personal assistant AI agent is a smart program that helps one person manage daily tasks. It can check a calendar, set reminders, and send alerts so you never miss a meeting. It can read emails, highlight key points, and even draft quick replies. If you ask a question, it searches trusted sources and gives a short answer. It can order food, book rides, or shop online when you give simple voice or text commands. Because it learns your habits, it suggests the best time to work, rest, or travel. All these actions run in the background, saving you time and reducing stress.

- `@article` [A Complete Guide on AI-powered Personal Assistants](https://medium.com/@alexander_clifford/a-complete-guide-on-ai-powered-personal-assistants-with-examples-2f5cd894d566)
- `@article` [9 Best AI Personal Assistants for Work, Chat and Home](https://saner.ai/best-ai-personal-assistants/)

#### Code generation

Code-generation agents take a plain language request, understand the goal, and then write or edit source code to meet it. They can build small apps, add features, fix bugs, refactor old code, write tests, or translate code from one language to another. This saves time for developers, helps beginners learn, and reduces human error. Teams use these agents inside code editors, chat tools, and automated pipelines. By handling routine coding tasks, the agents free people to focus on design, logic, and user needs.

- `@official` [GitHub Copilot](https://github.com/features/copilot)
- `@article` [Multi-Agent-based Code Generation](https://arxiv.org/abs/2312.13010)
- `@article` [From Prompt to Production: GitHub Blog](https://github.blog/ai-and-ml/github-copilot/from-prompt-to-production-building-a-landing-page-with-copilot-agent-mode/)

#### Data analysis

AI agents can automate data analysis by pulling information from files, databases, or live streams. They clean the data by spotting missing values, outliers, and making smart corrections. After cleaning, agents find patterns like sales spikes or sensor drops and can build charts or dashboards. Some run basic statistics, others apply machine learning to predict trends. Agents can also send alerts if numbers go beyond set limits, helping people stay informed without constant monitoring.

- `@article` [How AI Will Transform Data Analysis in 2025](https://www.devfi.com/ai-transform-data-analysis-2025/)
- `@article` [How AI Has Changed The World Of Analytics And Data Science](https://www.forbes.com/councils/forbestechcouncil/2025/01/28/how-ai-has-changed-the-world-of-analytics-and-data-science/k)

#### Web Scraping / Crawling

Web scraping and crawling let an AI agent collect data from many web pages without human help. The agent sends a request to a page, reads the HTML, and pulls out parts you ask for, such as prices, news headlines, or product details. It can then follow links on the page to reach more pages and repeat the same steps. This loop builds a large, up-to-date dataset in minutes or hours instead of days. Companies use it to track market prices, researchers use it to gather facts or trends, and developers use it to feed fresh data into other AI models. Good scraping code also respects site rules like robots.txt and avoids hitting servers too fast, so it works smoothly and fairly.

- `@article` [Crawl AI - Build Your AI With One Prompt](https://www.crawlai.org/)
- `@article` [AI-Powered Web Scraper with Crawl4AI and DeepSeek](https://brightdata.com/blog/web-data/crawl4ai-and-deepseek-web-scraping)
- `@article` [Best Web Scraping Tools for AI Applications](https://www.thetoolnerd.com/p/best-web-scraping-tools-for-ai-applications)
- `@article` [8 Best AI Web Scraping Tools I Tried - HubSpot Blog](https://blog.hubspot.com/website/ai-web-scraping)

#### NPC / Game AI

Game studios use AI agents to control non-player characters (NPCs). The agent observes the game state and decides actions like moving, speaking, or fighting. It can shift tactics when the player changes strategy, keeping battles fresh instead of predictable. A quest giver might use an agent to offer hints that fit the player’s progress. In open-world games, agents guide crowds to move around obstacles, set new goals, and react to threats, making towns feel alive. Designers save time by writing broad rules and letting agents fill in details instead of hand-coding every scene. Smarter NPC behavior keeps players engaged and boosts replay value.

- `@official` [Unity – AI for NPCs](https://dev.epicgames.com/documentation/en-us/unreal-engine/artificial-intelligence-in-unreal-engine?application_version=5.3)
- `@article` [AI-Driven NPCs: The Future of Gaming Explained](https://www.capermint.com/blog/everything-you-need-to-know-about-non-player-character-npc/)

## Writing Good Prompts

#### Be specific in what you want

When you ask an AI to do something, clear and exact words help it give the answer you want. State the goal, the format, and any limits up front. Say who the answer is for, how long it should be, and what to leave out. If numbers, dates, or sources matter, name them. For example, rather than “Explain World War II,” try “List three key events of World War II with dates and one short fact for each.” Being this precise cuts down on guesswork, avoids unwanted extra detail, and saves time by reducing follow-up questions.

- `@article` [Prompt Engineering Guide](https://www.promptingguide.ai/)
- `@article` [AI Prompting Examples, Templates, and Tips For Educators](https://honorlock.com/blog/education-ai-prompt-writing/)
- `@article` [How to Ask AI for Anything: The Art of Prompting](https://sixtyandme.com/using-ai-prompts/)

#### Provide additional context

Provide additional context means giving the AI enough background facts, constraints, and goals so it can reply in the way you need. Start by naming the topic and the purpose of the answer. Add who the answer is for, the tone you want, and any limits such as length, format, or style. List key facts, data, or examples that matter to the task. This extra detail stops the model from guessing and keeps replies on target. Think of it like guiding a new teammate: share the details they need, but keep them short and clear.

- `@article` [What is Context in Prompt Engineering?](https://www.godofprompt.ai/blog/what-is-context-in-prompt-engineering)
- `@article` [The Importance of Context for Reliable AI Systems](https://medium.com/mathco-ai/the-importance-of-context-for-reliable-ai-systems-and-how-to-provide-context-009bd1ac7189/)
- `@article` [Context Engineering: Why Feeding AI the Right Context Matters](https://inspirednonsense.com/context-engineering-why-feeding-ai-the-right-context-matters-353e8f87d6d3)

#### Use relevant technical terms

Using relevant technical terms means including precise vocabulary from the domain of the task instead of describing things in vague, general language. A model trained on technical text responds better to prompts phrased the way experts in that field would phrase them. This reduces ambiguity and helps the model retrieve and apply the right knowledge for the task.

- `@article` [AI Terms Glossary: AI Terms To Know In 2024](https://www.moveworks.com/us/en/resources/ai-terms-glossary)
- `@article` [15 Essential AI Agent Terms You Must Know](https://shivammore.medium.com/15-essential-ai-agent-terms-you-must-know-6bfc2f332f6d)
- `@article` [AI Agent Examples & Use Cases: Real Applications in 2025](https://eastgate-software.com/ai-agent-examples-use-cases-real-applications-in-2025/)

#### Use Examples in your Prompt

A clear way to guide an AI is to place one or two short samples inside your prompt. Show a small input and the exact output you expect. The AI studies these pairs and copies their pattern. Use plain words in the sample, keep the format steady, and label each part so the model knows which is which. If you need a list, show a list; if you need a table, include a small table. Good examples cut guesswork, reduce errors, and save you from writing long rules.

- `@article` [10 Real-World AI Agent Examples in 2025](https://www.chatbase.co/blog/ai-agent-examples)
- `@article` [GPT-4.1 Prompting Guide](https://cookbook.openai.com/examples/gpt4-1_prompting_guide)
- `@article` [AI Agent Examples & Use Cases: Real Applications in 2025](https://eastgate-software.com/ai-agent-examples-use-cases-real-applications-in-2025/)

#### Iterate and Test your Prompts

After you write a first prompt, treat it as a draft, not the final version. Run it with the AI, check the output, and note what is missing, wrong, or confusing. Change one thing at a time, such as adding an example, a limit on length, or a tone request. Test again and see if the result gets closer to what you want. Keep a record of each change and its effect, so you can learn patterns that work. Stop when the output is clear, correct, and repeatable. This loop of try, observe, adjust, and retry turns a rough prompt into a strong one.

- `@course` [Prompt Engineering Best Practices](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/)
- `@article` [Master Iterative Prompting: A Guide](https://blogs.vreamer.space/master-iterative-prompting-a-guide-to-more-effective-interactions-with-ai-50a736eaec38)
- `@video` [Prompt Engineering: The Iterative Process](https://www.youtube.com/watch?v=dOxUroR57xs)

#### Specify Length, format etc

When you give a task to an AI, make clear how long the answer should be and what shape it must take. Say “Write 120 words” or “Give the steps as a numbered list.” If you need a table, state the column names and order. If you want bullet points, mention that. Telling the AI to use plain text, JSON, or markdown stops guesswork and saves time. Clear limits on length keep the reply focused. A fixed format makes it easier for people or other software to read and use the result. Always put these rules near the start of your prompt so the AI sees them as important.

- `@article` [Mastering Prompt Engineering: Format, Length, and Audience](https://techlasi.com/savvy/mastering-prompt-engineering-format-length-and-audience-examples-for-2024/)
- `@article` [Ultimate Guide to Prompt Engineering](https://promptdrive.ai/prompt-engineering/)

## Examples of Tools

#### Web Search

Web search lets an AI agent pull fresh facts, news, and examples from the internet while it is working. The agent turns a user request into search words, sends them to a search engine, and reads the list of results. It then follows the most promising links, grabs the page text, and picks out the parts that answer the task. This helps the agent handle topics that were not in its training data, update old knowledge, or double-check details. Web search covers almost any subject and is much faster than manual research, but the agent must watch for ads, bias, or wrong pages and cross-check sources to stay accurate.

- `@article` [8 Best AI Search Engines for 2025](https://usefulai.com/tools/ai-search-engines)
- `@article` [Web Search Agent - PraisonAI Documentation](https://docs.praison.ai/agents/websearch)

#### Code Execution / REPL

A code execution or REPL tool lets an agent run code and see the actual result, rather than only generating code as text. This is useful for tasks like calculations, data processing, or verifying that generated code works before presenting it. Giving an agent this tool turns it from something that writes code into something that can test and correct its own output.

- `@article` [What is a REPL?](https://docs.replit.com/getting-started/intro-replit)
- `@article` [Code Execution AI Agent](https://docs.praison.ai/features/codeagent)
- `@article` [Building an AI Agent's Code Execution Environment](https://murraycole.com/posts/ai-code-execution-environment)
- `@article` [Python Code Tool](https://python.langchain.com/docs/integrations/tools/python/)

#### Database Queries

Database queries let an AI agent fetch, add, change, or remove data stored in a database. The agent sends a request written in a query language, most often SQL. The database engine then looks through its tables and returns only the rows and columns that match the rules in the request. With this tool, the agent can answer questions that need up-to-date numbers, user records, or other stored facts. It can also write new entries or adjust old ones to keep the data current. Because queries work in real time and follow clear rules, they give the agent a reliable way to handle large sets of structured information.

- `@article` [Building Your Own Database Agent](https://www.deeplearning.ai/short-courses/building-your-own-database-agent/)

#### API Requests

API requests let an AI agent ask another service for data or for an action. The agent builds a short message that follows the service’s rules, sends it over the internet, and waits for a reply. For example, it can call a weather API to get today’s forecast or a payment API to charge a customer. Each request has a method like GET or POST, a URL, and often a small block of JSON with needed details. The service answers with another JSON block that the agent reads and uses. Because API requests are fast and clear, they are a common tool for connecting the agent to many other systems without extra work.

- `@article` [Introduction to APIs - MDN Web Docs](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Client-side_APIs/Introduction)
- `@article` [How APIs Power AI Agents: A Comprehensive Guide](https://blog.treblle.com/api-guide-for-ai-agents/)

#### Email / Slack / SMS

Email, Slack, and SMS are message channels an AI agent can use to act on tasks and share updates. The agent writes and sends emails to give detailed reports or collect files. It posts to Slack to chat with a team, answer questions, or trigger alerts inside a workspace. It sends SMS texts for quick notices such as reminders, confirmations, or warnings when a fast response is needed. By picking the right channel, the agent reaches users where they already communicate, makes sure important information arrives on time, and can even gather replies to keep a task moving forward.

- `@official` [Twilio Messaging API](https://www.twilio.com/docs/usage/api)
- `@official` [Slack AI Agents](https://slack.com/ai-agents)

#### File System Access

File system access lets an AI agent read, create, change, or delete files and folders on a computer or server. With this power, the agent can open a text file to pull data, write a new report, save logs, or tidy up old files without human help. It can also move files between folders to keep things organized. This tool is useful for tasks such as data processing, report generation, and backup jobs. Strong safety checks are needed so the agent touches only the right files, avoids private data, and cannot harm the system by mistake.

- `@article` [Filesystem MCP server for AI Agents](https://playbooks.com/mcp/mateicanavra-filesystem)
- `@article` [File System Access API](https://developer.mozilla.org/en-US/docs/Web/API/File_System_Access_API)
- `@article` [Understanding File Permissions and Security](https://linuxize.com/post/understanding-linux-file-permissions/)
- `@video` [How File Systems Work?](https://www.youtube.com/watch?v=KN8YgJnShPM)

## Usage Examples

### Model Context Protocol (MCP)

Model Context Protocol (MCP) is an open standard that defines how AI applications connect to external tools, data sources, and services in a consistent way. Instead of building a custom integration for every tool an agent needs, MCP provides a common interface that any compliant client and server can use to communicate. This makes it easier to plug new capabilities into an agent without writing bespoke connection code each time.

- `@course` [MCP: Build Rich-Context AI Apps with Anthropic](https://www.deeplearning.ai/short-courses/mcp-build-rich-context-ai-apps-with-anthropic/)
- `@official` [Model Context Protocol](https://modelcontextprotocol.io/introduction)
- `@opensource` [Model Context Protocol](https://github.com/modelcontextprotocol/modelcontextprotocol)
- `@article` [Introducing the Azure MCP Server](https://devblogs.microsoft.com/azure-sdk/introducing-the-azure-mcp-server/)
- `@article` [The Ultimate Guide to MCP](https://guangzhengli.com/blog/en/model-context-protocol)

### Creating MCP Servers

An MCP server stores and shares conversation data for AI agents using the Model Context Protocol (MCP), a standard for agent memory management. Start by picking a language and web framework, then create REST endpoints like `/messages`, `/state`, and `/health`. Each endpoint exchanges JSON following the MCP schema. Store session logs with a session ID, role, and timestamp using a database or in-memory store. Add token-based authentication and filters so agents can fetch only what they need. Set limits on message size and request rates to avoid overload. Finally, write unit tests, add monitoring, and run load tests to ensure stability.

- `@official` [Model Context Protocol (MCP) Specification](https://www.anthropic.com/news/model-context-protocol)
- `@article` [How to Build and Host Your Own MCP Servers in Easy Steps?](https://collabnix.com/how-to-build-and-host-your-own-mcp-servers-in-easy-steps/)

### What is Agent Memory?

Agent memory is the part of an AI agent that keeps track of what has already happened. It stores past user messages, facts the agent has learned, and its own previous steps. This helps the agent remember goals, user likes and dislikes, and important details across turns or sessions. Memory can be short-term, lasting only for one conversation, or long-term, lasting across many. With a good memory the agent avoids repeating questions, stays consistent, and plans better actions. Without it, the agent would forget everything each time and feel unfocused.

- `@article` [Agentic Memory for LLM Agents](https://arxiv.org/abs/2502.12110)
- `@article` [Memory Management in AI Agents](https://python.langchain.com/docs/how_to/chatbots_memory/)
- `@article` [Storing and Retrieving Knowledge for Agents](https://www.pinecone.io/learn/langchain-retrieval-augmentation/)
- `@article` [Short-Term vs Long-Term Memory in AI Agents](https://adasci.org/short-term-vs-long-term-memory-in-ai-agents/)
- `@video` [Building Brain-Like Memory for AI Agents](https://www.youtube.com/watch?v=VKPngyO0iKg)

### Episodic vs Semantic Memory

Agent memory often has two parts. Episodic memory is relevant to the context of the current conversation and may be lost after the conversation ends. Semantic memory is relevant to the broader knowledge of the agent and is persistent.

- `@article` [What Is AI Agent Memory? - IBM](https://www.ibm.com/think/topics/ai-agent-memory)
- `@article` [Episodic Memory vs. Semantic Memory: The Key Differences](https://www.magneticmemorymethod.com/episodic-vs-semantic-memory/)
- `@article` [Memory Systems in LangChain](https://python.langchain.com/docs/how_to/chatbots_memory/)

## Core Components

#### MCP Hosts

MCP Hosts are computers or services that run the Model Context Protocol. They handle incoming calls, load the MCP manifest, check requests, and pass data between users, tools, and language models. Hosts may cache recent messages, track token usage, and add safety or billing checks before sending prompts to the model. They expose an API endpoint so apps can connect easily. You can run a host on your laptop for testing or deploy it on cloud platforms for scale. The host acts as the trusted bridge where agents, tools, and data meet.

- `@official` [Vercel Serverless Hosting](https://vercel.com/docs)
- `@opensource` [punkeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)
- `@article` [The Ultimate Guide to MCP](https://guangzhengli.com/blog/en/model-context-protocol)
- `@article` [AWS MCP Servers for Code Assistants](https://aws.amazon.com/blogs/machine-learning/introducing-aws-mcp-servers-for-code-assistants-part-1/)

#### MCP Client

The MCP Client is the part of an AI agent that talks to the language model API. It collects messages, files, and tool signals, packs them using the Model Context Protocol, and sends them to the model. When a reply comes back, it unpacks it, checks the format, and passes the result to other modules. It also tracks token usage, filters private data, retries failed calls, and logs important events for debugging.

- `@official` [Model Context Protocol](https://modelcontextprotocol.io/introduction)
- `@official` [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- `@official` [Anthropic API Documentation](https://docs.anthropic.com/claude/reference)
- `@opensource` [Model Context Protocol](https://github.com/modelcontextprotocol/modelcontextprotocol)

#### MCP Servers

An MCP server exposes a set of tools, data, or capabilities to any compatible client using the Model Context Protocol. It might, for example, provide access to a file system, a database, or a third party API. Because servers follow a shared protocol, they can be reused across different AI applications without custom integration work.

- `@opensource` [punkeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)
- `@article` [Introducing the Azure MCP Server](https://devblogs.microsoft.com/azure-sdk/introducing-the-azure-mcp-server/)
- `@article` [The Ultimate Guide to MCP](https://guangzhengli.com/blog/en/model-context-protocol)
- `@article` [AWS MCP Servers for Code Assistants](https://aws.amazon.com/blogs/machine-learning/introducing-aws-mcp-servers-for-code-assistants-part-1/)

## Deployment Modes

#### Local Desktop

A Local Desktop deployment means running the MCP server directly on your own computer instead of a remote cloud or server. You install the MCP software, needed runtimes, and model files onto your desktop or laptop. The server then listens on a local address like `127.0.0.1:8000`, accessible only from the same machine unless you open ports manually. This setup is great for fast tests, personal demos, or private experiments since you keep full control and avoid cloud costs. However, it's limited by your hardware's speed and memory, and others cannot access it without tunneling tools like ngrok or local port forwarding.

- `@article` [Build a Simple Local MCP Server](https://blog.stackademic.com/build-simple-local-mcp-server-5434d19572a4)
- `@article` [How to Build and Host Your Own MCP Servers in Easy Steps?](https://collabnix.com/how-to-build-and-host-your-own-mcp-servers-in-easy-steps/)
- `@article` [Expose localhost to Internet](https://ngrok.com/docs)
- `@video` [Run a Local Server on Your Machine](https://www.youtube.com/watch?v=ldGl6L4Vktk)

#### Remote / Cloud

Remote or cloud deployment places the MCP server on a cloud provider instead of a local machine. You package the server as a container or virtual machine, choose a service like AWS, Azure, or GCP, and give it compute, storage, and a public HTTPS address. A load balancer spreads traffic, while auto-scaling adds or removes copies of the server as demand changes. You secure the endpoint with TLS, API keys, and firewalls, and you send logs and metrics to the provider’s monitoring tools. This setup lets the server handle many users, updates are easier, and you avoid local hardware limits, though you must watch costs and protect sensitive data.

- `@official` [Edge AI vs. Cloud AI: Real-Time Intelligence Models](https://medium.com/@hassaanidrees7/edge-ai-vs-cloud-ai-real-time-intelligence-vs-centralized-processing-df8c6e94fd11)
- `@article` [Cloud AI vs. On-premises AI](https://www.pluralsight.com/resources/blog/ai-and-data/ai-on-premises-vs-in-cloud)
- `@article` [Cloud vs On-Premises AI Deployment](https://toxigon.com/cloud-vs-on-premises-ai-deployment)

## Within Prompt

### Short Term  Memory

Short-term memory refers to the immediate, transient information that an AI agent holds during a specific task or conversation. It is typically implemented by including recent interaction history, active goals, and relevant context directly within the model's prompt window. This data allows the agent to maintain coherence and follow the flow of a single session, though this information is usually cleared once the context limit is reached or the session ends.

- `@article` [Memory Management in AI Agents](https://python.langchain.com/docs/how_to/chatbots_memory/)
- `@article` [Build Smarter AI Agents: Manage Short-term and Long-term Memory](https://redis.io/blog/build-smarter-ai-agents-manage-short-term-and-long-term-memory-with-redis/)
- `@article` [Storing and Retrieving Knowledge for Agents](https://www.pinecone.io/learn/langchain-retrieval-augmentation/)
- `@article` [Short-Term vs Long-Term Memory in AI Agents](https://adasci.org/short-term-vs-long-term-memory-in-ai-agents/)
- `@video` [Building Brain-Like Memory for AI Agents](https://www.youtube.com/watch?v=VKPngyO0iKg)

### Long Term Memory

Long term memory in an AI agent stores important information for future use, like a digital notebook. It saves facts, past events, user preferences, and learned skills so the agent can make smarter and more consistent decisions over time. Unlike short-term memory, this data survives across sessions. When a similar situation comes up, the agent can look back and use what it already knows. Long term memory usually lives in a database, file system, or vector store and may hold text, numbers, embeddings, or past conversation states. Good management of long-term memory is key for building agents that feel personalized and get better with experience.

- `@article` [Long Term Memory in AI Agents](https://medium.com/@alozie_igbokwe/ai-101-long-term-memory-in-ai-agents-35f87f2d0ce0)
- `@article` [Memory Management in AI Agents](https://python.langchain.com/docs/how_to/chatbots_memory/)
- `@article` [Storing and Retrieving Knowledge for Agents](https://www.pinecone.io/learn/langchain-retrieval-augmentation/)
- `@article` [Short-Term vs Long-Term Memory in AI Agents](https://adasci.org/short-term-vs-long-term-memory-in-ai-agents/)
- `@video` [Building Brain-Like Memory for AI Agents](https://www.youtube.com/watch?v=VKPngyO0iKg)

## Maintaining Memory

#### RAG and Vector Databases

Using RAG with a vector database means storing pieces of information as embeddings and retrieving the most relevant ones by similarity search when the agent needs context. This combination lets an agent access a large body of knowledge without keeping it all in the prompt, since only the relevant retrieved pieces get added to context. It is a common way to give agents access to long term or external memory.

- `@article` [Understanding Retrieval-Augmented Generation (RAG) and Vector Databases](https://pureai.com/Articles/2025/03/03/Understanding-RAG.aspx)
- `@article` [Build Advanced Retrieval-Augmented Generation Systems](https://learn.microsoft.com/en-us/azure/developer/ai/advanced-retrieval-augmented-generation)
- `@article` [What Is Retrieval-Augmented Generation, aka RAG?](https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/)

#### User Profile Storage

User profile storage is the part of an AI agent’s memory that holds stable facts about each user, such as name, age group, language, past choices, and long-term goals. The agent saves this data in a file or small database so it can load it each time the same user returns. By keeping the profile separate from short-term conversation logs, the agent can remember preferences without mixing them with temporary chat history. The profile is updated only when the user states a new lasting preference or when old information changes, which helps prevent drift or bloat.

- `@article` [Storage Technology Explained: AI and Data Storage](https://www.computerweekly.com/feature/Storage-technology-explained-AI-and-the-data-storage-it-needs)
- `@article` [The Architect's Guide to Storage for AI - The New Stack](https://thenewstack.io/the-architects-guide-to-storage-for-ai/)

#### Summarization / Compression

Summarization or compression reduces the size of stored or in context information by condensing it into a shorter form that keeps the key details. This is used when conversation history or retrieved data grows too large to fit within a context window. Compressing older information lets an agent retain the gist of past interactions without spending excessive tokens on the full detail.

- `@article` [Evaluating LLMs for Text Summarization](https://insights.sei.cmu.edu/blog/evaluating-llms-for-text-summarization-introduction/)
- `@article` [The Ultimate Guide to AI Document Summarization](https://www.documentllm.com/blog/ai-document-summarization-guide)

#### Forgetting / Aging Strategies

Forgetting or aging strategies decide what stored information an agent should discard or deprioritize over time, since keeping everything indefinitely is neither practical nor useful. Common approaches include removing information after a set time, lowering its priority if it is not accessed, or replacing outdated details with newer ones. These strategies keep an agent's memory relevant and prevent it from being cluttered with stale or contradictory information.

- `@article` [Memory Management in AI Agents](https://python.langchain.com/docs/how_to/chatbots_memory/)
- `@article` [Memory Management for AI Agents](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/memory-management-for-ai-agents/4406359)

## Common Architectures

### RAG Agent

A RAG agent combines retrieval augmented generation with the ability to take actions, retrieving relevant documents as part of its reasoning process rather than just as a one time context lookup before generating text. This lets it decide when retrieval is needed and query external knowledge sources multiple times during a task. It is commonly used for question answering over private or specialized document collections.

- `@article` [What is RAG? - Retrieval-Augmented Generation AI Explained](https://aws.amazon.com/what-is/retrieval-augmented-generation/)
- `@article` [What Is Retrieval-Augmented Generation, aka RAG?](https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/)

### ReAct (Reason + Act)

ReAct is an agent architecture that interleaves reasoning steps with actions, having the model think through what to do, take an action, observe the result, and reason again before the next action. This tight loop between thought and action lets the agent adjust its plan based on real feedback rather than committing to a full plan upfront. It is one of the most widely used patterns for building tool using agents.

- `@official` [ReAct: Synergizing Reasoning and Acting in Language Models](https://react-lm.github.io/)
- `@article` [ReAct Systems: Enhancing LLMs with Reasoning and Action](https://learnprompting.org/docs/agents/react)

### Planner Executor

A planner executor architecture splits an agent into two roles: a planner that breaks a goal down into a sequence of steps, and an executor that carries out each step and reports back the result. This separation lets the planner focus on high level strategy while the executor handles the details of each individual action. It can make an agent's behavior easier to reason about and debug compared to a single combined loop.

- `@article` [Plan-and-Execute Agents](https://blog.langchain.dev/planning-agents/)
- `@article` [Plan and Execute: AI Agents Architecture](https://medium.com/@shubham.ksingh.cer14/plan-and-execute-ai-agents-architecture-f6c60b5b9598)

### DAG Agents

A DAG (Directed Acyclic Graph) agent is made of small parts called nodes that form a one-way graph with no loops. Each node does a task and passes its result to the next. Because there are no cycles, data always moves forward, making workflows easy to follow and debug. Independent nodes can run in parallel, speeding up tasks. If a node fails, you can trace and fix that part without touching the rest. DAG agents are ideal for jobs like data cleaning, multi-step reasoning, or workflows where backtracking isn’t needed.

- `@official` [Airflow: Directed Acyclic Graphs Documentation](https://airflow.apache.org/docs/apache-airflow/stable/concepts/dags.html)
- `@article` [What are DAGs in AI Systems?](https://www.restack.io/p/version-control-for-ai-answer-what-is-dag-in-ai-cat-ai)
- `@video` [DAGs Explained Simply](https://www.youtube.com/watch?v=1Yh5S-S6wsI)

#### Multi-Agents

Multi-agent systems involve multiple autonomous agents that interact with each other to achieve individual or collective goals. These agents can collaborate, compete, or coordinate their actions within a shared environment. The interactions between these agents can lead to emergent behaviors and solutions that are more complex and sophisticated than what a single agent could achieve on its own.

- `@article` [Guide to multi-agent systems (MAS)](https://cloud.google.com/discover/what-is-a-multi-agent-system)
- `@article` [What is multi-agent collaboration?](https://www.ibm.com/think/topics/multi-agent-collaboration)
- `@video` [Multi Agent Systems Explained: How AI Agents & LLMs Work Together](https://www.youtube.com/watch?v=sWH0T4Zez6I)

#### Self-critique Agents

Self-critique agents are a type of AI agent designed to evaluate and improve their own performance. They work by generating outputs, then analyzing those outputs to identify weaknesses or errors. Based on this self-analysis, the agent refines its approach and attempts to produce better results in subsequent iterations. This cycle of generation, critique, and refinement allows the agent to learn and adapt over time, improving its ability to solve problems or complete tasks effectively.

- `@article` [Reflection Agents](https://blog.langchain.com/reflection-agents/)
- `@article` [How Do Agents Learn from Their Own Mistakes? The Role of Reflection in AI](https://huggingface.co/blog/Kseniase/reflection)

## Vector DB / SQL / Custom

### Manual (from scratch)

Building an AI agent from scratch means writing every part of the system yourself, without ready-made libraries. You define how the agent senses inputs, stores memory, makes decisions, and learns over time. First, you pick a clear goal, like solving puzzles or chatting. Then you code the inputs (keyboard, mouse, text), decision logic (rules or neural networks), and memory (saving facts from past events). Testing is critical: you run the agent, watch its actions, debug, and improve. Though it takes longer, this approach gives deep understanding and full control over how the agent works and evolves.

- `@article` [A Step-by-Step Guide to Building an AI Agent From Scratch](https://www.neurond.com/blog/how-to-build-an-ai-agent)
- `@article` [How to Build AI Agents](https://wotnot.io/blog/build-ai-agents)
- `@article` [Build Your Own AI Agent from Scratch in 30 Minutes](https://medium.com/@gurpartap.sandhu3/build-you-own-ai-agent-from-scratch-in-30-mins-using-simple-python-1458f8099da0)
- `@video` [Building an AI Agent From Scratch](https://www.youtube.com/watch?v=bTMPwUgLZf0)

## Evaluation and Testing

#### Metrics to Track

To judge how well an AI agent works, you need clear numbers. Track accuracy, precision, recall, and F1 score to measure correctness. For ranking tasks, use metrics like mean average precision or ROC-AUC. If users interact with the agent, monitor response time, latency, and failure rates. Safety metrics count toxic or biased outputs, while robustness tests check how the agent handles messy or tricky inputs. Resource metrics—memory, CPU, and energy—show if it can scale. Pick the metrics that match your goal, compare against a baseline, and track trends across versions.

- `@article` [Robustness Testing for AI](https://mitibmwatsonailab.mit.edu/category/robustness/)
- `@article` [Complete Guide to Machine Learning Evaluation Metrics](https://medium.com/analytics-vidhya/complete-guide-to-machine-learning-evaluation-metrics-615c2864d916)
- `@article` [Measuring Model Performance](https://developers.google.com/machine-learning/crash-course/classification/accuracy)
- `@article` [A Practical Framework for (Gen)AI Value Measurement](https://medium.com/google-cloud/a-practical-framework-for-gen-ai-value-measurement-5fccf3b66c43)

#### Unit Testing for Individual Tools

Unit testing checks that each tool an AI agent uses works as expected when it stands alone. You write small tests that feed the tool clear input and then compare its output to a known correct answer. If the tool is a function that parses dates, you test many date strings and see if the function gives the right results. Good tests cover normal cases, edge cases, and error cases. Run the tests every time you change the code. When a test fails, fix the tool before moving on. This habit keeps bugs from spreading into larger agent workflows and makes later debugging faster.

- `@article` [Unit Testing Agents](https://docs.patronus.ai/docs/agent_evals/unit_testing)
- `@article` [Best AI Tools for Unit Testing: A Look at Top 14 AI Tools](https://thetrendchaser.com/best-ai-tools-for-unit-testing/)
- `@article` [AI for Unit Testing: Revolutionizing Developer Productivity](https://www.diffblue.com/resources/ai-for-unit-testing-revolutionizing-developer-productivity/)

#### Integration Testing for Flows

Integration testing for flows checks that an agent behaves correctly across a full multi step task, not just that individual tools work on their own. It verifies that the agent chooses the right tools in the right order and handles the combined behavior of reasoning, acting, and observing correctly. This catches issues that only show up when components interact, which unit tests on individual pieces would miss.

- `@article` [Integration Testing for AI-based Features with Humans](https://www.microsoft.com/en-us/research/publication/hint-integration-testing-for-ai-based-features-with-humans-in-the-loop/)
- `@article` [Integration Testing and Unit Testing in AI](https://www.aviator.co/blog/integration-testing-and-unit-testing-in-the-age-of-ai/)
- `@article` [Integration Testing Tutorial](https://www.guru99.com/integration-testing.html)

#### Human in the Loop Evaluation

Human-in-the-loop evaluation checks an AI agent by letting real people judge its output and behavior. Instead of trusting only automated scores, testers invite users, domain experts, or crowd workers to watch tasks, label answers, flag errors, and rate clarity, fairness, or safety. Their feedback shows problems that numbers alone miss, such as hidden bias, confusing language, or actions that feel wrong to a person. Teams study these notes, adjust the model, and run another round, repeating until the agent meets quality and trust goals. Mixing human judgment with data leads to a system that is more accurate, useful, and safe for everyday use.

- `@article` [Human in the Loop · Cloudflare Agents](https://developers.cloudflare.com/agents/concepts/human-in-the-loop/)
- `@article` [What is Human-in-the-Loop: A Guide](https://logifusion.com/what-is-human-in-the-loop-htil/)
- `@article` [Human-in-the-Loop ML](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-human-review-workflow.html)
- `@article` [The Importance of Human Feedback in AI (Hugging Face Blog)](https://huggingface.co/blog/rlhf)

#### LangSmith

LangSmith is a platform for debugging, testing, and monitoring LLM applications, including agents, by tracing each step of a run and logging inputs, outputs, and intermediate reasoning. It also supports building evaluation datasets and running automated tests against them to measure quality over time, alongside dashboards for tracking cost and latency in production. Built by the LangChain team, it is commonly paired with LangChain and LangGraph applications but can be used independently.

- `@official` [LangSmith](https://smith.langchain.com/)
- `@official` [LangSmith Documentation](https://docs.smith.langchain.com/)
- `@official` [Harden your application with LangSmith Evaluation](https://www.langchain.com/evaluation)
- `@article` [What is LangSmith and Why should I care as a developer?](https://medium.com/around-the-prompt/what-is-langsmith-and-why-should-i-care-as-a-developer-e5921deb54b5)

#### DeepEval

DeepEval is an open-source tool that helps you test and score the answers your AI agent gives. You write small test cases that show an input and the reply you hope to get, or a rule the reply must follow. DeepEval runs the agent, checks the reply with built-in measures such as similarity, accuracy, or safety, and then marks each test as pass or fail. You can add your own checks, store tests in code or YAML files, and run them in a CI pipeline so every new model or prompt version gets the same quick audit. The fast feedback makes it easy to spot errors, cut down on hallucinations, and compare different models before you ship.

- `@official` [DeepEval - The Open-Source LLM Evaluation Framework](https://www.deepeval.com/)
- `@opensource` [DeepEval GitHub Repository](https://github.com/confident-ai/deepeval)
- `@article` [Evaluate LLMs Effectively Using DeepEval: A Practical Guide](https://www.datacamp.com/tutorial/deepeval)
- `@video` [DeepEval - LLM Evaluation Framework](https://www.youtube.com/watch?v=ZNs2dCXHlfo)

#### Ragas

Ragas is an evaluation framework focused specifically on retrieval augmented generation pipelines, measuring things like the relevance of retrieved documents and the faithfulness of generated answers to that retrieved content. It provides a standard set of metrics tailored to RAG systems rather than general purpose LLM evaluation. This makes it useful for diagnosing whether errors come from the retrieval step or the generation step.

- `@official` [Ragas Documentation](https://docs.ragas.io/en/latest/)
- `@opensource` [explodinggradients/ragas](https://github.com/explodinggradients/ragas)
- `@article` [Evaluating RAG Applications with RAGAs](https://towardsdatascience.com/evaluating-rag-applications-with-ragas-81d67b0ee31a/n)

## Frameworks

### LLM Native "Function Calling"

LLM native function calling is a capability built directly into a model's API that lets it output a structured call to a predefined function, including the function name and arguments, instead of freeform text. The application executes the actual function and returns the result to the model to continue the conversation. This standardizes how models request actions, removing the need to parse tool calls out of plain text output.

- `@article` [A Comprehensive Guide to Function Calling in LLMs](https://thenewstack.io/a-comprehensive-guide-to-function-calling-in-llms/)
- `@article` [Function Calling with LLMs | Prompt Engineering Guide](https://www.promptingguide.ai/applications/function_calling)
- `@article` [Function Calling with Open-Source LLMs](https://medium.com/@rushing_andrei/function-calling-with-open-source-llms-594aa5b3a304)

#### OpenAI Functions Calling

OpenAI's function calling lets a model choose from a set of functions defined in the API request and return a structured call with the function name and arguments as JSON. The calling application executes the function and sends the result back for the model to use in its next response. It is one of the earliest and most widely adopted implementations of native tool calling.

- `@official` [OpenAI Documentation – Function Calling](https://platform.openai.com/docs/guides/function-calling)
- `@official` [OpenAI Cookbook – Using Functions with GPT Models](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_call_functions_with_chat_models.ipynb)
- `@article` [@officialOpenAI Blog – Announcing Function Calling and Other Updates](https://openai.com/blog/function-calling-and-other-api-updates)
- `@article` [@officialOpenAI API Reference – Functions Section](https://platform.openai.com/docs/api-reference/chat/create#functions)
- `@article` [@officialOpenAI Community – Discussions and Examples on Function Calling](https://community.openai.com/tag/function-calling)

#### OpenAI Assistant API

The OpenAI Assistants API is a higher level interface for building agents that manages conversation threads, tool calls, and file based context on OpenAI's servers, rather than requiring the developer to track state manually. It handles things like persisting conversation history and running tools like code execution or file search. This reduces the amount of infrastructure a developer needs to build to get a working agent.

- `@official` [OpenAI Documentation – Assistants API Overview](https://platform.openai.com/docs/assistants/overview)
- `@official` [OpenAI Blog – Introducing the Assistants API](https://openai.com/blog/assistants-api)
- `@official` [OpenAI Cookbook – Assistants API Example](https://github.com/openai/openai-cookbook/blob/main/examples/Assistants_API_overview_python.ipynb)
- `@official` [OpenAI API Reference – Assistants Endpoints](https://platform.openai.com/docs/api-reference/assistants)

#### Gemini Function Calling

Gemini function calling is Google's implementation of native tool calling, letting a Gemini model select from provided function definitions and return a structured call with arguments. The application runs the corresponding function and returns the output to continue the interaction. It follows the same general pattern as other providers' function calling, with its own specific request and response format.

- `@official` [Function Calling with the Gemini API](https://ai.google.dev/gemini-api/docs/function-calling)
- `@article` [Understanding Function Calling in Gemini](https://medium.com/google-cloud/understanding-function-calling-in-gemini-3097937f1905)

## Building Using Frameworks

#### LangChain

LangChain is a framework designed to simplify the creation of applications using large language models (LLMs). It provides tools and abstractions to connect LLMs to various data sources, create chains of calls to LLMs or other utilities, and build agents that can interact with their environment. Essentially, it helps developers structure, chain, and orchestrate different AI components to build more complex and capable AI applications.

- `@official` [LangChain Documentation](https://python.langchain.com/docs/introduction/)
- `@opensource` [langchain-ai/langchain](https://github.com/langchain-ai/langchain)
- `@article` [AI Agents with LangChain and LangGraph](https://www.udacity.com/course/ai-agents-with-langchain-and-langgraph--cd13764)
- `@video` [LangChain Crash Course - Build LLM Apps Fast (YouTube)](https://www.youtube.com/watch?v=nAmC7SoVLd8)

#### LangGraph

LangGraph is a Python library designed to help developers create robust and stateful conversational AI applications, often referred to as AI Agents. It allows you to structure complex agent workflows by defining states (data held throughout the conversation) and edges (transitions between states based on agent decisions or external events), creating a graph-like representation of the agent's reasoning process. This makes it easier to manage the flow of conversations and build more reliable and explainable AI agents.

- `@official` [LangGraph Docs](https://docs.langchain.com/oss/python/langgraph/overview?_gl=1*wnuiny*_gcl_au*MTI0NjQ3NzM5NS4xNzczMDQ5NDY2*_ga*MTgwMzY5ODQ5OS4xNzczMDQ5NDY2*_ga_47WX3HKKY2*czE3NzMwNDk0NjYkbzEkZzAkdDE3NzMwNDk0NjYkajYwJGwwJGgw)
- `@opensource` [langgraph](https://github.com/langchain-ai/langgraph)
- `@article` [LangGraph 101: Let’s Build A Deep Research Agent](https://towardsdatascience.com/langgraph-101-lets-build-a-deep-research-agent/?utm_source=roadmap&utm_medium=Referral&utm_campaign=TDS+roadmap+integration)
- `@video` [LangChain vs LangGraph: A Tale of Two Frameworks](https://www.youtube.com/watch?v=qAF1NjEVHhY&pp=ygUWbGFuZ2dyYXBoIHZzIGxhbmdjaGFpbg%3D%3D)

#### Haystack

Haystack is an open source framework for building search and question answering pipelines, including retrieval augmented generation and agent based applications. It provides modular components for document retrieval, ranking, and generation that can be combined into custom pipelines. It is often used in production search and NLP applications that need a flexible, composable architecture.

- `@official` [Haystack](https://haystack.deepset.ai/)
- `@official` [Haystack Overview](https://docs.haystack.deepset.ai/docs/intro)
- `@opensource` [deepset-ai/haystack](https://github.com/deepset-ai/haystack)

#### LlamaIndex

LlamaIndex is a framework focused on connecting language models to external data, providing tools for ingesting, indexing, and querying documents for retrieval augmented generation. It handles tasks like chunking documents, generating embeddings, and building indexes that support efficient retrieval. It is commonly used as the data layer underneath a RAG based agent.

- `@official` [LlamaIndex](https://llamaindex.ai/)
- `@official` [LlamaIndex Documentation](https://docs.smith.langchain.com/)
- `@official` [What is LlamaIndex.TS](https://ts.llamaindex.ai/docs/llamaindex)
- `@opensource` [run-llama/llama_index](https://github.com/run-llama/llama_index)
- `@article` [What is LlamaIndex? - IBM](https://www.ibm.com/think/topics/llamaindex)
- `@article` [LlamaIndex - Hugging Face](https://huggingface.co/llamaindex)

#### CrewAI

CrewAI is an open-source Python framework for creating teams of AI agents, called a crew. Each agent is assigned a name, role, and set of tools, and the system manages planning, communication, and execution between them. To use it, install the package, define agents in code, connect them with a `Crew` object, and assign a mission prompt. CrewAI interacts with an LLM like GPT-4 or Claude, passes messages, runs tools, and returns a final output. You can also add web search, custom functions, or memory stores. Logs are built-in to help debug and optimize workflows.

- `@official` [CrewAI](https://crewai.com/)
- `@official` [CrewAI Documentation](https://docs.crewai.com/)
- `@article` [Getting Started with CrewAI: Building AI Agents That Work Together](https://medium.com/@cammilo/getting-started-with-crewai-building-ai-agents-that-work-together-9c1f47f185ca)
- `@video` [Crew AI Full Tutorial For Beginners](https://www.youtube.com/watch?v=q6QLGS306d0)

#### AutoGen

AutoGen is a framework from Microsoft for building applications with multiple agents that communicate with each other to solve tasks. It defines agents with specific roles and lets them exchange messages, delegate subtasks, and collaborate toward a shared goal. It is commonly used for research and applications that benefit from multiple specialized agents working together.

- `@official` [AutoGen - Microsoft Research](https://www.microsoft.com/en-us/research/project/autogen/)
- `@opensource` [GitHub - microsoft/autogen](https://github.com/microsoft/autogen)

#### Smol Depot

Smol Depot is an open-source kit that lets you bundle all the parts of a small AI agent in one place. You keep prompts, settings, and code files together in a single folder, then point the Depot tool at that folder to spin the agent up. The tool handles tasks such as loading models, saving chat history, and calling outside APIs, so you do not have to write that glue code yourself. A simple command can copy a starter template, letting you focus on the logic and prompts that make your agent special. Because everything lives in plain files, you can track changes with Git and share the agent like any other project.

- `@official` [smol.ai - Continuous Fine-tuning Platform for AI Engineers](https://smol.candycode.dev/)
- `@article` [5-min Smol AI Tutorial](https://www.ai-jason.com/learning-ai/smol-ai-tutorial)
- `@video` [Smol AI Full Beginner Course](https://www.youtube.com/watch?v=d7qFVrpLh34)

#### Agno

Agno is a Python framework designed to streamline the process of building AI agents. It offers tools and abstractions that simplify tasks such as agent planning, tool use, and memory management, making it easier to create sophisticated and functional AI agents without managing low-level implementation details. It emphasizes modularity and composability, enabling developers to easily integrate different components and customize agent behavior.

- `@official` [Agno Docs](https://docs.agno.com/)
- `@opensource` [agno](https://github.com/agno-agi/agno)
- `@video` [Building Your First Agent With AGNO AGI ( Previously Phidata ) | For Complete Begineers](https://www.youtube.com/watch?v=s7Kkc6vA2K0)

## Debugging and Monitoring

#### Structured logging & tracing

Structured logging and tracing record an agent's execution in a consistent, machine readable format, capturing details like which tool was called, what arguments were used, and how long each step took. Unlike plain text logs, structured data can be filtered, searched, and analyzed programmatically. Tracing connects these individual log entries into a full picture of a single run, which is essential for debugging complex, multi step agent behavior.

- `@article` [Understanding Structured Logging: A Comprehensive Guide](https://www.graphapp.ai/blog/understanding-structured-logging-a-comprehensive-guide)
- `@article` [Structured Logging & Cloud Logging](https://cloud.google.com/logging/docs/structured-logging)
- `@article` [Best Practices for Logging in AI Applications](https://www.restack.io/p/best-ai-practices-software-compliance-answer-logging-best-practices-cat-ai)

#### LangSmith

LangSmith is a web tool that helps you see and fix what your AI agents are doing. It records each call that the agent makes to a language model, the input it used, and the answer it got back. You can replay any step, compare different prompts, measure cost, speed, and error rates, and tag runs for easy search. It also lets you store test sets and run quick checks so you know if new code makes the agent worse. By showing clear traces and charts, LangSmith makes it easier to debug, improve, and trust AI systems built with LangChain or other frameworks.

- `@official` [LangSmith](https://smith.langchain.com/)
- `@official` [LangSmith Documentation](https://docs.smith.langchain.com/)
- `@official` [Harden your application with LangSmith Evaluation](https://www.langchain.com/evaluation)
- `@article` [What is LangSmith and Why should I care as a developer?](https://medium.com/around-the-prompt/what-is-langsmith-and-why-should-i-care-as-a-developer-e5921deb54b5)

#### Helicone

Helicone is an open-source tool that helps you watch and understand how your AI agents talk to large language models. You send your model calls through Helicone’s proxy, and it records each request and response without changing the result. A clear web dashboard then shows logs, latency, token counts, error rates, and cost for every call. You can filter, search, and trace a single user journey, which makes it easy to spot slow prompts or rising costs. Helicone also lets you set alerts and share traces with your team, so problems get fixed fast and future changes are safer.

- `@official` [Helicone](https://www.helicone.ai/)
- `@official` [Helicone OSS LLM Observability](https://docs.helicone.ai/getting-started/quick-start)
- `@opensource` [Helicone/helicone](https://github.com/Helicone/helicone)

#### LangFuse

Langfuse is an open source observability and analytics platform for LLM applications, providing tracing, evaluation, and prompt management features. It captures detailed traces of agent runs, including nested tool calls, and lets teams analyze performance and quality over time. It can be self hosted, which appeals to teams with strict data privacy requirements.

- `@official` [LangFuse](https://langfuse.com/)
- `@official` [LangFuse Documentation](https://langfuse.com/docs)
- `@opensource` [langfuse/langfuse](https://github.com/langfuse/langfuse)
- `@article` [Langfuse: Open Source LLM Engineering Platform](https://www.ycombinator.com/companies/langfuse)

#### openllmetry

OpenLLMetry is an open source observability standard that extends OpenTelemetry, a widely used tracing framework, to cover LLM specific data like prompts, completions, and token usage. It lets teams instrument their LLM applications using familiar observability tooling rather than a separate, proprietary system. This makes it easier to integrate LLM monitoring into existing infrastructure that already uses OpenTelemetry.

- `@official` [OpenTelemetry Documentation](https://www.traceloop.com/blog/openllmetry)
- `@official` [What is OpenLLMetry? - traceloop](https://www.traceloop.com/docs/openllmetry/introduction)
- `@official` [Use Traceloop with Python](https://www.traceloop.com/docs/openllmetry/getting-started-python)
- `@opensource` [traceloop/openllmetry](https://github.com/traceloop/openllmetry)

## Observability Tools

#### Anthropic Tool Use

Anthropic tool use is Claude's implementation of native function calling, where the model can choose to call a defined tool with structured arguments as part of its response. The calling application executes the tool and returns the result, which Claude can use to continue reasoning or produce a final answer. It supports patterns like parallel tool calls and forcing a specific tool to be used when needed.

- `@official` [Anthropic Tool Use](https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview)

### Prompt Injection / Jailbreaks

Prompt injection, also called a jailbreak, is a trick that makes an AI system break its own rules. An attacker hides special words or symbols inside normal-looking text. When the AI reads this text, it follows the hidden instructions instead of its safety rules. The attacker might force the AI to reveal private data, produce harmful content, or give wrong advice. This risk grows when the AI talks to other software or pulls text from the internet, because harmful prompts can slip in without warning. Good defenses include cleaning user input, setting strong guardrails inside the model, checking outputs for policy breaks, and keeping humans in the loop for high-risk tasks.

- `@article` [Prompt Injection vs. Jailbreaking: What's the Difference?](https://learnprompting.org/blog/injection_jailbreaking)
- `@article` [Prompt Injection vs Prompt Jailbreak](https://codoid.com/ai/prompt-injection-vs-prompt-jailbreak-a-detailed-comparison/)
- `@article` [How Prompt Attacks Exploit GenAI and How to Fight Back](https://unit42.paloaltonetworks.com/new-frontier-of-genai-threats-a-comprehensive-guide-to-prompt-attacks/)

### Tool sandboxing / Permissioning

Tool sandboxing keeps the AI agent inside a safe zone where it can only run approved actions and cannot touch the wider system. Permissioning sets clear rules that say which files, networks, or commands the agent may use. Together they stop errors, leaks, or abuse by limiting what the agent can reach and do. Developers grant the smallest set of rights, watch activity, and block anything outside the plan. If the agent needs new access, it must ask and get a fresh permit. This simple fence protects user data, reduces harm, and builds trust in the agent’s work.

- `@article` [AI Sandbox | Harvard University Information Technology](https://www.huit.harvard.edu/ai-sandbox)
- `@article` [How to Set Up AI Sandboxes to Maximize Adoption](https://medium.com/@emilholmegaard/how-to-set-up-ai-sandboxes-to-maximize-adoption-without-compromising-ethics-and-values-637c70626130)
- `@article` [Sandboxes for AI - The Datasphere Initiative](https://www.thedatasphere.org/datasphere-publish/sandboxes-for-ai/)

### Data Privacy + PII Redaction

AI agents often process text, images, and logs that include personal data like names, phone numbers, or addresses. Leaks can cause fraud, stalking, or other harm, so laws like GDPR and CCPA require strict protections. A key method is PII redaction: scanning inputs and outputs to find and mask any personal details before storage or sharing. Redaction uses pattern rules, machine learning, or both. Teams should also keep audit logs, enforce access controls, and test their redaction flows often to prevent leaks.

- `@official` [GDPR Compliance Overview](https://gdpr.eu/)
- `@article` [Protect Sensitive Data with PII Redaction Software](https://redactor.ai/blog/pii-redaction-software-guide)
- `@article` [A Complete Guide on PII Redaction](https://enthu.ai/blog/what-is-pii-redaction/)

### Bias & Toxicity Guardrails

Bias and toxicity guardrails are checks put in place to detect and block outputs that are discriminatory, offensive, or otherwise harmful before they reach a user. These can be implemented through classifier models, keyword filters, or the underlying model's own safety training. They are important for agents that generate open ended content or interact directly with end users.

- `@article` [Define the Agent Guardrails](https://trailhead.salesforce.com/content/learn/modules/agentforce-agent-planning/define-the-agent-guardrails)
- `@article` [How to Build Safe AI Agents: Best Practices for Guardrails](https://medium.com/@sahin.samia/how-to-build-safe-ai-agents-best-practices-for-guardrails-and-oversight-a0085b50c022)

### Safety + Red Team Testing

Safety + Red Team Testing is the practice of checking an AI agent for harmful or risky behavior before and after release. Safety work sets rules, guardrails, and alarms so the agent follows laws, keeps data private, and treats people fairly. Red team testing sends skilled testers to act like attackers or troublemakers. They type tricky prompts, try to leak private data, force biased outputs, or cause the agent to give dangerous advice. Every weakness they find is logged and fixed by adding filters, better training data, stronger limits, or live monitoring. Running these tests often lowers the chance of real-world harm and builds trust with users and regulators.

- `@roadmap` [Visit Dedicated AI Red Teaming Roadmap](https://roadmap.sh/ai-red-teaming)
- `@article` [Enhancing AI safety: Insights and lessons from red teaming](https://www.microsoft.com/en-us/microsoft-cloud/blog/2025/01/14/enhancing-ai-safety-insights-and-lessons-from-red-teaming/)
- `@article` [AI Safety Testing in the Absence of Regulations](https://aisecuritycentral.com/ai-safety-testing/)
- `@article` [A Guide to AI Red Teaming - HiddenLayer](https://hiddenlayer.com/innovation-hub/a-guide-to-ai-red-teaming/)
