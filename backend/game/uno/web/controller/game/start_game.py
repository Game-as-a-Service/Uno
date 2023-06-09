
from flask import request
from uno.web.controller.util.api_request_base_schema import merge_request_dict
from uno.web.containers import Container
from uno.usecase.start_game_usecase import StartGameUseCase
from dependency_injector.wiring import inject, Provide

@inject
def start_game(usecase: StartGameUseCase = Provide[Container.startGameUseCase]):

    input_unchecked_dict = merge_request_dict(request)
    game_id = input_unchecked_dict.get("game_id")
    player_id = input_unchecked_dict.get("player_id")

    if game_id == None:
        return "<p>Game id is required!</p>"
    
    if player_id == None:
        return "<p>Player id is required!</p>"
    
    game_id = int(game_id)
    player_id = int(player_id)
    game = usecase.execute(game_id, player_id)

    return f"<p>start_game!{game}</p>"