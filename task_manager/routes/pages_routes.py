from flask import Blueprint, render_template, request, redirect
from task_manager.services.tasks_services import get_tasks, edit_task
from task_manager.models.tasks_models import TaskStatus

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


@pages_bp.route("/tasks/<int:task_id>/mark-done")
def mark_task_done(task_id):
    edit_task(task_id, {"status": TaskStatus.DONE.value})
    return redirect("/tasks")
