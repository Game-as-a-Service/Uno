
import abc
from typing import Optional
from .base_repository import BaseRepository
from ..model.deck import Deck

class DeckRepository(BaseRepository[Deck]):
    
    @abc.abstractmethod
    def get_by_player_id(self, player_id: int) -> Optional[Deck]:
        pass
    