
from uno.model.game import Game
from uno.usecase.game_repository import GameRepository
from .base_repository_memory_impl import BaseRepositoryInMemoryImpl
from .singleton import singleton

class GameRepositoryInMemoryImpl(BaseRepositoryInMemoryImpl[Game], GameRepository):
    pass


