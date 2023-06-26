from typing import Any
from flask import request
from uno.web.controller.util.api_request_base_schema import merge_request_dict
from uno.web.containers import Container
from uno.usecase.join_game_usecase import JoinGameUseCase, JoinGameUseCaseInput, JoinGameUseCaseOutput
from uno.web.controller.util.base_response import BasePresenter
from dependency_injector.wiring import inject, Provide

class JoinGamePresenter(JoinGameUseCaseOutput, BasePresenter):

    def presentWeb(self) -> Any:

        html = ""
        if self.isSuccess == True:
            html = f"""
            <p>join game!</p>
            <p>{self.game}</p>
            """
        else:
            html = f"""
            <p>join game fail!</p>
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
def join_game(usecase: JoinGameUseCase = Provide[Container.joinGameUseCase]):
    
    input_unchecked_dict = merge_request_dict(request)

    input = JoinGameUseCaseInput()

    presenter = JoinGamePresenter()
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

    if presenter.isSuccess != False:
        usecase.execute(input, presenter)

    return presenter.present()