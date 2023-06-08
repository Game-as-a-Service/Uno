
from flask import Flask

from .containers import Container
from . import views

# ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====
# 準備所有服務
container = Container()

# ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====
# 準備對外接口
app = Flask(__name__)
app.add_url_rule("/", "hello_world", views.hello_world)
app.add_url_rule("/create_game", "create_game", views.create_game)

if __name__ == "__main__":
    app.run()