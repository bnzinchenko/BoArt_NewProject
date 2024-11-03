from flask import Flask, Config
from .extensions import db
from .config import Config


from .routes.user import user
from .routes.animal import animal
from .routes.main import main


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.register_blueprint(user)
    app.register_blueprint(animal)
    app.register_blueprint(main)


    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app
