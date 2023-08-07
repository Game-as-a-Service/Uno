
# pytest -s -q tests/atdd/test_hello.py

from flask.testing import FlaskClient

def test_hello(client: FlaskClient):
    response = client.get("/")
    assert response.data == b'<p>Hello, World!</p>'
    