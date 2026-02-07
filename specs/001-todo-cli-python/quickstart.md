# Quickstart: Todo In-Memory CLI

## Setup
1. Ensure Python 3.13+ is installed.
2. Clone the repository.

## Usage Scenarios

### Creating and Viewing a Task
```bash
python -m src.cli.main add "My First Task" "This is the description"
python -m src.cli.main list
```

### Managing Task Lifecycle
```bash
python -m src.cli.main complete 1
python -m src.cli.main update 1 "Updated Title" "New description"
python -m src.cli.main delete 1
```

## Running Tests
```bash
pytest
```
