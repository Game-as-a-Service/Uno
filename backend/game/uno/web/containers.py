
from dependency_injector import containers, providers
from uno.repository.game_repository_in_memory_impl import GameRepositoryInMemoryImpl
from uno.usecase.create_game_usecase import CreateGameUseCase

# 教學
# https://python-dependency-injector.ets-labs.org/tutorials/flask.html
class Container(containers.DeclarativeContainer):

    # 對 views.py 的依賴
    wiring_config = containers.WiringConfiguration(
        modules=[".views", ".controller.game.create_game"]
    )

    # ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====
    # 以下是所有的依賴
    
    # repository
    gameRepository = providers.Factory(
        GameRepositoryInMemoryImpl
    )

    # usecase
    createGameUseCase = providers.Factory(
        CreateGameUseCase,
        repository=gameRepository,
    )

    