from flask import Flask
from .extensions import db, migrate
from config import Config

def create_app():
    app = Flask(__name__) # creates flask app object
    app.config.from_object(Config) #loads all config values

    db.init_app(app) #attaches sqlalchemy to flask
    migrate.init_app(app, db) #connects Flask-Migrate to Flask app & SQLAlchemy models

    return app