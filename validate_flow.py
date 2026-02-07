from src.services.task_service import TaskService

def validate():
    service = TaskService()
    
    # 1. Add
    t1 = service.add_task("Test", "Desc")
    print(f"Added task: {t1}")
    assert len(service.get_all_tasks()) == 1
    
    # 2. List
    tasks = service.get_all_tasks()
    print(f"List: {tasks}")
    
    # 3. Complete
    service.mark_task_complete(t1.id)
    print(f"Completed task: {t1}")
    assert t1.completed is True
    
    # 4. Update
    service.update_task(t1.id, "New", "Newer")
    print(f"Updated task: {t1}")
    assert t1.title == "New"
    
    # 5. Delete
    service.delete_task(t1.id)
    print("Deleted task")
    assert len(service.get_all_tasks()) == 0
    
    print("All Phase I features validated successfully!")

if __name__ == "__main__":
    validate()
