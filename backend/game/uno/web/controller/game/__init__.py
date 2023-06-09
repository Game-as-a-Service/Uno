
from flask import Blueprint

blueprint = Blueprint('game', __name__)

# api
# ---

#
from .create_game import create_game as _create_game
@blueprint.route("/create_game", methods = ["GET", "POST"])
def login():
    return _create_game(**locals())