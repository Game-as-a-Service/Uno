
from flask import Blueprint

blueprint = Blueprint('game', __name__)

# api
# ---

# http://localhost:5000/game/get_all?game_id=1
from .get_all import get_all as _get_all
@blueprint.route("/get_all", methods = ["GET", "POST"])
def get_all():
    return _get_all(**locals())

# http://localhost:5000/game/create_game?game_id=1
from .create_game import create_game as _create_game
@blueprint.route("/create_game", methods = ["GET", "POST"])
def create_game():
    return _create_game(**locals())

# http://localhost:5000/game/join_game?game_id=1&player_id=101
from .join_game import join_game as _join_game
@blueprint.route("/join_game", methods = ["GET", "POST"])
def join_game():
    return _join_game(**locals())

# http://localhost:5000/game/start_game?game_id=1&player_id=101
from .start_game import start_game as _start_game
@blueprint.route("/start_game", methods = ["GET", "POST"])
def start_game():
    return _start_game(**locals())