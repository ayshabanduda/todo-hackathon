import argparse
import sys

# Task: T006
def main():
    parser = argparse.ArgumentParser(description="Todo In-Memory Python CLI App")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Task title")
    add_parser.add_argument("description", nargs="?", default="", help="Task description")

    # List command
    subparsers.add_parser("list", help="List all tasks")

    # Update command
    update_parser = subparsers.add_parser("update", help="Update a task")
    update_parser.add_argument("id", type=int, help="Task ID")
    update_parser.add_argument("title", help="New task title")
    update_parser.add_argument("description", nargs="?", default="", help="New task description")

    # Complete command
    complete_parser = subparsers.add_parser("complete", help="Mark a task as complete")
    complete_parser.add_argument("id", type=int, help="Task ID")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task ID")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    from src.services.task_service import TaskService
    service = TaskService()

    try:
        if args.command == "add":
            task = service.add_task(args.title, args.description)
            print(f"Task added successfully with ID: {task.id}")

        elif args.command == "list":
            tasks = service.get_all_tasks()
            if not tasks:
                print("No tasks found.")
            else:
                print(f"{'ID':<5} {'Title':<20} {'Status':<10}")
                print("-" * 40)
                for task in tasks:
                    status = "Complete" if task.completed else "Pending"
                    print(f"{task.id:<5} {task.title:<20} {status:<10}")

        elif args.command == "complete":
            service.mark_task_complete(args.id)
            print(f"Task {args.id} marked as complete.")

        elif args.command == "update":
            service.update_task(args.id, args.title, args.description)
            print(f"Task {args.id} updated successfully.")

        elif args.command == "delete":
            service.delete_task(args.id)
            print(f"Task {args.id} deleted successfully.")
        else:
            print(f"Command '{args.command}' is not yet implemented.")

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
