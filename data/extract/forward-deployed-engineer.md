# Forward Deployed Engineer — plan extrait

- **Slug** : `forward-deployed-engineer`
- **Description amont** : Step-by-step guide to becoming a Forward Deployed Engineer in @currentYear@
- **Derniere modification amont** : 2026-06-30T07:38:33.403Z
- **Capture** : 2026-09-16
- **Volume** : 20 noeuds de contenu, 19 documentes, 30 ressources
- **Renvois vers d'autres roadmaps** : `https://roadmap.sh`, `https://roadmap.sh/ai-engineer`, `https://roadmap.sh/backend`, `https://roadmap.sh/backend?r=backend-beginner`, `https://roadmap.sh/datastructures-and-algorithms`, `https://roadmap.sh/devops`, `https://roadmap.sh/devops?r=devops-beginner`, `https://roadmap.sh/frontend`, `https://roadmap.sh/frontend?r=frontend-beginner`, `https://roadmap.sh/linux`, `https://roadmap.sh/system-design`

---

## FDE Roadmap

#### From X to FDE

Three backgrounds tend to transition well into the FDE role: software engineers, consultants, and product managers. Software engineers already have the technical foundation but often need to develop the ability to communicate AI tradeoffs to non-technical stakeholders and build a portfolio that shows they can own a full deployment, not just write code. Consultants and PMs can already translate data into business outcomes, which is half the job, but need to close the gap on engineering by building real agents, RAG pipelines, and eval frameworks from scratch.

