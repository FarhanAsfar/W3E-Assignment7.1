import logging
from task_manager.extensions import db
from task_manager.models.tasks_models import Task, TaskStatus 
from datetime import date 
from flask import jsonify
from sqlalchemy import or_


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
def get_tasks(status=None, q=None, sort=None):
    logger.info("Fetching tasks with filters")

    query = Task.query

    # filter by status
    if status:
        try:
            status_enum = TaskStatus(status)
            query = query.filter(Task.status == status_enum)
        except ValueError:
            logger.warning(f"Invalid status filter: {status}")
            raise ValueError(
                f"Invalid status. Allowed values: {[s.value for s in TaskStatus]}"
            )
    
    # filter by title or description
    if q:
        search_term = f"%{q}%"
        query = query.filter(
            or_(
                Task.title.ilike(search_term),
                Task.description.ilike(search_term)
            )
        )
    
    # filter by sorting
    if sort:
        if sort == "due_date":
            query = query.order_by(Task.due_date.asc())
        elif sort == "created_at":
            query = query.order_by(Task.created_at.desc())
        else:
            logger.warning(f"Invalid sort parameter: {sort}")
            raise ValueError("Invalid sort field. Use 'due_date' or 'created_at'")
    else:
        query = query.order_by(Task.created_at.desc())

    return query.all()
    

# get task by id logic
def get_task_by_id(task_id):
    task = Task.query.get(task_id)

    if not task:
        return jsonify({"message": "No task found"}), 404

    return task 

# edit task logic
def edit_task(task_id, data):
    logger.info(f"Updating task id={task_id}")
    
    task = Task.query.get(task_id)

    if not task:
        logger.warning(f"Task not found for update id={task_id}")
        raise ValueError("Task not found")
    
    title = data.get("title")
    description = data.get("description")
    status = data.get("status")
    due_date = data.get("due_date")

    if title is not None:
        try:
            task.title = title
        except ValueError:
            logger.warning("Could not update title")
            raise ValueError("Task update failed. Could not update title") 
    
    if description is not None:
        try:
            task.description = description 
        except ValueError:
            logger.warning("Could not update description")
            raise ValueError("Task update failed. Could not update description")
    
    if status is not None:
        try:
            task.status = TaskStatus(status)
        except ValueError:
            logger.warning(f"Invalid status update: {data['status']}")
            raise ValueError(
                f"Invalid status. Allowed values: {[s.value for s in TaskStatus]}"
            ) 
    
    if due_date is not None:
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
        
        task.due_date = due_date

    db.session.commit()
    logger.info(f"Task updated successfully id={task.id}")
    return task

# delete task logic
def delete_task(task_id):
    logger.info(f"Deleting task id={task_id}")

    task = Task.query.get(task_id)

    if not task:
        logger.warning(f"Task not found to delte id={task_id}")
        raise ValueError("Task not found")
    
    db.session.delete(task)
    db.session.commit()
    logger.info(f"Task deleted successfully id={task_id}")
    
    return True 
