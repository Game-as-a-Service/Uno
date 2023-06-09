
from typing import Dict
from flask import Request
from enum import Flag, auto

class Request_input_type(Flag):
    JSON = auto()
    ARGS = auto()
    FORM = auto()
    FILE = auto()

allType = Request_input_type.JSON | Request_input_type.ARGS | Request_input_type.FORM | Request_input_type.FILE

def merge_request_dict(
        request: Request, 
        type: Request_input_type = allType
    ) -> dict:

    result: Dict = {}

    if Request_input_type.JSON & type and request.is_json:
        result.update(request.get_json()) # type: ignore
    if Request_input_type.ARGS & type and request.args != None:
        result.update(request.args)
    if Request_input_type.FORM & type and request.form != None:
        result.update(request.form)
    if Request_input_type.FILE & type and request.files != None:
        result.update(request.files)

    return result
