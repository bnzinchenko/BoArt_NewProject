from flask import Flask, Config

from .extensions import login_manager
from .extensions import db, migrate
from .config import Config


from .routes.user import user
from .routes.animal import animal


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.register_blueprint(user)
    app.register_blueprint(animal)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)


    with app.app_context():
        db.create_all()

    return app
