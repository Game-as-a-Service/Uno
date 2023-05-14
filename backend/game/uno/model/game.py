
from enum import Enum, unique
from typing import List, Optional

@unique
class GameState(Enum):
    waiting = 1
    preparing = 2
    playing = 3
    end = 4

class Game:

    id = 0
    state = GameState.waiting
    players: List[int] = []

    @property
    def host(self) -> Optional[int]:
        if len(self.players) == 0:
            return None
        return self.players[0]

    @staticmethod
    def createGame(id: int):
        result = Game(id, GameState.waiting)
        return result

    def __init__(self, id: int, state: GameState):
        self.id = id
        self.state = state

    def joinPlayer(self, player_id: int):
        self.players.append(player_id)