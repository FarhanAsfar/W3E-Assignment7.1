from flask import Blueprint, render_template, request, redirect
from task_manager.services.tasks_services import get_tasks, edit_task
from task_manager.models.tasks_models import TaskStatus
from task_manager.services.tasks_services import get_task_by_id

pages_bp = Blueprint("pages", __name__)


@pages_bp.route("/")
def home_page():
    return render_template("home.html")


@pages_bp.route("/tasks")
def tasks_page():
    status = request.args.get("status")

    tasks = get_tasks(status=status)

    return render_template(
        "tasks.html",
        tasks=[task.to_dict() for task in tasks],
        statuses=[s.value for s in TaskStatus],
        selected_status=status
    )


@pages_bp.route("/tasks/<int:task_id>/toggle-status")
def toggle_task_status(task_id):
    task = get_task_by_id(task_id)

    if not task:
        return redirect("/tasks")

    new_status = (
        TaskStatus.TODO.value
        if task.status == TaskStatus.DONE
        else TaskStatus.DONE.value
    )

    edit_task(task_id, {"status": new_status})
    return redirect("/tasks")
