from flask import request
from uno.web.controller.util.api_request_base_schema import merge_request_dict
from uno.web.containers import Container
from uno.usecase.get_game_info_usecase import GetGameInfoUseCase
from dependency_injector.wiring import inject, Provide

@inject
def get_game_info(usecase: GetGameInfoUseCase = Provide[Container.getGameInfoUseCase]):
    
    input_unchecked_dict = merge_request_dict(request)
    game_id = input_unchecked_dict.get("game_id")

    if game_id == None:
        return "<p>Game id is required!</p>"

    game_id = int(game_id)
    msgList = usecase.execute(game_id)

    result = '<br>'.join(msgList)

    return f"<p>get_all!<br>{result}</p>"
