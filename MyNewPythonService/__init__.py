# -*- coding: utf-8 -*-
from flask import Flask, Blueprint, jsonify

from MyNewPythonService.swagger import spec

__version__ = '0.1.0'
__all__ = ['create_app']


def create_app():
    """
    Create the :class:`flask.app.Flask` app, as well as its models.
    Also, register blueprints.
    """
    app = Flask(__name__)

    from MyNewPythonService.views import main_app
    app.register_blueprint(main_app)

    from MyNewPythonService.mynewmicroservice.views import mynewmicroservice_app
    app.register_blueprint(mynewmicroservice_app)

    return app

