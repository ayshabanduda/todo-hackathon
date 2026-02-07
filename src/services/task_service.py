from typing import List
from src.models.task import Task
from src.services.repository import TaskRepository

# Task: T009
class TaskService:
    def __init__(self):
        self.repo = TaskRepository()

    def add_task(self, title: str, description: str = "") -> Task:
        if not title:
            raise ValueError("Title cannot be empty")
        # Task: T011 (added basic validation here as well)
        return self.repo.add(title, description)

    def get_all_tasks(self) -> List[Task]:
        return self.repo.get_all()

    # Task: T014, T016
    def mark_task_complete(self, task_id: int) -> Task:
        task = self.repo.get_by_id(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} not found")
        task.completed = True
        return task

    # Task: T019, T021
    def update_task(self, task_id: int, title: str, description: str = "") -> Task:
        task = self.repo.get_by_id(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} not found")
        if not title:
            raise ValueError("Title cannot be empty")
        task.title = title
        task.description = description
        return task

    def delete_task(self, task_id: int) -> bool:
        success = self.repo.delete(task_id)
        if not success:
            raise ValueError(f"Task with ID {task_id} not found")
        return True
