from dataclasses import dataclass

# Task: T004
@dataclass
class Task:
    id: int
    title: str
    description: str = ""
    completed: bool = False

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }
