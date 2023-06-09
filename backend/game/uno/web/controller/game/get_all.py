from flask import request
from uno.web.controller.util.api_request_base_schema import merge_request_dict
from uno.web.containers import Container
from uno.usecase.get_all_usecase import GetAllUsecase
from dependency_injector.wiring import inject, Provide

@inject
def get_all(usecase: GetAllUsecase = Provide[Container.getAllUsecase]):
    
    input_unchecked_dict = merge_request_dict(request)
    game_id = input_unchecked_dict.get("game_id")

    if game_id == None:
        return "<p>Game id is required!</p>"

    game_id = int(game_id)
    msgList = usecase.execute(game_id)

    result = '<br>'.join(msgList)

    return f"<p>get_all!<br>{result}</p>"
