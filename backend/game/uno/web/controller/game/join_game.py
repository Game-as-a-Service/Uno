from flask import request
from uno.web.controller.util.api_request_base_schema import merge_request_dict
from uno.web.containers import Container
from uno.usecase.join_game_usecase import JoinGameUseCase
from dependency_injector.wiring import inject, Provide

@inject
def join_game(usecase: JoinGameUseCase = Provide[Container.joinGameUseCase]):
    
    input_unchecked_dict = merge_request_dict(request)
    game_id = input_unchecked_dict.get("game_id")
    player_id = input_unchecked_dict.get("player_id")

    if game_id == None:
        return "<p>Game id is required!</p>"
    if player_id == None:
        return "<p>Player id is required!</p>"
    
    game = usecase.execute(game_id, player_id)

    return f"<p>join_game!{game}</p>"