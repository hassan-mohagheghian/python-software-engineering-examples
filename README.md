# Python Software Engineering Examples

A practical collection of small Python examples for learning software engineering
concepts step by step.

The repository starts with Python fundamentals, then moves into object-oriented
programming, SOLID principles, design patterns, and system design topics such as
caching, rate limiting, message queues, database replication, and microservices.

Each example is intentionally small and self-contained so it can be read, run,
and modified without needing a full application setup.

## Repository Structure

```text
PSE_001_Input_Output/          Input and output examples
PSE_002_Modules/              Module-level behavior and shared state
PSE_003_Functions/             Function basics and reusable behavior
PSE_004_Classes/              Class attributes and access conventions
PSE_005_OOP/                  Object-oriented programming concepts
PSE_006_SOLID_Principles/   SOLID principle examples
PSE_007_Design_Patterns/       Common object-oriented design patterns
PSE_008_System_Design/         Backend and distributed-system concepts
```

Folder names use this convention:

```text
PSE_<TOPIC_ABBREVIATION>_<ORDER>_<TOPIC_NAME>
```

`PSE` means Python Software Engineering. The topic abbreviation makes folders
quick to scan, and the number keeps the learning path ordered.

## Topics Covered

### Python Basics

- Reading one or more lines from standard input
- Working with simple log-style input
- Reading and writing text files
- Importing custom modules
- Sharing global variables between modules
- Defining and calling functions
- Public, protected, and private attribute conventions

### Object-Oriented Programming

- Abstraction
- Encapsulation
- Inheritance
- Polymorphism
- Composition
- Dependency Injection
- Association
- Aggregation
- Delegation
- Mixin
- Interface
- Abstract Class
- Duck Typing
- Protocol
- Factory Method
- Template Method
- State
- Value Object
- Entity
- Repository

### SOLID Principles

- SRP - Single Responsibility Principle
- OCP - Open/Closed Principle
- LSP - Liskov Substitution Principle
- ISP - Interface Segregation Principle
- DIP - Dependency Inversion Principle

### Design Patterns

- Strategy Pattern
- Factory Method Pattern
- Abstract Factory Pattern
- Adapter Pattern
- Facade Pattern
- Decorator Pattern
- Builder Pattern
- Proxy Pattern
- Composite Pattern
- Bridge Pattern
- Flyweight Pattern

### System Design

- Client-Server Model
- HTTP and REST
- DNS and Load Balancing
- GeoDNS and Regional Load Balancing
- Caching System
- Rate Limiting System
- Message Queue
- Database Replication
- Microservices Architecture

## How To Use

Run any example directly with Python:

```bash
python PSE_FN_003_Functions/01_basic_functions.py
python PSE_DP_007_Design_Patterns/01_strategy_pattern.py
python PSE_SD_008_System_Design/08_microservices_architecture/08_microservices_architecture.py
```

Most files include:

- a short explanation at the top
- a small implementation of the concept
- a `main()` function that demonstrates the behavior

The examples are educational simulations. System design examples use in-memory
data structures instead of real servers, databases, queues, or network calls so
the core idea stays easy to inspect.

## Requirements

The project uses only the Python standard library.

The current `pyproject.toml` requires:

```text
Python >= 3.14
```

Many examples may also work on earlier Python 3 versions, but the repository is
configured for Python 3.14 or newer.

## Notes

- This is a learning repo, not a production framework.
- Examples favor clarity over completeness.
- System design examples are simplified models of real-world architectures.
- Folder numbering is for learning order, not Python package naming.
- New topics should stay small, runnable, and focused on one concept.

## Contributing

Contributions and improvements are welcome. Good additions include:

- clearer explanations
- more focused examples
- missing design patterns
- additional system design topics
- small corrections or naming fixes

## License

This repository is provided for educational purposes. See [LICENSE](LICENSE) for
details.
