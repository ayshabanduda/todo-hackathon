# Research: Todo In-Memory Python CLI App

## Decision: CLI Framework
- **Decision**: Use Python's built-in `argparse` module.
- **Rationale**: `argparse` is part of the standard library, meeting the requirement of minimal dependencies for Phase I. It provides robust command-line parsing, automatic help generation, and sub-command support.
- **Alternatives considered**: `click` (rejected to avoid external dependencies in Phase I), `sys.argv` (rejected as too low-level and error-prone for multiple commands).

## Decision: State Management
- **Decision**: Use a Singleton or Dependency Injection pattern to manage a central `TaskRepository` containing a list of `Task` dictionaries.
- **Rationale**: Ensures a single source of truth for the in-memory state during the CLI execution. Although the process restarts each time in a traditional CLI, this structure allows for easier transition to persistent storage in later phases.
- **Alternatives considered**: Global variables (rejected for lack of testability and structure).

## Decision: Project Layout
- **Decision**: Follow the `src` layout with `models`, `services`, and `cli` modules.
- **Rationale**: Separates concerns (data, logic, interface) and aligns with the project constitution's requirement for structured development.
- **Alternatives considered**: Flat file structure (rejected as non-scalable for future phases).
