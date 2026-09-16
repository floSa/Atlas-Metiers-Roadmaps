# MLOps Roadmap — plan extrait

- **Slug** : `mlops`
- **Description amont** : Step by step guide to learn MLOps in @currentYear@
- **Derniere modification amont** : 2026-01-24T13:19:27.128Z
- **Capture** : 2026-09-16
- **Volume** : 62 noeuds de contenu, 62 documentes, 275 ressources
- **Renvois vers d'autres roadmaps** : `https://roadmap.sh`, `https://roadmap.sh/devops`, `https://roadmap.sh/machine-learning`, `https://roadmap.sh/python`, `https://www.linkedin.com/in/maria-vechtomova/`

---

## MLOps

### What is MLOps?

 
MLOps is a set of practices that combines machine learning, DevOps, and data engineering to deploy and maintain ML models in production reliably. It covers the full lifecycle of a model, from training and testing to deployment, monitoring, and retraining. The goal is to make ML systems repeatable, scalable, and easier to manage over time, similar to how DevOps standardized software delivery.

- `@article` [What is MLOps?](https://aws.amazon.com/what-is/mlops/)
- `@article` [Machine Learning Operations (MLOps) For Beginners](https://towardsdatascience.com/machine-learning-operations-mlops-for-beginners-a5686bfe02b2/?utm_source=roadmap&utm_medium=Referral&utm_campaign=TDS+roadmap+integration)
- `@article` [MLOps: What It Is, Why It Matters, and How to Implement It](https://web.archive.org/web/20251126053103/https://neptune.ai/blog/mlops)
- `@video` [What is MLOps?](https://www.youtube.com/watch?v=OejCJL2EC3k)

#### Python

Python is a widely used programming language known for its clear syntax and extensive libraries. It's a versatile tool that can handle many tasks, from simple scripting to complex software development. Its ease of use and the availability of specialized libraries for data analysis, machine learning, and automation make it a popular choice for building and deploying machine learning systems.

- `@roadmap` [Visit Dedicated Python Roadmap](https://roadmap.sh/python)
- `@official` [Python](https://www.python.org/)
- `@article` [Real Python](https://realpython.com/)
- `@article` [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)

### Programming Fundamentals

 
Programming fundamentals are the basic concepts needed to write and understand code, such as variables, loops, functions, and data structures. These concepts apply across languages and form the base for writing scripts, building pipelines, and automating tasks. Without them, working with any ML or data tool becomes much harder.

#### SQL

SQL, or Structured Query Language, is a standard language for managing and manipulating data held in relational database management systems (RDBMS). It allows users to define, access, and control data, enabling operations like creating databases, inserting, updating, deleting, and retrieving data based on specific criteria. SQL provides a structured way to interact with databases, ensuring data integrity and consistency.

- `@course` [Premium SQL Course - Roadmap](https://roadmap.sh/courses/sql)
- `@official` [Visit the Dedicated SQL Roadmap](https://roadmap.sh/sql)
- `@article` [SQL Tutorial](https://www.w3schools.com/sql/)
- `@article` [How I Learned SQL In 2 Weeks (From Scratch)](https://towardsdatascience.com/how-i-learned-sql-in-2-weeks-from-scratch-b78040f4e2c1/)
- `@video` [Full SQL Crash Course - Learn SQL in 90 Minutes](https://www.youtube.com/watch?v=7cIG41gjHB4)

#### DVC

DVC (Data Version Control) is an open-source tool designed to bring version control principles to machine learning projects, specifically for data and models. It extends Git's capabilities to handle large files, datasets, and machine learning models, which are typically not well-suited for traditional version control systems. DVC tracks changes to data and models, allowing you to reproduce experiments, revert to previous versions, and collaborate effectively on data-driven projects.

- `@official` [DVC](https://dvc.org/)
- `@official` [Get Started with DVC](https://doc.dvc.org/start)
- `@article` [The Complete Guide to Data Version Control With DVC](https://www.datacamp.com/tutorial/data-version-control-dvc)
- `@article` [Data and Machine Learning Model Versioning with DVC](https://towardsdatascience.com/data-and-machine-learning-model-versioning-with-dvc-34fdadd06b15/)
- `@video` [Versioning Data with DVC (Hands-On Tutorial!)](https://www.youtube.com/watch?v=kLKBcPonMYw)

### Version Control Systems

Version control systems are tools that track changes to files over time. They allow multiple people to work on the same project simultaneously without overwriting each other's work. These systems record a history of modifications, enabling users to revert to previous versions, compare changes, and understand who made specific alterations and when.

- `@roadmap` [Visit Dedicated Git & GitHub Roadmap](https://roadmap.sh/git-github)
- `@official` [Git Documentation](https://git-scm.com/docs)
- `@article` [Learn Git by Atlassian](https://www.atlassian.com/git)
- `@video` [hat is a Version Control System and why you should always use it](https://www.youtube.com/watch?v=IeXhYROClZk)

### CI/CD

CI/CD, which stands for Continuous Integration and Continuous Delivery/Deployment, is a software development practice focused on automating and streamlining the process of building, testing, and releasing software changes. Continuous Integration involves frequently merging code changes into a central repository, followed by automated builds and tests. Continuous Delivery/Deployment then automates the release of these changes to various environments, ultimately aiming for faster and more reliable software releases.

- `@official` [What is CI/CD?](https://about.gitlab.com/topics/ci-cd/)
- `@article` [A Primer: Continuous Integration and Continuous Delivery (CI/CD)](https://thenewstack.io/a-primer-continuous-integration-and-continuous-delivery-ci-cd/)
- `@article` [DevOps CI/CD Explained in 100 Seconds](https://thenewstack.io/category/ci-cd/)
- `@video` [Automate your Workflows with GitHub Actions](https://www.youtube.com/watch?v=scEDHsr3APg)
- `@feed` [Articles about CI/CD](https://app.daily.dev/tags/version-control?ref=roadmapsh)

#### GItLab

GitLab is a web-based DevOps platform that provides a single application for all stages of the software development lifecycle. It offers features like source code management (using Git), CI/CD pipelines, issue tracking, and project management. GitLab allows teams to collaborate on code, automate build, test, and deployment processes, and manage projects from planning to monitoring.

- `@official` [GitLab Website](https://gitlab.com/)
- `@official` [GitLab Docs](https://docs.gitlab.com/)
- `@article` [Read articles about Gitlab](https://towardsdatascience.com/tag/gitlab/)
- `@video` [GitLab Explained: What is GitLab and Why Use It?](https://www.youtube.com/watch?v=bnF7f1zGpo4)

#### Jenkins

Jenkins is an open-source automation server that helps automate the software development processes, including building, testing, and deploying code. It provides a platform for continuous integration and continuous delivery (CI/CD), allowing teams to automate repetitive tasks and streamline their workflows. Jenkins uses plugins to support various tools and technologies, making it highly customizable and adaptable to different project requirements.

- `@official` [Jenkins Website](https://www.jenkins.io/)
- `@official` [Jenkins Getting Started Guide](https://www.jenkins.io/doc/pipeline/tour/getting-started/)
- `@article` [Jenkins Tutorial](https://octopus.com/devops/jenkins/jenkins-tutorial/?utm_source=roadmap&utm_medium=link&utm_campaign=devops-ci-cd-gitlab-ci)
- `@article` [From DevOps to MLOPS: Integrate Machine Learning Models using Jenkins and Docker](https://towardsdatascience.com/from-devops-to-mlops-integrate-machine-learning-models-using-jenkins-and-docker-79034dbedf1/?utm_source=roadmap&utm_medium=Referral&utm_campaign=TDS+roadmap+integration)
- `@video` [Learn Jenkins! Complete Jenkins Course - Zero to Hero](https://www.youtube.com/watch?v=6YZvp2GwT0A)

### Cloud Computing

 
Cloud computing provides on-demand access to computing resources, such as servers, storage, and databases, over the internet instead of running everything on local hardware. It lets teams scale up resources for training large models or handling more traffic, then scale back down when not needed. Providers like AWS, Azure, and GCP offer these services on a pay-as-you-go basis.

- `@article` [Cloud Computing - IBM](https://www.ibm.com/think/topics/cloud-computing)
- `@article` [What is Cloud Computing? - Azure](https://azure.microsoft.com/en-gb/resources/cloud-computing-dictionary/what-is-cloud-computing)
- `@video` [What is Cloud Computing? - Amazon Web Services](https://www.youtube.com/watch?v=mxT233EdY5c)

#### GitHub Actions

GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform that allows you to automate your software development workflows directly in your GitHub repository. You can use it to build, test, and deploy your code, as well as automate other tasks like managing issues and pull requests. Workflows are defined in YAML files and triggered by events in your repository, such as pushes, pull requests, or scheduled times.

- `@official` [GitHub Actions Documentation](https://docs.github.com/en/actions)
- `@article` [GitHub Actions Guide](https://octopus.com/devops/github-actions/?utm_source=roadmap&utm_medium=link&utm_campaign=devops-ci-cd-github-actions)
- `@video` [What is GitHub Actions?](https://www.youtube.com/watch?v=URmeTqglS58)
- `@video` [Automate your Workflow with GitHub Actions](https://www.youtube.com/watch?v=nyKZTKQS_EQ)

#### CML

Continuous Machine Learning (CML) is a tool designed to bring continuous integration and continuous delivery (CI/CD) principles to machine learning projects. It allows data scientists and machine learning engineers to automate the process of training, evaluating, and deploying machine learning models. CML integrates with existing CI/CD systems to provide feedback on model performance and data quality with each code change.

- `@official` [CML](https://cml.dev/)
- `@official` [Get Started with CML](https://cml.dev/doc/start)
- `@article` [Continuous Machine Learning](https://towardsdatascience.com/continuous-machine-learning-e1ffb847b8da/?utm_source=roadmap&utm_medium=Referral&utm_campaign=TDS+roadmap+integration)

#### Docker

Docker is a platform that uses operating system-level virtualization to deliver software in packages called containers. These containers isolate software from its environment and ensure that it works uniformly despite differences between development and production environments. Docker simplifies the process of building, shipping, and running applications by packaging all dependencies, libraries, and configurations into a single unit.

- `@roadmap` [Visit Dedicated Docker Roadmap](https://roadmap.sh/docker)
- `@official` [Docker Documentation](https://docs.docker.com/)
- `@article` [A Data Scientist’s Guide to Docker Containers](https://towardsdatascience.com/a-data-scientists-guide-to-docker-containers/?utm_source=roadmap&utm_medium=Referral&utm_campaign=TDS+roadmap+integration)
- `@video` [Docker Tutorial](https://www.youtube.com/watch?v=RqTEHSBrYFw)
- `@video` [Docker Simplified in 55 Seconds](https://youtu.be/vP_4DlOH1G4)
- `@feed` [Explore top posts about Docker](https://app.daily.dev/tags/docker?ref=roadmapsh)

### Containerization

Containerization is a form of operating system virtualization that packages an application and its dependencies into a single, isolated unit called a container. This container includes everything the application needs to run, such as code, runtime, system tools, libraries, and settings. Containers offer a consistent and portable environment for applications, ensuring they run the same way regardless of where they are deployed.

- `@article` [What are Containers? - Google Cloud](https://cloud.google.com/learn/what-are-containers)
- `@article` [What is a Container? - Docker](https://www.docker.com/resources/what-container/)
- `@article` [Articles about Containers - The New Stack](https://thenewstack.io/category/containers/)
- `@video` [What are Containers?](https://www.youtube.com/playlist?list=PLawsLZMfND4nz-WDBZIj8-nbzGFD4S9oz)
- `@feed` [Explore top posts about Containers](https://app.daily.dev/tags/containers?ref=roadmapsh)

#### Kubernetes

Kubernetes is an open-source system for automating the deployment, scaling, and management of containerized applications. It groups containers that make up an application into logical units for easy management and discovery. By orchestrating containers across multiple machines, Kubernetes ensures high availability and efficient resource utilization, making it a powerful tool for managing complex deployments.

- `@roadmap` [Visit Dedicated Kubernetes Roadmap](https://roadmap.sh/kubernetes)
- `@official` [Kubernetes](https://kubernetes.io/)
- `@official` [Kubernetes Documentation](https://kubernetes.io/docs/home/)
- `@article` [Kubernetes: An Overview](https://thenewstack.io/kubernetes-an-overview/)
- `@video` [Kubernetes Crash Course for Absolute Beginners](https://www.youtube.com/watch?v=s_o8dwzRlu4)
- `@feed` [Explore top posts about Kubernetes](https://app.daily.dev/tags/kubernetes?ref=roadmapsh)

### Machine Learning Fundamentals

 
Machine learning fundamentals cover the core ideas needed to build predictive models, including how algorithms learn patterns from data and make predictions on new data. This includes concepts like training, testing, overfitting, and evaluation. A solid grasp of these fundamentals makes it easier to pick the right approach for a given problem.

- `@roadmap` [Visit the Dedicated Machine Learning Roadmap](https://roadmap.sh/machine-learning)
- `@course` [Fundamentals of Machine Learning - Microsoft](https://learn.microsoft.com/en-us/training/modules/fundamentals-machine-learning/)
- `@course` [MLCourse.ai](https://mlcourse.ai/)
- `@course` [Fast.ai](https://course.fast.ai)
- `@article` [Everything I Studied to Become a Machine Learning Engineer (No CS Background)](https://towardsdatascience.com/everything-i-studied-to-become-a-machine-learning-engineer-no-cs-background/?utm_source=roadmap&utm_medium=Referral&utm_campaign=TDS+roadmap+integration)

#### Spark

 
Spark, or Apache Spark, is an open-source engine for processing large amounts of data across many machines at once. It supports batch and streaming data processing, along with built-in libraries for SQL queries and machine learning. Its ability to handle data that does not fit on a single machine makes it a common tool in large-scale data pipelines.

- `@official` [ApacheSpark](https://spark.apache.org/documentation.html)
- `@article` [Spark By Examples](https://sparkbyexamples.com)
- `@article` [First Steps in Machine Learning with Apache Spark](https://towardsdatascience.com/first-steps-in-machine-learning-with-apache-spark-672fe31799a3/?utm_source=roadmap&utm_medium=Referral&utm_campaign=TDS+roadmap+integration)
- `@article` [Complete Guide to Spark and PySpark Setup for Data Science](https://towardsdatascience.com/complete-guide-to-spark-and-pyspark-setup-for-data-science-374ecd8d1eea/?utm_source=roadmap&utm_medium=Referral&utm_campaign=TDS+roadmap+integration)
- `@video` [Apache Spark Architecture - EXPLAINED!](https://www.youtube.com/watch?v=iXVIPQEGZ9Y)

#### Terraform

Terraform is an open-source infrastructure as code (IaC) tool that allows you to define and provision infrastructure using a declarative configuration language. It enables you to manage infrastructure resources across various cloud providers and on-premises environments in a consistent and automated manner. Terraform uses a state file to track the current configuration of your infrastructure, allowing you to plan and apply changes safely and predictably.

- `@roadmap` [Visit the Dedicated Terraform Roadmap](https://roadmap.sh/terraform)
- `@official` [Terraform](https://developer.hashicorp.com/terraform)
- `@article` [What is Terraform?](https://www.ibm.com/think/topics/terraform)
- `@article` [Automatically Managing Data Pipeline Infrastructures With Terraform](https://towardsdatascience.com/automatically-managing-data-pipeline-infrastructures-with-terraform-323fd1808a47/?utm_source=roadmap&utm_medium=Referral&utm_campaign=TDS+roadmap+integration)
- `@video` [Terraform Course - Automate your AWS cloud infrastructure](https://www.youtube.com/watch?v=SLB_c_ayRMo)

#### Ansible

Ansible is an open-source automation tool used to configure systems, deploy software, and orchestrate more advanced IT tasks. It uses a simple, human-readable language (YAML) to define automation tasks, called playbooks. Ansible works by connecting to nodes (servers, virtual machines, etc.) and pushing out small programs called "Ansible modules" to them. These modules are then executed on the nodes, and the modules are removed when finished.

- `@official` [Ansible Website](https://www.ansible.com/)
- `@article` [What is Ansible? A Tool to Automate Parts of Your Job](https://www.freecodecamp.org/news/what-is-ansible/)
- `@video` [Ansible in 100 Seconds](https://www.youtube.com/watch?v=xRMPKQweySE)
- `@video` [Ansible Full Course for Beginners](https://www.youtube.com/watch?v=9Ua2b06oAr4)
- `@video` [Ansible Full Course to Zero to Hero](https://www.youtube.com/watch?v=GROqwFFLl3s)

### Data Engineering Fundamentals

 
Data engineering fundamentals cover how data is collected, stored, and moved so it can be used for analysis or model training. This includes designing pipelines that pull data from various sources, clean it, and load it into a place where it can be accessed reliably. Good data engineering practices make sure ML models are trained on accurate and up-to-date data.

- `@roadmap` [Visit the Dedicated Data Engineer Roadmap](https://roadmap.sh/data-engineer)
- `@article` [Data Engineering 101](https://www.redpanda.com/guides/fundamentals-of-data-engineering)
- `@article` [How to Become a Data Engineer](https://towardsdatascience.com/how-to-become-a-data-engineer-c0319cb226c2/)
- `@video` [Fundamentals of Data Engineering](https://www.youtube.com/watch?v=mPSzL8Lurs0)

#### Kafka

Kafka is a distributed, fault-tolerant, high-throughput streaming platform. It's primarily used for building real-time data pipelines and streaming applications, allowing you to publish, subscribe to, store, and process streams of records. These streams can originate from various sources and be consumed by multiple applications simultaneously.

- `@official` [Apache Kafka Quickstart](https://kafka.apache.org/quickstart)
- `@article` [What is Apache Kafka?](https://aws.amazon.com/what-is/apache-kafka/)
- `@article` [End-to-End Data Engineering System on Real Data with Kafka, Spark, Airflow, Postgres, and Docker](https://towardsdatascience.com/end-to-end-data-engineering-system-on-real-data-with-kafka-spark-airflow-postgres-and-docker-a70e18df4090/?utm_source=roadmap&utm_medium=Referral&utm_campaign=TDS+roadmap+integration)
- `@video` [Apache Kafka Fundamentals](https://www.youtube.com/watch?v=B5j3uNBH8X4)
- `@feed` [Explore top posts about Kafka](https://app.daily.dev/tags/kafka?ref=roadmapsh)

#### MLOps Principles

 
MLOps principles are the core ideas that guide how teams build and operate ML systems. They include automation of the ML pipeline, reproducibility of experiments and results, continuous testing and monitoring, and collaboration between data scientists, engineers, and operations teams. Following these principles helps reduce manual work and makes it easier to catch problems before they reach production.

- `@article` [MLOps Principles](https://ml-ops.org/content/mlops-principles)

#### MLOps Components

 
MLOps components are the building blocks that together form a working ML pipeline. These usually include version control, CI/CD, orchestration, experiment tracking, data lineage, model training and serving, and monitoring. Each component handles a different part of the lifecycle, and combining them lets teams move a model from an idea to a stable production system.

- `@article` [MLOps Workflow, Components, and Key Practices](https://mlops.tv/p/understanding-ml-pipelines-through)
- `@article` [MLOps Lifecycle](https://www.moontechnolabs.com/blog/mlops-lifecycle/)

### Orchestration & Deployment

Orchestration and deployment involve automating the process of taking a trained machine learning model and making it available for use in a production environment. This includes managing the workflow of model building, testing, and releasing, as well as handling the infrastructure needed to serve the model and scale it to meet demand. It ensures that models are reliably and efficiently integrated into applications and systems.

- `@article` [What is orchestration?](https://www.redhat.com/en/topics/automation/what-is-orchestration)
- `@video` [What is Data Orchestration?](https://www.youtube.com/watch?v=iyw9puEmTrA)

#### KubeFlow

Kubeflow is an open-source machine learning platform designed to simplify the deployment and management of ML workflows on Kubernetes. It provides tools and components for building, training, and deploying machine learning models, allowing users to create portable and scalable ML pipelines. Kubeflow aims to make it easier for data scientists and engineers to leverage Kubernetes for their machine learning projects, handling tasks like resource management, model serving, and pipeline orchestration.

- `@official` [Kubeflow](https://www.kubeflow.org/)
- `@opensource` [kubeflow](https://github.com/kubeflow/kubeflow)
- `@article` [What is Kubeflow?](https://cloud.google.com/discover/what-is-kubeflow?hl=en)
- `@article` [Tutorial – Basic Kubeflow Pipeline From Scratch](https://towardsdatascience.com/tutorial-basic-kubeflow-pipeline-from-scratch-5f0350dc1905/?utm_source=roadmap&utm_medium=Referral&utm_campaign=TDS+roadmap+integration)
- `@video` [Kubeflow Explained for Beginners](https://www.youtube.com/watch?v=hvzEPlRdJ2Q)
- `@video` [Intro to Kubeflow Pipelines](https://www.youtube.com/watch?v=_AY8mmbR1o4&list=PLIivdWyY5sqLS4lN75RPDEyBgTro_YX7x)

### Infrastructure as Code

 
Infrastructure as Code, or IaC, means defining and managing computing infrastructure, such as servers and networks, using configuration files instead of manual setup. These files can be versioned, reviewed, and reused, which makes infrastructure changes more predictable and repeatable. It reduces the risk of manual errors when setting up environments for training or deploying models.

- `@article` [What is Infrastructure as Code?](https://www.redhat.com/en/topics/automation/what-is-infrastructure-as-code-iac)
- `@article` [Automatically Managing Data Pipeline Infrastructures With Terraform](https://towardsdatascience.com/automatically-managing-data-pipeline-infrastructures-with-terraform-323fd1808a47/?utm_source=roadmap&utm_medium=Referral&utm_campaign=TDS+roadmap+integration)
- `@video` [Terraform Course for Beginners](https://www.youtube.com/watch?v=SLB_c_ayRMo)
- `@video` [8 Terraform Best Practices](https://www.youtube.com/watch?v=gxPykhPxRW0)

#### Grafana

Grafana is an open-source data visualization and monitoring tool. It allows users to query, visualize, alert on, and explore metrics, logs, and traces. Grafana connects to various data sources, such as Prometheus, Graphite, Elasticsearch, and InfluxDB, to create customizable dashboards that display real-time data and historical trends.

- `@official` [Grafana](https://grafana.com/)
- `@official` [Grafana Docs](https://grafana.com/docs/)
- `@official` [Grafana Webinars and Videos](https://grafana.com/videos/)
- `@article` [What is Grafana?](https://www.redhat.com/en/topics/data-services/what-is-grafana)
- `@video` [Grafana Explained in Under 5 Minutes ⏲](https://www.youtube.com/watch?v=lILY8eSspEo)
- `@video` [Grafana for Beginners Ep. 1](https://www.youtube.com/watch?v=TQur9GJHIIQ&list=PLDGkOdUX1Ujo27m6qiTPPCpFHVfyKq9jT)

### Monitoring & Observability

Monitoring and observability involve tracking the performance and health of machine learning models and the infrastructure they rely on. This includes gathering metrics, logs, and traces to understand how models are behaving in production, identify potential issues like performance degradation or data drift, and gain insights into the overall system's operation. The goal is to ensure models are accurate, reliable, and deliver value as expected.

- `@article` [What’s the Difference Between Observability and Monitoring?](https://aws.amazon.com/compare/the-difference-between-monitoring-and-observability/)
- `@article` [Observability and Instrumentation: What They Are and Why They Matter](https://newrelic.com/blog/best-practices/observability-instrumentation)
- `@video` [What is observability?](https://www.youtube.com/watch?v=--17See0KHs)
- `@video` [Monitoring vs Observability](https://www.youtube.com/watch?v=b6yWa3V2iBQ)

#### Data Lineage

 
Data lineage is the record of where data comes from, how it moves, and how it gets transformed before reaching a model. It shows the full path from raw source to final training dataset. This helps teams trace errors back to their origin and understand the impact of a change made upstream.

- `@article` [What is Data Lineage?](https://www.ibm.com/topics/data-lineage)
- `@article` [What is a Feature Store](https://www.snowflake.com/guides/what-feature-store-machine-learning/)

#### Model Training & Serving

 
Model training is the process of teaching a machine learning model to make predictions using data, while serving is making that trained model available to handle real requests. Serving usually involves wrapping the model in an API so applications can send input and get predictions back. Together they cover the step where a model moves from a notebook experiment to something an application can actually use.

- `@opensource` [What is model training?](https://www.ibm.com/think/topics/model-training)
- `@article` [What Is AI Model Training & Why Is It Important?](https://www.oracle.com/uk/artificial-intelligence/ai-model-training/)
- `@article` [KServe Tutorial](https://towardsdatascience.com/kserve-highly-scalable-machine-learning-deployment-with-kubernetes-aa7af0b71202/?utm_source=roadmap&utm_medium=Referral&utm_campaign=TDS+roadmap+integration)
- `@video` [Five Steps to Create a New AI Model](https://www.youtube.com/watch?v=jcgaNrC4ElU&t=172s)

#### TFLite

TFLite is a lightweight version of TensorFlow, designed for running machine learning models on mobile, embedded, and IoT devices. It enables on-device inference, meaning models can be executed directly on the device without needing a network connection or relying on cloud-based processing. This reduces latency, improves privacy, and allows for offline functionality.

- `@official` [TensorFlow Lite](https://www.tensorflow.org/lite/guide)
- `@article` [TensorFlow Lite Tutorial: How to Get Up and Running](https://www.influxdata.com/blog/tensorflow-lite-tutorial-how-to-get-up-and-running/)
- `@video` [TensorFlow Lite for Edge Devices - Tutorial](https://www.youtube.com/watch?v=OJnaBhCixng)
- `@video` [TensorFlow Lite in Android with Google Play services](https://www.youtube.com/watch?v=SEeEsbWZog8&list=PLQY2H8rRoyvwhLghMaygIJS0_f_blnUlJ)

#### SHAP

SHAP (SHapley Additive exPlanations) is a method used to explain the output of any machine learning model. It uses concepts from game theory to assign each feature a value representing its contribution to the prediction. These values, known as SHAP values, indicate the degree to which each feature contributed to the model's output for a specific instance, facilitating a deeper understanding of the model's decision-making process.

- `@official` [Welcome to the SHAP documentation](https://shap.readthedocs.io/en/latest/)
- `@opensource` [shap](https://github.com/shap/shap)
- `@article` [Explainable AI - Understanding and Trusting Machine Learning Models](https://www.datacamp.com/tutorial/explainable-ai-understanding-and-trusting-machine-learning-models)
- `@article` [When Shapley Values Break: A Guide to Robust Model Explainability](https://towardsdatascience.com/when-shapley-values-break-a-guide-to-robust-model-explainability/?utm_source=roadmap&utm_medium=Referral&utm_campaign=TDS+roadmap+integration)
- `@video` [SHAP values for beginners | What they mean and their applications](https://www.youtube.com/watch?v=MQ6fFDwjuco)

#### Monitoring & Observability

 
Monitoring and observability track how a system behaves once it is running, using metrics, logs, and alerts. For ML systems, this also means watching model accuracy over time, since predictions can degrade as real-world data shifts away from the training data. Catching this early lets teams retrain or fix a model before it causes bigger problems.

- `@article` [ML Monitoring vs ML Observability](https://medium.com/marvelous-mlops/ml-monitoring-vs-ml-observability-understanding-the-differences-fff574a8974f)
- `@article` [Building a Robust Data Observability Framework to Ensure Data Quality and Integrity](https://towardsdatascience.com/building-a-robust-data-observability-framework-to-ensure-data-quality-and-integrity-07ff6cffdf69/?utm_source=roadmap&utm_medium=Referral&utm_campaign=TDS+roadmap+integration)
- `@video` [ML Observability vs ML Monitoring: What's the difference?](https://www.youtube.com/watch?v=k1Reed3QIYE)

#### PyTorch Mobile

PyTorch Mobile is a framework that allows you to run PyTorch models directly on mobile devices, like smartphones and tablets. It enables on-device machine learning inference, meaning the model computations happen locally without needing a network connection to a remote server. This offers benefits like reduced latency, increased privacy, and the ability to function offline.

- `@official` [Welcome to the ExecuTorch Documentation](https://docs.pytorch.org/executorch/stable/index.html)
- `@opensource` [executorch](https://github.com/pytorch/executorch)
- `@video` [ExecuTorch 1.0: General Availability Status for Mobile and Embedded...- Mergen Nachin & Cemal Bilgin](https://www.youtube.com/watch?v=toirKRTLgJA)
- `@video` [PyTorch Mobile and Android Neural Networks API | PyTorch Developer Day 2020](https://www.youtube.com/watch?v=B-2spa3UCTU)

#### Jetson

NVIDIA Jetson is a series of embedded computing systems designed for AI and robotics applications. These systems-on-modules (SoMs) provide high-performance processing capabilities in a compact, energy-efficient form factor, enabling developers to deploy AI models and perform complex computations directly on edge devices. Jetson platforms are commonly used in applications like autonomous vehicles, drones, smart cameras, and industrial automation, where real-time data processing and low latency are critical.

- `@official` [NVIDIA Jetson Modules](https://developer.nvidia.com/embedded/jetson-modules)
- `@article` [What Is NVIDIA Jetson? A Beginner’s Guide to Powerful Edge AI Modules](https://blog.aetherix.com/nvidia-jetson-beginners-guide/)
- `@video` [NVIDIA Jetson Orin Nano Super COMPLETE Setup Guide & Tutorial](https://www.youtube.com/watch?v=-PjMC0gyH9s)

### Edge AI

Edge AI refers to running machine learning models directly on devices, like smartphones, sensors, or embedded systems, rather than relying on a central server or cloud infrastructure. This approach brings computation and data processing closer to the source of data generation. This enables faster response times, reduced latency, enhanced privacy, and the ability to operate in environments with limited or no network connectivity.

- `@course` [What Is Edge Computing?](https://www.udemy.com/course/edge-computing/)
- `@article` [What Is Edge AI and How Does It Work?](https://blogs.nvidia.com/blog/what-is-edge-ai/)
- `@article` [What is Edge AI?](https://www.ibm.com/think/topics/edge-ai)
- `@article` [What is Edge Computing - Cloudflare Docs](https://www.cloudflare.com/learning/serverless/glossary/what-is-edge-computing/)
- `@article` [What is Edge Computing? Is It More Than a Buzzword?](https://www.howtogeek.com/devops/what-is-edge-computing-is-it-more-than-a-buzzword/)

### Explainable AI

Explainable AI (XAI) refers to methods and techniques used to make the decisions of machine learning models understandable to humans. It aims to shed light on how a model arrives at a particular prediction, identifying the factors that influenced the outcome. This allows users to understand, trust, and effectively manage AI systems.

- `@article` [What is Explainable AI (XAI)?](https://www.ibm.com/think/topics/explainable-ai)
- `@article` [Explainable AI (XAI) | Giskard](https://www.giskard.ai/glossary/explainable-ai-xai)
- `@article` [How to Leverage Explainable AI for Better Business Decisions](https://towardsdatascience.com/how-to-leverage-explainable-ai-for-better-business-decisions/?utm_source=roadmap&utm_medium=Referral&utm_campaign=TDS+roadmap+integration)
- `@video` [Explainable AI: Demystifying AI Agents Decision-Making](https://www.youtube.com/watch?v=yJkCuEu3K68)

#### Go

 
Go, also called Golang, is a programming language known for its simplicity, speed, and strong support for concurrent programs. Many infrastructure and DevOps tools, such as Docker and Kubernetes, are written in Go. Learning it helps when building lightweight services or contributing to tools in the cloud-native ecosystem.

- `@roadmap` [Visit Dedicated Go Roadmap](https://roadmap.sh/golang)
- `@official` [A Tour of Go – Go Basics](https://go.dev/tour/welcome/1)
- `@official` [Go Reference Documentation](https://go.dev/doc/)
- `@article` [Making a RESTful JSON API in Go](https://thenewstack.io/make-a-restful-json-api-go/)
- `@article` [Go, the Programming Language of the Cloud](https://thenewstack.io/go-the-programming-language-of-the-cloud/)
- `@video` [Go Programming Course](https://www.youtube.com/watch?v=un6ZyFkqFKo)

#### Bash

Bash (Bourne Again Shell) is a Unix shell and command language used for interacting with the operating system through a terminal. It allows users to execute commands, automate tasks via scripting, and manage system operations. As the default shell for many Linux distributions, it supports command-line utilities, file manipulation, process control, and text processing. Bash scripts can include loops, conditionals, and functions, making it a powerful tool for system administration, automation, and task scheduling.

- `@roadmap` [Visit the Dedicated Shell-Bash Roadmap](https://roadmap.sh/shell-bash)
- `@opensource` [bash-guide](https://github.com/Idnan/bash-guide)
- `@article` [Bash Reference Manual](https://www.gnu.org/software/bash/manual/bashref.html)
- `@video` [Bash Scripting Course](https://www.youtube.com/watch?v=tK9Oc6AEnR4)

#### Git

 
Git is a distributed version control system that tracks changes to files and lets multiple people collaborate on the same codebase. It works by creating commits, which are snapshots of the project at a point in time, and branches, which let people work on separate features in parallel. Almost every modern software and ML project uses Git to manage its code.

- `@roadmap` [Visit Dedicated Git & GitHub Roadmap](https://roadmap.sh/git-github)
- `@article` [Learn Git with Tutorials, News and Tips - Atlassian](https://www.atlassian.com/git)
- `@article` [Getting Started with Git and GitHub: A Complete Tutorial for Beginner](https://towardsdatascience.com/learn-basic-git-commands-for-your-data-science-works-2a75396d530d/?utm_source=roadmap&utm_medium=Referral&utm_campaign=TDS+roadmap+integration)
- `@article` [Git Cheat Sheet](https://cs.fyi/guide/git-cheatsheet)
- `@video` [Git & GitHub Crash Course For Beginners](https://www.youtube.com/watch?v=SWYqp7iY_Tc)
- `@feed` [Explore top posts about Git](https://app.daily.dev/tags/git?ref=roadmapsh)

#### GitHub

 
GitHub is a web platform for hosting Git repositories, adding features like pull requests, issue tracking, and code review on top of Git. Teams use it to collaborate on code, review changes before merging, and automate workflows with GitHub Actions. It has become one of the most common places to store and share code publicly or privately.

- `@roadmap` [Visit Dedicated Git & GitHub Roadmap](https://roadmap.sh/git-github)
- `@official` [GitHub](https://github.com)
- `@official` [GitHub Documentation](https://docs.github.com/en/get-started/quickstart)
- `@article` [Comprehensive Guide to GitHub for Data Scientists](https://towardsdatascience.com/comprehensive-guide-to-github-for-data-scientist-d3f71bd320da/?utm_source=roadmap&utm_medium=Referral&utm_campaign=TDS+roadmap+integration)
- `@video` [What is GitHub?](https://www.youtube.com/watch?v=w3jLJU7DT5E)
- `@feed` [Explore top posts about GitHub](https://app.daily.dev/tags/github?ref=roadmapsh)

#### AWS / Azure / GCP

 
AWS, Azure, and GCP are the three largest cloud computing providers, each offering a wide range of services for computing, storage, networking, and machine learning. They differ in pricing, tooling, and specific service names, but cover similar core capabilities. Most companies choose one as their primary provider based on cost, existing infrastructure, or team familiarity.

- `@roadmap` [Visit Dedicated AWS Roadmap](https://roadmap.sh/aws)
- `@official` [Microsoft Azure](https://docs.microsoft.com/en-us/learn/azure/)
- `@official` [Google Cloud Platform](https://cloud.google.com/)
- `@official` [GCP Learning Resources](https://cloud.google.com/training)
- `@feed` [Explore top posts about AWS](https://app.daily.dev/tags/aws?ref=roadmapsh)

#### Cloud-native ML Services

Cloud-native ML services are pre-built machine learning tools and platforms offered by cloud providers. These services allow users to build, train, and deploy machine learning models without managing the underlying infrastructure. They often include features like automated model training, scalable deployment options, and integration with other cloud services.

- `@official` [AWS Sage Maker](https://aws.amazon.com/sagemaker/)
- `@official` [Azure ML](https://azure.microsoft.com/en-gb/products/machine-learning)
- `@official` [Vertex AI Platform](https://cloud.google.com/vertex-ai?hl=en)
- `@article` [What is cloud native?](https://cloud.google.com/learn/what-is-cloud-native?hl=en)
- `@article` [Azure ML vs. AWS SageMaker: A Deep Dive into Model Training — Part 1](https://towardsdatascience.com/azure-ml-vs-aws-sagemaker-a-deep-dive-into-scalable-model-training-part-1/?utm_source=roadmap&utm_medium=Referral&utm_campaign=TDS+roadmap+integration)
- `@article` [AWS vs. Azure: A Deep Dive into Model Training – Part 2](https://towardsdatascience.com/aws-vs-azure-a-deep-dive-into-model-training-part-2/?utm_source=roadmap&utm_medium=Referral&utm_campaign=TDS+roadmap+integration)
- `@video` [What is Cloud Native?](https://www.youtube.com/watch?v=fp9_ubiKqFU)

## Tools

#### Maths & Statistics

Mathematics and statistics provide the foundational principles for understanding and building machine learning models. These disciplines offer the tools to analyze data, quantify uncertainty, and optimize model performance. Key areas include linear algebra for data representation and manipulation, calculus for optimization algorithms, probability theory for handling uncertainty, and statistical inference for concluding data.

- `@book` [Introductory Statistics](https://assets.openstax.org/oscms-prodcms/media/documents/IntroductoryStatistics-OP_i6tAI7e.pdf)
- `@article` [Computer Science 70, 001 - Spring 2015 - Discrete Mathematics and Probability Theory](http://www.infocobuild.com/education/audio-video-courses/computer-science/cs70-spring2015-berkeley.html)
- `@article` [Discrete Mathematics By IIT Ropar NPTEL](https://nptel.ac.in/courses/106/106/106106183/)
- `@article` [Introduction to Statistics](https://imp.i384100.net/3eRv4v)
- `@article` [How to Learn the Math Needed for Data Science](https://towardsdatascience.com/how-to-learn-the-math-needed-for-data-science-86c6643b0c59/?utm_source=roadmap&utm_medium=Referral&utm_campaign=TDS+roadmap+integration)
- `@video` [Lec 1 | MIT 6.042J Mathematics for Computer Science, Fall 2010](https://www.youtube.com/watch?v=L3LMbpZIKhQ&list=PLB7540DEDD482705B)
- `@video` [Discrete Mathematics by Shai Simonson (19 videos)](https://www.youtube.com/playlist?list=PLWX710qNZo_sNlSWRMVIh6kfTjolNaZ8t)
- `@video` [tatistics - A Full University Course on Data Science Basics](https://www.youtube.com/watch?v=xxpc-HPKN28)

#### Machine Learning

 
Machine learning is a method of teaching computers to find patterns in data and make predictions or decisions without being explicitly programmed for the task. A model learns from examples during training, then applies what it learned to new, unseen data. It covers approaches like supervised, unsupervised, and reinforcement learning.

- `@roadmap` [Visit the Dedicated Machine Learning Roadmap](https://roadmap.sh/machine-learning)
- `@book` [Machine Learning: The Basics](https://alexjungaalto.github.io/MLBasicsBook.pdf)
- `@article` [What is Machine Learning (ML)?](https://www.ibm.com/topics/machine-learning)
- `@video` [What is Machine Learning?](https://www.youtube.com/watch?v=9gGnTQTYNaE)
- `@video` [Complete Machine Learning in One Video | Machine Learning Tutorial For Beginners 2025 | Simplilearn](https://www.youtube.com/watch?v=PtYRUoJRE9s)

#### Airflow

Airflow is a platform used to programmatically author, schedule, and monitor workflows. It allows you to define workflows as Directed Acyclic Graphs (DAGs) of tasks, where each task represents a unit of work. Airflow then executes these tasks in the specified order, handling dependencies, retries, and logging along the way.

- `@official` [Airflow](https://airflow.apache.org/)
- `@official` [Airflow Docs](https://airflow.apache.org/docs)
- `@opensource` [airflow](https://github.com/apache/airflow)
- `@article` [Building Pipelines In Apache Airflow – For Beginners](https://towardsdatascience.com/building-pipelines-in-apache-airflow-for-beginners-58f87a1512d5/?utm_source=roadmap&utm_medium=Referral&utm_campaign=TDS+roadmap+integration)
- `@video` [What is Apache Airflow? For beginners](https://www.youtube.com/watch?v=CGxxVj13sOs)
- `@video` [Apache Airflow Tutorial for Data Engineers](https://www.youtube.com/watch?v=y5rYZLBZ_Fw)
- `@feed` [Explore top posts about Apache Airflow](https://app.daily.dev/tags/apache-airflow?ref=roadmapsh)

#### Prometheus

Prometheus is an open-source monitoring and alerting toolkit originally built at SoundCloud. It collects and stores metrics as time-series data, meaning metrics are stored with a timestamp at which they were recorded, along with optional key-value pairs called labels. Prometheus uses a pull model to scrape metrics from instrumented jobs, either directly or via push gateways for short-lived jobs. It offers a powerful query language (PromQL) to analyze and visualize the collected data, enabling users to set up alerts based on defined thresholds.

- `@official` [Prometheus Website](https://prometheus.io/)
- `@official` [Prometheus Docs](https://prometheus.io/docs/introduction/overview/)
- `@official` [Getting Started with Prometheus](https://prometheus.io/docs/tutorials/getting_started/)
- `@video` [Introduction to the Prometheus Monitoring System | Key Concepts and Features](https://www.youtube.com/watch?v=STVMGrYIlfg&t=16s)

#### LIME

LIME (Local Interpretable Model-agnostic Explanations) is a technique used to understand the predictions of machine learning models by approximating them locally with a more interpretable model. It focuses on explaining individual predictions by perturbing the input data around a specific instance and observing how the model's prediction changes. This allows one to identify which features are most important for that particular prediction, even if the underlying model is complex and opaque.

- `@official` [lime](https://github.com/marcotcr/lime)
- `@article` [Explainable AI - Understanding and Trusting Machine Learning Models](https://www.datacamp.com/tutorial/explainable-ai-understanding-and-trusting-machine-learning-models)
- `@video` [Understanding LIME | Explainable AI](https://www.youtube.com/watch?v=CYl172IwqKs)

#### Deep Learning

Deep learning is a subset of machine learning that uses artificial neural networks with multiple layers (hence "deep") to analyze data with complex structures. These networks learn hierarchical representations of data, where each layer extracts increasingly abstract features from the previous layer. This allows deep learning models to automatically discover intricate patterns and relationships in data, making them particularly effective for tasks like image recognition, natural language processing, and speech recognition.

- `@roadmap` [Visit the Dedicated Machine Learning Roadmap](https://roadmap.sh/machine-learning)
- `@book` [Deep Learning Book](https://www.deeplearningbook.org/)
- `@course` [Practical Deep Learning](https://course.fast.ai/)
- `@article` [Introduction to Deep Learning](https://www.ibm.com/topics/deep-learning)
- `@video` [What is a Neural Network?](https://www.youtube.com/watch?v=aircAruvnKk)

#### Model Evaluation

Model evaluation is the process of assessing the performance of a machine learning model using various metrics and techniques. It helps determine how well the model generalizes to unseen data and whether it meets the desired performance criteria. This involves using different evaluation metrics depending on the type of problem (e.g., accuracy, precision, recall, F1-score for classification; RMSE, MAE for regression) and employing techniques like cross-validation to obtain a reliable estimate of the model's performance.

- `@article` [What is Model Evaluation](https://domino.ai/data-science-dictionary/model-evaluation)
- `@article` [Model Evaluation Metrics](https://www.markovml.com/blog/model-evaluation-metrics)
- `@article` [How to Evaluate the Performance of Your ML/ AI Models](https://towardsdatascience.com/how-to-evaluate-the-performance-of-your-ml-ai-models-ba1debc6f2fa/?utm_source=roadmap&utm_medium=Referral&utm_campaign=TDS+roadmap+integration)
- `@video` [How to evaluate ML models | Evaluation metrics for machine learning](https://www.youtube.com/watch?v=LbX4X71-TFI)

#### Data Pipelines

Data pipelines are a series of automated processes that transport and transform data from various sources to a destination for analysis or storage. They typically involve steps like data extraction, cleaning, transformation, and loading (ETL) into databases, data lakes, or warehouses. Pipelines can handle batch or real-time data, ensuring that large-scale datasets are processed efficiently and consistently. They play a crucial role in ensuring data integrity and enabling businesses to derive insights from raw data for reporting, analytics, or machine learning.

- `@article` [What is a Data Pipeline? - IBM](https://www.ibm.com/topics/data-pipeline)
- `@article` [How to Build Data Pipelines for Machine Learning](https://towardsdatascience.com/how-to-build-data-pipelines-for-machine-learning-b97bbef050a5/)
- `@article` [Read Articles about Data Pipelines](https://towardsdatascience.com/tag/data-pipeline/)
- `@video` [What are Data Pipelines?](https://www.youtube.com/watch?v=oKixNpz6jNo)

#### Data Lakes & Warehouses

Data lakes and data warehouses are both systems for storing large amounts of data, but they differ in structure and purpose. A data lake stores data in its raw, unprocessed format, allowing for flexibility in analysis and exploration. A data warehouse, on the other hand, stores data that has been structured and transformed for specific analytical purposes, often optimized for querying and reporting.

- `@article` [Data Lake Definition](https://azure.microsoft.com/en-gb/resources/cloud-computing-dictionary/what-is-a-data-lake)
- `@article` [Data Lake VS Data Warehouse](https://towardsdatascience.com/data-lake-vs-data-warehouse-2e3df551b800/?utm_source=roadmap&utm_medium=Referral&utm_campaign=TDS+roadmap+integration)
- `@video` [What is a Data Lake?](https://www.youtube.com/watch?v=LxcH6z8TFpI)
- `@video` [What is a Data Warehouse?](https://www.youtube.com/watch?v=k4tK2ttdSDg)
- `@video` [Data Lake VS Data Warehouse VS Data Marts](https://www.youtube.com/watch?v=w9-WoReNKHk)

#### Data Ingestion Architecture

 
Data ingestion architecture describes how data flows into a system from its original sources, such as databases, APIs, or streaming platforms. It defines whether data arrives in batches or in real time, and how it gets validated and stored along the way. A well-designed architecture keeps data reliable even as sources and volumes grow.

- `@article` [Data Ingestion Patterns](https://docs.aws.amazon.com/whitepapers/latest/aws-cloud-data-ingestion-patterns-practices/data-ingestion-patterns.html)
- `@article` [Data pipeline design patterns](https://towardsdatascience.com/data-pipeline-design-patterns-100afa4b93e3/?utm_source=roadmap&utm_medium=Referral&utm_campaign=TDS+roadmap+integration)
- `@article` [How to Build an AI-Powered Weather ETL Pipeline with Databricks and GPT-4o: From API To Dashboard](https://towardsdatascience.com/how-to-build-an-ai-powered-weather-etl-pipeline-with-databricks-and-gpt-4o-from-api-to-dashboard/?utm_source=roadmap&utm_medium=Referral&utm_campaign=TDS+roadmap+integration)
- `@video` [What is a data pipeline?](https://www.youtube.com/watch?v=kGT4PcTEPP8)

#### Scikit-learn

Scikit-learn is a Python library that provides simple and efficient tools for data mining and data analysis. It features various classification, regression, clustering algorithms, and tools for model selection, preprocessing, and dimensionality reduction. It's built on NumPy, SciPy, and matplotlib, making it a robust and versatile library for a wide range of machine learning tasks.

- `@official` [scikit-learn: machine learning in Python](https://scikit-learn.org/)
- `@opensource` [scikit-learn](https://github.com/scikit-learn/scikit-learn)
- `@article` [What is Scikit-Learn (Sklearn)?](https://www.ibm.com/think/topics/scikit-learn)
- `@video` [How to train and test a neural network using scikit-learn and Keras in Jupyter Notebook](https://www.youtube.com/watch?v=_JG71FIP1rk)
- `@video` [Scikit-learn Crash Course - Machine Learning Library for Python](https://www.youtube.com/watch?v=0B5eIE_1vpU)

#### TensorFlow

TensorFlow is an open-source software library created by Google for numerical computation and large-scale machine learning. It provides a comprehensive ecosystem of tools, libraries, and community resources that allows researchers and developers to build and deploy ML-powered applications. TensorFlow is particularly well-suited for deep learning tasks, enabling the creation of complex neural networks for image recognition, natural language processing, and more.

- `@official` [Tensorflow](https://www.tensorflow.org/)
- `@official` [Tensorflow Documentation](https://www.tensorflow.org/learn)
- `@article` [Mastering Deep Learning with TensorFlow: From Beginner to Expert](https://towardsdatascience.com/an-introduction-to-tensorflow-fa5b17051f6b/?utm_source=roadmap&utm_medium=Referral&utm_campaign=TDS+roadmap+integration)
- `@video` [Tensorflow in 100 seconds](https://www.youtube.com/watch?v=i8NETqtGHms)
- `@video` [Python TensorFlow for Machine Learning – Neural Network Text Classification Tutorial](https://www.youtube.com/watch?v=VtRLrQ3Ev-U)

#### PyTorch

PyTorch is an open-source machine learning framework primarily developed by Meta AI. It's used for a variety of applications, including computer vision, natural language processing, and reinforcement learning. PyTorch is known for its dynamic computation graph, which allows for more flexibility and easier debugging compared to static graph frameworks. It provides a comprehensive set of tools and libraries to build and train neural networks.

- `@official` [PyTorch](https://pytorch.org/)
- `@official` [PyTorch Docs](https://pytorch.org/docs/stable/index.html)
- `@article` [What is PyTorc? | IBM](https://www.ibm.com/think/topics/pytorch)
- `@article` [PyTorch Explained: From Automatic Differentiation to Training Custom Neural Networks](https://towardsdatascience.com/the-basics-of-deep-learning-with-pytorch-in-1-hour/?utm_source=roadmap&utm_medium=Referral&utm_campaign=TDS+roadmap+integration)
- `@video` [PyTorch in 100 seconds](https://www.youtube.com/watch?v=ORMx45xqWkA)
- `@video` [PyTorch for Deep Learning & Machine Learning – Full Course](https://www.youtube.com/watch?v=V_xro1bcAuA)

#### MLFlow

MLflow is an open-source platform designed to manage the complete machine learning lifecycle. It provides tools for tracking experiments, packaging code into reproducible runs, and deploying models to various platforms. MLflow helps data scientists and engineers streamline their workflows, collaborate effectively, and ensure the reliability of their machine learning projects.

- `@official` [MLFlow](https://mlflow.org/)
- `@official` [MLFlow Docs](https://mlflow.org/docs/latest/)
- `@opensource` [mlflow](https://github.com/mlflow/mlflow)
- `@article` [Streamline Your Machine Learning Workflow with MLFlow](https://www.datacamp.com/tutorial/mlflow-streamline-machine-learning-workflow)
- `@article` [Comprehensive Guide to MlFlow](https://towardsdatascience.com/comprehensive-guide-to-mlflow-b84086b002ae/?utm_source=roadmap&utm_medium=Referral&utm_campaign=TDS+roadmap+integration)
- `@video` [MLFlow Tutorial | ML Ops Tutorial](https://www.youtube.com/watch?v=6ngxBkx05Fs)
- `@video` [MLflow for Machine Learning Development - Video Introduction](https://www.youtube.com/watch?v=5pPflDSdFLg&list=PLQqR_3C2fhUUOmaeowgv4WquvH515zVmo)

## Tools

#### Flink

Apache Flink is an open-source stream processing framework designed for real-time and batch data processing with low latency and high throughput. It supports event time processing, fault tolerance, and stateful operations, making it ideal for applications like real-time analytics, fraud detection, and event-driven systems. Flink is highly scalable, integrates with various data systems, and is widely used in industries for large-scale, real-time data processing tasks.

- `@official` [Apache Flink Documentation](https://flink.apache.org/)
- `@article` [Apache Flink](https://www.tutorialspoint.com/apache_flink/apache_flink_introduction.htm)
- `@article` [An Introduction to Stream Processing with Apache Flink](https://towardsdatascience.com/an-introduction-to-stream-processing-with-apache-flink-b4acfa58f14d/?utm_source=roadmap&utm_medium=Referral&utm_campaign=TDS+roadmap+integration)
- `@video` [Introduction | Apache Flink 101](https://www.youtube.com/watch?v=3cg5dABA6mo&list=PLa7VYi0yPIH1UdmQcnUr8lvjbUV8JriK0)
- `@feed` [Explore top posts about Apache Flink](https://app.daily.dev/tags/apache-flink?ref=roadmapsh)

#### Version Control

 
Version control tracks changes to files over time, so teams can see what changed, who changed it, and roll back if needed. In ML projects, this applies not just to code but also to datasets, model files, and configuration. Without it, reproducing a past result or debugging a regression becomes very difficult.

- `@roadmap` [Visit the Dedicated Git & GitHub Roadmpa](https://roadmap.sh/git-github)
- `@official` [Git](https://git-scm.com/)
- `@official` [Git Documentation](https://git-scm.com/docs)
- `@article` [What is Version Control?](https://www.atlassian.com/git/tutorials/what-is-version-control)
- `@article` [Getting Started with Git and GitHub: A Complete Tutorial for Beginner](https://towardsdatascience.com/learn-basic-git-commands-for-your-data-science-works-2a75396d530d/)

#### CI/CD

 
CI/CD stands for Continuous Integration and Continuous Delivery, a practice of automatically testing and shipping code changes. In an ML context, CI/CD pipelines also test data quality, validate model performance, and automate retraining or redeployment when new code or data arrives. This reduces manual steps and helps catch broken models before they go live.

- `@article` [What is CI/CD? - GitLab](https://about.gitlab.com/topics/ci-cd/)
- `@article` [What is CI/CD? - Redhat](https://www.redhat.com/en/topics/devops/what-is-ci-cd)
- `@video` [CI/CD In 5 Minutes](https://www.youtube.com/watch?v=42UP1fxi2SY)

#### Orchestration

 
Orchestration means coordinating the different steps of an ML workflow so they run in the right order, automatically. A typical pipeline might need to pull data, preprocess it, train a model, evaluate it, then deploy it, and orchestration tools handle scheduling, dependencies, and retries for these steps. This removes the need to run each step by hand.

- `@article` [A Complete Guide to Understanding Data Orchestration](https://towardsdatascience.com/a-complete-guide-to-understanding-data-orchestration-87a20b46297c/?utm_source=roadmap&utm_medium=Referral&utm_campaign=TDS+roadmap+integration)
- `@article` [Data Orchestration Tools (Quick Reference Guide)](https://www.montecarlodata.com/blog-11-data-orchestration-tools)
- `@video` [What is Data Orchestration?](https://www.youtube.com/watch?v=iyw9puEmTrA)

#### Experiment Tracking

 
Experiment tracking records the details of each model training run, such as hyperparameters, code version, dataset used, and resulting metrics. This makes it possible to compare different runs and understand which changes actually improved the model. Data scientists rely on this to avoid losing track of what was tried and what worked.

- `@article` [Experiment Tracking](https://madewithml.com/courses/mlops/experiment-tracking/#dashboard)
- `@article` [ML Flow Model Registry](https://mlflow.org/docs/latest/model-registry.html)
