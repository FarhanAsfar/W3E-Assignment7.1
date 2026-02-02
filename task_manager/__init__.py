from flask import Flask
from .extensions import db, migrate
from config import Config
from task_manager.utils.logger import setup_logger

def create_app():
    app = Flask(__name__) # creates flask app object
    app.config.from_object(Config) #loads all config values

    db.init_app(app) #attaches sqlalchemy to flask
    migrate.init_app(app, db) #connects Flask-Migrate to Flask app & SQLAlchemy models

    logger = setup_logger()
    logger.info("Task manager application started")

    from task_manager.routes.tasks_routes import task_bp
    app.register_blueprint(task_bp)

    return app