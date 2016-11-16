# -*- coding: utf-8 -*-
from flask import url_for


def test_mynewmicroservice_index(client):
    res = client.get(url_for('mynewmicroservice_app.index'))
    assert res.data == b'Hello World!'
