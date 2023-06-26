
from flask import Blueprint

blueprint = Blueprint('game', __name__)

# api
# ---

# http://localhost:5000/game/get_game_info?game_id=1
from .get_game_info import get_game_info as _get_game_info
@blueprint.route("/get_game_info", methods = ["GET", "POST"])
def get_game_info():
    return _get_game_info(**locals())

# http://localhost:5000/game/create_game?game_id=1
# http://localhost:5000/game/create_game?game_id=1&present=json
from .create_game import create_game as _create_game
@blueprint.route("/create_game", methods = ["GET", "POST"])
def create_game():
    return _create_game(**locals())

# http://localhost:5000/game/join_game?game_id=1&player_id=101
# http://localhost:5000/game/join_game?game_id=1&player_id=101&present=json
from .join_game import join_game as _join_game
@blueprint.route("/join_game", methods = ["GET", "POST"])
def join_game():
    return _join_game(**locals())

# http://localhost:5000/game/start_game?game_id=1&player_id=101
from .start_game import start_game as _start_game
@blueprint.route("/start_game", methods = ["GET", "POST"])
def start_game():
    return _start_game(**locals())

# http://localhost:5000/game/play_card?game_id=1&player_id=101&index=0
from .play_card import play_card as _play_card
@blueprint.route("/play_card", methods = ["GET", "POST"])
def play_card():
    return _play_card(**locals())

# http://localhost:5000/game/check_player?player_id=101
# http://localhost:5000/game/check_player?player_id=101&present=json
from .check_player import check_player as _check_player
@blueprint.route("/check_player", methods = ["GET", "POST"])
def check_player():
    return _check_player(**locals())