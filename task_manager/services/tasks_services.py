from task_manager.extensions import db
from task_manager.models.tasks_models import Task 
from datetime import date 

def create_task(data):
    title = data.get("title")
    description = data.get("description")
    due_date = data.get("due_date")

    if not title:
        raise ValueError("Title is required")

    task = Task(
        title=title,
        description=description,
        due_date=date.fromisoformat(due_date) if due_date else None
    )

    db.session.add(task)
    db.session.commit()

    return task
