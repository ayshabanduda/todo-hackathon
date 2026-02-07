import pytest
from src.services.task_service import TaskService
from src.services.repository import TaskRepository

# Task: T007
@pytest.fixture
def task_service():
    repo = TaskRepository()
    repo.clear()
    return TaskService()

def test_add_task(task_service):
    task = task_service.add_task("Test Task", "Test Description")
    assert task.id == 1
    assert task.title == "Test Task"
    assert task.description == "Test Description"
    assert task.completed is False

def test_get_all_tasks(task_service):
    task_service.add_task("Task 1")
    task_service.add_task("Task 2")
    tasks = task_service.get_all_tasks()
    assert len(tasks) == 2
    assert tasks[0].title == "Task 1"
    assert tasks[1].title == "Task 2"

def test_add_task_empty_title(task_service):
    with pytest.raises(ValueError, match="Title cannot be empty"):
        task_service.add_task("")

# Task: T012
def test_mark_task_complete(task_service):
    task = task_service.add_task("Finish Hackathon")
    assert task.completed is False
    updated_task = task_service.mark_task_complete(task.id)
    assert updated_task.completed is True

def test_mark_non_existent_task_complete(task_service):
    with pytest.raises(ValueError, match="Task with ID 999 not found"):
        task_service.mark_task_complete(999)

# Task: T017
def test_update_task(task_service):
    task = task_service.add_task("Old Title", "Old Desc")
    updated_task = task_service.update_task(task.id, "New Title", "New Desc")
    assert updated_task.title == "New Title"
    assert updated_task.description == "New Desc"

def test_delete_task(task_service):
    task = task_service.add_task("To be deleted")
    assert len(task_service.get_all_tasks()) == 1
    task_service.delete_task(task.id)
    assert len(task_service.get_all_tasks()) == 0

def test_update_non_existent_task(task_service):
    with pytest.raises(ValueError, match="Task with ID 999 not found"):
        task_service.update_task(999, "Title", "Desc")

def test_delete_non_existent_task(task_service):
    with pytest.raises(ValueError, match="Task with ID 999 not found"):
        task_service.delete_task(999)
