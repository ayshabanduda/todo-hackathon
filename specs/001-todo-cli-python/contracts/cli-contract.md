# CLI Contract: Todo App

## Commands

### Add Task
- **Command**: `add`
- **Arguments**: `"title"`, `"description"`
- **Response**: Confirmation message with assigned ID.
- **Example**: `python -m src.cli.main add "Buy Milk" "Low fat"`

### List Tasks
- **Command**: `list`
- **Arguments**: None
- **Response**: Formatted table of tasks.
- **Example**: `python -m src.cli.main list`

### Update Task
- **Command**: `update`
- **Arguments**: `<id>`, `"title"`, `"description"`
- **Response**: Confirmation message.
- **Example**: `python -m src.cli.main update 1 "Buy Milk" "Full fat"`

### Complete Task
- **Command**: `complete`
- **Arguments**: `<id>`
- **Response**: Confirmation message.
- **Example**: `python -m src.cli.main complete 1`

### Delete Task
- **Command**: `delete`
- **Arguments**: `<id>`
- **Response**: Confirmation message.
- **Example**: `python -m src.cli.main delete 1`
