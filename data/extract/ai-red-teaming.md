# AI Red Teaming — plan extrait

- **Slug** : `ai-red-teaming`
- **Description amont** : Learn to become a red teaming expert in AI in @currentYear@
- **Derniere modification amont** : 2026-03-20T12:25:38.799Z
- **Capture** : 2026-09-16
- **Volume** : 64 noeuds de contenu, 64 documentes, 209 ressources
- **Renvois vers d'autres roadmaps** : `https://learnprompting.org`, `https://roadmap.sh`, `https://roadmap.sh/backend`

---

## AI Red Teaming

#### AI Security Fundamentals

This covers the foundational concepts essential for AI Red Teaming, bridging traditional cybersecurity with AI-specific threats. An AI Red Teamer must understand common vulnerabilities in ML models (like evasion or poisoning), security risks in the AI lifecycle (from data collection to deployment), and how AI capabilities can be misused. This knowledge forms the basis for designing effective tests against AI systems.

- `@article` [Building Trustworthy AI: Contending with Data Poisoning](https://nisos.com/research/building-trustworthy-ai/)
- `@article` [What Is Adversarial AI in Machine Learning?](https://www.paloaltonetworks.co.uk/cyberpedia/what-are-adversarial-attacks-on-AI-Machine-Learning)

#### Why Red Team AI Systems?

AI systems introduce novel risks beyond traditional software, such as emergent unintended capabilities, complex failure modes, susceptibility to subtle data manipulations, and potential for large-scale misuse (e.g., generating disinformation). AI Red Teaming is necessary because standard testing methods often fail to uncover these unique AI vulnerabilities. It provides critical, adversary-focused insights needed to build genuinely safe, reliable, and secure AI before deployment.

- `@course` [Introduction to Prompt Hacking](https://learnprompting.org/courses/intro-to-prompt-hacking)
- `@article` [Prompt Hacking Offensive Measures](https://learnprompting.org/docs/prompt_hacking/offensive_measures/introduction)

### Introduction

AI Red Teaming is the practice of simulating adversarial attacks against AI systems to proactively identify vulnerabilities, potential misuse scenarios, and failure modes before malicious actors do. Distinct from traditional cybersecurity red teaming, it focuses on the unique attack surfaces of AI models, such as prompt manipulation, data poisoning, model extraction, and evasion techniques. The primary goal for an AI Red Teamer is to test the robustness, safety, alignment, and fairness of AI systems, particularly complex ones like LLMs, by adopting an attacker's mindset to uncover hidden flaws and provide actionable feedback for improvement.

- `@article` [A Guide to AI Red Teaming](https://hiddenlayer.com/innovation-hub/a-guide-to-ai-red-teaming/)
- `@article` [What is AI Red Teaming? (Learn Prompting)](https://learnprompting.org/blog/what-is-ai-red-teaming)
- `@article` [What is AI Red Teaming? The Complete Guide](https://mindgard.ai/blog/what-is-ai-red-teaming)

#### Ethical Considerations

Ethical conduct is crucial for AI Red Teamers. While simulating attacks, they must operate within strict legal and ethical boundaries defined by rules of engagement, focusing on improving safety without causing real harm or enabling misuse. This includes respecting data privacy, obtaining consent where necessary, responsibly disclosing vulnerabilities, and carefully considering the potential negative impacts of both the testing process and the AI capabilities being tested. The goal is discovery for defense, not exploitation.

- `@article` [Red-Teaming in AI Testing: Stress Testing](https://www.labelvisor.com/red-teaming-abstract-competitive-testing-data-selection/)
- `@article` [Responsible AI assessment - Responsible AI | Coursera](https://www.coursera.org/learn/ai-security)
- `@article` [Responsible AI Principles (Microsoft)](https://www.microsoft.com/en-us/ai/responsible-ai)

#### Supervised Learning

AI Red Teamers analyze systems built using supervised learning to probe for vulnerabilities like susceptibility to adversarial examples designed to cause misclassification, sensitivity to data distribution shifts, or potential for data leakage related to the labeled training data. Understanding how these models learn input-output mappings is key to devising tests that challenge their learned boundaries.

- `@article` [AI and cybersecurity: a love-hate revolution](https://www.alter-solutions.com/en-us/articles/ai-cybersecurity-love-hate-revolution)
- `@article` [What Is Supervised Learning?](https://www.ibm.com/think/topics/supervised-learning)
- `@article` [What is Supervised Learning?](https://cloud.google.com/discover/what-is-supervised-learning)

#### Role of Red Teams

The role of an AI Red Team is to rigorously challenge AI systems from an adversarial perspective. They design and execute tests to uncover vulnerabilities related to the model's logic, data dependencies, prompt interfaces, safety alignments, and interactions with surrounding infrastructure. They provide detailed reports on findings, potential impacts, and remediation advice, acting as a critical feedback loop for AI developers and stakeholders to improve system security and trustworthiness before and after deployment.

- `@article` [The Complete Guide to Red Teaming: Process, Benefits & More](https://mindgard.ai/blog/red-teaming)
- `@article` [The Complete Red Teaming Checklist \[PDF\]: 5 Key Steps - Mindgard AI](https://mindgard.ai/blog/red-teaming-checklist)
- `@article` [Red Teaming in Defending AI Systems](https://protectai.com/blog/expanding-role-red-teaming-defending-ai-systems)

#### Unsupervised Learning

When red teaming AI systems using unsupervised learning (e.g., clustering algorithms), focus areas include assessing whether the discovered patterns reveal sensitive information, if the model can be manipulated to group data incorrectly, or if dimensionality reduction techniques obscure security-relevant features. Understanding these models helps identify risks associated with pattern discovery on unlabeled data.

- `@article` [How Unsupervised Learning Works with Examples](https://www.coursera.org/articles/unsupervised-learning)
- `@article` [Supervised vs. Unsupervised Learning: Which Approach is Best?](https://www.digitalocean.com/resources/articles/supervised-vs-unsupervised-learning)

#### Confidentiality, Integrity, Availability

The CIA Triad is directly applicable in AI Red Teaming. Confidentiality tests focus on preventing leakage of training data or proprietary model details. Integrity tests probe for susceptibility to data poisoning or model manipulation. Availability tests assess resilience against denial-of-service attacks targeting the AI model or its supporting infrastructure.

- `@article` [Confidentiality, Integrity, Availability: Key Examples](https://www.datasunrise.com/knowledge-center/confidentiality-integrity-availability-examples/)
- `@article` [The CIA Triad: Confidentiality, Integrity, Availability](https://www.veeam.com/blog/cybersecurity-cia-triad-explained.html)
- `@article` [What's The CIA Triad? Confidentiality, Integrity, & Availability, Explained](https://www.splunk.com/en_us/blog/learn/cia-triad-confidentiality-integrity-availability.html)

#### Reinforcement Learning

Red teaming RL-based AI systems involves testing for vulnerabilities such as reward hacking (exploiting the reward function to induce unintended behavior), unsafe exploration (agent takes harmful actions during learning), or susceptibility to adversarial perturbations in the environment's state. Understanding the agent's policy and value functions is crucial for designing effective tests against RL agents.

- `@course` [Deep Reinforcement Learning Course by HuggingFace](https://huggingface.co/learn/deep-rl-course/unit0/introduction)
- `@article` [Resources to Learn Reinforcement Learning](https://towardsdatascience.com/best-free-courses-and-resources-to-learn-reinforcement-learning-ed6633608cb2/)
- `@article` [What is reinforcement learning?](https://online.york.ac.uk/resources/what-is-reinforcement-learning/)
- `@article` [Diverse and Effective Red Teaming with Auto-generated Rewards and Multi-step Reinforcement Learning](https://arxiv.org/html/2412.18693v1)

#### Threat Modeling

AI Red Teams apply threat modeling to identify unique attack surfaces in AI systems, such as manipulating training data, exploiting prompt interfaces, attacking the model inference process, or compromising connected tools/APIs. Before attacking an AI system, red teamers perform threat modeling to map out possible adversaries (from curious users to state actors) and attack vectors, prioritizing tests based on likely impact and adversary capability.

- `@article` [Core Components of AI Red Team Exercises (Learn Prompting)](https://learnprompting.org/blog/what-is-ai-red-teaming)
- `@article` [Threat Modeling Process](https://owasp.org/www-community/Threat_Modeling_Process)
- `@article` [Threat Modeling](https://owasp.org/www-community/Threat_Modeling)

#### Neural Networks

Understanding neural network architectures (layers, nodes, activation functions) is vital for AI Red Teamers. This knowledge allows for targeted testing, such as crafting adversarial examples that exploit specific activation functions or identifying potential vulnerabilities related to network depth or connectivity. It provides insight into the 'black box' for more effective white/grey-box testing.

- `@article` [Neural Networks Explained: A Beginner's Guide](https://www.skillcamper.com/blog/neural-networks-explained-a-beginners-guide)
- `@article` [Neural networks | Machine Learning](https://developers.google.com/machine-learning/crash-course/neural-networks)
- `@article` [Red Teaming with Artificial Intelligence-Driven Cyberattacks: A Scoping Review](https://arxiv.org/html/2503.19626)

#### Risk Management

AI Red Teamers contribute to the AI risk management process by identifying and demonstrating concrete vulnerabilities. Findings from red team exercises inform risk assessments, helping organizations understand the likelihood and potential impact of specific AI threats and prioritize resources for mitigation based on demonstrated exploitability.

- `@article` [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- `@article` [A Beginner's Guide to Cybersecurity Risks and Vulnerabilities](https://online.champlain.edu/blog/beginners-guide-cybersecurity-risk-management)
- `@article` [Cybersecurity Risk Management: Frameworks, Plans, and Best Practices](https://hyperproof.io/resource/cybersecurity-risk-management-process/)

#### Generative Models

AI Red Teamers focus heavily on generative models (like GANs and LLMs) due to their widespread use and unique risks. Understanding how they generate content is key to testing for issues like generating harmful/biased outputs, deepfakes, prompt injection vulnerabilities, or leaking sensitive information from their vast training data.

- `@course` [Introduction to Generative AI](https://learnprompting.org/courses/intro-to-gen-ai)
- `@article` [What is Generative AI?](https://learnprompting.org/docs/basics/generative_ai)
- `@article` [Generative AI beginner's guide](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)

#### Vulnerability Assessment

While general vulnerability assessment scans infrastructure, AI Red Teaming extends this to assess vulnerabilities specific to the AI model and its unique interactions. This includes probing for prompt injection flaws, testing for adversarial example robustness, checking for data privacy leaks, and evaluating safety alignment failures – weaknesses not typically found by standard IT vulnerability scanners.

- `@article` [AI red-teaming in critical infrastructure: Boosting security and trust in AI systems](https://www.dnv.com/article/ai-red-teaming-for-critical-infrastructure-industries/)
- `@article` [The Ultimate Guide to Vulnerability Assessment](https://strobes.co/blog/guide-vulnerability-assessment/)
- `@article` [Vulnerability Scanning Tools](https://owasp.org/www-community/Vulnerability_Scanning_Tools)

#### Large Language Models

LLMs are a primary target for AI Red Teaming. Understanding their architecture (often Transformer-based), training processes (pre-training, fine-tuning), and capabilities (text generation, summarization, Q&A) is essential for identifying vulnerabilities like prompt injection, jailbreaking, data regurgitation, and emergent harmful behaviors specific to these large-scale models.

- `@article` [What is an LLM (large language model)?](https://www.cloudflare.com/learning/ai/what-is-large-language-model/)
- `@article` [ChatGPT For Everyone](https://learnprompting.org/courses/chatgpt-for-everyone)
- `@article` [What Are Large Language Models? A Beginner's Guide for 2025](https://www.kdnuggets.com/large-language-models-beginners-guide-2025)

#### Prompt Engineering

For AI Red Teamers, prompt engineering is both a tool and a target. It's a tool for crafting inputs to test model boundaries and vulnerabilities (e.g., creating jailbreak prompts). It's a target because understanding how prompts influence LLMs is key to identifying prompt injection vulnerabilities and designing defenses. Mastering prompt design is fundamental to effective LLM red teaming.

- `@course` [Introduction to Prompt Engineering](https://learnprompting.org/courses/intro-to-prompt-engineering)
- `@article` [System Prompts - InjectPrompt](https://www.injectprompt.com/t/system-prompts)
- `@article` [The Ultimate Guide to Red Teaming LLMs and Adversarial Prompts (Kili Technology)](https://kili-technology.com/large-language-models-llms/red-teaming-llms-and-adversarial-prompts)

#### Jailbreak Techniques

Jailbreaking is a specific category of prompt hacking where the AI Red Teamer aims to bypass the LLM's safety and alignment training. They use techniques like creating fictional scenarios, asking the model to simulate an unrestricted AI, or using complex instructions to trick the model into generating content that violates its own policies (e.g., generating harmful code, hate speech, or illegal instructions).

- `@article` [InjectPrompt](https://injectprompt.com)
- `@article` [Jailbreaking Guide - Learn Prompting](https://learnprompting.org/docs/prompt_hacking/jailbreaking)
- `@article` [Jailbroken: How Does LLM Safety Training Fail? (arXiv)](https://arxiv.org/abs/2307.02483)

### Prompt Hacking

Prompt hacking is a core technique for AI Red Teamers targeting LLMs. It involves crafting inputs (prompts) to manipulate the model into bypassing safety controls, revealing hidden information, or performing unintended actions. Red teamers systematically test various prompt hacking methods (like jailbreaking, role-playing, or instruction manipulation) to assess the LLM's resilience against adversarial user input.

- `@course` [Introduction to Prompt Hacking](https://learnprompting.org/courses/intro-to-prompt-hacking)
- `@article` [Prompt Hacking Guide](https://learnprompting.org/docs/prompt_hacking/introduction)
- `@article` [SoK: Prompt Hacking of LLMs (arXiv 2023)](https://arxiv.org/abs/2311.05544)

#### Safety Filter Bypasses

AI Red Teamers specifically target the safety mechanisms (filters, guardrails) implemented within or around an AI model. They test techniques like using synonyms for blocked words, employing different languages, embedding harmful requests within harmless text, or using character-level obfuscation to evade detection and induce the model to generate prohibited content, thereby assessing the robustness of the safety controls.

- `@article` [Bypassing AI Content Filters](https://www.restack.io/p/ai-driven-content-moderation-answer-bypass-filters-cat-ai)
- `@article` [How to Bypass Azure AI Content Safety Guardrails](https://mindgard.ai/blog/bypassing-azure-ai-content-safety-guardrails)
- `@article` [The Best Methods to Bypass AI Detection: Tips and Techniques](https://www.popai.pro/resources/the-best-methods-to-bypass-ai-detection-tips-and-techniques/)

#### Model Weight Stealing

AI Red Teamers assess the risk of attackers reconstructing or stealing the proprietary weights of a trained model, often through API query-based attacks. Testing involves simulating such attacks to understand how easily the model's functionality can be replicated, which informs defenses like query rate limiting, watermarking, or differential privacy.

- `@article` [A Playbook for Securing AI Model Weights](https://www.rand.org/pubs/research_briefs/RBA2849-1.html)
- `@article` [How to Steal a Machine Learning Model (SkyCryptor)](https://skycryptor.com/blog/how-to-steal-a-machine-learning-model)
- `@article` [On the Limitations of Model Stealing with Uncertainty Quantification Models](https://openreview.net/pdf?id=ONRFHoUzNk)

### Model Vulnerabilities

This category covers attacks and tests targeting the AI model itself, beyond the prompt interface. AI Red Teamers investigate inherent weaknesses in the model's architecture, training data artifacts, or prediction mechanisms, such as susceptibility to data extraction, poisoning, or adversarial manipulation.

- `@article` [AI Security Risks Uncovered: What You Must Know in 2025](https://ttms.com/uk/ai-security-risks-explained-what-you-need-to-know-in-2025/)
- `@article` [Weaknesses in Modern AI](https://insights.sei.cmu.edu/blog/weaknesses-and-vulnerabilities-in-modern-ai-why-security-and-safety-are-so-challenging/)
- `@article` [AI and ML Vulnerabilities (CNAS Report)](https://www.cnas.org/publications/reports/understanding-and-mitigating-ai-vulnerabilities)

#### Prompt Injection

Prompt injection is a critical vulnerability tested by AI Red Teamers. They attempt to insert instructions into the LLM's input that override its intended system prompt or task, causing it to perform unauthorized actions, leak data, or generate malicious output. This tests the model's ability to distinguish trusted instructions from potentially harmful user/external input.

- `@course` [Advanced Prompt Hacking - Learn Prompting](https://learnprompting.org/courses/advanced-prompt-hacking)
- `@article` [Prompt Injection & the Rise of Prompt Attacks](https://www.lakera.ai/blog/guide-to-prompt-injection)
- `@article` [Prompt Injection (Learn Prompting)](https://learnprompting.org/docs/prompt_hacking/injection)
- `@article` [Prompt Injection Attack Explanation (IBM)](https://research.ibm.com/blog/prompt-injection-attacks-against-llms)
- `@article` [Prompt Injection: Impact, How It Works & 4 Defense Measures](https://www.tigera.io/learn/guides/llm-security/prompt-injection/)
- `@course` [Prompt Injection: Hands-on Exercise Against a Live Assistant](https://ransomleak.com/exercises/clawdbot-prompt-injection/)

#### Unauthorized Access

AI Red Teamers test if vulnerabilities in the AI system or its interfaces allow attackers to gain unauthorized access to data, functionalities, or underlying infrastructure. This includes attempting privilege escalation via prompts, exploiting insecure API endpoints connected to the AI, or manipulating the AI to access restricted system resources.

- `@article` [Defending Model Files from Unauthorized Access](https://developer.nvidia.com/blog/defending-ai-model-files-from-unauthorized-access-with-canaries/)
- `@article` [OWASP API Security Project](https://owasp.org/www-project-api-security/)
- `@article` [Detecting Unauthorized Usage](https://www.unr.edu/digital-learning/instructional-strategies/understanding-and-integrating-generative-ai-in-teaching/how-can-i-detect-unauthorized-ai-usage)

#### Direct

Direct injection attacks occur when malicious instructions are inserted directly into the prompt input field by the user interacting with the LLM. AI Red Teamers use this technique to assess if basic instructions like "Ignore previous prompt" can immediately compromise the model's safety or intended function, testing the robustness of the system prompt's influence.

- `@article` [Prompt Injection](https://learnprompting.org/docs/prompt_hacking/injection?srsltid=AfmBOooOKRzLT0Hn2PNdAa69Fietniztfds6Fo1PO8WuIyyXjbLb6XgI)
- `@article` [Prompt Injection & the Rise of Prompt Attacks](https://www.lakera.ai/blog/guide-to-prompt-injection)
- `@article` [Prompt Injection Cheat Sheet (FlowGPT)](https://flowgpt.com/p/prompt-injection-cheat-sheet)

#### Indirect

Indirect injection involves embedding malicious prompts within external data sources that the LLM processes, such as websites, documents, or emails. AI Red Teamers test this by poisoning data sources the AI might interact with (e.g., adding hidden instructions to a webpage summarized by the AI) to see if the AI executes unintended commands or leaks data when processing that source.

- `@article` [The Practical Application of Indirect Prompt Injection Attacks](https://www.researchgate.net/publication/382692833_The_Practical_Application_of_Indirect_Prompt_Injection_Attacks_From_Academia_to_Industry)
- `@article` [How to Prevent Indirect Prompt Injection Attacks](https://www.cobalt.io/blog/how-to-prevent-indirect-prompt-injection-attacks)
- `@article` [Indirect Prompt Injection Data Exfiltration](https://embracethered.com/blog/posts/2024/chatgpt-macos-app-persistent-data-exfiltration/)

## Model Extraction

#### Countermeasures

AI Red Teamers must also understand and test defenses against prompt hacking. This includes evaluating the effectiveness of input sanitization, output filtering, instruction demarcation (e.g., XML tagging), contextual awareness checks, model fine-tuning for resistance, and applying the principle of least privilege to LLM capabilities and tool access.

- `@article` [Prompt Hacking Defensive Measures](https://learnprompting.org/docs/prompt_hacking/defensive_measures/introduction)
- `@article` [Mitigating Prompt Injection Attacks (NCC Group Research)](https://research.nccgroup.com/2023/12/01/mitigating-prompt-injection-attacks/)
- `@article` [Prompt Injection & the Rise of Prompt Attacks](https://www.lakera.ai/blog/guide-to-prompt-injection)
- `@article` [Prompt Injection: Impact, How It Works & 4 Defense Measures](https://www.tigera.io/learn/guides/llm-security/prompt-injection/)
- `@article` [OpenAI Best Practices for Prompt Security](https://platform.openai.com/docs/guides/prompt-engineering/strategy-write-clear-instructions)

#### Data Poisoning

AI Red Teamers simulate data poisoning attacks by evaluating how introducing manipulated or mislabeled data into potential training or fine-tuning datasets could compromise the model. They assess the impact on model accuracy, fairness, or the potential creation of exploitable backdoors, informing defenses around data validation and provenance.

- `@article` [AI Poisoning](https://www.aiblade.net/p/ai-poisoning-is-it-really-a-threat)
- `@article` [Detecting and Preventing Data Poisoning Attacks on AI Models](https://arxiv.org/abs/2503.09302)
- `@article` [Poisoning Web-Scale Training Data (arXiv)](https://arxiv.org/abs/2310.12818)

#### Adversarial Examples

A core AI Red Teaming activity involves generating adversarial examples – inputs slightly perturbed to cause misclassification or bypass safety filters – to test model robustness. Red teamers use various techniques (gradient-based, optimization-based, or black-box methods) to find inputs that exploit model weaknesses, informing developers on how to harden the model.

- `@article` [Adversarial Examples – Interpretable Machine Learning Book](https://christophm.github.io/interpretable-ml-book/adversarial.html)
- `@article` [Adversarial Testing for Generative AI](https://developers.google.com/machine-learning/guides/adv-testing)
- `@video` [How AI Can Be Tricked With Adversarial Attacks](https://www.youtube.com/watch?v=J3X_JWQkvo8?v=MPcfoQBDY0w)

### Code Injection

AI Red Teamers test for code injection vulnerabilities specifically in the context of AI applications. This involves probing whether user input, potentially manipulated via prompts, can lead to the execution of unintended code (e.g., SQL, OS commands, or script execution via generated code) within the application layer or connected systems, using the AI as a potential vector.

- `@article` [Code Injection in LLM Applications](https://neuraltrust.ai/blog/code-injection-in-llms)
- `@article` [Code Injection](https://learnprompting.org/docs/prompt_hacking/offensive_measures/code_injection)
- `@article` [Code Injection](https://owasp.org/www-community/attacks/Code_Injection)

#### Model Inversion

AI Red Teamers perform model inversion tests to assess if an attacker can reconstruct sensitive training data (like images, text snippets, or personal attributes) by repeatedly querying the model and analyzing its outputs. Success indicates privacy risks due to data memorization, requiring mitigation techniques like differential privacy or output filtering.

- `@article` [Model inversion and membership inference: Understanding new AI security risks](https://www.hoganlovells.com/en/publications/model-inversion-and-membership-inference-understanding-new-ai-security-risks-and-mitigating-vulnerabilities)
- `@article` [Extracting Training Data from LLMs (arXiv)](https://arxiv.org/abs/2012.07805)
- `@article` [Model Inversion Attacks: A Survey of Approaches and Countermeasures](https://arxiv.org/html/2411.10023v1)

#### Insecure Deserialization

AI Red Teamers investigate if serialized objects used by the AI system (e.g., for saving model states, configurations, or transmitting data) can be manipulated by an attacker. They test if crafting malicious serialized objects could lead to remote code execution or other exploits when the application deserializes the untrusted data.

- `@article` [Lightboard Lessons: OWASP Top 10 - Insecure Deserialization](https://community.f5.com/kb/technicalarticles/lightboard-lessons-owasp-top-10---insecure-deserialization/281509)
- `@article` [How Hugging Face Was Ethically Hacked](https://www.aiblade.net/p/how-hugging-face-was-ethically-hacked)
- `@article` [OWASP TOP 10: Insecure Deserialization](https://blog.detectify.com/best-practices/owasp-top-10-insecure-deserialization/)
- `@article` [Insecure Deserialization](https://owasp.org/www-community/vulnerabilities/Insecure_Deserialization)

## Model Manipulation

#### Remote Code Execution

AI Red Teamers attempt to achieve RCE on systems hosting or interacting with AI models. This could involve exploiting vulnerabilities in the AI framework itself, the web server, connected APIs, or tricking an AI agent with code execution capabilities into running malicious commands provided via prompts. RCE is often the ultimate goal of exploiting other vulnerabilities like code injection or insecure deserialization.

- `@article` [Exploiting LLMs with Code Execution (GitHub Gist)](https://gist.github.com/coolaj86/6f4f7b30129b0251f61fa7baaa881516)
- `@article` [What is remote code execution?](https://www.cloudflare.com/learning/security/what-is-remote-code-execution/)

#### Black Box Testing

In AI Red Teaming, black-box testing involves probing the AI system with inputs and observing outputs without any knowledge of the model's architecture, training data, or internal logic. This simulates an external attacker and is crucial for finding vulnerabilities exploitable through publicly accessible interfaces, such as prompt injection or safety bypasses discoverable via API interaction.

- `@article` [Black-Box, Gray Box, and White-Box Penetration Testing](https://www.eccouncil.org/cybersecurity-exchange/penetration-testing/black-box-gray-box-and-white-box-penetration-testing-importance-and-uses/)
- `@article` [What is Black Box Testing](https://www.imperva.com/learn/application-security/black-box-testing/)
- `@article` [LLM red teaming guide (open source)](https://www.promptfoo.dev/docs/red-team/)

#### Adversarial Training

AI Red Teamers evaluate the effectiveness of adversarial training as a defense. They test if models trained on adversarial examples are truly robust or if new, unseen adversarial attacks can still bypass the hardened defenses. This helps refine the adversarial training process itself.

- `@article` [Model Robustness: Building Reliable AI Models](https://encord.com/blog/model-robustness-machine-learning-strategies/)
- `@article` [Adversarial Testing for Generative AI](https://developers.google.com/machine-learning/guides/adv-testing)
- `@article` [Detecting and Preventing Data Poisoning Attacks on AI Models](https://arxiv.org/abs/2503.09302)

### Infrastructure Security

AI Red Teamers assess the security posture of the infrastructure hosting AI models (cloud environments, servers, containers). They look for misconfigurations, unpatched systems, insecure network setups, or inadequate access controls that could allow compromise of the AI system or leakage of sensitive data/models.

- `@article` [AI Infrastructure Attacks (VentureBeat)](https://venturebeat.com/ai/understanding-ai-infrastructure-attacks/)
- `@article` [Network Infrastructure Security - Best Practices and Strategies](https://www.dataguard.com/blog/network-infrastructure-security-best-practices-and-strategies/)
- `@article` [Secure Deployment of ML Systems (NIST)](https://csrc.nist.gov/publications/detail/sp/800-218/final)

#### White Box Testing

White-box testing in AI Red Teaming grants the tester full access to the model's internals (architecture, weights, training data, source code). This allows for highly targeted attacks, such as crafting precise adversarial examples using gradients, analyzing code for vulnerabilities, or directly examining training data for biases or PII leakage. It simulates insider threats or deep analysis scenarios.

- `@article` [Black-Box, Gray Box, and White-Box Penetration Testing](https://www.eccouncil.org/cybersecurity-exchange/penetration-testing/black-box-gray-box-and-white-box-penetration-testing-importance-and-uses/)
- `@article` [What is White Box Penetration Testing](https://www.getastra.com/blog/security-audit/white-box-penetration-testing/)
- `@article` [The Art of White Box Pentesting](https://infosecwriteups.com/cracking-the-code-the-art-of-white-box-pentesting-de296bc22c67)

#### Robust Model Design

AI Red Teamers assess whether choices made during model design (architecture selection, regularization techniques, ensemble methods) effectively contribute to robustness against anticipated attacks. They test if these design choices actually prevent common failure modes identified during threat modeling.

- `@article` [Model Robustness: Building Reliable AI Models](https://encord.com/blog/model-robustness-machine-learning-strategies/)
- `@article` [Understanding Robustness in Machine Learning](https://www.alooba.com/skills/concepts/machine-learning/robustness/)
- `@article` [Towards Evaluating the Robustness of Neural Networks (arXiv by Goodfellow et al.)](https://arxiv.org/abs/1608.04644)

#### API Protection

AI Red Teamers rigorously test the security of APIs providing access to AI models. They probe for OWASP API Top 10 vulnerabilities like broken authentication/authorization, injection flaws, security misconfigurations, and lack of rate limiting, specifically evaluating how these could lead to misuse or compromise of the AI model itself.

- `@article` [Securing APIs with AI for Advanced Threat Protection](https://adevait.com/artificial-intelligence/securing-apis-with-ai)
- `@article` [Securing Machine Learning APIs (IBM)](https://developer.ibm.com/articles/se-securing-machine-learning-apis/)
- `@article` [OWASP API Security Project (Top 10 2023)](https://owasp.org/www-project-api-security/)

#### Grey Box Testing

Grey-box AI Red Teaming involves testing with partial knowledge of the system, such as knowing the model type (e.g., GPT-4), having access to some documentation, or understanding the general system architecture but not having full model weights or source code. This allows for more targeted testing than black-box while still simulating realistic external attacker scenarios where some information might be gleaned.

- `@article` [AI Transparency: Connecting AI Red Teaming and Compliance](https://splx.ai/blog/ai-transparency-connecting-ai-red-teaming-and-compliance)
- `@article` [Black-Box, Gray Box, and White-Box Penetration Testing](https://www.eccouncil.org/cybersecurity-exchange/penetration-testing/black-box-gray-box-and-white-box-penetration-testing-importance-and-uses/)
- `@article` [Understanding Black Box, White Box, and Grey Box Testing](https://www.frugaltesting.com/blog/understanding-black-box-white-box-and-grey-box-testing-in-software-testing)

#### Continuous Monitoring

AI Red Teamers assess the effectiveness of continuous monitoring systems by attempting attacks and observing if detection mechanisms trigger appropriate alerts and responses. They test if monitoring covers AI-specific anomalies (like sudden shifts in output toxicity or unexpected resource consumption by the model) in addition to standard infrastructure monitoring.

- `@article` [Cyber Security Monitoring: 5 Key Components](https://www.bitsight.com/blog/5-things-to-consider-building-continuous-security-monitoring-strategy)
- `@article` [Cyber Security Monitoring: Definition and Best Practices](https://www.sentinelone.com/cybersecurity-101/cybersecurity/cyber-security-monitoring/)
- `@article` [Cybersecurity Monitoring: Definition, Tools & Best Practices](https://nordlayer.com/blog/cybersecurity-monitoring/)

#### Authentication

AI Red Teamers test the authentication mechanisms controlling access to AI systems and APIs. They attempt to bypass logins, steal or replay API keys/tokens, exploit weak password policies, or find flaws in MFA implementations to gain unauthorized access to the AI model or its management interfaces.

- `@article` [Red-Teaming in AI Testing: Stress Testing](https://www.labelvisor.com/red-teaming-abstract-competitive-testing-data-selection/)
- `@article` [What is Authentication vs Authorization?](https://auth0.com/intro-to-iam/authentication-vs-authorization)
- `@article` [JWT Attacks](https://portswigger.net/web-security/jwt)

#### Automated vs Manual

AI Red Teaming typically employs a blend of automated tools (for large-scale scanning, fuzzing prompts, generating basic adversarial examples) and manual human testing (for creative jailbreaking, complex multi-stage attacks, evaluating nuanced safety issues like bias). Automation provides scale, while manual testing provides depth and creativity needed to find novel vulnerabilities.

- `@article` [Automation Testing vs. Manual Testing: Which is the better approach?](https://www.opkey.com/blog/automation-testing-vs-manual-testing-which-is-better)
- `@article` [Manual Testing vs Automated Testing: What's the Difference?](https://www.leapwork.com/blog/manual-vs-automated-testing)
- `@article` [Spikee](https://spikee.ai)

## Defense Strategies

#### Authorization

AI Red Teamers test authorization controls to ensure that authenticated users can only access the AI features and data permitted by their roles/permissions. They attempt privilege escalation, try to access other users' data via the AI, or manipulate the AI to perform actions beyond its authorized scope.

- `@article` [What is Authentication vs Authorization?](https://auth0.com/intro-to-iam/authentication-vs-authorization)
- `@article` [Identity and access management (IAM) fundamental concepts](https://learn.microsoft.com/en-us/entra/fundamentals/identity-fundamental-concepts)
- `@article` [OWASP API Security Project](https://owasp.org/www-project-api-security/)

#### Continuous Testing

Applying continuous testing principles to AI security involves integrating automated red teaming checks into the development pipeline (CI/CD). This allows for regular, automated assessment of model safety, robustness, and alignment as the model or application code evolves, catching regressions or new vulnerabilities early. Tools facilitating Continuous Automated Red Teaming (CART) are emerging.

- `@article` [Continuous Automated Red Teaming (CART)](https://www.firecompass.com/continuous-automated-red-teaming/)
- `@article` [What is Continuous Penetration Testing? Process and Benefits](https://qualysec.com/continuous-penetration-testing/)
- `@article` [What is Continuous Testing and How Does it Work?](https://www.blackduck.com/glossary/what-is-continuous-testing.html)

#### Conferences

Attending major cybersecurity conferences (DEF CON, Black Hat, RSA) and increasingly specialized AI Safety/Security conferences allows AI Red Teamers to learn about cutting-edge research, network with peers, and discover new tools and attack/defense techniques.

- `@article` [Black Hat Events](https://www.blackhat.com/)
- `@article` [DEF CON Hacking Conference](https://defcon.org/)
- `@article` [Global Conference on AI, Security and Ethics 2025](https://unidir.org/event/global-conference-on-ai-security-and-ethics-2025/)
- `@article` [RSA Conference](https://www.rsaconference.com/)

#### Research Groups

Following and potentially contributing to research groups at universities (like CMU, Stanford, Oxford), non-profits (like OpenAI, Anthropic), or government bodies (like UK's AISI) focused on AI safety, security, and alignment provides deep insights into emerging threats and mitigation strategies relevant to AI Red Teaming.

- `@article` [AI Cybersecurity | Global Cyber Security Capacity Centre (Oxford)](https://gcscc.ox.ac.uk/ai-security)
- `@article` [Anthropic Research](https://www.anthropic.com/research)
- `@article` [Center for AI Safety](https://www.safe.ai/)
- `@article` [The AI Security Institute (AISI)](https://www.aisi.gov.uk/)

#### Forums

Engaging in online forums, mailing lists, Discord servers, or subreddits dedicated to AI security, adversarial ML, prompt engineering, or general cybersecurity helps AI Red Teamers exchange knowledge, ask questions, learn about new tools/techniques, and find collaboration opportunities.

- `@article` [LearnPrompting Prompt Hacking Discord](https://discord.com/channels/1046228027434086460/1349689482651369492)
- `@article` [Reddit - r/ChatGPTJailbreak](https://www.reddit.com/r/ChatGPTJailbreak/)
- `@article` [Reddit - r/artificial](https://www.reddit.com/r/artificial/)
- `@article` [Reddit - r/cybersecurity](https://www.reddit.com/r/cybersecurity/)

#### Testing Platforms

Platforms used by AI Red Teamers range from general penetration testing OS distributions like Kali Linux to specific AI red teaming tools/frameworks like Microsoft's PyRIT or Promptfoo, and vulnerability scanners like OWASP ZAP adapted for API testing of AI services. These platforms provide the toolsets needed to conduct assessments.

- `@article` [AI Red Teaming Agent - Azure AI Foundry | Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-red-teaming-agent)
- `@article` [Kali Linux](https://www.kali.org/)
- `@article` [OWASP Zed Attack Proxy (ZAP)](https://owasp.org/www-project-zap/)
- `@article` [Promptfoo](https://www.promptfoo.dev/)
- `@article` [PyRIT (Python Risk Identification Tool for generative AI)](https://github.com/Azure/PyRIT)

## Community Engagement

#### Monitoring Solutions

AI Red Teamers interact with monitoring tools primarily to test their effectiveness (evasion) or potentially exploit vulnerabilities within them. Understanding tools like IDS (Snort, Suricata), network analyzers (Wireshark), and SIEMs helps red teamers simulate attacks that might bypass or target these defensive systems.

- `@article` [Open Source IDS Tools: Comparing Suricata, Snort, Bro (Zeek), Linux](https://levelblue.com/blogs/security-essentials/open-source-intrusion-detection-tools-a-quick-overview)
- `@article` [Snort](https://www.snort.org/)
- `@article` [Suricata](https://suricata.io/)
- `@article` [Wireshark](https://www.wireshark.org/)
- `@article` [Zeek (formerly Bro)](https://zeek.org/)

#### Lab Environments

AI Red Teamers need environments to practice attacking vulnerable systems safely. While traditional labs (HTB, THM, VulnHub) build general pentesting skills, platforms are emerging with labs specifically focused on AI/LLM vulnerabilities, prompt injection, or adversarial ML challenges.

- `@article` [HackAPrompt Playground](https://learnprompting.org/hackaprompt-playground)
- `@article` [InjectPrompt Playground](https://playground.injectprompt.com/)
- `@article` [Gandalf AI Prompt Injection Lab](https://gandalf.lakera.ai/)
- `@article` [PromptTrace](https://prompttrace.airedlab.com/)

#### Benchmark Datasets

AI Red Teamers may use or contribute to benchmark datasets specifically designed to evaluate AI security. These datasets (like HackAprompt, SecBench, NYU CTF Bench, CySecBench) contain prompts or scenarios targeting vulnerabilities, safety issues, or specific cybersecurity capabilities, allowing for standardized testing of models.

- `@article` [HackAPrompt Dataset](https://huggingface.co/datasets/hackaprompt/hackaprompt-dataset)
- `@article` [CySecBench: Generative AI-based CyberSecurity-focused Prompt Dataset](https://github.com/cysecbench/dataset)
- `@article` [NYU CTF Bench: A Scalable Open-Source Benchmark Dataset for Evaluating LLMs in Offensive Security](https://proceedings.neurips.cc/paper_files/paper/2024/hash/69d97a6493fbf016fff0a751f253ad18-Abstract-Datasets_and_Benchmarks_Track.html)
- `@article` [SecBench: A Comprehensive Multi-Dimensional Benchmarking Dataset for LLMs in Cybersecurity](https://arxiv.org/abs/2412.20787)

#### LLM Security Testing

The core application area for many AI Red Teamers today involves specifically testing Large Language Models for vulnerabilities like prompt injection, jailbreaking, harmful content generation, bias, and data privacy issues using specialized prompts and evaluation frameworks.

- `@course` [AI Red Teaming Courses - Learn Prompting](https://learnprompting.org/blog/ai-red-teaming-courses)
- `@article` [SecBench: A Comprehensive Multi-Dimensional Benchmarking Dataset for LLMs in Cybersecurity](https://arxiv.org/abs/2412.20787)
- `@article` [The Ultimate Guide to Red Teaming LLMs and Adversarial Prompts (Kili Technology)](https://kili-technology.com/large-language-models-llms/red-teaming-llms-and-adversarial-prompts)
- `@course` [OWASP LLM, Agentic and MCP Top 10: Exploit-then-Fix Labs](https://ransomleak.com/catalogue/ai-security/)

#### CTF Challenges

Capture The Flag competitions increasingly include AI/ML security challenges. Participating in CTFs (tracked on CTFtime) or platforms like picoCTF helps AI Red Teamers hone skills in reverse engineering, web exploitation, and cryptography applied to AI systems, including specialized AI safety CTFs.

- `@article` [HackAPrompt](https://www.hackaprompt.com/)
- `@article` [Progress from our Frontier Red Team](https://www.anthropic.com/news/strategic-warning-for-ai-risk-progress-and-insights-from-our-frontier-red-team)
- `@article` [CTFtime.org](https://ctftime.org/)

#### Custom Testing Scripts

AI Red Teamers frequently write custom scripts (often in Python) to automate bespoke attacks, interact with specific AI APIs, generate complex prompt sequences, parse model outputs at scale, or implement novel exploit techniques not found in standard tools. Proficiency in scripting is essential for advanced AI red teaming.

- `@article` [Python for Cybersecurity: Key Use Cases and Tools](https://panther.com/blog/python-for-cybersecurity-key-use-cases-and-tools)
- `@article` [Python for cybersecurity: use cases, tools and best practices](https://softteco.com/blog/python-for-cybersecurity)
- `@article` [Scapy](https://scapy.net/)

#### Agentic AI Security

As AI agents capable of autonomous action become more common, AI Red Teamers must test their unique security implications. This involves assessing risks related to goal hijacking, unintended actions through tool use, exploitation of planning mechanisms, and ensuring agents operate safely within their designated boundaries. A growing share of real-world incidents target the tool-connection layer rather than the model itself — confused-deputy attacks where a tool server forwards a caller's credentials to a downstream service it was never issued for, or a malicious instruction hidden in untrusted content (e.g. a GitHub issue) tricking an agent into exfiltrating data through a fully trusted tool. Testing an agentic system means testing its tool boundaries and cross-server trust as rigorously as its prompts.

- `@article` [AI Agents - Learn Prompting](https://learnprompting.org/docs/intermediate/ai_agents)
- `@article` [EmbraceTheRed](https://embracethered.com/)
- `@official` [Model Context Protocol - Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)
- `@article` [GitHub MCP Exploited: Accessing Private Repositories via MCP - Invariant Labs](https://invariantlabs.ai/blog/mcp-github-vulnerability)
- `@course` [Agentic Goal Hijacking: Hands-on Exercise](https://ransomleak.com/exercises/agentic-goal-hijack/)

#### Red Team Simulations

Participating in or conducting structured red team simulations against AI systems (or components) provides the most realistic practice. This involves applying methodologies, TTPs (Tactics, Techniques, and Procedures), reconnaissance, exploitation, and reporting within a defined scope and objective, specifically targeting AI vulnerabilities.

- `@article` [A Simple Guide to Successful Red Teaming](https://www.cobaltstrike.com/resources/guides/a-simple-guide-to-successful-red-teaming)
- `@article` [The Complete Guide to Red Teaming: Process, Benefits & More](https://mindgard.ai/blog/red-teaming)
- `@article` [The Complete Red Teaming Checklist \[PDF\]: 5 Key Steps - Mindgard AI](https://mindgard.ai/blog/red-teaming-checklist)

#### Reporting Tools

AI Red Teamers use reporting techniques and potentially tools to clearly document their findings, including discovered vulnerabilities, successful exploit steps (e.g., effective prompts), assessed impact, and actionable recommendations tailored to AI systems. Good reporting translates technical findings into understandable risks for stakeholders.

- `@article` [The Complete Red Teaming Checklist \[PDF\]: 5 Key Steps - Mindgard AI](https://mindgard.ai/blog/red-teaming-checklist)
- `@article` [Penetration Testing Report: 6 Key Sections and 4 Best Practices](https://brightsec.com/blog/penetration-testing-report/)
- `@article` [Penetration testing best practices: Strategies for all test types](https://www.strikegraph.com/blog/pen-testing-best-practices)

#### Responsible Disclosure

A critical practice for AI Red Teamers is responsible disclosure: privately reporting discovered AI vulnerabilities (e.g., a successful jailbreak, data leak method, or severe bias) to the model developers or system owners, allowing them time to remediate before any public discussion, thus preventing malicious exploitation.

- `@article` [0din.ai Policy](https://0din.ai/policy)
- `@article` [Huntr Guidelines](https://huntr.com/guidelines)
- `@article` [Google Vulnerability Reward Program (VRP)](https://bughunters.google.com/)

## Practical Experience

#### Specialized Courses

Targeted training is crucial for mastering AI Red Teaming. Look for courses covering adversarial ML, prompt hacking, LLM security, ethical hacking for AI, and specific red teaming methodologies applied to AI systems offered by platforms like Learn Prompting, Coursera, or security training providers.

- `@course` [AI Red Teaming Courses - Learn Prompting](https://learnprompting.org/blog/ai-red-teaming-courses)
- `@course` [AI Security | Coursera](https://www.coursera.org/learn/ai-security)
- `@course` [Free Online Cyber Security Courses with Certificates in 2025](https://www.eccouncil.org/cybersecurity-exchange/cyber-novice/free-cybersecurity-courses-beginners/)

#### Emerging Threats

AI Red Teamers must stay informed about potential future threats enabled by more advanced AI, such as highly autonomous attack agents, AI-generated malware that evades detection, sophisticated deepfakes for social engineering, or large-scale exploitation of interconnected AI systems. Anticipating these helps shape current testing priorities. One concrete example: in April 2026, researchers disclosed an architectural flaw across the official MCP SDKs (Python, TypeScript, Java, and Rust) allowing remote code execution, affecting an estimated 200,000 deployed servers across widely-used agent tooling. Because agents increasingly share common protocol layers and tooling infrastructure rather than each running bespoke code, a single flaw in that shared layer can propagate across the whole ecosystem at once — a different failure mode than a vulnerability scoped to one vendor's model, and one red team priorities should account for.

- `@article` [AI Security Risks Uncovered: What You Must Know in 2025](https://ttms.com/uk/ai-security-risks-explained-what-you-need-to-know-in-2025/)
- `@article` [Why Artificial Intelligence is the Future of Cybersecurity](https://www.darktrace.com/blog/why-artificial-intelligence-is-the-future-of-cybersecurity)
- `@article` [AI Index 2024](https://aiindex.stanford.edu/report/)
- `@article` [MCP Supply Chain Advisory: RCE Vulnerabilities Across the AI Ecosystem - OX Security](https://www.ox.security/blog/mcp-supply-chain-advisory-rce-vulnerabilities-across-the-ai-ecosystem/)
- `@article` [Critical RCE in Anthropic MCP Inspector (CVE-2025-49596) - Oligo Security](https://www.oligo.security/blog/critical-rce-vulnerability-in-anthropic-mcp-inspector-cve-2025-49596)

#### Industry Credentials

Beyond formal certifications, recognition in the AI Red Teaming field comes from practical achievements like finding significant vulnerabilities (responsible disclosure), winning AI-focused CTFs or hackathons (like HackAPrompt), contributing to AI security research, or building open-source testing tools.

- `@article` [HackAPrompt](https://hackaprompt.com)
- `@article` [RedTeam Arena](https://redarena.ai)

#### Advanced Techniques

The practice of AI Red Teaming itself will evolve. Future techniques may involve using AI adversaries to automatically discover complex vulnerabilities, developing more sophisticated methods for testing AI alignment and safety properties, simulating multi-agent system failures, and creating novel metrics for evaluating AI robustness against unknown future attacks.

- `@article` [AI red-teaming in critical infrastructure: Boosting security and trust in AI systems](https://www.dnv.com/article/ai-red-teaming-for-critical-infrastructure-industries/)
- `@article` [Advanced Techniques in AI Red Teaming for LLMs](https://neuraltrust.ai/blog/advanced-techniques-in-ai-red-teaming)
- `@article` [Diverse and Effective Red Teaming with Auto-generated Rewards and Multi-step Reinforcement Learning](https://arxiv.org/html/2412.18693v1)

## Certifications

#### Research Opportunities

AI Red Teaming relies on ongoing research. Key areas needing further investigation include scalable methods for finding elusive vulnerabilities, understanding emergent behaviors in complex models, developing provable safety guarantees, creating better benchmarks for AI security, and exploring the socio-technical aspects of AI misuse and defense.

- `@article` [Cutting-Edge Research on AI Security bolstered with new Challenge Fund](https://www.gov.uk/government/news/cutting-edge-research-on-ai-security-bolstered-with-new-challenge-fund-to-ramp-up-public-trust-and-adoption)
- `@article` [Careers | The AI Security Institute (AISI)](https://www.aisi.gov.uk/careers)
- `@article` [Research - Anthropic](https://www.anthropic.com/research)

#### Industry Standards

As AI matures, AI Red Teamers will increasingly need to understand and test against emerging industry standards and regulations for AI safety, security, and risk management, such as the NIST AI RMF, ISO/IEC 42001, and sector-specific guidelines, ensuring AI systems meet compliance requirements.

- `@article` [ISO 42001: The New Compliance Standard for AI Management Systems](https://www.brightdefense.com/resources/iso-42001-compliance/)
- `@article` [ISO 42001: What it is & why it matters for AI management](https://www.itgovernance.co.uk/iso-42001)
- `@article` [NIST AI Risk Management Framework (AI RMF)](https://www.nist.gov/itl/ai-risk-management-framework)
- `@article` [ISO/IEC 42001: Information technology — Artificial intelligence — Management system](https://www.iso.org/standard/81230.html)
