
from uno.model.player import Player
from uno.usecase.player_repository import PlayerRepository
from .base_repository_memory_impl import BaseRepositoryInMemoryImpl
from .singleton import singleton

class PlayerRepositoryInMemoryImpl(BaseRepositoryInMemoryImpl[Player], PlayerRepository):
    
    def getMaxId(self) -> int:
        max_id = 0
        for player in self.object_list:
            if player.id > max_id:
                max_id = player.id
        return max_id + 1
