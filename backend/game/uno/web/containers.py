
from dependency_injector import containers, providers

from uno.repository.game_repository_in_memory_impl import GameRepositoryInMemoryImpl
from uno.repository.player_repository_in_memory_impl import PlayerRepositoryInMemoryImpl

from uno.usecase.create_game_usecase import CreateGameUseCase
from uno.usecase.join_game_usecase import JoinGameUseCase
from uno.usecase.start_game_usecase import StartGameUseCase

# 教學
# https://python-dependency-injector.ets-labs.org/tutorials/flask.html
class Container(containers.DeclarativeContainer):

    # 對 views.py 的依賴
    wiring_config = containers.WiringConfiguration(
        modules=[
            ".views", 
            ".controller.game.create_game", 
            ".controller.game.join_game",
            ".controller.game.start_game",
        ]
    )

    # ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====
    # 以下是所有的依賴
    
    # repository
    gameRepository = providers.Factory(
        GameRepositoryInMemoryImpl
    )

    playerRepository = providers.Factory(
        PlayerRepositoryInMemoryImpl
    )

    # usecase
    createGameUseCase = providers.Factory(
        CreateGameUseCase,
        gameRepo=gameRepository,
    )

    joinGameUseCase = providers.Factory(
        JoinGameUseCase,
        gameRepo=gameRepository,
        playerRepo=playerRepository,
    )

    startGameUseCase = providers.Factory(
        StartGameUseCase,
        gameRepo=gameRepository,
    )
    