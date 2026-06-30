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
001_IO_Input_Output/        Input and output examples
002_Modules/                Module-level behavior and shared state
003_Classes/                Class attributes and access conventions
004_OOP/                    Object-oriented programming concepts
005_SOLID_Principles/       SOLID principle examples
006_Design_Patterns/        Common object-oriented design patterns
007_System_Design/          Backend and distributed-system concepts
```

Numbered folders keep the learning path ordered. Some folder names start with
numbers for readability in the file browser, so they are meant to be run as
example files rather than imported as normal Python packages.

## Topics Covered

### Python Basics

- Reading one or more lines from standard input
- Working with simple log-style input
- Reading and writing text files
- Sharing global variables between modules
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
python 006_Design_Patterns/01_strategy_pattern.py
python 007_System_Design/08_microservices_architecture/08_microservices_architecture.py
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
