
from dependency_injector import containers, providers

from uno.repository.game_repository_in_memory_impl import GameRepositoryInMemoryImpl
from uno.repository.player_repository_in_memory_impl import PlayerRepositoryInMemoryImpl
from uno.repository.deck_repository_in_memory_impl import DeckRepositoryInMemoryImpl

from uno.usecase.get_game_info_usecase import GetGameInfoUseCase
from uno.usecase.create_game_usecase import CreateGameUseCase
from uno.usecase.join_game_usecase import JoinGameUseCase
from uno.usecase.start_game_usecase import StartGameUseCase
from uno.usecase.play_card_usecase import PlayCardUsecase
from uno.usecase.check_player_usecase import CheckPlayerUseCase
from uno.usecase.get_game_list_usecase import GetGameListUseCase

# 教學
# https://python-dependency-injector.ets-labs.org/tutorials/flask.html
class Container(containers.DeclarativeContainer):

    # 對 views.py 的依賴
    wiring_config = containers.WiringConfiguration(
        modules=[
            ".views", 
            ".controller.game.get_game_info",
            ".controller.game.create_game", 
            ".controller.game.join_game",
            ".controller.game.start_game",
            ".controller.game.play_card",
            ".controller.game.check_player",
            ".controller.game.get_game_list",
        ]
    )

    # ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====
    # 以下是所有的依賴
    
    # repository
    gameRepository = providers.Singleton(
        GameRepositoryInMemoryImpl
    )

    playerRepository = providers.Singleton(
        PlayerRepositoryInMemoryImpl
    )

    deckRepository = providers.Singleton(
        DeckRepositoryInMemoryImpl
    )

    # usecase
    getGameInfoUseCase = providers.Singleton(
        GetGameInfoUseCase,
        gameRepo=gameRepository,
        playerRepo=playerRepository,
        deckRepo=deckRepository,
    )

    createGameUseCase = providers.Singleton(
        CreateGameUseCase,
        gameRepo=gameRepository,
    )

    joinGameUseCase = providers.Singleton(
        JoinGameUseCase,
        gameRepo=gameRepository,
        playerRepo=playerRepository,
    )

    startGameUseCase = providers.Singleton(
        StartGameUseCase,
        gameRepo=gameRepository,
        deckRepo=deckRepository,
    )

    playCardGameUseCase = providers.Singleton(
        PlayCardUsecase,
        gameRepo=gameRepository,
        deckRepo=deckRepository,
    )

    checkPlayerUsecase = providers.Singleton(
        CheckPlayerUseCase,
        gameRepo=gameRepository,
        playerRepo=playerRepository,
    )
    
    getGameListUseCase = providers.Singleton(
        GetGameListUseCase,
        gameRepo=gameRepository,
    )