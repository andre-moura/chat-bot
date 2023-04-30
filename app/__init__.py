from flask import Flask
import secrets
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.config['SECRET_KEY'] = secrets.token_hex()

    from app.controllers.main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/main')

    return app