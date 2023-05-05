
from enum import Enum, unique

@unique
class GameState(Enum):
    Created = 1
    Started = 2
    Finished = 3

class Game:

    id = 0
    state = GameState.Created

    @staticmethod
    def createGame(id: int):
        result = Game(id, GameState.Created)
        return result

    def __init__(self, id: int, state: GameState):
        self.id = id
        self.state = state
