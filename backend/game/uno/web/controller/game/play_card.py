from flask import request
from uno.web.controller.util.api_request_base_schema import merge_request_dict
from uno.web.containers import Container
from uno.usecase.play_card_usecase import PlayCardUsecase
from dependency_injector.wiring import inject, Provide

@inject
def play_card(usecase: PlayCardUsecase = Provide[Container.playCardGameUseCase]):

    input_unchecked_dict = merge_request_dict(request)
    game_id = input_unchecked_dict.get("game_id")
    player_id = input_unchecked_dict.get("player_id")
    index = input_unchecked_dict.get("index")

    if game_id == None:
        return "<p>Game id is required!</p>"
    if player_id == None:
        return "<p>Player id is required!</p>"
    if index == None:
        return "<p>index is required!</p>"
    
    game_id = int(game_id)
    player_id = int(player_id)
    index = int(index)
    game = usecase.execute(game_id, player_id, index)

    return f"<p>play_card!{game}</p>"