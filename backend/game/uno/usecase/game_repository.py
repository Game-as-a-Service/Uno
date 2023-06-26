
import abc
from typing import Optional
from .base_repository import BaseRepository
from ..model.game import Game

class GameRepository(BaseRepository[Game]):
    
    @abc.abstractmethod
    def findPlayerInGame(self, player_id) -> Optional[Game]:
        pass

    @abc.abstractmethod
    def getMaxId(self) -> int:
        pass
    