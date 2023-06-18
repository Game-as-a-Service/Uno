
import abc
from .base_repository import BaseRepository
from ..model.player import Player

class PlayerRepository(BaseRepository[Player]):
    
    @abc.abstractmethod
    def getMaxId(self) -> int:
        pass