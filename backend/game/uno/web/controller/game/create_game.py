
from uno.web.containers import Container
from uno.usecase.create_game_usecase import CreateGameUseCase
from dependency_injector.wiring import inject, Provide

@inject
def create_game(usecase: CreateGameUseCase = Provide[Container.createGameUseCase]):
    print("create_game", usecase, type(usecase).__name__)
    usecase.execute(9527)

    return "<p>Game created!</p>"

