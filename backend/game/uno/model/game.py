
from enum import Enum, unique

@unique
class GameState(Enum):
    waiting = 1
    preparing = 2
    playing = 3
    end = 4

class Game:

    id = 0
    state = GameState.waiting

    @staticmethod
    def createGame(id: int):
        result = Game(id, GameState.waiting)
        return result

    def __init__(self, id: int, state: GameState):
        self.id = id
        self.state = state
