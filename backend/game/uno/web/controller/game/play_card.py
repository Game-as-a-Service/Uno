from typing import Any
from flask import request
from uno.web.controller.util.api_request_base_schema import merge_request_dict
from uno.web.containers import Container
from uno.usecase.play_card_usecase import PlayCardUsecase, PlayCardUsecaseInput, PlayCardUsecaseOutput
from dependency_injector.wiring import inject, Provide
from uno.web.controller.util.base_response import BasePresenter

class PlayCardPresenter(PlayCardUsecaseOutput, BasePresenter):
    def presentWeb(self) -> Any:
        html = ""
        if self.isSuccess == True:
            html = f"""
            <p>play card!</p>
            <p>{self.game}</p>
            """
        else:
            html = f"""
            <p>play card fail!</p>
            <p>{self.error}</p>
            """
        return html
    
    def presentJson(self) -> Any:
        res = {
            "isSuccess": self.isSuccess,
            "game_id": self.game.id if self.game != None else None,
            "error": str(self.error) if self.isSuccess == False else None,
        }
        return res

@inject
def play_card(usecase: PlayCardUsecase = Provide[Container.playCardGameUseCase]):

    input_unchecked_dict = merge_request_dict(request)

    input = PlayCardUsecaseInput()

    presenter = PlayCardPresenter()
    presenter.detectPresentType(input_unchecked_dict)

    game_id = input_unchecked_dict.get("game_id")
    if game_id != None:
        input.game_id = int(game_id)
    else:
        presenter.error = Exception("game_id is required!")
        presenter.isSuccess = False

    player_id = input_unchecked_dict.get("player_id")
    if player_id != None:
        input.player_id = int(player_id)
    else:
        presenter.error = Exception("player_id is required!")
        presenter.isSuccess = False

    index = input_unchecked_dict.get("index")
    if index != None:
        input.index = int(index)
    else:
        presenter.error = Exception("index is required!")
        presenter.isSuccess = False
    
    if presenter.isSuccess != False:
        usecase.execute(input, presenter)

    return presenter.present()