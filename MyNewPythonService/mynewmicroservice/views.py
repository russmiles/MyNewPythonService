# -*- coding: utf-8 -*-
from flask import Blueprint

__all__ = ['mynewmicroservice_app']

mynewmicroservice_app = Blueprint('mynewmicroservice_app', __name__)


@mynewmicroservice_app.route('/')
def index():
    return "Hello World!"
