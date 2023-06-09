
from uno.web.containers import Container
from uno.usecase.join_game_usecase import JoinGameUseCase
from dependency_injector.wiring import inject, Provide

@inject
def join_game(usecase: JoinGameUseCase = Provide[Container.joinGameUseCase]):
    
    print("join_game", usecase, type(usecase).__name__)
    usecase.execute(9527, 101)

    return "<p>join_game!</p>"