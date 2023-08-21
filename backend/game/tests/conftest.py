from flask.testing import FlaskClient
import pytest
from uno.web.app import app as web_app

# https://dormousehole.readthedocs.io/en/latest/testing.html

@pytest.fixture()
def app():
    yield web_app
    print("teardown web_app")

@pytest.fixture()
def client(app) -> FlaskClient:
    return app.test_client()

