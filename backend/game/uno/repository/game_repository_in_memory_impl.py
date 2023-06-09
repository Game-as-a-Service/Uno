
from uno.model.game import Game
from uno.usecase.game_repository import GameRepository
from .base_repository_memory_impl import BaseRepositoryInMemoryImpl

class GameRepositoryInMemoryImpl(BaseRepositoryInMemoryImpl[Game], GameRepository):
    pass


