
from flask import Flask
from flask_compress import Compress # type: ignore
from flask_cors import CORS # type: ignore

from .containers import Container
from . import views

# ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====
# 準備所有服務
container = Container()

# ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====
# 準備對外接口
app = Flask(__name__)
app.container = container # type: ignore
# 給測試用
app.add_url_rule("/", "hello_world", views.hello_world)

from uno.web.controller.game import blueprint as game
app.register_blueprint(game, url_prefix = '/game')

Compress(app)
CORS(app)

if __name__ == "__main__":
    app.run()