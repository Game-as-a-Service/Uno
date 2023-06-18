
from typing import Optional
from uno.model.game import Game
from uno.usecase.game_repository import GameRepository
from .base_repository_memory_impl import BaseRepositoryInMemoryImpl
from .singleton import singleton

class GameRepositoryInMemoryImpl(BaseRepositoryInMemoryImpl[Game], GameRepository):
    
    def findPlayerInGame(self, player_id) -> Optional[Game]:
        
        for game in self.object_list:
            if player_id in game.players:
                return game
        return None


