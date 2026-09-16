# Data Engineer Roadmap — plan extrait

- **Slug** : `data-engineer`
- **Description amont** : Step by step guide to becoming a Data Engineer in @currentYear@
- **Derniere modification amont** : 2026-08-07T06:34:48.171Z
- **Capture** : 2026-09-16
- **Volume** : 186 noeuds de contenu, 186 documentes, 398 ressources
- **Renvois vers d'autres roadmaps** : `https://roadmap.sh`, `https://roadmap.sh/data-analyst`, `https://roadmap.sh/devops`, `https://roadmap.sh/mlops`, `https://roadmap.sh/python-data-analysis`, `https://roadmap.sh/sql`

---

## Data Engineer

#### What is Data Engineering?

Data engineering is the practice of designing and building systems for the aggregation, storage and analysis of data at scale. Data engineers excel at creating and deploying algorithms, data pipelines and workflows that sort raw data into ready-to-use datasets. Data engineering is an integral component of the modern data platform and makes it possible for businesses to analyze and apply the data they receive, regardless of the data source or format.

- `@article` [What is data engineering?](https://www.ibm.com/think/topics/data-engineering)
- `@video` [How Data Engineering Works?](https://www.youtube.com/watch?v=qWru-b6m030)

#### Data Engineering vs Data Science

Data engineering and data science are distinct but complementary roles within the field of data. Data engineering focuses on building and maintaining the infrastructure for data collection, storage, and processing, essentially creating the systems that make data available for downstream users. On the other hand, data science professionals, like data analysts and data scientists, uses that data to extract insights, build predictive models, and ultimately inform decision-making.

- `@video` [Should You Be a Data Scientist, Analyst or Engineer?](https://www.youtube.com/watch?v=dUnKYhripIE)

### Introduction

Data engineering is the discipline of designing, building, and maintaining systems that collect, store, and process data at scale. It sits between raw data sources and the analysts, scientists, and applications that consume that data. The work involves building pipelines, managing storage infrastructure, and ensuring data is reliable and accessible.

- `@video` [What Does a Data Engineer ACTUALLY Do?](https://www.youtube.com/watch?v=hTjo-QVWcK0)

#### Skills and Responsibilities

A data engineer works across a broad set of tools and systems: programming languages, databases, cloud platforms, pipeline orchestration, and distributed computing. Core responsibilities include building and maintaining data pipelines, managing database schemas, optimizing query performance, and ensuring data quality. Collaboration with data scientists, analysts, and software engineers is also a regular part of the role.

- `@article` [Top Data Engineer Skills and Responsibilities](https://www.simplilearn.com/data-engineer-role-article)
- `@video` [What skills do you need as a Data Engineer?](https://www.youtube.com/watch?v=sF04UxNAvmg)

#### Data Engineering Lifecycle

The data engineering lifecycle describes the stages data moves through from creation to consumption. These stages typically include generation, ingestion, storage, transformation, and serving. Each stage has its own tools, failure modes, and design considerations. Understanding the full lifecycle helps engineers make better decisions about architecture and tooling.

- `@book` [Fundamentals of Data Engineering](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/)
- `@article` [Data Engineering Lifecycle](https://medium.com/towards-data-engineering/data-engineering-lifecycle-d1e7ee81632e)
- `@video` [Getting Into Data Engineering](https://www.youtube.com/watch?v=hZu_87l62J4)

## Python is recommended

#### Choosing the Right Technologies

Selecting the right technology stack depends on data volume, team size, latency requirements, and budget. There is no universal best choice; a small startup may do well with a simple Postgres setup, while a large enterprise may need distributed processing and a cloud data warehouse. The decision involves evaluating trade-offs between cost, complexity, scalability, and maintainability.

- `@book` [Fundamentals of Data Engineering](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/)
- `@article` [Build hybrid and multicloud architectures using Google Cloud](https://cloud.google.com/architecture/hybrid-multicloud-patterns)
- `@article` [The Unfulfilled Promise of Serverless](https://www.lastweekinaws.com/blog/the-unfulfilled-promise-of-serverless/)

#### Python

Python’s inherent characteristics and the wealth of resources that have grown around it have made it the data engineer’s language of choice. Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically-typed and garbage-collected.

- `@roadmap` [Visit the Dedicated Python Roadmap](https://roadmap.sh/python)
- `@article` [Tutorial Series: How to Code in Python](https://www.digitalocean.com/community/tutorials/how-to-write-your-first-python-3-program)
- `@article` [Google's Python Class](https://developers.google.com/edu/python)
- `@video` [Learn Python - Full Course](https://www.youtube.com/watch?v=4M87qBgpafk)

#### Java

Java has had a big influence on data engineering because many core big data tools and frameworks, like Hadoop, Spark (originally in Scala, which runs on the JVM), and Kafka, are built using Java or run on the Java Virtual Machine (JVM). This means Java’s performance, scalability, and cross-platform capabilities have shaped how large-scale data processing systems are designed.

- `@roadmap` [Visit the Dedicated Java Roadmap](https://roadmap.sh/java)
- `@course` [Introduction to Java by Hyperskill (JetBrains Academy)](https://hyperskill.org/courses/8)
- `@video` [Java Tutorial for Beginners](https://www.youtube.com/watch?v=eIrMbAQSU34&feature=youtu.be)
- `@video` [Java + DSA + Interview Preparation Course (For beginners)](https://www.youtube.com/playlist?list=PL9gnSGHSqcnr_DxHsP7AW9ftq0AtAyYqJ)

#### Scala

Scala is a programming language that combines the strengths of object-oriented and functional programming, and it runs on the Java Virtual Machine (JVM). In data engineering, Scala is especially important because Apache Spark, one of the most popular big data processing frameworks, was written in Scala. This means Scala can use Spark’s features directly and efficiently, often with cleaner and more concise code than Java. Its ability to handle complex data transformations with less code makes it a powerful tool for building fast, scalable data pipelines.

- `@roadmap` [Visit the Dedicated Scala Roadmap](https://roadmap.sh/scala)
- `@official` [The Scala Programming Language](https://www.scala-lang.org/)
- `@article` [Scala for Beginners: An Introduction](https://daily.dev/blog/scala-for-beginners-an-introduction)
- `@video` [Scala Tutorial](https://www.youtube.com/playlist?list=PLS1QulWo1RIagob5D6kMIAvu7DQC5VTh3)

#### Go

Go is a compiled language developed by Google, known for its simplicity, fast execution, and strong concurrency model. In data engineering, it is used to build lightweight, high-throughput services and tools. Its performance characteristics make it a good fit for data pipeline components where latency and resource efficiency matter.

- `@roadmap` [Visit Dedicated Go Roadmap](https://roadmap.sh/golang)
- `@official` [Go Documentation](https://go.dev/doc/)
- `@article` [Go, the Programming Language of the Cloud](https://thenewstack.io/go-the-programming-language-of-the-cloud/)
- `@video` [Go Programming â€“ Golang Course with Bonus Projects](https://www.youtube.com/watch?v=un6ZyFkqFKo)

### Programming Skills

To be successful as a data engineer, you need to be proficient in coding. This involves knowing basic concepts and principles that form the foundation of any computer programming language. These include understanding variables, which store data for processing, control structures such as loops and conditional statements that direct the flow of a program, data structures which organize and store data efficiently, and algorithms which provide step-by-step instructions to solve specific problems or perform specific tasks.

## Understand Different Steps

### Data Structures and Algorithms

Data structures and algorithms form the foundation for writing efficient code. This knowledge is relevant for data engineers when optimizing queries, designing storage schemas, and building processing logic that scales. Common topics include arrays, hash maps, trees, sorting, and complexity analysis.

- `@roadmap` [Visit the Dedicated DSA Roadmap](https://roadmap.sh/datastructures-and-algorithms)
- `@article` [Interview Questions about Data Structures](https://www.csharpstar.com/csharp-algorithms/)
- `@video` [Data Structures Illustrated](https://www.youtube.com/watch?v=9rhT3P1MDHk&list=PLkZYeFmDuaN2-KUIv-mvbjfKszIGJ4FaY)
- `@video` [Intro to Algorithms](https://www.youtube.com/watch?v=rL8X2mlNHPM)

#### Data Generation

Data generation refers to how raw data is produced and originates in a system. Data can come from user interactions, application logs, IoT sensors, databases, APIs, and many other sources. Understanding where data comes from and how it is structured at the source is the starting point for any data pipeline design.

- `@article` [The Concept of Data Generation](https://www.marktechpost.com/2023/02/27/the-concept-of-data-generation/)
- `@video` [Analog vs. Digital](https://www.youtube.com/watch?v=zzvglgC5ut0)

## 1

### Git and GitHub

Git is a distributed version control system that tracks changes to code over time. GitHub is a platform built on top of Git that adds collaboration features like pull requests, code review, and CI/CD integrations. Data engineers use Git to manage pipeline code, infrastructure configurations, and shared scripts across teams.

- `@roadmap` [Visit Dedicated Git & GitHub Roadmap](https://roadmap.sh/git-github)
- `@course` [Why use Git? (Interactive Lesson)](https://inter-git.com/lessons/introduction)
- `@article` [Git by Example - Learn Version Control with Bite-sized Lessons](https://antonz.org/git-by-example/)
- `@video` [Git & GitHub Crash Course For Beginners](https://www.youtube.com/watch?v=SWYqp7iY_Tc)

#### Data Storage

Data storage in the engineering lifecycle refers to where and how data is persisted after it is generated or ingested. The choice of storage system depends on access patterns, data volume, latency requirements, and cost. Options range from relational databases to object storage, data lakes, and columnar warehouses.

- `@article` [What is data storage?](https://www.ibm.com/think/topics/data-storage)

## 2

### Data Engineering Lifecycle

The data engineering lifecycle describes the stages data moves through from creation to consumption. These stages typically include generation, ingestion, storage, transformation, and serving. Each stage has its own tools, failure modes, and design considerations. Understanding the full lifecycle helps engineers make better decisions about architecture and tooling.

- `@book` [Fundamentals of Data Engineering](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/)
- `@article` [Data Engineering Lifecycle](https://medium.com/towards-data-engineering/data-engineering-lifecycle-d1e7ee81632e)
- `@video` [Getting Into Data Engineering](https://www.youtube.com/watch?v=hZu_87l62J4)

### Linux Basics

Knowledge of UNIX is a must for almost all kind of development as most of the code that you write is most likely going to be finally deployed on a UNIX/Linux machine. Linux has been the backbone of the free and open source software movement, providing a simple and elegant operating system for almost all your needs.

- `@roadmap` [Visit Dedicated Linux Roadmap](https://roadmap.sh/linux)
- `@course` [Coursera - Unix Courses](https://www.coursera.org/courses?query=unix)
- `@article` [Linux Basics](https://dev.to/rudrakshi99/linux-basics-2onj)
- `@video` [Linux Operating System - Crash Course](https://www.youtube.com/watch?v=ROjZy1WbCIA)

#### Data Ingestion

Data ingestion is the third step in the data engineering lifecycle. It entails the process of collecting and importing data files from various sources into a database for storage, processing and analysis. The goal of data ingestion is to clean and store data in an accessible and consistent central repository to prepare it for use within the organization.

- `@article` [What is Data Ingestion?](https://www.ibm.com/think/topics/data-ingestion)
- `@article` [Data Ingestion](https://www.qlik.com/us/data-ingestion)

## 3

### Networking Fundamentals

Networking fundamentals cover how data moves between systems: IP addressing, DNS, HTTP, TCP/UDP, and firewalls. Data engineers encounter networking when configuring cloud resources, troubleshooting pipeline failures, or setting up secure connections between services. A basic understanding of how networks operate helps diagnose connectivity issues and design reliable architectures.

- `@roadmap` [Visit the Dedicated Network Engineer Roadmap](https://roadmap.sh/network-engineer)
- `@article` [Khan Academy - Networking](https://www.khanacademy.org/computing/code-org/computers-and-the-internet)
- `@video` [Computer Networking Course - Network Engineering](https://www.youtube.com/watch?v=qiQR5rTSshw)
- `@video` [Networking Video Series (21 videos)](https://www.youtube.com/playlist?list=PLEbnTDJUr_IegfoqO4iPnPYQui46QqT0j)

#### Data Serving

Data serving is the last step in the data engineering process. Once the data is stored in your data architectures and transformed into coherent and useful format, it's time for get value from it. Data serving refers to the different ways data is used by downstream applications and users to create value. There are many ways companies can extract value from data, including training machine learning models, BI Analytics, and reverse ETL.

## 4

### Distributed Systems Basics

A distributed system is a collection of independent computers that communicate and coordinate to appear as a single unified system. They are widely used for scalability, fault tolerance, and high availability in modern applications. However, they bring challenges such as synchronization, consistency trade-offs (CAP theorem), concurrency, and network latency.

- `@article` [Introduction to Distributed Systems](https://www.freecodecamp.org/news/a-thorough-introduction-to-distributed-systems-3b91562c9b3c/)
- `@article` [Distributed Systems Guide](https://www.baeldung.com/cs/distributed-systems-guide)
- `@video` [Distributed Systems Explained](https://www.youtube.com/watch?v=IJWwfMyPu1c)

#### Database

A database is an organized, structured collection of electronic data that is stored, managed, and accessed via a computer system, usually controlled by a Database Management System (DBMS). Databases organize various types of data, such as words, numbers, images, and videos, allowing users to easily retrieve, update, and modify it for various purposes, from managing customer information to analyzing business processes.

#### Data Normalization

Data normalization is the process of organizing a relational database to reduce redundancy and improve data integrity. It involves decomposing tables into smaller, related ones according to normal forms (1NF, 2NF, 3NF, etc.). Normalized schemas are easier to maintain but may require more joins when querying.

- `@article` [What is Normalization in DBMS (SQL)? 1NF, 2NF, 3NF, BCNF Database with Example](https://www.guru99.com/database-normalization.html)
- `@video` [Complete guide to Database Normalization in SQL](https://www.youtube.com/watch?v=rBPQ5fg_kiY)

### Sources of Data

Sources of data are origins or locations from which data is collected, categorized as primary (direct, firsthand information) or secondary (collected by others). Common primary sources include surveys, interviews, experiments, and sensor data. Secondary sources encompass databases, published reports, government data, books, articles, and web data like social media posts. Data sources can also be classified as internal (within an organization) or external (from outside sources).

#### APIs

APIs (Application Programming Interfaces) expose data from external services in a structured format, typically JSON or XML over HTTP. Many data pipelines pull data from third-party APIs such as payment processors, marketing platforms, or social networks. Rate limits, authentication, and schema changes are common challenges when ingesting from APIs.

- `@roadmap` [Visit the Dedicated Java Roadmap](https://roadmap.sh/api-design)
- `@article` [What is an API?](https://aws.amazon.com/what-is/api/)
- `@article` [A Beginner's Guide to APIs](https://www.postman.com/what-is-an-api/)

#### Logs

Logs are files that record events, activities, and system operations over time. They provide a detailed historical record of what has happened within a system, including timestamps, event details, performance data, errors, and user actions. Logs are crucial for troubleshooting problems, monitoring system health and performance, investigating security incidents, and understanding how users interact with a system.

#### Data Modelling Techniques

Data modelling is the process of defining how data is structured and related within a storage system. Common techniques include entity-relationship (ER) modelling for transactional databases and dimensional modelling (star and snowflake schemas) for analytics. The choice of model affects query performance, flexibility, and how easy it is to evolve the schema over time.

- `@article` [7 data modeling techniques and concepts for business](https://www.techtarget.com/searchdatamanagement/tip/7-data-modeling-techniques-and-concepts-for-business)

### Data Collection Considerations

When collecting data, engineers must account for reliability, latency, volume, and schema consistency. Other considerations include data privacy regulations, deduplication, and handling of missing or malformed records. Good collection design reduces problems downstream in the pipeline.

- `@book` [Fundamentals of Data Engineering](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/)

#### Mobile Apps

Mobile apps are programs for phones and tablets, usually from app stores. They can be native (for one OS like iOS or Android), hybrid (web tech in a native shell), or cross-platform (like React Native). Apps use phone features like GPS and cameras. They do many things from games to shopping. Good mobile apps focus on easy use, speed, offline working, and security.

#### IoT

IoT, or Internet of Things, refers to a network of connected devices that interact with their environment. IoT devices extend beyond standard devices such as PCs, laptops, and smartphones, including smart locks, connected thermostats, and temperature sensors. In industrial settings, this also includes connected machines, robots, and package tracking devices, and many more. IoT Devices measure and collect data about their environment and some also interact by performing certain predefined actions, for example, turning the heat up or down.

- `@article` [What is the Internet of Things (IoT)?](https://www.ibm.com/think/topics/internet-of-things)
- `@article` [Internet of Things](https://en.wikipedia.org/wiki/Internet_of_things)
- `@video` [What is IoT (Internet of Things)? An Introduction](https://www.youtube.com/watch?v=4FxU-xpuCww)

#### CAP Theorem

The CAP theorem states that a distributed system can provide at most two of three guarantees: Consistency, Availability, and Partition Tolerance. In practice, network partitions are unavoidable, so systems must choose between consistency and availability when a partition occurs. This trade-off shapes the design of distributed databases like Cassandra, DynamoDB, and HBase.

- `@article` [What is CAP Theorem?](https://www.bmc.com/blogs/cap-theorem/)
- `@article` [An Illustrated Proof of the CAP Theorem](https://mwhittaker.github.io/blog/an_illustrated_proof_of_the_cap_theorem/)
- `@article` [CAP Theorem and its applications in NoSQL Databases](https://www.ibm.com/uk-en/cloud/learn/cap-theorem)
- `@video` [What is CAP Theorem?](https://www.youtube.com/watch?v=_RbsFXWRZ10)

#### OLTP vs OLAP

OLTP (Online Transaction Processing) systems are optimized for fast, frequent read and write operations, typically backing operational applications. OLAP (Online Analytical Processing) systems are designed for complex queries over large datasets, used in reporting and analytics. The two have different storage formats, indexing strategies, and performance characteristics.

- `@article` [What is OLTP?](https://www.oracle.com/uk/database/what-is-oltp/)
- `@article` [What is OLAP? - Online Analytical Processing Explained](https://aws.amazon.com/what-is/olap/)
- `@video` [OLTP vs OLAP](https://www.youtube.com/watch?v=iw-5kFzIdgY)

#### Learn SQL

SQL stands for Structured Query Language. It is a standardized programming language designed to manage and interact with relational database management systems (RDBMS). SQL allows you to create, read, edit, and delete data stored in database tables by writing specific queries.

- `@roadmap` [Visit Dedicated SQL Roadmap](https://roadmap.sh/sql)
- `@article` [SQL Tutorial - Essential SQL For The Beginners](https://www.sqltutorial.org/)

#### Indexing

Indexes are data structures that speed up query performance by allowing the database to find rows without scanning the entire table. They are created on one or more columns and come in various types, including B-tree, hash, and full-text indexes. Indexes improve read performance but add overhead to writes and storage.

#### Transactions

Transactions in SQL are units of work that group one or more database operations into a single, atomic unit. They ensure data integrity by following the ACID properties: Atomicity (all or nothing), Consistency (database remains in a valid state), Isolation (transactions don't interfere with each other), and Durability (committed changes are permanent). Transactions are essential for maintaining data consistency in complex operations and handling concurrent access to the database.

- `@article` [Transactions](https://www.tutorialspoint.com/sql/sql-transactions.htm)
- `@article` [A Guide to ACID Properties in Database Management Systems](https://www.mongodb.com/resources/basics/databases/acid-transactions)

### Database Fundamentals

Database fundamentals cover the core concepts that apply across most relational database systems: how data is organized into tables, how queries are executed, and how the database ensures consistency and durability. Topics include normalization, indexing, transactions, and query optimization. These concepts apply whether using PostgreSQL, MySQL, or any other relational system.

- `@article` [Oracle: What is a Database?](https://www.oracle.com/database/what-is-database/)
- `@article` [NoSQL Explained](https://www.mongodb.com/nosql-explained)
- `@video` [What is Relational Database](https://youtu.be/OqjJjpjDRLc)
- `@video` [How do NoSQL Databases work](https://www.youtube.com/watch?v=0buKQHokLK8)

#### Slowly Changing Dimension - SCD

Slowly Changing Dimensions (SCDs) are a data warehousing technique used to track changes in dimension data over time. Instead of simply overwriting old data with new data, SCDs allow you to maintain historical records of how dimension attributes have changed. This is crucial for accurate analysis of historical trends and business performance.

- `@article` [Implementing Slowly Changing Dimensions (SCDs) in Data Warehouses](https://www.sqlshack.com/implementing-slowly-changing-dimensions-scds-in-data-warehouses/)

### Relational Databases

Relational databases store data in tables with rows and columns, and use SQL for querying. Relationships between tables are defined through foreign keys. They are the most widely used type of database for transactional applications and form the backbone of most operational systems.

- `@course` [Databases and SQL](https://www.edx.org/course/databases-5-sql)
- `@article` [Relational Databases](https://www.ibm.com/cloud/learn/relational-databases)
- `@article` [Intro To Relational Databases](https://www.udacity.com/course/intro-to-relational-databases--ud197)
- `@video` [What is Relational Database](https://youtu.be/OqjJjpjDRLc)

#### Horizontal vs Vertical Scaling

Horizontal scaling is the process of adding more machines or nodes to an existing pool in a system to distribute the workload and address increased load. By contrast, vertical scaling involves increasing the computing power of individual machines in a system. This is achieved by adjusting or upgrading hardware components, such as CPU, RAM, and network speed.

- `@article` [Horizontal Vs. Vertical Scaling: Which Should You Choose?](https://www.cloudzero.com/blog/horizontal-vs-vertical-scaling/)
- `@video` [Vertical Vs Horizontal Scaling: Key Differences You Should Know](https://www.youtube.com/watch?v=dvRFHG2-uYs)

#### Star vs Snowflake Schema

Star and snowflake schemas are two approaches to organizing data in a data warehouse. A star schema has a central fact table connected directly to dimension tables, making queries simple and fast. A snowflake schema normalizes dimension tables into multiple related tables, reducing redundancy but requiring more joins. Star schemas are more common in analytical systems due to their query performance.

### Column

Column-family databases (also called wide-column stores) organize data into rows and dynamic columns grouped into column families. They are optimized for read and write operations on large datasets spread across many machines. This model is well suited for time-series data, logging, and analytical workloads.

- `@article` [What are columnar databases? Here are 35 examples.](https://www.tinybird.co/blog-posts/what-is-a-columnar-database)
- `@article` [Columnar Databases](https://www.techtarget.com/searchdatamanagement/definition/columnar-database)
- `@video` [WWhat is a Columnar Database? (vs. Row-oriented Database)](https://www.youtube.com/watch?v=1MnvuNg33pA)

### NoSQL Databases

NoSQL databases are a category of database management systems designed for handling unstructured, semi-structured, or rapidly changing data. Unlike traditional relational databases, which use fixed schemas and SQL for querying, NoSQL databases offer flexible data models and can be classified into several types:

1.  **Document Stores**: Store data in JSON, BSON, or XML formats, allowing for flexible and hierarchical data structures (e.g., MongoDB, CouchDB).
2.  **Key-Value Stores**: Store data as key-value pairs, suitable for high-speed read and write operations (e.g., Redis, Riak).
3.  **Column-Family Stores**: Store data in columns rather than rows, which is useful for handling large volumes of data and wide columnar tables (e.g., Apache Cassandra, HBase).
4.  **Graph Databases**: Optimize the storage and querying of data with complex relationships using graph structures (e.g., Neo4j, Amazon Neptune).

NoSQL databases are often used for applications requiring high scalability, flexibility, and performance, such as real-time analytics, content management systems, and distributed data storage.

- `@article` [NoSQL Explained](https://www.mongodb.com/nosql-explained)
- `@video` [How do NoSQL Databases work](https://www.youtube.com/watch?v=0buKQHokLK8)
- `@video` [SQL vs NoSQL Explained](https://www.youtube.com/watch?v=ruz-vK8IesE)
- `@feed` [Explore top posts about NoSQL](https://app.daily.dev/tags/nosql?ref=roadmapsh)

### Graph

Graph databases store data as nodes and edges, representing entities and the relationships between them. They are optimized for queries that traverse relationships, such as finding connections between users or mapping dependencies. Graph databases are used in social networks, fraud detection, recommendation engines, and knowledge graphs.

- `@article` [What is a Graph database?](https://aws.amazon.com/nosql/graph/)
- `@article` [Graph database](https://en.wikipedia.org/wiki/Graph_database)
- `@video` [Introduction to NoSQL](https://www.youtube.com/watch?v=qI_g07C_Q5I)

### Key-Value

Key value databases, also known as key value stores, are NoSQL database types where data is stored as key value pairs and optimized for reading and writing that data. The data is fetched by a unique key or a number of unique keys to retrieve the associated value with each key. Both keys and values can be anything, ranging from simple objects to complex compound objects. Key-value databases are highly partitionable and allow horizontal scaling at a level that other types of databases cannot achieve.

- `@article` [What is a Key Value Database? - AWS](https://aws.amazon.com/nosql/key-value/)
- `@article` [What Is A Key-Value Database? - MongoDB](https://www.mongodb.com/resources/basics/databases/key-value-database)

### What is Data Warehouse?

A data warehouse is a centralized repository for storing large volumes of structured, historical data from multiple sources. It is optimized for analytical queries rather than transactional operations. Data warehouses power business intelligence, reporting, and data analysis, providing a single source of truth across an organization.

- `@article` [What Is a Data Warehouse?](https://www.oracle.com/database/what-is-a-data-warehouse/)
- `@video` [What is a Data Warehouse?](https://www.youtube.com/watch?v=k4tK2ttdSDg)

### Data Warehousing Architectures

Data warehousing architectures describe how data is organized, stored, and accessed across a warehouse system. Common patterns include traditional ETL-based warehouses, cloud-native warehouses, data lakehouse architectures, and federated query systems. The choice of architecture affects cost, query performance, scalability, and how fresh the data available for analysis is.

#### Data Mart

A data mart is a subset of a data warehouse, focused on a specific business function or department. A data mart is streamlined for quicker querying and a more straightforward setup, catering to the specialized needs of a particular team, or function. Data marts only hold data relevant to a specific department or business unit, enabling quicker access to specific datasets, and simpler management

- `@article` [What is a Data Mart?](https://www.ibm.com/think/topics/data-mart)
- `@article` [WData Mart vs Data Warehouse: a Detailed Comparison](https://www.datacamp.com/blog/data-mart-vs-data-warehouse)
- `@video` [Data Lake VS Data Warehouse VS Data Marts](https://www.youtube.com/watch?v=w9-WoReNKHk)

### Data Mesh

A data mesh is a modern approach to data architecture that shifts data management from a centralized model to a decentralized one. It emphasizes domain-oriented ownership, where data management aligns with specific business areas. This alignment makes data operations more scalable and flexible, leveraging the knowledge and expertise of those closest to the data. Data mesh is defined by four principles: data domains, data products, self-serve data platform, and federated computational governance.

- `@article` [What Is a Data Mesh? - AWS](https://aws.amazon.com/what-is/data-mesh)
- `@video` [Data Mesh Architecture](https://www.datamesh-architecture.com/)

### Cloud Computing

Cloud computing refers to the delivery of computing resources, including servers, storage, databases, networking, and software, over the internet. Major cloud providers offer on-demand infrastructure that scales with usage and is billed per consumption. Cloud platforms are the dominant environment for modern data engineering work.

- `@article` [Cloud Computing - IBM](https://www.ibm.com/think/topics/cloud-computing)
- `@article` [What is Cloud Computing? - Azure](https://azure.microsoft.com/en-gb/resources/cloud-computing-dictionary/what-is-cloud-computing)
- `@video` [What is Cloud Computing? - Amazon Web Services](https://www.youtube.com/watch?v=mxT233EdY5c)

#### Cloud Architectures

Cloud architectures describe how systems are designed to run on cloud infrastructure. Common patterns include multi-tier architectures, microservices, event-driven designs, and serverless functions. Good cloud architecture balances cost, reliability, scalability, and security.

- `@article` [What is cloud architecture? - Google](https://cloud.google.com/learn/what-is-cloud-architecture)
- `@video` [WWhat is Cloud Architecture and Common Models?](https://www.youtube.com/watch?v=zTP-bx495hU)

#### Batch

Batch processing is a method in which large volumes of collected data are processed in chunks or batches. This approach is especially effective for resource-intensive jobs, repetitive tasks, and managing extensive datasets where real-time processing isn’t required. It is ideal for applications like data warehousing, ETL (Extract, Transform, Load), and large-scale reporting. Data batch processing is mainly automated, requiring minimal human interaction once the process is set up. Tasks are predefined, and the system executes them according to a scheduled timeline, typically during off-peak hours when computing resources are readily available.

- `@article` [What is Batch Processing?](https://aws.amazon.com/what-is/batch-processing/)
- `@article` [Batch And Streaming Demystified For Unification](https://towardsdatascience.com/batch-and-streaming-demystified-for-unification-dee0b48f921d/)

#### Hybrid

Hybrid data ingestion combines aspects of both real-time and batch ingestion. This approach gives you the flexibility to adapt your data ingestion strategy as your needs evolve. For example, you could process data in real-time for critical applications and in batches for less time-sensitive tasks. Two common hybrid methods are Lambda architecture-based and micro-batching.

- `@article` [What is Data Ingestion: Types, Tools, and Real-Life Use Cases](https://estuary.dev/blog/data-ingestion/)
- `@article` [Lambda Architecture](https://www.databricks.com/glossary/lambda-architecture)
- `@article` [What is Micro Batching: A Comprehensive Guide 101](https://hevodata.com/learn/micro-batching/)

### Types of Data Ingestion

The primary types of data ingestion are Batch, Streaming, and Hybrid. Batch ingestion processes data in large, scheduled chunks, suitable for non-time-sensitive tasks like monthly reports. Streaming (or Real-time) ingestion handles data as it arrives, ideal for time-sensitive applications such as fraud detection or IoT monitoring. Hybrid ingestion combines both methods, offering flexibility for diverse business needs.

#### Realtime

Real-time processing, also known as streaming processing, involves the immediate ingestion, as well as analysis, of data as it is generated, providing instantaneous insights and enabling timely decisions in time-sensitive applications like financial trading, medical monitoring, and autonomous vehicles. This differs from batch processing, which handles data in later batches, and typically involves continuous data streaming, low latency, and high availability to deliver immediate outcomes for critical tasks.

### Data Pipelines

Data pipelines are a series of automated processes that transport and transform data from various sources to a destination for analysis or storage. They typically involve steps like data extraction, cleaning, transformation, and loading (ETL) into databases, data lakes, or warehouses. Pipelines can handle batch or real-time data, ensuring that large-scale datasets are processed efficiently and consistently. They play a crucial role in ensuring data integrity and enabling businesses to derive insights from raw data for reporting, analytics, or machine learning.

- `@article` [What is a Data Pipeline? - IBM](https://www.ibm.com/topics/data-pipeline)
- `@video` [What are Data Pipelines?](https://www.youtube.com/watch?v=oKixNpz6jNo)

### Cluster Computing Basics

Cluster computing refers to using a group of connected machines that work together as a single system to process data. It enables workloads that are too large or slow for a single machine by distributing computation across multiple nodes. Concepts like job scheduling, distributed file systems, and resource management are central to working with clusters.

## Relational Databases

#### MySQL

MySQL is an open-source relational database management system (RDBMS) known for its speed, reliability, and ease of use. It uses SQL (Structured Query Language) for database interactions and supports a range of features for data management, including transactions, indexing, and stored procedures. MySQL is widely used for web applications, data warehousing, and various other applications due to its scalability and flexibility. It integrates well with many programming languages and platforms, and is often employed in conjunction with web servers and frameworks in popular software stacks like LAMP (Linux, Apache, MySQL, PHP/Python/Perl). MySQL is maintained by Oracle Corporation and has a large community and ecosystem supporting its development and use.

- `@official` [MySQL](https://www.mysql.com/)
- `@article` [MySQL for Developers](https://planetscale.com/courses/mysql-for-developers/introduction/course-introduction)
- `@article` [MySQL Tutorial](https://www.mysqltutorial.org/)
- `@video` [MySQL Complete Course](https://www.youtube.com/watch?v=5OdVJbNCSso)

#### PostgreSQL

PostgreSQL is an open-source relational database known for its standards compliance, extensibility, and advanced feature set. It supports complex queries, JSON storage, full-text search, and custom data types. PostgreSQL is widely used in both transactional and analytical workloads.

- `@roadmap` [Visit Dedicated PostgreSQL DBA Roadmap](https://roadmap.sh/postgresql-dba)
- `@official` [PostgreSQL Website](https://www.postgresql.org/)
- `@article` [Learn PostgreSQL - Full Tutorial for Beginners](https://www.postgresqltutorial.com/)
- `@video` [Postgres tutorial for Beginners](https://www.youtube.com/watch?v=SpfIwlAYaKk)

#### MariaDB

MariaDB server is a community developed fork of MySQL server. Started by core members of the original MySQL team, MariaDB actively works with outside developers to deliver the most feature rich, stable, and sanely licensed open SQL server in the industry. MariaDB was created with the intention of being a more versatile, drop-in replacement version of MySQL

- `@official` [MariaDB](https://mariadb.org/)
- `@article` [MariaDB vs MySQL](https://www.guru99.com/mariadb-vs-mysql.html)
- `@video` [MariaDB Tutorial For Beginners in One Hour](https://www.youtube.com/watch?v=_AMj02sANpI)

#### Aurora DB

Amazon Aurora (Aurora) is a fully managed relational database engine that's compatible with MySQL and PostgreSQL. Aurora includes a high-performance storage subsystem. Its MySQL- and PostgreSQL-compatible database engines are customized to take advantage of that fast distributed storage. The underlying storage grows automatically as needed. Aurora also automates and standardizes database clustering and replication, which are typically among the most challenging aspects of database configuration and administration.

- `@official` [SAmazon Aurora](https://aws.amazon.com/rds/aurora/)

#### Oracle

Oracle Database is a commercial relational database system widely used in enterprise environments. It is known for its robustness, advanced features, and support for very large-scale deployments. Oracle is common in financial services, healthcare, and government sectors where long-term vendor support and mature tooling are priorities.

- `@official` [Oracle Docs](https://docs.oracle.com/en/database/index.html)
- `@video` [Oracle SQL Tutorial for Beginners](https://www.youtube.com/watch?v=ObbNGhcxXJA)

#### MS SQL

Microsoft SQL Server (MS SQL) is a relational database developed by Microsoft, commonly used in enterprise and Windows-based environments. It integrates tightly with the Microsoft ecosystem, including Azure, Power BI, and .NET. MS SQL supports T-SQL, Microsoft's extension of SQL with additional procedural capabilities.

- `@roadmap` [Visit Dedicated SQL Roadmap](https://roadmap.sh/sql)
- `@official` [MS SQL](https://www.microsoft.com/en-ca/sql-server/)
- `@article` [Tutorials for SQL Server](https://docs.microsoft.com/en-us/sql/sql-server/tutorials-for-sql-server-2016?view=sql-server-ver15)
- `@video` [SQL Server tutorial for beginners](https://www.youtube.com/watch?v=-EPMOaV7h_Q)

### Document

\*\*Document Databases are a type of No-SQL databases that store data in JSON, BSON, or XML formats, allowing for flexible, semi-structured and hierarchical data structures. These databases are characterized by their dynamic schema, scalability through distribution, and ability to intuitively map data models to application code. Popular examples include MongoDB, which allows for easy storage and retrieval of varied data types without requiring a rigid, predefined schema.

- `@article` [What is a Document Database?](https://www.mongodb.com/resources/basics/databases/document-databases)
- `@article` [Document-oriented database](https://en.wikipedia.org/wiki/Document-oriented_database)

#### MongoDB

MongoDB is a NoSQL, open-source database designed for storing and managing large volumes of unstructured or semi-structured data. It uses a document-oriented data model where data is stored in BSON (Binary JSON) format, which allows for flexible and hierarchical data representation. Unlike traditional relational databases, MongoDB doesn't require a fixed schema, making it suitable for applications with evolving data requirements or varying data structures. It supports horizontal scaling through sharding and offers high availability with replica sets. MongoDB is commonly used for applications requiring rapid development, real-time analytics, and large-scale data handling, such as content management systems, IoT applications, and big data platforms.

- `@roadmap` [Visit Dedicated MongoDB Roadmap](https://roadmap.sh/mongodb)
- `@official` [MongoDB Website](https://www.mongodb.com/)
- `@official` [Learning Path for MongoDB Developers](https://learn.mongodb.com/catalog)
- `@article` [MongoDB Online Sandbox](https://mongoplayground.net/)

#### ElasticSearch

Elasticsearch is a distributed search and analytics engine built on Apache Lucene. It is designed for full-text search, log analysis, and real-time data exploration. Elasticsearch is commonly used as the backend for search features in applications and as a centralized store for log and event data, often alongside Kibana.

- `@roadmap` [Visit the Dedicated Elasticsearch Roadmap](https://roadmap.sh/elasticsearch)
- `@official` [Elasticsearch Website](https://www.elastic.co/elasticsearch/)
- `@official` [Elasticsearch Documentation](https://www.elastic.co/guide/index.html)
- `@video` [What is Elasticsearch](https://www.youtube.com/watch?v=ZP0NmfyfsoM)

#### CosmosDB

Azure Cosmos DB is a native No-SQL database service and vector database for working with the document data model. It can arbitrarily store native JSON documents with flexible schema. Data is indexed automatically and is available for query using a flavor of the SQL query language designed for JSON data. It also supports vector search. You can access the API using SDKs for popular frameworks such [as.NET](http://as.NET), Python, Java, and Node.js.

- `@official` [What are Containers?](https://azure.microsoft.com/en-us/products/cosmos-db#FAQ)
- `@official` [CAzure Cosmos DB - Database for the AI Era](https://learn.microsoft.com/en-us/azure/cosmos-db/introduction)
- `@video` [What is Azure Cosmos DB?](https://www.youtube.com/watch?v=hBY2YcaIOQM&)

#### CouchDB

Apache CouchDB is an open-source document database that uses JSON for documents and HTTP as its API. It is designed for reliability and offline-first use cases, with a built-in replication protocol that syncs data between devices and servers. CouchDB is used in scenarios where data needs to be available and writable even without a network connection.

- `@official` [CouchDB Documentation](https://docs.couchdb.org/en/stable/intro/overview.html)
- `@article` [What is CouchDB?](https://www.ibm.com/think/topics/couchdb)

#### Neo4j

Neo4j is the most widely used graph database. It stores data natively as nodes and relationships and uses Cypher, a declarative query language designed for graph traversal. Neo4j is used for applications where relationship-heavy queries are central, such as recommendation systems and network analysis.

- `@official` [Neo4j Website](https://neo4j.com)
- `@video` [Neo4j in 100 Seconds](https://www.youtube.com/watch?v=T6L9EoBy8Zk)
- `@video` [Neo4j Course for Beginners](https://www.youtube.com/watch?v=_IgbB24scLI)

#### Neptune

Amazon Neptune is a managed graph database service on AWS that supports both the Property Graph model (with Gremlin) and RDF (with SPARQL). It is designed for highly connected datasets and scales to billions of relationships. Neptune is used for knowledge graphs, fraud detection, and identity resolution.

- `@official` [AWS Neptune](https://aws.amazon.com/neptune/)
- `@article` [Setting Up Amazon Neptune Graph Database](https://cliffordedsouza.medium.com/setting-up-amazon-neptune-graph-database-2b73512a7388)
- `@video` [Getting Started with Neptune Serverless](https://www.youtube.com/watch?v=b04-jjM9t4g)

#### Cassandra

Apache Cassandra is an open-source distributed wide-column database designed for high availability and linear scalability. It has no single point of failure and is optimized for fast writes across multiple data centers. Cassandra is used for time-series data, IoT workloads, and applications requiring continuous uptime.

- `@official` [Apache Cassandra](https://cassandra.apache.org/_/index.html)
- `@article` [Cassandra - Quick Guide](https://www.tutorialspoint.com/cassandra/cassandra_quick_guide.htm)
- `@video` [Apache Cassandra - Course for Beginners](https://www.youtube.com/watch?v=J-cSy5MeMOA)

#### BigTable

Bigtable is a high-performance, scalable database that excels at capturing, processing, and analyzing data in real-time. It aggregates data as it's written, providing immediate insights into user behavior, A/B testing results, and engagement metrics. This real-time capability also fuels AI/ML models for interactive applications. Bigtable integrates seamlessly with both Dataflow, enriching streaming pipelines with low-latency lookups, and BigQuery, enabling real-time serving of analytics in user-facing applications and ad-hoc querying on the same data.

- `@official` [Bigtable: Fast, Flexible NoSQL](https://cloud.google.com/bigtable?hl=en#scale-your-latency-sensitive-applications-with-the-nosql-pioneer)
- `@article` [Google Bigtable](https://www.techtarget.com/searchdatamanagement/definition/Google-BigTable)

#### HBase

HBase is a column-oriented No-SQL database management system that runs on top of Hadoop Distributed File System (HDFS), a main component of Apache Hadoop. HBase provides a fault-tolerant way of storing sparse data sets, which are common in many big data use cases. It is well-suited for real-time data processing or random read/write access to large volumes of data. HBase applications are written in Java™ much like a typical Apache MapReduce application.

- `@official` [Apacha HBase?](https://hbase.apache.org/)
- `@article` [What is HBase?](https://www.ibm.com/think/topics/hbase)
- `@article` [Apache HBase](https://en.wikipedia.org/wiki/Apache_HBase)

#### Redis

Redis is an in-memory key-value store known for its extremely low latency. It supports a variety of data structures including strings, lists, sets, sorted sets, and hashes. Redis is widely used for caching, real-time leaderboards, pub/sub messaging, and session storage.

- `@roadmap` [Visit Dedicated Redis Roadmap](https://roadmap.sh/redis)
- `@course` [Redis Crash Course](https://www.youtube.com/watch?v=XCsS_NVAa1g)
- `@official` [Redis Documentation](https://redis.io/docs/latest/)
- `@video` [Redis in 100 Seconds](https://www.youtube.com/watch?v=G1rOthIU-uo)

#### Memcached

Memcached is a high-performance, distributed in-memory caching system. It is simpler than Redis, supporting only key-value string storage, but is very fast and horizontally scalable. Memcached is commonly used to cache database query results and reduce load on backend systems.

- `@opensource` [memcached](https://github.com/memcached/memcached#readme)
- `@article` [Memcached Tutorial](https://www.tutorialspoint.com/memcached/index.htm)
- `@video` [Redis vs Memcached](https://www.youtube.com/watch?v=Gyy1SiE8avE)

#### DynamoDB

Amazon DynamoDB is a fully managed key-value and document database service on AWS. It provides single-digit millisecond performance at any scale and handles replication and scaling automatically. DynamoDB is commonly used for applications that require predictable performance and high availability without database administration.

- `@official` [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)

### Data Warehouse

A data warehouse stores structured, processed data from operational systems, optimized for analytical queries. It typically uses columnar storage and is populated through ETL or ELT processes. Common cloud data warehouses include Google BigQuery, Snowflake, and Amazon Redshift.

- `@article` [What Is a Data Warehouse?](https://www.oracle.com/database/what-is-a-data-warehouse/)
- `@video` [What is a Data Warehouse?](https://www.youtube.com/watch?v=k4tK2ttdSDg)

#### Google BigQuery

BigQuery is a managed, serverless data warehouse product by Google, offering scalable analysis over large quantities of data. It is a Platform as a Service (PaaS) that supports querying using a dialect of SQL. BigQuery is NoOps, meaning there is no infrastructure to manage and you don't need a database administrator. BigQuery lets you focus on analyzing data to find meaningful insights while using familiar SQL and built-in machine learning at unmatched price-performance.

- `@official` [BigQuery overview](https://cloud.google.com/bigquery/docs/introduction)
- `@official` [From data warehouse to autonomous data and AI platform](https://cloud.google.com/bigquery)
- `@video` [What is BigQuery?](https://www.youtube.com/watch?v=d3MDxC_iuaw)

#### Snowflake

Snowflake is a cloud-based data platform that provides a data warehouse as a service. It allows organizations to store, analyze, and share data, offering features like data engineering, data governance, and collaboration capabilities. Snowflake is known for its scalability, ease of use, and ability to handle diverse workloads, including data warehousing, data lakes, and machine learning.

- `@official` [Snowflake Docs](https://docs.snowflake.com/)
- `@official` [Snowflake in 20 minutes](https://docs.snowflake.com/en/user-guide/tutorials/snowflake-in-20minutes)
- `@video` [Learn Snowflake in 2 Hours](https://www.youtube.com/watch?v=mP3QbYURT9k)

#### Amazon Redshift

Amazon Redshift is a cloud-based data warehouse service from Amazon that lets you store and analyze large amounts of data quickly. It’s designed for running complex queries on huge datasets, so businesses can use it to turn raw data into useful reports and insights. You can load data into Redshift from many sources, and then use SQL to explore it, just like you would with a regular database — but it’s optimized to handle much bigger data and run faster.

- `@official` [Amazon Redshift](https://aws.amazon.com/redshift/)
- `@video` [Getting Started with Amazon Redshift - AWS Online Tech Talks](https://www.youtube.com/watch?v=dfo4J5ZhlKI)

## Other Data Architectures

#### Data Fabric

Data fabric is an architectural concept that aims to provide a unified layer for accessing and managing data across heterogeneous environments, including on-premises and multiple clouds. It uses metadata, automation, and integration patterns to connect disparate data sources. Data fabric focuses on making data discoverable and accessible without requiring it to be moved to a central location.

- `@article` [What is a data fabric?](http://ibm.com/think/topics/data-fabric)
- `@article` [Data Fabric defined](https://www.jamesserra.com/archive/2021/06/data-fabric-defined/)
- `@article` [How Data Fabric Can Optimize Data Delivery](https://www.gartner.com/en/data-analytics/topics/data-fabric)

#### Data Hub

A data hub is a centralized platform that acts as an integration point for data flowing between multiple systems. Unlike a data warehouse, a data hub focuses on data movement and integration rather than storage for analytics. It often combines features of a message broker, metadata catalog, and integration layer.

- `@article` [Data hub](https://en.wikipedia.org/wiki/Data_hub)
- `@article` [What is a Data Hub? Definition, 7 Key Benefits & Why You Might Need One](https://www.cdata.com/blog/what-is-a-data-hub)

#### Metadata-first Architecture

A metadata-first architecture treats metadata as a first-class citizen in data system design. Rather than just documenting data after the fact, metadata is captured and used actively to govern, discover, and lineage-track data across the organization. This approach supports better data quality, compliance, and self-service analytics.

#### Serverless Options

Serverless data storage involves using cloud provider services for databases and object storage that automatically scale infrastructure and implement a consumption-based, pay-as-you-go model, eliminating the need for developers to manage, provision, or maintain any physical or virtual servers. This approach simplifies development, reduces operational overhead, and offers cost-effectiveness by charging only for the resources used, allowing teams to focus on applications rather than infrastructure management.

- `@article` [What Is Serverless Computing?](https://www.ibm.com/think/topics/serverless)

### Data Lake

A data lake is a centralized storage repository that holds large amounts of raw data in its native format, including structured, semi-structured, and unstructured data. Unlike a data warehouse, a data lake does not enforce a schema on ingestion. Data is stored cheaply at scale and processed when needed, which enables flexibility for future analysis.

- `@article` [Data Lake Definition](https://azure.microsoft.com/en-gb/resources/cloud-computing-dictionary/what-is-a-data-lake)
- `@video` [What is a Data Lake?](https://www.youtube.com/watch?v=LxcH6z8TFpI)

#### Databricks Delta Lake

Delta Lake is the optimized storage layer that provides the foundation for tables in a lakehouse on Databricks. Delta Lake is open source software that extends Parquet data files with a file-based transaction log for ACID transactions and scalable metadata handling. Delta Lake is fully compatible with Apache Spark APIs, and was developed for tight integration with Structured Streaming, allowing you to easily use a single copy of data for both batch and streaming operations and providing incremental processing at scale.

- `@book` [The Delta Lake Series — Fundamentals and Performance](https://www.databricks.com/resources/ebook/the-delta-lake-series-fundamentals-performance)
- `@official` [What is Delta Lake in Databricks?](https://docs.databricks.com/aws/en/delta)
- `@video` [Delta Lake](https://www.databricks.com/resources/demos/videos/lakehouse-platform/delta-lake)

#### Snowflake

Snowflake is a cloud-based data platform that provides a data warehouse as a service. It allows organizations to store, analyze, and share data, offering features like data engineering, data governance, and collaboration capabilities. Snowflake is known for its scalability, ease of use, and ability to handle diverse workloads, including data warehousing, data lakes, and machine learning.

- `@official` [Snowflake Docs](https://docs.snowflake.com/)
- `@official` [Snowflake in 20 minutes](https://docs.snowflake.com/en/user-guide/tutorials/snowflake-in-20minutes)
- `@video` [Learn Snowflake in 2 Hours](https://www.youtube.com/watch?v=mP3QbYURT9k)

#### Onehouse

Onehouse Managed Lakehouse is a cloud-native SaaS product built on top of Apache Hudi. It replaces painful, inefficient do-iy-yourseld data lake management around file sizing, masking, deletion, clustering, access control, caching, etc. with foundational data infrastructure as a service, to ingest, store, optimize and transform your data on industry-leading open data formats.

- `@official` [Onehouse](https://www.onehouse.ai/)

## AWS

#### Amazon EC2 ( Compute)

Amazon EC2 (Elastic Compute Cloud) provides virtual servers in the AWS cloud. Users can choose instance types optimized for compute, memory, or storage, and pay only for what they run. EC2 is used for running data processing jobs, hosting databases, and building custom data infrastructure on AWS.

- `@official` [EC2 - User Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)
- `@video` [Introduction to Amazon EC2](https://www.youtube.com/watch?v=eaicwmnSdCs)

#### S3 (Storage)

Amazon S3 (Simple Storage Service) is an object storage service offered by Amazon Web Services (AWS). It provides scalable, secure and durable storage on the internet. Designed for storing and retrieving any amount of data from anywhere on the web, it is a key tool for many companies in the field of data storage, including mobile applications, websites, backup and restore, archive, enterprise applications, IoT devices, and big data analytics.

- `@official` [S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)

#### Amazon RDS (Database)

Amazon RDS (Relational Database Service) is a managed relational database service from AWS that supports MySQL, PostgreSQL, MariaDB, Oracle, and MS SQL Server. It handles provisioning, backups, patching, and replication automatically. RDS is used for transactional databases that require minimal database administration overhead.

- `@official` [Amazon RDS](https://aws.amazon.com/rds/)

#### Glue (ETL)

AWS Glue is a fully managed ETL service that automates the discovery, cataloging, and transformation of data. It includes a data catalog for storing metadata, a job scheduler, and a serverless Spark environment for running transformations. Glue is commonly used to move and transform data between S3, Redshift, and other AWS services.

- `@official` [Amazon RDS](https://aws.amazon.com/rds/)

#### Azure Virtual Machines

Azure Virtual Machines (VMs) enable virtualization without requiring hardware investments. They provide customizable environments for development, testing, and cloud applications so you can run different operating systems like Ubuntu on a Windows host based on your needs. One of the key advantages of Azure VMs is the pay-as-you-go pricing model. It allows you to scale resources up or down as needed, ensuring cost efficiency without wasting resources.

- `@official` [Azure Virtual Machines](https://azure.microsoft.com/en-us/products/virtual-machines)
- `@official` [Virtual Machines in Azure](https://learn.microsoft.com/en-us/azure/virtual-machines/overview)
- `@video` [AVirtual Machines in Azure | Beginner's Guide](https://www.youtube.com/watch?v=_abaWXoQFZU)

#### Azure Blob Storage

Azure Blob Storage is Microsoft's object storage solution for the cloud. “Blob” stands for Binary Large Object, a term used to describe storage for unstructured data like text, images, and video. Azure Blob Storage is Microsoft Azure’s solution for storing these blobs in the cloud. It offers flexible storage—you only pay based on your usage. Depending on the access speed you need for your data, you can choose from various storage tiers (hot, cool, and archive). Being cloud-based, it is scalable, secure, and easy to manage.

- `@official` [Azure Blob Storage](https://azure.microsoft.com/en-us/products/storage/blobs)
- `@official` [Introduction to Azure Blob Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction)
- `@video` [A Beginners Guide to Azure Blob Storage](https://www.youtube.com/watch?v=ah1XqItWkuc&t=300s)

#### Azure SQL Database

Azure SQL Database is a fully managed Platform as a Service (PaaS) offering. It abstracts the underlying infrastructure, enabling developers to focus on building and deploying applications without worrying about database maintenance tasks.

- `@official` [Azure SQL Database](https://azure.microsoft.com/en-us/products/azure-sql/database)
- `@official` [What is Azure SQL Database?](https://learn.microsoft.com/en-us/azure/azure-sql/database/sql-database-paas-overview?view=azuresql)
- `@video` [Azure SQL for Beginners](https://www.youtube.com/playlist?list=PLlrxD0HtieHi5c9-i_Dnxw9vxBY-TqaeN)

#### Data Factory (ETL)

Data Factory, most commonly referring to Microsoft's Azure Data Factory, is a cloud-based data integration service that allows you to create, schedule, and orchestrate workflows to move and transform data from various sources into a centralized location for analysis. It provides tools for building Extract, Transform, and Load (ETL) pipelines, enabling businesses to prepare data for analytics, business intelligence, and other data-driven initiatives without extensive coding, thanks to its visual, code-free interface and native connectors.

- `@course` [Microsoft Azure - Data Factory](https://www.coursera.org/learn/microsoft-azure---data-factory)
- `@official` [What is Azure Data Factory?](https://learn.microsoft.com/en-us/azure/data-factory/introduction)
- `@official` [Azure Data Factory Documentation](https://learn.microsoft.com/en-gb/azure/data-factory/)

#### Compute Engine (Compute)

Google Cloud Compute Engine provides virtual machine instances on Google's infrastructure. It supports custom machine types, preemptible VMs for cost savings, and integration with other Google Cloud services. Compute Engine is used for running custom workloads, data processing jobs, and services that require full control over the operating environment.

- `@course` [The Basics of Google Cloud Compute](https://www.cloudskillsboost.google/course_templates/754)
- `@official` [Compute Engine overview](https://cloud.google.com/compute/docs/overview)
- `@video` [WCompute Engine in a minute](https://www.youtube.com/watch?v=IuK4gQeHRcI)

#### Google Cloud Storage

Google Cloud Storage (GCS) is a scalable, secure, and durable object storage service within Google Cloud Platform (GCP) designed for storing and retrieving unstructured data of any type or size. It allows users to store data in "buckets" and access it through APIs, web interfaces, or command-line tools for applications, backups, media hosting, and big data analytics. GCS offers different storage classes to optimize costs based on data access frequency, strong security with encryption, and high availability through redundant data storage across multiple locations.

- `@article` [Cloud Storage](https://cloud.google.com/storage)
- `@article` [Google Cloud Storage](https://en.wikipedia.org/wiki/Google_Cloud_Storage)
- `@article` [Cloud Storage in a minute](https://www.youtube.com/watch?v=wNOs3LlsH6k)

#### Cloud SQL (Database)

Google Cloud SQL is a fully-managed, cost-effective and scalable database service that makes it easy to set-up, maintain, manage and administer MySQL, PostgreSQL, and SQL Server databases in the cloud. Hosted on Google Cloud Platform, Cloud SQL provides a database infrastructure for applications running anywhere.

- `@course` [Cloud SQL](https://www.cloudskillsboost.google/course_templates/701)
- `@official` [Cloud SQL](https://cloud.google.com/sql)
- `@official` [Cloud SQL overview](https://cloud.google.com/sql/docs/introduction)

#### Dataflow

Dataflow is a Google Cloud service that provides unified stream and batch data processing at scale. Typical use cases for Dataflow include Data movement,ETL processes, BI dashboarding, and applying ML in real time to streaming data.

- `@official` [Dataflow](https://cloud.google.com/products/dataflow)
- `@article` [Dataflow](https://en.wikipedia.org/wiki/Google_Cloud_Dataflow)
- `@video` [What is Google Dataflow](https://www.youtube.com/watch?v=KalJ0VuEM7s)

## ETL Process

#### Extract Data

The first step in ETL processes involves extract data from data sources to a staging area. Data can come in various types and formats, from SQL or NoSQL databases and plan text to image and video files.

#### Transform Data

In the second step, ETL tools transform and consolidate the raw data in the staging area to prepare it for the target data warehouse. The data transformation phase is normally the most complex and prone to errors, as it can involved multiple transformations, including basic data cleaning operations, deduplication, cata casting, filtering, grouping, encrypting, and many more.

#### Load Data

In the third step, the transformed data is moved from the staging area into the targe data storage solution, such as a data warehouse or data lake. For most organizations, the data loading process is automated, well-defined, continuous and batch-driven.

#### Apache Airflow

Apache Airflow is an open-source tool that helps you schedule, organize, and monitor workflows. Think of it like a to-do list for your data tasks, but smarter — you can set tasks to run in a specific order, track their progress, and see what happens if something fails. It’s often used for automating data pipelines so that data moves, gets processed, and is ready for use without manual work.

- `@official` [Apache Airflow](https://airflow.apache.org/)

#### dbt

dbt, also known as the data build tool, is designed to simplify the management of data warehouses and transform the data within. This is primarily the T, or transformation, within ELT (or sometimes ETL) processes. It allows for easy transition between data warehouse types, such as Snowflake, BigQuery, Postgres, or DuckDB. dbt also provides the ability to use SQL across teams of multiple users, simplifying interaction. In addition, dbt translates between SQL dialects as appropriate to connect to different data sources and warehouses.

- `@course` [dbt Official Courses](https://learn.getdbt.com/catalog)
- `@official` [dbt Documentation](https://docs.getdbt.com/docs/build/documentation)

#### Luigi

Luigi is a powerful, easy-to-use open-source framework for building data pipelines with Python. It handles dependency resolution, workflow management, visualization etc. Luigi helps to build the data pipeline, typically associated with long-running batch processes.

- `@official` [Luigi Docs](https://luigi.readthedocs.io/)
- `@article` [Getting Started with Luigi—What, Why & How](https://medium.com/big-data-processing/getting-started-with-luigi-what-why-how-f8e639a1f2a5)

#### Prefect

Prefect is an open-source orchestration engine that turns your Python functions into production-grade data pipelines with minimal friction. You can build and schedule workflows in pure Python—no DSLs or complex config files—and run them anywhere you can run Python. Prefect handles the heavy lifting for you out of the box: automatic state tracking, failure handling, real-time monitoring, and more.

- `@official` [Prefect Docs](https://docs.prefect.io/v3/get-started)
- `@video` [Getting Started with Prefect](https://www.youtube.com/watch?v=D5DhwVNHWeU)

## Azure

#### What is Cluster Computing

Cluster computing is a model where multiple computers are networked together to act as a unified processing system. Tasks are split across nodes in the cluster and executed in parallel. This approach is used in big data processing, scientific computing, and any workload that exceeds single-machine capacity.

- `@article` [What is cluster computing? - IBM](https://www.ibm.com/think/topics/cluster-computing)
- `@article` [Computer cluster - Wikipedia](http://en.wikipedia.org/wiki/Computer_cluster)
- `@video` [WUnderstand the Basic Cluster Concepts](https://www.youtube.com/watch?v=8BBDxzJL6fY)

#### Distributed File Systems

A Distributed File System (DFS) allows multiple computers to access and share files across a network as if they were stored on a single local machine. It distributes data across multiple servers, enhancing accessibility and data redundancy. This enables users to access files from various locations and devices, promoting collaboration and data availability.

- `@article` [What is a Distributed File System (DFS)? A Complete Guide](http://starwindsoftware.com/blog/what-is-a-distributed-file-system-dfs-a-complete-guide/)

#### HDFS

HDFS (Hadoop Distributed File System) is Hadoop’s primary storage system. It is designed to reliably store data across a cluster of machines. Its architecture is set up for this type of access to large datasets and is optimized for fault tolerance, scalability, and data locality.

- `@official` [HDFS Architecture Guide](https://hadoop.apache.org/docs/r1.2.1/hdfs_design.html)
- `@article` [Hadoop Distributed File System (HDFS)](https://www.databricks.com/glossary/hadoop-distributed-file-system-hdfs)
- `@article` [What is Hadoop Distributed File System (HDFS)?](https://www.ibm.com/think/topics/hdfs)

## Data Pipeline Tools

#### Job Scheduling

A scheduling system manages and distributes computational jobs across multiple interconnected computers (a cluster) to optimize resource utilization and job completion. The goal is to efficiently allocate cluster resources (like processors and memory) to incoming jobs based on factors such as user priority, job requirements, and deadlines.

- `@article` [Job scheduler](https://en.wikipedia.org/wiki/Job_scheduler)
- `@article` [Cluster Resources — Job Scheduling](https://supun-kamburugamuve.medium.com/cluster-resources-job-scheduling-bb63644476bc)

#### Cluster Management Tools

Cluster management software maximizes the work that a cluster of computers can perform. A cluster manager balances workload to reduce bottlenecks, monitors the health of the elements of the cluster, and manages failover when an element fails. A cluster manager can also help a system administrator to perform administration tasks on elements in the cluster.

#### Kubernetes

Kubernetes is an open-source container orchestration system that automates the deployment, scaling, and management of containerized applications. In data engineering, it is used to run pipeline workers, schedule jobs, and manage microservices. Kubernetes has become the standard infrastructure layer for modern data platforms.

- `@roadmap` [Visit the Dedicated Java Kubernetes](https://roadmap.sh/kubernetes)
- `@official` [Kubernetes Documentation](https://kubernetes.io/docs/home/)
- `@article` [Kubernetes: An Overview](https://thenewstack.io/kubernetes-an-overview/)
- `@video` [Kubernetes Crash Course for Absolute Beginners](https://www.youtube.com/watch?v=s_o8dwzRlu4)

#### Apache Hadoop YARN

Apache Hadoop YARN (Yet Another Resource Negotiator) is the part of Hadoop that manages resources and runs jobs on a cluster. It has a ResourceManager that controls all cluster resources and an ApplicationMaster for each job that schedules and runs tasks. YARN lets different tools like MapReduce and Spark share the same cluster, making it more efficient, flexible, and reliable.

- `@video` [Hadoop Yarn Tutorial](https://www.youtube.com/watch?v=6bIF9VwRwE0)

## Cloud Providers

#### Apache Spark

Apache Spark is a distributed data processing engine for large-scale batch and streaming workloads. It processes data in memory across a cluster, making it significantly faster than MapReduce for many workloads. Spark supports Python, Scala, Java, and R, and provides APIs for SQL, streaming, machine learning, and graph processing.

- `@official` [ApacheSpark](https://spark.apache.org/documentation.html)
- `@article` [Spark By Examples](https://sparkbyexamples.com)

### Big Data Tools

Big data tools are designed to process and analyze datasets too large to handle with traditional single-machine tools. They distribute computation across clusters and are optimized for throughput at scale. The most widely used big data processing framework is Apache Spark, with Hadoop-based tools remaining common in legacy environments.

- `@article` [What is Big Data?](https://cloud.google.com/learn/what-is-big-data?hl=en)
- `@video` [Introduction to Big Data with Spark and Hadoop](http://youtube.com/watch?v=vHlwg4ciCsI&t=80s&ab_channel=freeCodeAcademy)

#### Docker

Docker is the most widely used platform for building, shipping, and running containers. It packages code and its dependencies into a lightweight, portable image that runs the same in any environment. Data engineers use Docker to containerize pipeline code, ensure reproducible environments, and simplify deployment.

- `@roadmap` [Visit Dedicated Docker Roadmap](https://roadmap.sh/docker)
- `@official` [Docker Documentation](https://docs.docker.com/)
- `@video` [Docker Tutorial](https://www.youtube.com/watch?v=RqTEHSBrYFw)
- `@video` [Docker simplified in 55 seconds](https://youtu.be/vP_4DlOH1G4)

#### Kubernetes

Kubernetes is an open-source system for automating the deployment, scaling, and operation of containerized applications. It manages clusters of containers across multiple nodes and handles load balancing, self-healing, and rolling updates. Data engineers use Kubernetes to run distributed processing jobs, schedule pipeline workers, and manage infrastructure at scale.

- `@roadmap` [Visit the Dedicated Kubernetes Roadmap](https://roadmap.sh/kubernetes)
- `@official` [Kubernetes Documentation](https://kubernetes.io/docs/home/)
- `@article` [Kubernetes: An Overview](https://thenewstack.io/kubernetes-an-overview/)
- `@video` [Kubernetes Crash Course for Absolute Beginners](https://www.youtube.com/watch?v=s_o8dwzRlu4)

### Containers & Orchestration

Containers package an application and its dependencies into a portable, isolated unit that runs consistently across environments. Container orchestration automates the deployment, scaling, and management of these containers across a cluster. Together, containers and orchestration form the foundation for running modern data workloads in cloud and hybrid environments.

- `@article` [What are Containers? - Google Cloud](https://cloud.google.com/learn/what-are-containers)
- `@article` [Articles about Containers - The New Stack](https://thenewstack.io/category/containers/)
- `@video` [What are Containers?](https://www.youtube.com/playlist?list=PLawsLZMfND4nz-WDBZIj8-nbzGFD4S9oz)
- `@video` [Why You Need Data Orchestration](https://www.youtube.com/watch?v=ZtlS5-G-gng)

#### Google Cloud GKE

Google Kubernetes Engine (GKE) is Google Cloud's managed Kubernetes service. It handles cluster provisioning, upgrades, and scaling automatically, reducing the operational burden of running Kubernetes. GKE is used to run containerized data workloads on Google Cloud infrastructure.

- `@official` [GKE](https://cloud.google.com/kubernetes-engine)
- `@video` [What is Google Kubernetes Engine (GKE)?](https://www.youtube.com/watch?v=Rl5M1CzgEH4)

#### AWS EKS

Amazon EKS (Elastic Kubernetes Service) is AWS's managed Kubernetes service. It runs the Kubernetes control plane across multiple availability zones and integrates with AWS services like IAM, VPC, and ECR. EKS is used to run containerized data pipelines and services on AWS without managing the Kubernetes control plane directly.

- `@official` [Amazon Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks/)
- `@official` [Concepts of Amazon EKS](https://docs.aws.amazon.com/eks/)

#### Prometheus

Prometheus is a free software application used for event monitoring and alerting. It records real-time metrics in a time series database built using a HTTP pull model, with flexible queries and real-time alerting.

- `@official` [Prometheus Documentation](https://prometheus.io/docs/introduction/overview/)
- `@official` [Getting Started with Prometheus](https://prometheus.io/docs/tutorials/getting_started/)

### CI/CD

CI/CD (Continuous Integration and Continuous Delivery) is a set of practices and tools for automating the testing and deployment of code changes. In data engineering, CI/CD pipelines validate pipeline code, run tests, and deploy updates to production automatically. This reduces manual errors and accelerates the delivery of pipeline changes.

- `@article` [What is CI/CD? Continuous Integration and Continuous Delivery](https://www.guru99.com/continuous-integration.html)
- `@article` [Continuous Integration vs Delivery vs Deployment](https://www.guru99.com/continuous-integration-vs-delivery-vs-deployment.html)
- `@article` [CI/CD Pipeline: Learn with Example](https://www.guru99.com/ci-cd-pipeline.html)

#### GitHub Actions

GitHub Actions is a CI/CD platform built into GitHub. It allows developers to define automated workflows as YAML files that trigger on code events like pushes and pull requests. GitHub Actions is widely used to run tests, lint code, build Docker images, and deploy data pipelines.

- `@official` [GitHub Actions Documentation](https://docs.github.com/en/actions)

#### Circle CI

CircleCI is a CI/CD service that can be integrated with GitHub, BitBucket and GitLab repositories. The service that can be used as a SaaS offering or self-managed using your own resources.

- `@official` [CircleCI](https://circleci.com/)
- `@official` [CircleCI Documentation](https://circleci.com/docs)
- `@official` [Configuration Tutorial](https://circleci.com/docs/config-intro)

#### Datadog

Datadog is a monitoring and analytics platform for large-scale applications. It encompasses infrastructure monitoring, application performance monitoring, log management, and user-experience monitoring. Datadog aggregates data across your entire stack with 400+ integrations for troubleshooting, alerting, and graphing.

- `@official` [Datadog Documentation](https://docs.datadoghq.com/)

#### Sentry

Sentry tracks your software performance, measuring metrics like throughput and latency, and displaying the impact of errors across multiple systems. Sentry captures distributed traces consisting of transactions and spans, which measure individual services and individual operations within those services.

- `@official` [Sentry Documentation](https://docs.sentry.io/)

### Monitoring

Monitoring is the practice of collecting and analyzing metrics, logs, and events from running systems to track their health and performance. For data pipelines, monitoring covers job success rates, data freshness, latency, and resource usage. Good monitoring enables fast detection and diagnosis of failures before they affect downstream consumers.

- `@article` [Top Monitoring Tools](https://thectoclub.com/tools/best-application-monitoring-software/)

#### GitLab CI

GitLab offers a CI/CD service that can be used as a SaaS offering or self-managed using your own resources. You can use GitLab CI with any GitLab hosted repository, or any BitBucket Cloud or GitHub repository in the GitLab Premium self-managed, GitLab Premium SaaS and higher tiers.

- `@official` [GitLab Documentation](https://docs.gitlab.com/)
- `@official` [Get Started with GitLab CI](https://docs.gitlab.com/ee/ci/quick_start/)
- `@official` [Learn GitLab Tutorials](https://docs.gitlab.com/ee/tutorials/)
- `@official` [GitLab CI/CD Examples](https://docs.gitlab.com/ee/ci/examples/)

#### ArgoCD

Argo CD is a declarative GitOps continuous delivery tool for Kubernetes. It continuously monitors a Git repository and ensures that the state of the Kubernetes cluster matches the desired state defined in code. Argo CD is used in data engineering to manage Kubernetes-based pipeline deployments and infrastructure changes through Git.

- `@official` [Argo CD - Argo Project](https://argo-cd.readthedocs.io/en/stable/)
- `@video` [ArgoCD Tutorial for Beginners](https://www.youtube.com/watch?v=MeU5_k9ssrs)
- `@video` [What is ArgoCD](https://www.youtube.com/watch?v=p-kAqxuJNik)

#### New Relic

New Relic is an observability platform that helps you build better software. You can bring in data from any digital source so that you can fully understand your system and how to improve it.

- `@official` [Learn New Relic](https://learn.newrelic.com/)

#### Unit Testing

Unit testing is where individual **units** (modules, functions/methods, routines, etc.) of software are tested to ensure their correctness. This low-level testing ensures smaller components are functionally sound while taking the burden off of higher-level tests. Generally, a developer writes these tests during the development process and they are run as automated tests.

- `@article` [Unit Testing Tutorial](https://www.guru99.com/unit-testing-guide.html)
- `@video` [What is Unit Testing?](https://youtu.be/3kzHmaeozDI)

#### Integration Testing

Integration Testing is a type of testing where software modules are integrated logically and tested as a group. A typical software project consists of multiple software modules coded by different programmers. This testing level aims to expose defects in the interaction between these software modules when they are integrated. Integration Testing focuses on checking data communication amongst these modules.

- `@article` [Integration Testing Tutorial](https://www.guru99.com/integration-testing.html)

#### What and why use them?

Messaging systems solve the problem of tight coupling between systems. Instead of one service directly calling another, it sends a message to a broker, and the consumer reads it when ready. This improves reliability, scalability, and flexibility, especially when producers and consumers operate at different speeds or scales.

### Testing

Testing in data engineering involves verifying that pipelines, transformations, and data outputs behave correctly. This includes unit tests for individual functions, integration tests for pipeline components, and data quality tests that validate the output data itself. A well-tested pipeline catches regressions early and builds confidence in the reliability of data delivered to consumers.

- `@article` [What is Software Testing?](https://www.guru99.com/software-testing-introduction-importance.html)
- `@article` [Testing Pyramid](https://www.browserstack.com/guide/testing-pyramid-for-test-automation)

#### End-to-End Testing

End-to-end or (E2E) testing is a form of testing used to assert your entire application works as expected from start to finish or "end-to-end". E2E testing differs from unit testing in that it is completely decoupled from the underlying implementation details of your code. It is typically used to validate an application in a way that mimics the way a user would interact with it.

- `@article` [End to End Testing](https://microsoft.github.io/code-with-engineering-playbook/automated-testing/e2e-testing/)
- `@article` [End to End Testing: Importance, Process, Best Practices & Frameworks](https://testgrid.io/blog/end-to-end-testing-a-detailed-guide/)

#### Async vs Sync Communication

Synchronous communication means the sender waits for a response before continuing. Asynchronous communication means the sender sends a message and continues without waiting. Messaging systems enable asynchronous communication, which is better suited for high-throughput pipelines where blocking would create bottlenecks.

- `@article` [Synchronous And Asynchronous Data Transmission: The Differences And How to Use Them](https://www.computer.org/publications/tech-news/trends/synchronous-asynchronous-data-transmission)
- `@article` [Synchronous vs Asynchronous Communication: What’s the Difference?](https://www.getguru.com/reference/synchronous-vs-asynchronous-communication)

#### Functional Testing

Functional testing is a type of software testing that validates the software system against the functional requirements/specifications. The purpose of functional tests is to test each function of the software application by providing appropriate input and verifying the output against the functional requirements.

- `@article` [What is Functional Testing? Types & Examples](https://www.guru99.com/functional-testing.html)
- `@article` [Functional Testing : A Detailed Guide](https://www.browserstack.com/guide/functional-testing)

#### Messages vs Streams

Messages are discrete, individual units of data sent from a producer to a consumer. Streams are continuous, ordered sequences of data that consumers process in real time or replay from a position. Systems like RabbitMQ focus on message delivery, while Apache Kafka is designed around the stream abstraction and supports log retention and replay.

#### A/B Testing

A/B testing is a way to compare two versions of something to see which one works better. You split your audience into two groups, one sees version A, the other sees version B — and then you measure which version gets better results, like more clicks, sales, or sign-ups. This helps you make decisions based on real data instead of guesses.

- `@article` [A software engineer's guide to A/B testing](https://posthog.com/product-engineers/ab-testing-guide-for-engineers)
- `@video` [A/B Testing for Beginners](https://www.youtube.com/watch?v=VpTlNRUcIDo)

#### Best Practices

Best practices for messaging systems include designing idempotent consumers to handle duplicate delivery, setting appropriate retention and replication policies, monitoring consumer lag, and planning for schema evolution. Dead-letter queues are used to handle messages that fail processing repeatedly without losing them.

- `@article` [Best Practices for Message Queue Architecture](https://abhishek-patel.medium.com/best-practices-for-message-queue-architecture-f69d47e3565)

### Messaging Systems

Messaging systems, commonly known as messaging queues, make it possible for applications to communicate asynchronously, by sending messages to each other via a queue. A message queue provides temporary storage between the sender and the receiver so that the sender can keep operating without interruption when the destination program is busy or not connected.

- `@article` [Messaging Queues](https://aws.amazon.com/message-queue/)
- `@article` [Messaging Queues Tutorial](https://www.tutorialspoint.com/inter_process_communication/inter_process_communication_message_queues.htm)

#### Load Testing

Load Testing is a type of Performance Testing that determines the performance of a system, software product, or software application under real-life-based load conditions. Load testing determines the behavior of the application when multiple users use it at the same time. It is the response of the system measured under varying load conditions.

- `@article` [Load testing and Best Practices](https://loadninja.com/load-testing/)

#### Smoke Testing

Smoke Testing is a software testing process that determines whether the deployed software build is stable or not. Smoke testing is a confirmation for QA team to proceed with further software testing. It consists of a minimal set of tests run on each build to test software functionalities.

- `@article` [Smoke Testing | Software Testing](https://www.guru99.com/smoke-testing.html)

### Infrastructure as Code - IaC

Infrastructure as Code (IaC) is the practice of managing and provisioning infrastructure through machine-readable configuration files rather than manual processes. Tools like Terraform, AWS CloudFormation, and Pulumi allow teams to define infrastructure declaratively and version it in Git. IaC makes infrastructure reproducible, auditable, and easier to manage at scale.

- `@article` [What is Infrastructure as Code?](https://aws.amazon.com/what-is/iac/)
- `@article` [Infrastructure as Code](https://en.wikipedia.org/wiki/Infrastructure_as_code)
- `@video` [What is Infrastructure as Code?](https://www.youtube.com/watch?v=zWw2wuiKd5o)

#### Declarative vs Imperative

When it comes to Infrastructure as Code (IaC), there are two fundamental styles: imperative and declarative.

In **imperative IaC**, you specify a list of steps the IaC tool should follow to provision a new resource. You tell your IaC tool how to create each environment using a sequence of command imperatives. Imperative IaC can offer more flexibility as it allows you to dictate each step. However, this can result in increased complexity. Popular imperative IaC tools are Chef and Puppet

In **declarative IaC**, you specify the name and properties of the infrastructure resources you wish to provision, and then the IaC tool figures out how to achieve that end result on its own. You declare to your IaC tool what you want, but not how to get there. Declarative IaC, while less flexible, tends to be simpler and more manageable. Terraform is the most popular declarative IaC tool

- `@article` [Infrastructure as Code: From Imperative to Declarative and Back Again](https://thenewstack.io/infrastructure-as-code-from-imperative-to-declarative-and-back-again/)
- `@article` [Declarative vs Imperative Programming for Infrastructure as Code (IaC)](https://www.copado.com/resources/blog/declarative-vs-imperative-programming-for-infrastructure-as-code-iac)

#### Idempotency

Idempotency is a crucial concept in IaC. An idempotent operation produces the same result regardless of how many times it’s executed. In the context of IaC, this means that applying the same configuration multiple times should not change the end state of the system. The role of idempotency in IaC scripts is to ensure consistency and prevent unintended side effects. For example, if a script to create a virtual machine (VM) is run twice, it should not create two VMs. Instead, it should recognize that the VM already exists and take no action.

- `@article` [Why idempotence was important to DevOps](https://dev.to/startpher/why-idempotence-was-important-to-devops-2jn3)
- `@article` [Idempotency: The Secret to Seamless DevOps and Infrastructure](https://medium.com/@tiwari.sushil/idempotency-the-secret-to-seamless-devops-and-infrastructure-bf22e63e1be5)

#### Reusability

One of the goals of Infrastructure as Code (IaC) is to create modular, standardized units of code—like modules or templates that can be used across multiple projects, environments, and teams, embodying the "Don't Repeat Yourself" (DRY) principle. This approach significantly boosts efficiency, consistency, and maintainability, as it allows for rapid deployment of identical infrastructure patterns, enforces organizational standards, simplifies complex setups, and improves collaboration by providing shared, tested building blocks for infrastructure management.

- `@article` [What is Infrastructure as Code (IaC)?](https://www.redhat.com/en/topics/automation/what-is-infrastructure-as-code-iac)

#### Environmental Management

Environmental management, or Environment as Code (EaC) takes the concept of Infrastructure as Code (IaC) one step further. EaC applies DevOps principles to manage and automate entire software environments—including infrastructure, applications, and configurations—using code, making them reproducible, versionable, and reliable. It extends IaC by focusing not just on the underlying servers and networks but on the complete, connected system of services and applications that run on top of it. This approach helps increase efficiency, speeds up deployments, and provides a consistent, auditable process for creating and managing development, testing, and production environments.

- `@article` [EWhat Is Environment as Code (EaaC)?](https://www.bunnyshell.com/blog/what-is-environment-as-code-eaac/)

### Data Analytics

Data analytics is the process of examining datasets to draw conclusions and support decision-making. It covers a spectrum from descriptive analytics (what happened) to diagnostic (why it happened), predictive (what might happen), and prescriptive (what to do). Data engineers build the infrastructure that makes analytics possible by ensuring clean, accessible, and timely data.

- `@course` [Introduction to Data Analytics](https://www.coursera.org/learn/introduction-to-data-analytics)
- `@article` [The 4 Types of Data Analysis: Ultimate Guide](https://careerfoundry.com/en/blog/data-analytics/different-types-of-data-analysis/)
- `@video` [Descriptive vs Diagnostic vs Predictive vs Prescriptive Analytics: What's the Difference?](https://www.youtube.com/watch?v=QoEpC7jUb9k)
- `@video` [Types of Data Analytics](https://www.youtube.com/watch?v=lsZnSgxMwBA)

### Business Intelligence

Business intelligence (BI) refers to the tools and processes used to collect, analyze, and visualize business data to support decisions. BI platforms connect to data warehouses and allow business users to build reports and dashboards without writing code. Common BI tools include Tableau, Power BI, Looker, and Streamlit.

- `@roadmap` [Visit the Dedicated BI Analyst Roadmap](https://roadmap.sh/bi-analyst)
- `@article` [What is business intelligence (BI)?](https://www.ibm.com/think/topics/business-intelligence)
- `@article` [Business intelligence: A complete overview](https://www.tableau.com/business-intelligence/what-is-business-intelligence)
- `@video` [What is business intelligence?](https://www.youtube.com/watch?v=l98-BcB3UIE)

### Authentication vs Authorization

Authentication and authorization are popular terms in modern computer systems that often confuse people. **Authentication** is the process of confirming the identity of a user or a device (i.e., an entity). During the authentication process, an entity usually relies on some proof to authenticate itself, i.e. an authentication factor. In contrast to authentication, **authorization** refers to the process of verifying what resources entities (users or devices) can access, or what actions they can perform, i.e., their access rights.

- `@article` [Basic Authentication](https://roadmap.sh/guides/basic-authentication)
- `@article` [What is Authentication vs Authorization?](https://auth0.com/intro-to-iam/authentication-vs-authorization)

### Encryption

Encryption is used to protect data from being stolen, changed, or compromised and works by scrambling data into a secret code that can only be unlocked with a unique digital key. Encrypted data can be protected while at rest on computers or in transit between them, or while being processed, regardless of whether those computers are located on-premises or are remote cloud servers.

- `@article` [What is Encryption?](https://cloud.google.com/learn/what-is-encryption)
- `@video` [What is Encryption?](https://www.youtube.com/watch?v=9chKCUQ8_VQ)

### Tokenization

Tokenization replaces sensitive data values with non-sensitive placeholders called tokens. The original value is stored securely in a token vault, and the token can be used in systems that do not need the actual data. Tokenization is used to protect payment card numbers, personal identifiers, and other sensitive field

- `@article` [Explaining Tokens — the Language and Currency of AI](https://blogs.nvidia.com/blog/ai-tokens-explained/)

### Data Masking

Data masking is a process that creates a copy of real data but replaces sensitive information with false but realistic-looking data, preserving the format and structure of the original data for non-production uses like software testing, training, and development. The goal is to protect confidential information and ensure compliance with data protection regulations by preventing unauthorized access to real sensitive data without compromising the usability of the data for other business functions.

- `@article` [Data masking](https://en.wikipedia.org/wiki/Data_masking)
- `@article` [What is data masking?](https://aws.amazon.com/what-is/data-masking/)

### Data Obfuscation

Statistical data obfuscation involves altering the values of sensitive data in a way that preserves the statistical properties and relationships within the data. It ensures that the masked data maintains the overall distribution, patterns, and correlations of the original data for accurate statistical analysis. Statistical data obfuscation techniques include applying mathematical functions or perturbation algorithms to the data.

#### Data Quality

Data quality refers to how well data meets the requirements for its intended use in terms of accuracy, completeness, consistency, timeliness, and validity. Poor data quality leads to incorrect analysis and poor decisions. Data engineers implement quality checks at ingestion and transformation stages to catch and prevent data issues.

#### Data Lineage

**Data Lineage** refers to the life-cycle of data, including its origins, movements, characteristics and quality. It's a critical component in Data Engineering for tracking the journey of data through every process in a pipeline, from raw input to model output. Data lineage helps in maintaining transparency, ensuring compliance, and facilitating data debugging or tracing data related bugs. It provides a clear representation of data sources, transformations, and dependencies thereby aiding in audits, governance, or reproduction of machine learning models.

- `@article` [What is Data Lineage? - IBM](https://www.ibm.com/topics/data-lineage)

### Reverse ETL

Reverse ETL is the process of extracting data from a data warehouse, transforming it to fit the requirements of operational systems, and then loading it into those other systems. This approach contrasts with traditional ETL, where data is extracted from operational systems, transformed, and loaded into a data warehouse.

- `@video` [What is Reverse ETL?](https://www.youtube.com/watch?v=DRAGfc5or2Y)

#### Metadata Management

Metadata management involves capturing, storing, and governing information about data assets, including their structure, origin, ownership, and usage. A metadata catalog makes data discoverable and helps teams understand what data is available and how it is defined. Tools like Apache Atlas, DataHub, and Alation are used for metadata management.

#### Data Interoperability

Data interoperability is the ability of diverse systems and applications to access, exchange, and cooperatively use data in a coordinated and meaningful way, even across organizational boundaries. It ensures that data can flow freely, maintaining its integrity and context, allowing for improved efficiency, collaboration, and decision-making by breaking down data silos. Achieving data interoperability often relies on data standards, metadata, and common data elements to define how data is collected, formatted, and interpreted.

- `@article` [Data Interoperability](https://www.sciencedirect.com/topics/computer-science/data-interoperability)
- `@article` [What is Data Interoperability? – Exploring the Process and Benefits](https://www.codelessplatforms.com/blog/what-is-data-interoperability/)

#### ETL vs Reverse ETL

ETL (Extract, Transform, Load) moves data from operational systems into a data warehouse for analysis. Reverse ETL goes in the opposite direction, syncing processed data from the warehouse back into operational tools like Salesforce, HubSpot, or Intercom. The two patterns are complementary and together form a complete data activation workflow.

- `@article` [What is ETL?](https://www.snowflake.com/guides/what-etl)
- `@article` [ETL vs Reverse ETL vs Data Activation](https://airbyte.com/data-engineering-resources/etl-vs-reverse-etl-vs-data-activation)
- `@article` [ETL vs Reverse ETL: An Overview, Key Differences, & Use Cases](https://portable.io/learn/etl-vs-reverse-etl)

#### Data Quality

Data quality refers to the degree to which a dataset is accurate, complete, consistent, relevant, and timely, making it fit for its intended use. High-quality data is reliable and trustworthy, enabling better decision-making, accurate analysis, and effective strategies, while poor data quality can lead to flawed insights, wasted resources, and negative consequences for an organization.

- `@article` [What is Data Quality?](https://www.ibm.com/think/topics/data-quality)

#### Reverse ETL Usecases

Common use cases for reverse ETL include syncing customer health scores to a CRM, pushing segmented user lists to a marketing automation platform, and sending product usage data to customer success tools. It enables business teams to act on insights derived in the data warehouse without needing access to it directly.

#### GDPR

GDPR (General Data Protection Regulation) is a data privacy law enacted by the European Union that governs how personal data of EU residents is collected, stored, processed, and shared. It grants individuals rights over their data, including the right to access, correct, and delete it. Data engineers must design systems that support these rights and comply with GDPR requirements such as data minimization and purpose limitation.

- `@official` [GDPR](https://gdpr-info.eu/)
- `@article` [What is GDPR Compliance in Web Application and API Security?](https://probely.com/blog/what-is-gdpr-compliance-in-web-application-and-api-security/)

#### ECPA

The Electronic Communications Privacy Act (ECPA) is a US federal law that regulates government access to electronic communications and stored data. It sets rules for when law enforcement can intercept communications or compel disclosure of stored data from service providers. Data engineers working with communication data must be aware of ECPA requirements when designing storage and access controls.

- `@official` [California Consumer Privacy Act (CCPA)](https://oag.ca.gov/privacy/ccpa)
- `@article` [What is the California Consumer Privacy Act (CCPA)?](https://www.ibm.com/think/topics/ccpa-compliance)
- `@video` [What is the California Consumer Privacy Act? | CCPA Explained?](https://www.youtube.com/watch?v=dpzsAgrDAO4)

#### EU AI Act

The Artificial Intelligence Act of the European Union, also known as the EU AI Act, is a comprehensive regulatory framework that is established to ensure safety and that fundamental human rights are upheld in the use of AI technologies. It governs the development and/or use of AI in the European Union. The act takes a risk-based approach to regulation, applying different rules to AI systems according to the risk they pose.

Considered the world's first comprehensive regulatory framework for AI, the EU AI Act prohibits some AI uses outright and implements strict governance, risk management and transparency requirements for others.

- `@official` [The EU AI Act Explorer](https://artificialintelligenceact.eu/ai-act-explorer/)
- `@article` [AI Act - European Commission](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- `@article` [Artificial Intelligence Act](https://en.wikipedia.org/wiki/Artificial_Intelligence_Act)
- `@video` [The EU AI Act Explained](https://www.youtube.com/watch?v=s_rxOnCt3HQ)

## Hadoop Ecosystem

#### HDFS

HDFS (Hadoop Distributed File System) is Hadoop’s primary storage system. It is designed to reliably store data across a cluster of machines. Its architecture is set up for this type of access to large datasets and is optimized for fault tolerance, scalability, and data locality.

- `@official` [HDFS Architecture Guide](https://hadoop.apache.org/docs/r1.2.1/hdfs_design.html)
- `@article` [Hadoop Distributed File System (HDFS)](https://www.databricks.com/glossary/hadoop-distributed-file-system-hdfs)
- `@article` [What is Hadoop Distributed File System (HDFS)?](https://www.ibm.com/think/topics/hdfs)

#### YARN

Apache Hadoop YARN (Yet Another Resource Negotiator) is the part of Hadoop that manages resources and runs jobs on a cluster. It has a ResourceManager that controls all cluster resources and an ApplicationMaster for each job that schedules and runs tasks. YARN lets different tools like MapReduce and Spark share the same cluster, making it more efficient, flexible, and reliable.

- `@video` [Hadoop Yarn Tutorial](https://www.youtube.com/watch?v=6bIF9VwRwE0)

#### MapReduce

MapReduce is a prominent data processing technique used by Data Analysts around the world. It allows them to handle large data sets with complex, unstructured data efficiently. MapReduce breaks down a big data problem into smaller sub-tasks (Map) and then takes those results to create an output in a more usable format (Reduce). This technique is particularly useful in conducting exploratory analysis, as well as in handling big data operations such as text processing, graph processing, or more complicated machine learning algorithms.

- `@article` [MapReduce](https://www.databricks.com/glossary/mapreduce)
- `@article` [What is Apache MapReduce?](https://www.ibm.com/topics/mapreduce)

## Common Tools

#### Apache Kafka

Apache Kafka is an open-source stream-processing software platform developed by LinkedIn and donated to the Apache Software Foundation. It is written in Scala and Java and operates based on a message queue, designed to handle real-time data feeds. Kafka functions as a kind of message broker service in between the data producers and the consumers, facilitating efficient transmission of data. It can be viewed as a durable message broker where applications can process and reprocess streamed data. Kafka is a highly scalable and fault-tolerant system which ensures data delivery without loss.

- `@official` [Apache Kafka Docs](https://kafka.apache.org/43/getting-started/introduction/)
- `@article` [Kafka Streams Confluent](https://kafka.apache.org/documentation/streams/)
- `@video` [Apache Kafka Fundamentals](https://www.youtube.com/watch?v=B5j3uNBH8X4)
- `@video` [Kafka in 100 Seconds](https://www.youtube.com/watch?v=uvb00oaa3k8)

#### RabbitMQ

RabbitMQ is an open-source message broker that implements the AMQP protocol. It routes messages between producers and consumers using exchanges and queues, supporting patterns like publish/subscribe, work queues, and routing. RabbitMQ is used for task queues, service-to-service communication, and event notification systems.

- `@official` [RabbitMQ Tutorials](https://www.rabbitmq.com/getstarted.html)
- `@video` [RabbitMQ Tutorial - Message Queues and Distributed Systems](https://www.youtube.com/watch?v=nFxjaVmFj5E)
- `@video` [RabbitMQ in 100 Seconds](https://m.youtube.com/watch?v=NQ3fZtyXji0)

#### AWS SQS

Amazon Simple Queue Service (Amazon SQS) offers a secure, durable, and available hosted queue that lets you integrate and decouple distributed software systems and components. Amazon SQS offers common constructs such as dead-letter queues and cost allocation tags. It provides a generic web services API that you can access using any programming language that the AWS SDK supports.

- `@official` [Amazon Simple Queue Service](https://aws.amazon.com/sqs/)
- `@official` [What is Amazon Simple Queue Service?](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)

#### AWS SNS

Amazon SNS (Simple Notification Service) is a fully managed pub/sub messaging service from AWS. It allows a single message to be sent to multiple subscribers simultaneously through topics. SNS is commonly used alongside SQS to fan out messages to multiple queues or trigger downstream processing in Lambda functions and data pipelines.

- `@official` [Amazon Simple Notification Service (SNS)](http://aws.amazon.com/sns/)
- `@official` [Send Fanout Event Notifications](https://aws.amazon.com/getting-started/hands-on/send-fanout-event-notifications/)
- `@article` [What is Pub/Sub Messaging?](https://aws.amazon.com/what-is/pub-sub-messaging/)

## Common Tools

#### Terraform

Terraform is an open-source infrastructure as code (IaC) tool developed by HashiCorp, used to define, provision, and manage cloud and on-premises infrastructure using declarative configuration files. It supports multiple cloud providers like AWS, Azure, and Google Cloud, as well as various services and platforms, enabling infrastructure automation across diverse environments. Terraform's state management and modular structure allow for efficient scaling, reusability, and version control of infrastructure. It is widely used for automating infrastructure provisioning, reducing manual errors, and improving infrastructure consistency and repeatability.

- `@roadmap` [Visit Dedicated Terraform Roadmap](https://roadmap.sh/terraform)
- `@course` [Complete Terraform Course](https://www.youtube.com/watch?v=7xngnjfIlK4)
- `@official` [Terraform Documentation](https://www.terraform.io/docs)
- `@official` [Terraform Tutorials](https://learn.hashicorp.com/terraform)
- `@article` [How to Scale Your Terraform Infrastructure](https://thenewstack.io/how-to-scale-your-terraform-infrastructure/)
- `@feed` [Explore top posts about Terraform](https://app.daily.dev/tags/terraform?ref=roadmapsh)

#### OpenTofu

OpenTofu is an infrastructure as code tool that lets you define both cloud and on-prem resources in human-readable configuration files that you can version, reuse, and share. You can then use a consistent workflow to provision and manage all of your infrastructure throughout its lifecycle. OpenTofu can manage low-level components like compute, storage, and networking resources, as well as high-level components like DNS entries and SaaS features.

- `@official` [OpenTofu Docs](https://opentofu.org/docs/)
- `@video` [OpenWhat is OpenTofu ?Explained with Demo](https://www.youtube.com/watch?v=6eHV63BVqmA)

#### AWS CDK

The AWS Cloud Development Kit (AWS CDK) is an open-source software development framework used to provision cloud infrastructure resources in a safe, repeatable manner through AWS CloudFormation. AWS CDK offers the flexibility to write infrastructure as code in popular languages like Python, Java, Go, and C#.

- `@course` [AWS CDK Crash Course for Beginners](https://www.youtube.com/watch?v=D4Asp5g4fp8)
- `@official` [AWS CDK](https://aws.amazon.com/cdk/)
- `@official` [AWS CDK Documentation](https://docs.aws.amazon.com/cdk/index.html)
- `@opensource` [AWS CDK Examples](https://github.com/aws-samples/aws-cdk-examples)
- `@feed` [Explore top posts about AWS](https://app.daily.dev/tags/aws?ref=roadmapsh)

#### Google Deployment  Mgr.

Google Cloud Deployment Manager is an infrastructure deployment service that automates the creation and management of Google Cloud resources. It provides users with flexible template and configuration files to create deployments that have a variety of Google Cloud services, such as Cloud Storage, Compute Engine, and Cloud SQL, configured to work together.

Important, Google Deployment Manager will reach end of support on 31 December 2025. An alternative to this tool is **Google Infrastructure Manager**. Infrastructure Manager (Infra Manager) automates the deployment and management of Google Cloud infrastructure resources using Terraform. Infra Manager allows users to deploy programmatically to Google Cloud, allowing to use this service rather than maintaining a different toolchain to work with Terraform on Google Cloud.

- `@official` [Infrastructure Manager Overview](https://cloud.google.com/infrastructure-manager/docs/overview)
- `@official` [Google Cloud Deployment Manager documentation](https://cloud.google.com/deployment-manager/docs)

## BI Tools

#### Microsoft Power BI

Microsoft Power BI is a business intelligence and data visualization platform from Microsoft. It connects to a wide range of data sources and allows users to build interactive dashboards and reports. Power BI integrates tightly with the Microsoft ecosystem including Azure and Excel.

- `@official` [Power BI](https://www.microsoft.com/en-us/power-platform/products/power-bi)
- `@video` [Power BI for beginners](https://www.youtube.com/watch?v=NNSHu0rkew8)

#### Streamlit

Streamlit is a free and open-source framework to rapidly build and share machine learning and data science web apps. It is a Python-based library specifically designed for data and machine learning engineers. Data scientists or machine learning engineers are not web developers and they're not interested in spending weeks learning to use these frameworks to build web apps. Instead, they want a tool that is easier to learn and to use, as long as it can display data and collect needed parameters for modeling.

- `@official` [Streamlit Docs](https://docs.streamlit.io/)
- `@video` [EStreamlit Explained: Python Tutorial for Data Scientists](https://www.youtube.com/watch?v=c8QXUrvSSyg)

#### Tableu

Tableau is a powerful data visualization tool utilized extensively by data analysts worldwide. Its primary role is to transform raw, unprocessed data into an understandable format without any technical skills or coding. Data analysts use Tableau to create data visualizations, reports, and dashboards that help businesses make more informed, data-driven decisions. They also use it to perform tasks like trend analysis, pattern identification, and forecasts, all within a user-friendly interface. Moreover, Tableau's data visualization capabilities make it easier for stakeholders to understand complex data and act on insights quickly.

- `@official` [Tableau](https://www.tableau.com/en-gb)
- `@video` [What is Tableau?](https://www.youtube.com/watch?v=NLCzpPRCc7U)

#### Looker

Looker is a Google cloud-based business intelligence and data analytics platform. It allows users to explore, analyze, and visualize data to gain insights and make data-driven decisions. Looker is known for its ability to connect to various data sources, create custom dashboards, and generate reports. It also facilitates the integration of analytics, visualizations, and relevant information into business processes.

- `@official` [Looker business intelligence platform embedded analytics](https://cloud.google.com/looker)
- `@video` [What is Looker?](https://www.youtube.com/watch?v=EmkNPAzla0Y&pp=0gcJCfwAo7VqN5tD)

## Tools

#### Hightouch

Hightouch is a reverse ETL and AI platform crafted for marketing and personalization, allowing companies to uncover insights, execute campaigns, and develop AI agents using their data. It features an AI Decisioning Platform for lifecycle marketing and a Composable Customer Data Platform (CDP) that is adaptable, secure, and quick to deploy, built on top of a data warehouse.

- `@official` [Hightouch Docs](https://hightouch.com/docs)
- `@video` [What is Hightouch? - The Data Activation Platform](https://www.youtube.com/watch?v=vMm87-MC7og)

#### Census

Census is a reverse ETL platform that synchronizes data from a data warehouse to various business applications and SaaS apps like Salesforce and Hubspot. It's a crucial part of the modern data stack, enabling businesses to operationalize their data by making it available in the tools where teams work, like CRMs, marketing platforms, and more.

- `@official` [Census Documentation](https://developers.getcensus.com/getting-started/introduction)
- `@article` [A starter guide to reverse ETL with Census](https://www.getcensus.com/blog/starter-guide-for-first-time-census-users)
- `@video` [How to "Reverse ETL" with Census](https://www.youtube.com/watch?v=XkS7DQFHzbA)

#### Segment

Segment is an analytics platform that provides a single API for collecting, storing, and routing customer data from various sources. With Segment, data engineers can easily add analytics tracking to their app, without having to integrate with multiple analytics tools individually. Segment acts as a single point of integration, allowing developers to send data to multiple analytics tools with a single API.

- `@official` [flutter_segment](https://pub.dev/packages/flutter_segment)

## Data and AI Regulations

### Machine Learning

Machine learning, a subset of artificial intelligence, is an indispensable tool in the hands of a data analyst. It provides the ability to automatically learn, improve from experience and make decisions without being explicitly programmed. In the context of a data analyst, machine learning contributes significantly in uncovering hidden insights, recognising patterns or making predictions based on large amounts of data. Through the use of varying algorithms and models, data analysts are able to leverage machine learning to convert raw data into meaningful information, making it a critical concept in data analysis.

- `@roadmap` [Visit the Dedicated Java Roadmap](https://roadmap.sh/machine-learning)
- `@article` [What is Machine Learning (ML)?](https://www.ibm.com/topics/machine-learning)
- `@video` [What is Machine Learning?](https://www.youtube.com/watch?v=9gGnTQTYNaE)

### MLOps

MLOps is a practice for collaboration and communication between data scientists and operations professionals to help manage production ML lifecycle. It is a set of best practices that aims to automate the ML lifecycle, including training, deployment, and monitoring. MLOps helps organizations to scale ML models and deliver business value faster.

- `@roadmap` [Visit the Dedicated MLOps Roadmap](https://roadmap.sh/mlops)
