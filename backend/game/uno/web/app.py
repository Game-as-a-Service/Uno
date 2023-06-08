
from flask import Flask

from .containers import Container
from . import views

# ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====
container = Container()

app = Flask(__name__)
app.container = container
app.add_url_rule("/", "hello_world", views.hello_world)

if __name__ == "__main__":
    app.run()