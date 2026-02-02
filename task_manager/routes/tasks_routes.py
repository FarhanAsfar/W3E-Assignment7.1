from flask import Blueprint, request, jsonify
from task_manager.extensions import db
from task_manager.services.tasks_services import create_task, get_tasks, get_task_by_id, edit_task, delete_task

task_bp = Blueprint("tasks", __name__, url_prefix="/api/v1/tasks")

# create task route
@task_bp.route("/create-task", methods=["POST"])
def create_task_route():
    try:
        task = create_task(request.get_json())

        return jsonify(task.to_dict()), 201

    except ValueError as e:
        return jsonify({"error": str(e)}), 400


# get all task route
@task_bp.route("", methods=["GET"])
def get_tasks_route():
    try:
        tasks = get_tasks()

        return jsonify([task.to_dict() for task in tasks]), 200
    
    except ValueError as e:
        return jsonify({"error": "Failed to fetch tasks", "details": str(e)}), 500


# get a specific task by id route
@task_bp.route("/task-by-id/<int:task_id>", methods=["GET"])
def get_task_by_id_route(task_id):
    try:
        task = get_task_by_id(task_id)

        if not task:
            return jsonify({"error": "Task not found"}), 404
        
        return jsonify({"message":"Fetched task successfully", "task": task.to_dict()}), 200
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


# edit task route
@task_bp.route("/edit-task/<int:task_id>", methods=["PUT"])
def update_task_route(task_id):
    try:
        # sending both id and the new data
        task = edit_task(task_id, request.get_json())

        return jsonify({"message":"Task updated successfully", "task": task.to_dict()}), 200
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


# delete task route
@task_bp.route("/delete-task/<int:task_id>", methods=["DELETE"])
def delete_task_route(task_id):
    try:
        task = delete_task(task_id)
        if not task:
            return jsonify({"message": "Not task found"}), 404
        
        return jsonify({"message": f"Task {task_id} deleted"}), 204
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 400