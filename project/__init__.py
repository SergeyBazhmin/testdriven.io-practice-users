import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

migrate = Migrate()

bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)

    CORS(app)

    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    from project.api.views import users_blueprint
    app.register_blueprint(users_blueprint)

    return app
