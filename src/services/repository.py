from typing import List, Optional
from src.models.task import Task

# Task: T005
class TaskRepository:
    _instance: Optional['TaskRepository'] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TaskRepository, cls).__new__(cls)
            cls._instance.tasks: List[Task] = []
            cls._instance.next_id: int = 1
        return cls._instance

    def add(self, title: str, description: str = "") -> Task:
        task = Task(id=self.next_id, title=title, description=description)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_all(self) -> List[Task]:
        return self.tasks

    def get_by_id(self, task_id: int) -> Optional[Task]:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def delete(self, task_id: int) -> bool:
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                self.tasks.pop(i)
                return True
        return False

    def clear(self):
        """Helper for tests to reset state."""
        self.tasks = []
        self.next_id = 1
