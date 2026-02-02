import logging
from task_manager.extensions import db
from task_manager.models.tasks_models import Task, TaskStatus 
from datetime import date 
from flask import jsonify


logger = logging.getLogger("task_manager")

# create task from given user request
def create_task(data):
    logger.info("Creating new task")
    
    title = data.get("title")
    description = data.get("description")
    due_date = data.get("due_date")
    status = data.get("status", TaskStatus.TODO.value)

    if not title:
        logger.warning("Task creating failed: title missing")
        raise ValueError("Title is required")
    
    # validate status
    try:
        status_enum = TaskStatus(status)
    except ValueError:
        logger.warning(f"Invalid task status: {status}")
        raise ValueError(
            f"Invalid status. Allowed values: {[s.value for s in TaskStatus]}"
        )
    
    # validate due date
    parsed_due_date = None
    if due_date:
        try:
            parsed_due_date = date.fromisoformat(due_date)
        except ValueError:
            logger.warning("Invalid date format.")
            raise ValueError("invalid date format. Use YYYY-MM-DD")
        
        if parsed_due_date < date.today():
            logger.warning(f"Invalid due date (past): {due_date}")
            raise ValueError("Due date can't be in the past")

    task = Task(
        title=title,
        description=description,
        status=status_enum,
        due_date=date.fromisoformat(due_date) if due_date else None
    )

    db.session.add(task)
    db.session.commit()

    logger.info(f"Task created successfully (id={task.id})")

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

# edit task logic
def edit_task(task_id, data):
    task = Task.query.get(task_id)

    if not task:
        raise ValueError("Task not found")
    
    title = data.get("title")
    description = data.get("description")
    status = data.get("status")
    due_date = data.get("due_date")

    if title is not None:
        task.title = title 
    
    if description is not None:
        task.description = description 
    
    if status is not None:
        try:
            task.status = TaskStatus(status)
        except ValueError:
            raise ValueError(
                f"Invalid status. Allowed values: {[s.value for s in TaskStatus]}"
            ) 
    
    if due_date is not None:
        task.due_date = due_date

    db.session.commit()
    return task

# delete task logic
def delete_task(task_id):
    task = Task.query.get(task_id)

    if not task:
        raise ValueError("Task not found")
    
    db.session.delete(task)
    db.session.commit()

    return True 
