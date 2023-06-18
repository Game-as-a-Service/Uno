
import json
from flask import request
from uno.web.controller.util.api_request_base_schema import merge_request_dict
from uno.web.containers import Container
from uno.usecase.check_player_usecase import CheckPlayerUsecase
from dependency_injector.wiring import inject, Provide

@inject
def check_player(usecase: CheckPlayerUsecase = Provide[Container.checkPlayerUsecase]):

    input_unchecked_dict = merge_request_dict(request)
    player_id = input_unchecked_dict.get("player_id")

    player_id = int(player_id)
    result = usecase.execute(player_id)

    response = {}
    game = result["game"]
    if game is not None:
        response["game_id"] = game.id

    player = result["player"]
    if player is not None:
        response["player_id"] = player.id

    return json.dumps(response)