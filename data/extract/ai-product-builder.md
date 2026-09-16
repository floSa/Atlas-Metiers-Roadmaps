# AI Product Builder — plan extrait

- **Slug** : `ai-product-builder`
- **Description amont** : A step-by-step guide to building and shipping products with AI.
- **Derniere modification amont** : 2026-06-25T07:26:26.674Z
- **Capture** : 2026-09-16
- **Volume** : 52 noeuds de contenu, 50 documentes, 120 ressources
- **Renvois vers d'autres roadmaps** : `https://bit.cloud/?c=rsh-a`, `https://roadmap.sh`, `https://roadmap.sh/claude-code`, `https://roadmap.sh/full-stack`, `https://roadmap.sh/vibe-coding`

---

## AI Product Builder

#### Problem Definition

Start by writing one or two sentences describing the problem your app solves and who it solves it for. If you cannot explain the problem clearly, the generated output will be unfocused. This is the most important input you give to the entire process.

#### App Anatomy

Every app has the same basic parts: a front end that users interact with, a back end that processes logic, a database that stores data, and an API that connects them. Understanding this structure helps you review what the AI generates and ask better questions when something does not work as expected.

- `@roadmap` [Visit the Dedicated Frontend Roadmap](https://roadmap.sh/frontend/)
- `@roadmap` [Visit the Dedicated Fr Backend](https://roadmap.sh/backend)
- `@roadmap` [Visit the Dedicated API Design Roadmap](https://roadmap.sh/api-design)
- `@article` [Web Application Architecture: Front-end, Middleware and Back-end](https://dev.to/techelopment/web-application-architecture-front-end-middleware-and-back-end-2ld7)

### AI Product Creation Cycle

AI tools are changing how software is built. The traditional approach of writing code from scratch is being replaced by a new paradigm: you generate a working product from your requirements, test it with real users, and refine it in repeated cycles until it is ready to ship.

- `@article` [Will AI make us all product builders?](https://www.fundament.design/p/will-ai-make-us-all-product-builders?hide_intro_popup=true)
- `@article` [Building AI Products: From Concept to Launch](https://www.digitalocean.com/resources/articles/building-ai-products#understanding-the-ai-product-lifecycle)

#### Feature Scoping

List only the features that are strictly necessary for the first version of the product. Every feature you add increases the complexity of the generated code and the time needed to test and refine it. Start small, ship fast, and add features in later iterations.

- `@article` [How to effectively scope your software projects](https://www.freecodecamp.org/news/how-to-effectively-scope-your-software-projects-from-planning-to-execution-e96cbcac54b9/)

### Definition & Scope

Before writing a single prompt, you need to know what you are building and why. This means defining the problem, identifying the core features, and setting the project's technical boundaries. A clear scope saves time and prevents the AI from generating things you do not need.

- `@article` [How to scope your AI product](https://uxdesign.cc/how-to-scope-your-ai-product-5b9885ef3851)

#### Tech Stack & Constraints

Define the technologies you want to use before generating anything. AI generation tools produce better output when given clear constraints rather than being left to choose freely. An important note when choosing your tech stack is to pick a popular stack like React, Next.js, Tailwind, or Supabase. AI tools have been trained on large amounts of code using these technologies and produce more reliable output with them. Niche or very new tools increase the chance of errors in the generated code and make it harder to find help when something breaks.

- `@roadmap` [Visit the Dedicated Vibe Coding Roadmap](https://roadmap.sh/vibe-coding)
- `@article` [The Best Tech Stack in the Age of AI](https://thebootstrappedfounder.com/the-best-tech-stack-in-the-age-of-ai/)

## Product Development Cycle

#### Choose a Prototype Tool

Developers are increasingly moving away from traditional design tools like Figma and Miro toward AI prototyping tools that generate a working version of the app directly from a text description. Tools like Lovable, Replit, and Bolt let you go from idea to something clickable in minutes, which makes it easier to validate a concept before committing to a full generation cycle. Choose based on your familiarity and the complexity of what you are building.

- `@article` [Best AI Prototyping Tools in 2026: Ranked by Use Case](https://www.banani.co/blog/best-ai-prototyping-tools)
- `@article` [Prototyping Tools: A Comprehensive Guide Intro](https://www.coursera.org/articles/prototyping-tools)

#### Feedback & Validation

Before generating the full product, share the prototype with your team and some potential users. You are looking for obvious gaps or misunderstandings in the design. Catching these at the prototype stage is much cheaper than fixing them after generation.

### 1. Prototyping

A prototype is a visual representation of your app before any code is generated. It helps you align with stakeholders, catch missing features early, and give the generation tool a concrete reference to work from. It does not need to be detailed; it just needs to be clear enough to communicate intent.

- `@article` [Software prototyping: What it is, its process, and the best tools to use](https://www.hostinger.com/tutorials/software-prototyping#h-can-i-create-prototypes-with-ai)

### 2. Generation

This is the step where your prototype and requirements are turned into a working codebase by an AI tool. The output should include a front end, a back end, a database schema, and an API layer. The quality of the output depends directly on the clarity of your inputs.

### 3. Refinement

Once you have a generated codebase, you will need to adjust it. Some changes are small and targeted; others require regenerating a larger part of the application. Knowing which type of change you are dealing with before you start saves time and reduces the risk of breaking something that already works.

## AI App Builders

#### Lovable

Lovable generates a working front-end application from a text description. It is one of the fastest ways to move from an idea to a clickable prototype. The output is sufficient for early user testing but may require refinement before it is ready for production.

- `@official` [Lovable Docs](https://docs.lovable.dev/introduction/welcome)
- `@article` [What is Lovable AI? A Deep Dive into the Builder | UI Bakery Blog](https://uibakery.io/blog/what-is-lovable-ai)
- `@video` [Master Lovable In 24 Minutes](https://www.youtube.com/watch?v=rqvtLxwMklo)

#### Replit

Replit is a browser-based coding environment that also supports AI-assisted app generation. It is useful when you want to prototype and immediately run the code in the same place. It works well for small projects and quick experiments.

- `@official` [Replit Docs](https://docs.replit.com/getting-started/intro-replit)
- `@article` [What is Replit? An honest look at the AI app builder in 2025](https://www.eesel.ai/blog/replit)
- `@video` [Getting Started with Replit](https://www.youtube.com/watch?v=St95nPOwsa8&list=PLto9KpJAqHMTzEMDAFT4r5LlI4NByngyT)

#### Claude Design

#### v0

v0 is Vercel's UI generation tool. You describe a component or screen, and it produces React code ready to use in your project. It is best for generating individual UI components rather than full applications.

- `@official` [v0 Docs](https://v0.app/docs)
- `@article` [Transforming how you work with v0 - Vercel](https://vercel.com/blog/transforming-how-you-work-with-v0)
- `@video` [How To Use v0 by Vercel For Beginners](https://www.youtube.com/watch?v=41SR07p243Q)

#### Hope

Hope is an agentic architect that transforms human prompts into composable, production-ready software. By automating complex engineering, it bridges the gap between rapid prototyping and professional standards, enabling teams to build scalable, enterprise-grade systems in hours.

- `@official` [Hope: Ships to Production](https://bit.cloud/products/hope-ai?c=ai-roadmap)
- `@official` [Get started with Hope](https://bit.cloud/docsc=rsh-a?c=rsh-a)

#### Bolt

Bolt generates full-stack applications from a prompt and produces clean, readable code. It is faster than writing from scratch and gives you more control over the output than most no-code tools. It works particularly well for standard web app structures.

- `@official` [Getting Started with Bolt](https://support.bolt.new/building/quickstart)
- `@article` [Bolt.new Review 2025: The Good, Bad, and Surprising Findings for Developers](https://trickle.so/blog/bolt-new-review)
- `@video` [Bolt.New AI Tutorial for Beginners: Create an App in Under 20 Minutes!](https://www.youtube.com/watch?v=5zfOitaKfmM)

#### Claude Code

Claude Code is a terminal-based AI tool built by Anthropic. It is designed to reason through complex code problems, explain unfamiliar codebases, and help with debugging. It works best when you need to understand what the generated code is doing before modifying it.

- `@roadmap` [Visit the Dedicated Claude Code Roadmap](https://roadmap.sh/claude-code)
- `@official` [Claude Code Overview](https://code.claude.com/docs/en/overview)
- `@article` [Claude Code: From Zero to Hero](https://medium.com/@dan.avila7/claude-code-from-zero-to-hero-bebe2436ac32)
- `@video` [Claude Code Tutorial for Beginners](https://www.youtube.com/watch?v=eMZmDH3T2bY)

#### Gemini CLI

Gemini CLI is Google's command-line AI tool for developers. It integrates with your existing terminal workflow and can assist with code generation, explanation, and refactoring. It is a practical option if you are already working within the Google Cloud infrastructure.

- `@course` [Hands-on with Gemini CLI](https://codelabs.developers.google.com/gemini-cli-hands-on#0)
- `@official` [Gemini CLI Docs](https://geminicli.com/docs/)
- `@video` [Gemini CLI: The AI agent that lives in your terminal](https://www.youtube.com/watch?v=C5Cjvpfzc_0)

#### Codex

Codex is OpenAI's code-focused model, available through the API and integrated into tools like GitHub Copilot. It is strong at generating boilerplate and translating natural language descriptions into working code. It works best for well-defined, contained tasks rather than open-ended architectural decisions.

- `@course` [Introduction to OpenAI Codex](https://www.coursera.org/learn/introduction-to-openai-codex)
- `@official` [Codex Docs](https://developers.openai.com/codex)
- `@video` [Getting started with Codex](https://www.youtube.com/watch?v=px7XlbYgk7I)

## Use AI-assisted Coding Tools

#### Claude Code

Claude Code works in the terminal and is best used when you need to understand a piece of generated code before modifying it. Give it a specific problem; ask it to explain a function, trace a bug, or rewrite a block of logic. It reasons through the code step by step, which makes it reliable for changes where the consequences are not immediately obvious.

- `@roadmap` [Visit the Dedicated Claude Code Roadmap](https://roadmap.sh/claude-code)
- `@official` [Claude Code Overview](https://code.claude.com/docs/en/overview)
- `@article` [Claude Code: From Zero to Hero](https://medium.com/@dan.avila7/claude-code-from-zero-to-hero-bebe2436ac32)
- `@video` [laude Code Tutorial for Beginners](https://www.youtube.com/watch?v=eMZmDH3T2bY)

#### Codex

Codex is best for translating a clearly defined requirement into working code. Describe the specific behavior you want; it generates the implementation. It works well for adding a new function, rewriting a poorly structured block, or converting logic from one pattern to another. Keep the scope narrow; the more specific the input, the more useful the output.

- `@course` [Introduction to OpenAI Codex](https://www.coursera.org/learn/introduction-to-openai-codex)
- `@official` [Codex Docs](https://developers.openai.com/codex)
- `@video` [Getting started with Codex](https://www.youtube.com/watch?v=px7XlbYgk7I)

#### Cursor

Cursor lets you select any part of the codebase and ask questions or request changes directly in the editor. It is the most practical tool for navigating AI-generated code you did not write yourself. Use it to understand what a file does, rename a pattern across the codebase, or make a targeted edit without having to read every line around it.

- `@course` [Cursor Learn](https://cursor.com/learn)
- `@official` [Cursor Docs](https://cursor.com/docs)
- `@video` [Cursor AI Tutorial for Beginners](https://www.youtube.com/watch?v=3289vhOUdKA)
- `@video` [Cursor Tutorial for Beginners (AI Code Editor)](https://www.youtube.com/watch?v=ocMOZpuAMw4)

#### Copilot

Copilot works inline as you type and is best used when you know what you want to write but want to move faster. It predicts the next line or block based on the surrounding code. It is less useful for understanding unfamiliar code and more useful for extending code you already understand; use it when adding new logic to an existing file.

- `@official` [GitHub Copilot Docs](https://docs.github.com/en/copilot)
- `@official` [Copilot Tutorials](https://github.com/features/copilot/tutorials)
- `@video` [Intro to GitHob Copilot in Visual Studio](https://www.youtube.com/watch?v=z1ycDvspv8U)

## Technical but Powerful

#### Targeted Change

A targeted change is a small, localized fix: a bug in a component, a layout adjustment, a logic tweak. Use AI-assisted coding tools like Cursor, Claude Code, or Copilot to make these changes directly in the code without touching the broader architecture.

#### New Feature / Structural Change

When a change affects the architecture of the app, such as adding a new service, reworking the data model, or introducing a new user flow, go back through the generation tool rather than patching the code manually. This keeps the codebase consistent and reduces technical debt.

## Learn by the need

#### HTML / CSS / JavaScript

These are the three foundational technologies of every web app. HTML defines the structure of a page, CSS controls how it looks, and JavaScript makes it interactive. You will encounter them when refining the front end of any generated application.

- `@roadmap` [Visit the Dedicated Frontend Roadmap](https://roadmap.sh/frontend)
- `@roadmap` [Visit the Dedicated HTML Roadmap](https://roadmap.sh/html)
- `@roadmap` [Visit the Dedicated CSS Roadmap](https://roadmap.sh/css)
- `@roadmap` [Visit the Dedicated JavaScript Roadmap](https://roadmap.sh/javascript)

#### React

React is the most widely used library for building web interfaces. Most AI-generated front ends use React by default. You will need a basic understanding of components, props, and state when making targeted changes to the UI layer of a generated app.

- `@roadmap` [Visit the Dedicated React Roadmap](https://roadmap.sh/react)
- `@official` [React Docs](https://react.dev/reference/react)
- `@video` [Full Stack React Developer Course](https://www.youtube.com/watch?v=Bvwq_S0n2pk)

#### Browsers / DevTools

Browser developer tools let you inspect HTML, debug JavaScript, monitor network requests, and measure performance directly in the browser. They are the first place to look when something in the front end is not working as expected.

- `@article` [How Browsers Work](https://www.ramotion.com/blog/what-is-web-browser/)
- `@article` [What are browser developer tools?](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Tools_and_setup/What_are_browser_developer_tools)
- `@video` [How Do Web Browsers Work?](https://www.youtube.com/watch?v=5rLFYtXHo9s)
- `@video` [nderstand Browser Dev Tools Network Tab (and avoid these mistakes...)](https://www.youtube.com/watch?v=2CC0fugc_2o)

#### Node.js

Node.js is the runtime that allows JavaScript to run on a server. Most AI-generated back ends use Node.js. You will need a basic understanding of it when modifying API routes, adding middleware, or debugging server-side logic.

- `@roadmap` [Visit the Dedicated Node.js Roadmap](https://roadmap.sh/nodejs)
- `@official` [Node.jsLearn Node.js Official WebsiteDocs](https://nodejs.org/en/learn/getting-started/introduction-to-nodejs)
- `@video` [Node.js and Express.js Full Course](https://www.youtube.com/watch?v=Oe421EPjeBE)

## Change Management & CI

#### User Testing

User testing means putting the app in front of real people and watching how they use it. You are not looking for opinions; you are looking for moments where they hesitate, get confused, or do something unexpected. Each session gives you concrete input for the next refinement cycle.

- `@article` [What is User Testing? Definition, Types & Methods](https://trymata.com/blog/what-is-user-testing/)

#### Unit Testing

A unit test checks that a single function or component behaves as expected in isolation. AI-generated codebases sometimes include unit tests automatically; if they do not, write them for the parts of the code that handle critical business logic. They are the fastest type of test to run and the easiest to debug when they fail.

- `@article` [What is Unit Testing?](https://www.guru99.com/unit-testing-guide.html)
- `@video` [What is Unit Testing?](https://youtu.be/x95ez7_V7rA?si=JhCVhcEN7zZOkxdp)

#### Integration Testing

Integration tests check that different parts of the app work correctly together; for example, that a form submission reaches the database and returns the right response. They catch problems that unit tests miss because they test the connections between components, not the components themselves.

- `@article` [Integration Testing](https://www.guru99.com/integration-testing.html)
- `@article` [Unit Test vs Integration Test: What's the Difference?](https://www.testim.io/blog/unit-test-vs-integration-test/)
- `@video` [What is Integration Testing?](https://www.youtube.com/watch?v=kRD6PA6uxiY)

#### E2E Testing

End-to-end tests simulate a real user moving through the app from start to finish. They verify that the full system works as expected in an environment that resembles production. Tools like Playwright or Cypress automate these flows so you can run them on every deployment without manual effort.

- `@article` [End to End Testing](https://microsoft.github.io/code-with-engineering-playbook/automated-testing/e2e-testing/)
- `@article` [End to End Testing: Importance, Process, Best Practices & Frameworks](https://testgrid.io/blog/end-to-end-testing-a-detailed-guide/)

#### GitHub

GitHub is the most widely used platform for hosting and managing code. It tracks every change to the codebase, makes it easy to collaborate with others, and integrates with most CI/CD tools. Setting up a GitHub repository should be one of the first things you do after generating the codebase.

- `@roadmap` [Visit Dedicated Git & GitHub Roadmap](https://roadmap.sh/git-github)
- `@official` [GitHub Docs](https://docs.github.com/en/get-started/quickstart)
- `@video` [What is GitHub?](https://www.youtube.com/watch?v=w3jLJU7DT5E)

#### GitLab

GitLab is an alternative to GitHub that combines version control with built-in CI/CD pipelines and project management tools. It is a good option if you want everything in one platform or if your organization already uses it.

- `@official` [https://about.gitlab.com/get-started/ Documentation](https://docs.gitlab.com/)
- `@official` [Get Started with Gitlab](https://about.gitlab.com/get-started/)
- `@video` [GitLab Explained: What is GitLab and Why Use It?](https://www.youtube.com/watch?v=bnF7f1zGpo4)

#### Bit Cloud

Bit Cloud is how humans and AI agents build software autonomously. It enables them to build and maintain software as independent, decoupled building blocks—each owned separately, yet composable into larger systems—so everyone can work in parallel without friction.

- `@official` [Get started with Hope](https://bit.cloud/docs?c=rsh-a)
- `@official` [Get started with your agent](https://bit.cloud/docs/install-bit/?c=rsh-a)

#### Azure DevOps

Azure DevOps is Microsoft's platform for managing code, pipelines, and project tasks. It integrates tightly with Azure infrastructure and is a common choice in enterprise environments. It covers version control, CI/CD, and issue tracking in a single platform.

- `@official` [Azure DevOps](https://azure.microsoft.com/en-us/products/devops)
- `@video` [Azure DevOps Tutorial for Beginners | CI/CD with Azure Pipelines](https://www.youtube.com/watch?v=4BibQ69MD8c)

## Testing & Feedback

### 4. Collaboration

At this stage, you bring other people into the process: teammates, testers, or early users. Their feedback drives the next round of refinement. This node also covers the tools and practices that keep the codebase stable when multiple people are working on it at the same time.

## Cloud Providers

#### Cloudflare

Cloudflare offers serverless deployment for front-end apps and lightweight back-end functions through Cloudflare Workers and Pages. It has a generous free tier and deploys to a global edge network, which means fast load times for users anywhere in the world.

- `@roadmap` [Visit the Dedicated Cloudflare Roadmap](https://roadmap.sh/cloudflare)
- `@official` [Getting started with Cloudflare](https://developers.cloudflare.com/pages/get-started/)
- `@video` [What is Cloudflare?](https://www.youtube.com/watch?v=XHvmX3FhTwU)
- `@video` [IntroLearn Cloudflare Workers 101 - Full Course for Beginnersduction to Cloudflare](https://www.youtube.com/watch?v=24cml1rKGBs)

#### Vercel

Vercel is a platform designed for deploying and hosting web applications, particularly those built with modern frontend frameworks and static site generators. It provides features like automatic deployments from Git repositories, serverless functions, and a global content delivery network (CDN) to ensure fast and reliable performance. Vercel simplifies the process of taking a frontend project from development to production.

- `@official` [Vercel Documentation](https://vercel.com/docs)
- `@official` [Vercel Quick Start](https://vercel.com/docs/getting-started-with-vercel)
- `@video` [Vercel Tutorial - Host a Website for Free](https://www.youtube.com/watch?v=Vx5nPGdsFaU)

#### Bit Cloud

#### DigitalOcean

DigitalOcean is a cloud provider focused on simplicity and developer experience. Its App Platform lets you deploy a full-stack application from a GitHub repository with minimal configuration. It is a practical middle ground between the simplicity of serverless platforms and the complexity of AWS or GCP.

- `@official` [DigitalOcean](https://www.digitalocean.com/)
- `@official` [DigitalOcean Tutorials](https://www.digitalocean.com/community/tutorials)
- `@video` [Getting Started With Kubernetes on DigitalOcean](https://www.youtube.com/watch?v=cJKdo-glRD0)

#### Railway

Railway is a deployment platform designed for speed and simplicity. It detects the type of project automatically and configures the deployment environment accordingly. It supports databases, back-end services, and front-end apps in the same project, which makes it convenient for full-stack deployments.

- `@official` [Railway](https://railway.com/)
- `@official` [Quick Start Tutorial](https://docs.railway.com/quick-start)
- `@video` [Fastest Way to Deploy a Full Stack Web App (Railway)](https://www.youtube.com/watch?v=JQIKobOcQ9k)

#### Render

Render is a cloud platform that supports web services, background workers, cron jobs, and static sites. It is straightforward to configure and deploy directly from a GitHub repository. It is a good option for full-stack apps that need a persistent server without the overhead of managing infrastructure manually.

- `@official` [Render Docs + Quickstarts](https://render.com/docs)
- `@article` [Render: Cloud Deployment with Less Engineering](https://thenewstack.io/render-cloud-deployment-with-less-engineering/)
- `@video` [Deploy any application with one click using Render | Cloud Application Platform](https://www.youtube.com/watch?v=yWxBUcG_C7g)

#### AWS

AWS is the largest cloud provider in the world. It offers infrastructure for computing, storage, databases, networking, and dozens of other services. It requires more configuration than PaaS options but gives you complete control over how your application runs and scales.

- `@roadmap` [Visit the Dedicated AWS Roadmap](https://roadmap.sh/aws)
- `@official` [AWS Cloud Essentials](https://aws.amazon.com/getting-started/cloud-essentials/)
- `@official` [Overview of Amazon Web Services](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/introduction.html)

#### Azure

Azure is Microsoft's cloud platform. It is a strong choice for teams already using Microsoft tools or working in enterprise environments. It covers the full range of infrastructure needs and integrates well with GitHub, Active Directory, and other Microsoft services.

- `@official` [Azure Website](https://azure.microsoft.com/en-us/)
- `@opensource` [Microsoft Azure Guide](https://github.com/mikeroyal/Azure-Guide)
- `@video` [icrosoft Azure Fundamentals Certification Course (AZ-900)](https://www.youtube.com/watch?v=5abffC-K40c)

#### GCP

Google Cloud Platform is Google's cloud infrastructure service. It is particularly strong for data processing, machine learning workloads, and applications that need to integrate with other Google services. It is a competitive alternative to AWS for teams comfortable with Google's ecosystem.

- `@official` [Google Cloud Platform](https://cloud.google.com)
- `@official` [Cloud Computing, Hosting Services, and APIs](https://cloud.google.com/gcp)
- `@video` [Google Cloud Platform Video Course](https://www.youtube.com/watch?v=fZOz13joN0o)

#### MongoDB / Atlas

MongoDB is a document-based database that stores data in a flexible, JSON-like format. Atlas is MongoDB's managed cloud service, which handles backups, scaling, and monitoring automatically. It is a good fit for apps where the data structure is likely to change as the product evolves.

- `@roadmap` [Visit Dedicated MongoDB Roadmap](https://roadmap.sh/mongodb)
- `@official` [MongoDB Website](https://www.mongodb.com/)
- `@official` [Learning Path for MongoDB Developers](https://learn.mongodb.com/catalog)
- `@official` [Vector Search in MongoDB Atlas](https://www.mongodb.com/products/platform/atlas-vector-search)

#### PostgreSQL / MySQL

PostgreSQL and MySQL are relational databases that store data in structured tables with defined relationships. They are the most widely used databases for web applications and are well supported by every major cloud provider. Use them when your data has a clear, stable structure and relationships between entities matter.

- `@roadmap` [Visit Dedicated PostgreSQL DBA Roadmap](https://roadmap.sh/postgresql-dba)
- `@official` [PostgreSQL Docs](https://www.postgresql.org/docs/)
- `@official` [MySQL Docs](https://dev.mysql.com/doc/)
- `@article` [Learn PostgreSQL - Full Tutorial for Beginners](https://www.postgresqltutorial.com/)
- `@article` [MySQL Tutorial](https://www.mysqltutorial.org/)

#### Supabase

Supabase is an open-source alternative to Firebase built on top of PostgreSQL. It provides a managed database, built-in authentication, real-time subscriptions, and an auto-generated API. It is one of the fastest ways to add a back end to a generated front-end application.

- `@official` [Supabase Docs](https://supabase.com/docs)
- `@video` [Supabase Full Course 2025 | Become a Supabase Pro in 1.5 Hours](https://www.youtube.com/watch?v=kyphLGnSz6Q)

## Platform as a Service (PaaS)

### 5. Deployment

Deployment is the process of making your app available to real users. The right deployment option depends on your technical experience, expected traffic, and budget. Start with the simplest option that meets your needs and scale up as the product grows.

- `@article` [What is software deployment?](https://www.atlassian.com/agile/software-development/software-deployment)
