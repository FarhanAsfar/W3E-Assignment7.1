from task_manager.extensions import db
from task_manager.models.tasks_models import Task, TaskStatus 
from datetime import date 
from flask import jsonify

# create task from given user request
def create_task(data):
    title = data.get("title")
    description = data.get("description")
    due_date = data.get("due_date")
    status = data.get("status", TaskStatus.TODO.value)

    if not title:
        raise ValueError("Title is required")
    
    # validate status
    try:
        status_enum = TaskStatus(status)
    except ValueError:
        raise ValueError(
            f"Invalid status. Allowed values: {[s.value for s in TaskStatus]}"
        )

    task = Task(
        title=title,
        description=description,
        status=status_enum,
        due_date=date.fromisoformat(due_date) if due_date else None
    )

    db.session.add(task)
    db.session.commit()

    return task


# get all task logic
def get_tasks():
    try:
        return Task.query.order_by(Task.created_at.desc()).all()
    except Exception as e:
        raise ValueError("Unable to fetch tasks")
    

# get task by id logic
def get_task_by_id(task_id):
    task = Task.query.get(task_id)

    if not task:
        return jsonify({"message": "No task found"}), 404

    return task 

