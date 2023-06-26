
import json
from typing import Any
from flask import request
from uno.web.controller.util.api_request_base_schema import merge_request_dict
from uno.web.containers import Container
from uno.usecase.check_player_usecase import CheckPlayerUsecase, CheckPlayerUsecaseInput, CheckPlayerUsecaseOutput
from uno.web.controller.util.base_response import BasePresenter
from dependency_injector.wiring import inject, Provide

class CheckPlayerPresenter(CheckPlayerUsecaseOutput, BasePresenter):

    def presentWeb(self) -> Any:
        
        html = ""
        if self.isSuccess == True:
            html = f"""
            <p>check player!</p>
            <p>{self.game}</p>
            <p>{self.player}</p>
            """
        else:
            html = f"""
            <p>check player fail!</p>
            <p>{self.error}</p>
            """
        return html
    
    def presentJson(self) -> Any:
        res = {
            "isSuccess": self.isSuccess,
            "game_id": self.game.id if self.game != None else None,
            "player_id": self.player.id if self.player != None else None,
            "error": str(self.error) if self.isSuccess == False else None,
        }
        return res

@inject
def check_player(usecase: CheckPlayerUsecase = Provide[Container.checkPlayerUsecase]):

    input_unchecked_dict = merge_request_dict(request)

    input = CheckPlayerUsecaseInput()

    presenter = CheckPlayerPresenter()
    presenter.detectPresentType(input_unchecked_dict)

    player_id = input_unchecked_dict.get("player_id")
    if player_id != None:
        input.player_id = int(player_id)
    else:
        presenter.error = Exception("player_id is required!")
        presenter.isSuccess = False

    if presenter.isSuccess != False:
        usecase.execute(input, presenter)

    return presenter.present()