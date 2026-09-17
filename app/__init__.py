"""Application Factory module."""

from flask import Flask
from app.core.config import config
from app.routes.api import api_bp


def create_app(test_config=None) -> Flask:
    """Create and configure an instance of the Flask application.

    Follows the Application Factory Pattern (Clean Architecture).
    """
    app = Flask(__name__)

    # Load configuration
    app.config["SECRET_KEY"] = config.SECRET_KEY
    if test_config:
        app.config.update(test_config)

    # Register blueprints
    app.register_blueprint(api_bp)

    return app
