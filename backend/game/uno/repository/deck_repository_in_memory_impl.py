
from typing import Optional
from uno.model.deck import Deck
from uno.usecase.deck_repository import DeckRepository
from .base_repository_memory_impl import BaseRepositoryInMemoryImpl
from .singleton import singleton

@singleton
class DeckRepositoryInMemoryImpl(BaseRepositoryInMemoryImpl[Deck], DeckRepository):
    
    def get_by_player_id(self, player_id: int) -> Optional[Deck]:
        
        for object in self.object_list:
            if getattr(object, "playerId") == player_id:
                return object
        return None

