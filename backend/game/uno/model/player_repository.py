
import abc
from typing import Optional
from .player import Player

class PlayerRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def save_or_update(self, player: Player) -> str:
        # TODO: Should return game id.
        pass

    @abc.abstractmethod
    def get(self, game_id) -> Optional[Player]:
        pass