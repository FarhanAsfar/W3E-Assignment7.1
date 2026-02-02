from flask import Blueprint, request, jsonify
from task_manager.extensions import db
from task_manager.services.tasks_services import create_task

task_bp = Blueprint("tasks", __name__, url_prefix="/api/v1/tasks")
