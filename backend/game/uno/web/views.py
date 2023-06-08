
from dependency_injector.wiring import inject, Provide
from .containers import Container
from uno.usecase.create_game_usecase import CreateGameUseCase

def hello_world():
    return "<p>Hello, World!</p>"

@inject
def create_game(usecase: CreateGameUseCase = Provide[Container.createGameUseCase]):
    print("create_game", usecase, type(usecase).__name__)
    usecase.execute(9527)

    return "<p>Game created!</p>"