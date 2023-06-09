
from flask import Blueprint

blueprint = Blueprint('game', __name__)

# api
# ---

# http://localhost:5000/game/create_game?game_id=1
from .create_game import create_game as _create_game
@blueprint.route("/create_game", methods = ["GET", "POST"])
def create_game():
    return _create_game(**locals())

# http://localhost:5000/game/join_game
from .join_game import join_game as _join_game
@blueprint.route("/join_game", methods = ["GET", "POST"])
def join_game():
    return _join_game(**locals())