- `@article` [The Definitive Guide to Forward Deployed Engineer Interviews in 2026](https://www.sundeepteki.org/advice/the-definitive-guide-to-forward-deployed-engineer-interviews-in-2026)

### Introduction

A Forward Deployed Engineer is a software engineer who works directly inside a customer's environment to build, deploy, and stabilize AI systems. The role originated at Palantir, where engineers called Deltas would embed with clients, sometimes on military bases, to ship code overnight based on feedback from the field that same day. That same idea is now at the center of how companies like OpenAI and Anthropic are bringing AI into large enterprises. The job requires technical depth, the ability to read an unfamiliar codebase quickly, and the communication skills to explain what AI can and cannot do to a non-technical decision maker.

- `@article` [Forward deployed engineer is AI’s hottest job](https://thenewstack.io/forward-deployed-engineer-fde-openai-google/)
- `@article` [Forward-deployed engineer: The complete guide](https://www.rocketlane.com/blogs/forward-deployed-engineer)

#### Roles & Responsabilities

The FDE job has three phases: audit, evals, and deployment. In the audit phase, you embed with different teams inside the customer's organization, map their workflows, identify bottlenecks, and decide where AI can create real value and where it cannot. In the evals phase, you build systems to measure whether the AI is actually working, not just whether it produces an answer, but whether it reasons through problems the way a skilled human would. In the deployment phase, you ship the system into production, starting with the smallest possible unit of autonomy and layering on capabilities only after each step is proven to work.

- `@article` [Forward-deployed engineer: The complete guide](https://www.rocketlane.com/blogs/forward-deployed-engineer)

### Linux Skills

Linux is an open-source operating system used widely in servers, cloud environments, and developer workstations. Most production software runs on Linux, so being comfortable navigating a Linux system, managing processes, reading logs, and configuring services is a practical necessity for anyone building and deploying in real customer environments.

- `@course` [Linux for Noobs](https://labex.io/courses/linux-for-noobs)
- `@article` [Practice Linux Fundamentals](https://labex.io/linuxjourney)
- `@video` [Linux Fundamentals](https://www.youtube.com/watch?v=kPylihJRG70)

### Frontend Skills

Frontend development refers to the part of web development concerned with what users see and interact with in a browser. It covers HTML for structure, CSS for styling, and JavaScript for interactivity. FDEs who can build functional frontends are more self-sufficient in customer engagements, able to deliver end-to-end demos and working prototypes without depending on a separate frontend team.

- `@book` [Frontend Development Handbook](https://github.com/FrontendMasters/front-end-handbook-2019/blob/master/exports/Front-end%20Developer%20Handbook%202019.pdf)
- `@video` [Frontend web development - a complete overview](https://www.youtube.com/watch?v=WG5ikvJ2TKA)

### Backend Skills

Backend development refers to the server-side logic of a web application, including handling requests, running business logic, interacting with databases, and returning responses. Backend systems are typically built with Python, Node.js, Java, or Go, connected to databases and external services. FDEs who can build solid backend systems can own the full delivery of a feature rather than handing off at the API boundary.

- `@article` [What is backend? A comprehensive intro to server-side development](https://alokai.com/blog/what-is-backend)
- `@video` [How The Backend Works](https://www.youtube.com/watch?v=4r6WdaY3SOA)

### DSA & System Design

Data structures are ways of organizing data in memory, such as arrays, linked lists, trees, graphs, and hash maps. Algorithms are step-by-step procedures for solving problems, like sorting, searching, or traversal. Knowing these well means being able to evaluate performance characteristics of code, debug inefficiencies in customer systems, and reason clearly about solutions to technical problems.

- `@roadmap` [Visit the Dedicated Data Structures & Algorithms Roadmap](https://roadmap.sh/datastructures-and-algorithms)
- `@article` [Data Structures and Algorithms (DSA) Tutorial](https://www.tutorialspoint.com/data_structures_algorithms/index.htm)
- `@video` [What Are Data Structures?](https://www.youtube.com/watch?v=bum_19loj9A)

### AI Engineering Skills

AI Engineering

AI engineering involves building software systems that use machine learning models and large language models (LLMs) as components. This includes selecting models, integrating them via APIs, engineering prompts, managing context, and deploying AI features in production. AI engineering is at the core of the job of FDEs. It's what turns an AI model into a product that runs reliably inside a company's infrastructure.

- `@article` [What Is an AI Engineer? (And How to Become One)](https://www.coursera.org/articles/ai-engineer)
- `@video` [AI, Machine Learning, Deep Learning and Generative AI Explained](https://www.youtube.com/watch?v=qYNweeDHiyU)

### DevOps Skills

## Customer Delivery & Field Skills

#### Requirements Gathering

Project requirements come from observation as much as from conversation. You watch how teams actually work, not just how they describe their work, because those two things are often different. The goal is to surface the undocumented workflow, the data source people actually trust, and the edge cases that would break an agent in its first week of production. Written requirements are useful, but the real requirements live in the room with the people doing the work.

- `@course` [Requirements Gathering in Business Analysis](https://www.coursera.org/learn/requirements-gathering-in-business-analysis)
- `@article` [Requirements Gathering in Software Engineering](https://www.jamasoftware.com/requirements-management-guide/requirements-gathering-and-management-processes/what-is-requirements-gathering/)
- `@video` [Requirement Gathering Techniques For A Business Analyst](https://www.youtube.com/watch?v=8EBWxW5Cn1g)

#### Technical Scoping & Sequencing

Technical scoping involves breaking a project into discrete tasks, estimating their complexity, and identifying dependencies. Sequencing means ordering those tasks logically, starting with the highest-risk or most uncertain parts. A well-scoped and sequenced project is easier to track and deliver on time, and gives the customer visibility into what is being built and in what order.

- `@article` [How to effectively scope your software projects](https://medium.com/free-code-camp/how-to-effectively-scope-your-software-projects-from-planning-to-execution-e96cbcac54b9)
- `@video` [Project Scope Statement \[IN 4 EASY STEPS\]](https://www.youtube.com/watch?v=QDLk2QIuJkg)

#### Enterprise Workflow

Enterprise workflows are the processes and systems through which large organizations operate, including approvals, handoffs, integrations with existing tools, and compliance requirements. Building for enterprise environments requires understanding these workflows and designing solutions that fit within them.

- `@article` [What is enterprise workflow management?](https://www.manageengine.com/appcreator/enterprise-workflow-management.html)

#### Tradeoffs: Scope, Speed, Quality

Every project involves tradeoffs between scope (how much is built), speed (how fast it is delivered), and quality (how well it holds up over time). Reducing scope can speed things up without sacrificing quality. Cutting corners on quality can speed things up in the short term but creates problems later. FDEs need to understand and communicate these tradeoffs clearly, helping customers make informed decisions rather than just agreeing to everything and delivering less than expected.

- `@article` [Project management triangle: Triple constraint guide](https://asana.com/resources/project-management-triangle)
- `@video` [What is the Iron Triangle? Time, Cost, Quality, Scope?](https://www.youtube.com/watch?v=JHSHOAfV-uw)

### Discovery & Scoping

Discovery and scoping is the phase of a customer engagement where the team identifies the problem to solve, understands the current state of the customer's systems and processes, and defines what success looks like. It involves asking the right questions, identifying constraints, and setting realistic expectations before any building begins. Getting this phase right determines whether the rest of the engagement goes smoothly or runs into avoidable problems.

- `@article` [AI Techniques (Production): Use Case Discovery & System Scoping](https://academy.openai.com/public/clubs/builders-etkn1/videos/ai-techniques-production-use-case-discovery-and-system-scoping-2025-12-11)
- `@article` [AI Discovery & Scoping Session](https://www.elevatecorporatetraining.com.au/ai-discovery-scoping/)

#### ROI & AI Impact

Understanding return on investment (ROI) for AI projects means being able to quantify how an AI system creates value, whether through cost savings, productivity improvements, revenue growth, or risk reduction. It also means being honest about what AI can realistically deliver. FDEs who can frame AI work in business terms help customers build confidence in the investment and avoid overselling what the technology can do.

- `@article` [How to maximize AI ROI in 2026](https://www.ibm.com/think/insights/ai-roi)
- `@article` [What is ROI and How to Calculate Return on Investment](https://www.esade.edu/beyond/en/what-is-roi-and-how-to-calculate-return-on-investment/)

### Business Acumen

Business acumen is the ability to understand how an organization operates, what its priorities are, how it makes money, and where technology can create real value. Being able to connect engineering decisions to business outcomes is what makes FDEs different from traditional software engineers.

#### Stakeholder Management

Stakeholder management in FDE work is less about keeping people happy and more about making sure the right people know what is happening before it becomes a problem. This means identifying who the skeptics are early, giving them the evidence they need to trust the system (usually evals), managing expectations before a demo rather than after it goes wrong, and escalating blockers fast rather than letting them quietly slow the engagement. The technical work can be excellent, and the engagement can still fail if the people who need to approve, adopt, or fund the system never get bought in.

- `@article` [Stakeholder Management Guide: Definitions, Processes & More](https://simplystakeholders.com/resources/guides/stakeholder-management/)

#### Technical Writing

Technical writing is the practice of producing clear, accurate, and useful documentation for software systems. This includes API docs, architecture decision records, runbooks, onboarding guides, and design documents. Technical writing is especially important because good documentation is often what allows a customer to operate and extend a system after the engagement ends, without needing to call the FDE back for every question.

- `@roadmap` [Visit the Dedicated Technical Writer Roadmap](https://roadmap.sh/technical-writer)

### Communication

If you cannot explain what AI can and cannot do to a non-technical VP, you cannot be an FDE. Communication in this role is about translating between two different worlds: the technical reality of what you are building and the business reality of what the customer needs to justify the investment. That means being able to speak about token costs and latency in the same conversation where you are explaining ROI to an executive. It also means knowing when to say AI is not the right answer.

#### Product Feedback Loop

A product feedback loop is the cycle of shipping something, collecting feedback from users or stakeholders, and using that input to improve future iterations. This usually means working closely with the customer to observe how the delivered product is actually being used, identifying gaps between expectation and reality, and feeding those observations back into the build process while still on the engagement.
