# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""
import json

from flask import Flask, jsonify
from marshmallow.exceptions import ValidationError
from werkzeug.exceptions import default_exceptions, HTTPException

from betly import public
from betly.extensions import bcrypt, cache, db, debug_toolbar, login_manager, migrate
from betly.settings import ProdConfig
from betly.api.v1 import users, sessions, registrations, bet


def create_app(config_object=ProdConfig):
    """An application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_error_handlers(app)
    return app


def register_extensions(app):
    """Register Flask extensions."""
    bcrypt.init_app(app)
    cache.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    debug_toolbar.init_app(app)
    migrate.init_app(app, db)
    return None


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(public.views.blueprint)
    app.register_blueprint(sessions.views.blueprint)
    app.register_blueprint(registrations.views.blueprint)
    app.register_blueprint(users.views.blueprint)
    app.register_blueprint(bet.views.blueprint)
    return None

def register_error_handlers(app):
    """Return JSON errors to the user."""
    @app.errorhandler(ValidationError)
    def handle_marshmallow_validation_error(ex):
        import ipdb; ipdb.set_trace()
        response = jsonify(message="422: Unprocessable Entity", description=ex.messages)
        response.status_code = 422
        return response

    def make_json_error(ex):
        response = jsonify(message=str(ex), description=ex.description)
        response.status_code = (ex.code if isinstance(ex, HTTPException) else 500)
        return response

    for code in default_exceptions:
        app.error_handler_spec[None][code] = make_json_error
