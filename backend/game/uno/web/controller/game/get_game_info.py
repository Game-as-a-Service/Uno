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

        def player_to_dto(player):
            result = {
                "id": player.id,
            }
            return result

        player_dto_list = list(map(player_to_dto, self.player_list))

        def card_to_dto(card):
            result = {
                "symbol": card.symbol,
                "color": card.color,
                "function": card.function,
            }
            return result

        def deck_to_dto(deck):
            result = {
                "player_id": deck.playerId,
                "card_list": list(map(card_to_dto, deck.cardList)),
            }
            return result
        deck_dto_list = list(map(deck_to_dto, self.deck_list))

        res = {
            "isSuccess": self.isSuccess,
            "game_id": self.game.id if self.game != None else None,
            "game_states": self.game.state if self.game != None else None,
            "host": self.game.host if self.game != None else None,
            "player_list": player_dto_list,
            "deck_list": deck_dto_list,
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
