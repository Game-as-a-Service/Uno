
from flask import request
from uno.web.controller.util.api_request_base_schema import merge_request_dict
from uno.web.containers import Container
from uno.usecase.create_game_usecase import CreateGameUseCase
from dependency_injector.wiring import inject, Provide

@inject
def create_game(usecase: CreateGameUseCase = Provide[Container.createGameUseCase]):
    
    input_unchecked_dict = merge_request_dict(request)
    game_id = input_unchecked_dict.get("game_id")

    if game_id == None:
        return "<p>Game id is required!</p>"

    game_id = int(game_id)
    game = usecase.execute(game_id)

    return f"<p>Game created!{game}</p>"

