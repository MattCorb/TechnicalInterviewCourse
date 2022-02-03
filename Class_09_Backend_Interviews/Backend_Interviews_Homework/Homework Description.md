# Backend Interview Homework

- Write down your answers for the following questions and then paste your answers into the "Backend Assignment" quiz on learningsuite. 

    1. What is CI/CD? What are some good CI/CD practices?
    CI/CD is a method to frequently deliver apps to customers by introducing automation into the stages of app development. The main concepts attributed to CI/CD are continuous integration, continuous delivery, and continuous deployment. CI/CD is a solution to the problems integrating new code can cause for development and operations teams (AKA "integration hell").

    Specifically, CI/CD introduces ongoing automation and continuous monitoring throughout the lifecycle of apps, from integration and testing phases to delivery and deployment. Taken together, these connected practices are often referred to as a "CI/CD pipeline" and are supported by development and operations teams working together in an agile way with either a DevOps or site reliability engineering (SRE) approach.
        Commit early, commit often. ...
        Keep the builds green. ...
        Build only once. ...
        Streamline your tests. ...
        Clean your environments. ...
        Make it the only way to deploy to production. ...
        Monitor and measure your pipeline. ...
        Make it a team effort.

    2. What is and what are the benefits of using a binary tree?
    A binary tree is a tree data structure composed of nodes, each of which has at most, two children, referred to as left and right nodes. The tree starts off with a single node known as the root.

    Each node in the tree contains the following:
        Data
        Pointer to the left child
        Pointer to the right child

        In case of a leaf node, the pointers to the left and right child point to null.
    
    binary trees are mainly used for searching and sorting as they provide a means to store data hierarchically. Some common operations that can be conducted on binary trees include insertion, deletion, and traversal

    3. What does SOLID mean?
    S - Single-responsiblity Principle
        A class should have one and only one reason to change, meaning that a class should have only one job.
    O - Open-closed Principle
        Objects or entities should be open for extension but closed for modification.
    L - Liskov Substitution Principle
        Let q(x) be a property provable about objects of x of type T. Then q(y) should be provable for objects y of type S where S is a subtype of T.
    I - Interface Segregation Principle
        A client should never be forced to implement an interface that it doesn’t use, or clients shouldn’t be forced to depend on methods they do not use.
    D - Dependency Inversion Principle
        Entities must depend on abstractions, not on concretions. It states that the high-level module must not depend on the low-level module, but they should depend on abstractions.

    4. What is abstraction? Give an example.
        One way to think of abstraction is as synonymous with generalization. You take something and separate the idea from its implementation. If, for instance, you wanted to create a program to multiply five times six, you wouldn't build an application to only multiply those two numbers. Instead, you'd create a program capable of multiplying any two numbers. To put it another way, abstraction is a way of thinking about a function's specific use as separate from its more generalized purpose. Thinking this way lets you create flexible, scalable, and adaptable functions and programs.

        An API is an intermediary that allows applications to communicate but abstracts the details of what is being communicated and how—simplifying the process of application-to-application communication and providing a level of security.

    5. What is a singleton? Give an example of when to use this principle.

        a Singleton Class is a Class that has, and can only have, only one instance. This is useful when exactly one object is needed to coordinate actions across the system.

        State patterns to preserve the state of an application or website.