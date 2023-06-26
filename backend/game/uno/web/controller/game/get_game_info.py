from typing import Any
from flask import request
from uno.web.controller.util.api_request_base_schema import merge_request_dict
from uno.web.containers import Container
from uno.usecase.get_game_info_usecase import GetGameInfoUseCase, GetGameInfoUseCaseInput, GetGameInfoUseCaseOutput
from dependency_injector.wiring import inject, Provide
from uno.web.controller.util.base_response import BasePresenter

class GetGameInfoPresenter(GetGameInfoUseCaseOutput, BasePresenter):
    
    def presentWeb(self) -> str:
        
        html = ""
        if self.isSuccess == True:
            html = f"""
            <p>get game info!</p>
            """
            html += f"""
            <p>{self.game}</p>
            """
            for player in self.player_list:
                html += f"""
                <p>{player}</p>
                """
            for deck in self.deck_list:
                html += f"""
                <p>{deck}</p>
                """
        else:
            html = f"""
            <p>get game info fail!</p>
            <p>{self.error}</p>
            """
        return html
    
    def presentJson(self) -> Any:
        res = {
            "isSuccess": self.isSuccess,
            # "game": self.game,
            # "player_list": self.player_list,
            # "deck_list": self.deck_list,
            "error": str(self.error) if self.isSuccess == False else None,
        }
        return res

@inject
def get_game_info(usecase: GetGameInfoUseCase = Provide[Container.getGameInfoUseCase]):
    
    input_unchecked_dict = merge_request_dict(request)

    input = GetGameInfoUseCaseInput()

    presenter = GetGameInfoPresenter()
    presenter.detectPresentType(input_unchecked_dict)

    game_id = input_unchecked_dict.get("game_id")

    if game_id != None:
        input.game_id = int(game_id)
    else:
        presenter.error = Exception("game_id is required!")
        presenter.isSuccess = False

    if presenter.isSuccess != False:
        usecase.execute(input, presenter)
    
    return presenter.present()
