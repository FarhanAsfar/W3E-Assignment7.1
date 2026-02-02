from flask import Blueprint, request, jsonify
from task_manager.extensions import db
from task_manager.services.tasks_services import create_task

task_bp = Blueprint("tasks", __name__, url_prefix="/api/v1/tasks")

@task_bp.route("", methods=["POST"])
def create_task_route():
    try:
        task = create_task(request.get_json())

        return jsonify({
            "id": task.id,
            "title": task.title,
            "status": task.status,
            "due_date": task.due_date,
            "created_at": task.created_at
        }), 201

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
