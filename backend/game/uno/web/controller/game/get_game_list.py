
from flask import request
from uno.web.controller.util.base_response import BasePresenter
from uno.web.controller.util.api_request_base_schema import merge_request_dict
from uno.web.containers import Container
from uno.usecase.get_game_list_usecase import GetGameListUseCase, GetGameListUseCaseInput, GetGameListUseCaseOutput
from dependency_injector.wiring import inject, Provide
from typing import Any

class GetGameListPresenter(GetGameListUseCaseOutput, BasePresenter):
    
    def presentWeb(self) -> Any:
        
        html = ""
        if self.isSuccess == True:
            html = f"""
            <p>get game list!</p>
            """
            for game in self.game_list:
                html += f"""
                <p>{game}</p>
                """
        else:
            html = f"""
            <p>get game list fail!</p>
            <p>{self.error}</p>
            """
        return html
    
    def presentJson(self) -> Any:
        game_id_list = list(map(lambda game: game.id, self.game_list))
        res = {
            "isSuccess": self.isSuccess,
            "game_id_list": game_id_list,
            "error": str(self.error) if self.isSuccess == False else None,
        }
        return res

@inject
def get_game_list(usecase: GetGameListUseCase = Provide[Container.getGameListUseCase]):

    input_unchecked_dict = merge_request_dict(request)

    input = GetGameListUseCaseInput()

    presenter = GetGameListPresenter()
    presenter.detectPresentType(input_unchecked_dict)

    if presenter.isSuccess != False:
        usecase.execute(input, presenter)

    return presenter.present()