# Todo In-Memory CLI App (Phase I)

A simple, robust Todo application written in Python 3.13+ using Spec-Driven Development.

## Features
- **Add Tasks**: Title and optional description.
- **List Tasks**: View all tasks with their current status.
- **Complete Tasks**: Mark tasks as finished.
- **Update Tasks**: Modify title and description of existing tasks.
- **Delete Tasks**: Remove tasks from the list.

## Prerequisites
- Python 3.13+
- [uv](https://github.com/astral-sh/uv) (recommended)

## Installation

1. Clone the repository.
2. Create and activate a virtual environment:
   ```bash
   uv venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # Unix
   ```
3. Install the project in editable mode:
   ```bash
   uv pip install -e .
   ```

## Usage

Use the `todo` command (if installed) or run via `python -m src.cli.main`:

```bash
# Add a task
python -m src.cli.main add "Task Title" "Task Description"

# List tasks
python -m src.cli.main list

# Complete a task
python -m src.cli.main complete 1

# Update a task
python -m src.cli.main update 1 "New Title" "New Description"

# Delete a task
python -m src.cli.main delete 1
```

## Running Tests
```bash
uv run pytest
```

## Traceability
This project follows strict SDD. All code changes are linked to Task IDs in the comments.
