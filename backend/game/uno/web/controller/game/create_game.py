
from flask import request
from uno.web.controller.util.base_response import BasePresenter
from uno.web.controller.util.api_request_base_schema import merge_request_dict
from uno.web.containers import Container
from uno.usecase.create_game_usecase import CreateGameUseCase, CreateGameUseCaseInput, CreateGameUseCaseOutput
from dependency_injector.wiring import inject, Provide
from typing import Any

class CreateGamePresenter(CreateGameUseCaseOutput, BasePresenter):

    def presentWeb(self) -> Any:
        
        html = ""
        if self.isSuccess == True:
            html = f"""
            <p>Game created!</p>
            <p>{self.game}</p>
            """
        else:
            html = f"""
            <p>Game not created!</p>
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
def create_game(usecase: CreateGameUseCase = Provide[Container.createGameUseCase]):
    
    input_unchecked_dict = merge_request_dict(request)

    input = CreateGameUseCaseInput()

    presenter = CreateGamePresenter()
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
