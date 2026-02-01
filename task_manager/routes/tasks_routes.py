from flask import Blueprint, request, jsonify
from task_manager.extensions import db
from task_manager.models.tasks_models import Task

task_bp = Blueprint("tasks", __name__, url_prefix="/api/v1/tasks")
