
import abc
from typing import List, Optional
from .game import Game

class GameRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def save_or_update(self, game: Game) -> str:
        # TODO: Should return game id.
        pass

    @abc.abstractmethod
    def get(self, game_id) -> Optional[Game]:
        pass

    @abc.abstractmethod
    def find_waiting_game(self) -> List[Game]:
        pass
    