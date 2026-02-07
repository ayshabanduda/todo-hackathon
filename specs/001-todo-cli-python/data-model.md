# Data Model: Todo In-Memory Python CLI

## Task Entity

| Field | Type | Description | Validation |
|-------|------|-------------|------------|
| id | Integer | Unique identifier | Auto-incrementing, > 0 |
| title | String | Brief title of the task | Non-empty, max 100 chars |
| description | String | Detailed description | Optional |
| completed | Boolean | Completion status | Defaults to False |

## State Transitions
- **Pending** -> **Complete**: Via `complete` command.
- **Any State** -> **Deleted**: Via `delete` command.
