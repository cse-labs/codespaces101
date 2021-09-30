import pytest
import mock
import flask
import pdb;

import api.math_api
from api.math_api import add

def test__add__x_not_passed__returns_400(mocker):
    app = flask.Flask(__name__)

    with app.test_request_context('/?y=4'):
        message, code = add()
        assert code == 400

def test__add__y_not_passed__returns_400(mocker):
    app = flask.Flask(__name__)

    with app.test_request_context('/?x=4'):
        message, code = add()
        assert code == 400

def test__add__x_not_numeric__returns_400(mocker):
    app = flask.Flask(__name__)

    with app.test_request_context('/?x=ggg&y=4'):
        message, code = add()
        assert code == 400

def test__add__y_not_numeric__returns_400(mocker):
    app = flask.Flask(__name__)

    with app.test_request_context('/?x=4&y=ggg'):
        message, code = add()
        assert code == 400

def test__add__z_and_y_integers_passed__returns_sum(mocker):
    app = flask.Flask(__name__)

    with app.test_request_context('/?x=4&y=5'):
        response = add()
        assert response == '9.0'

def test__add__z_and_y_floats_passed__returns_sum(mocker):
    app = flask.Flask(__name__)

    with app.test_request_context('/?x=4.4&y=5.5'):
        response = add()
        assert response == '9.9'