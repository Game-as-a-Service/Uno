
from uno.model.player import Player
from uno.usecase.player_repository import PlayerRepository
from .base_repository_memory_impl import BaseRepositoryInMemoryImpl

class PlayerRepositoryInMemoryImpl(BaseRepositoryInMemoryImpl[Player], PlayerRepository):
    pass
