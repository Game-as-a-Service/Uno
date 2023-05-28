
from enum import Enum, unique
from typing import List, Optional

@unique
class GameState(Enum):
    waiting = 1
    preparing = 2
    playing = 3
    end = 4

class Game:

    # id = 0 # static variable
    # state = GameState.waiting # static variable
    # players: List[int] = [] # static variable

    # attribte_a = 1234

    def __init__(self, id: int, state: GameState = GameState.waiting, players: List[int] = []):
        print("init")
        self.id = id
        self.state = state
        self.players = players

        # self.attribte_b = 5678
        # self._attribte_c = 9999
        # self._attribte_d = 9999
        
    # def get_attribte_c(self):
    #     return self._attribte_c
    # def set_attribte_c(self, value):
    #     self._attribte_c = value

    # Python setter 和 getter
    # https://medium.com/bryanyang0528/python-setter-%E5%92%8C-getter-6c08a9d37d46

    # @property # 裝飾器
    # def attribte_d(self):
    #     return self._attribte_d
    
    # @attribte_d.setter
    # def set_attribte_d(self, value):
    #     self._attribte_d = value

    @property
    def host(self) -> Optional[int]:
        if len(self.players) == 0:
            return None
        return self.players[0]

    # @host.setter #不寫代表唯讀
    # def set_host(self, value):
    #     pass

    @staticmethod
    def createGame(id: int):
        result = Game(id, GameState.waiting, [])
        return result

    def joinPlayer(self, player_id: int):

        # pre condition
        if len(self.players) >= 10:
            raise Exception("too many players")
        
        if player_id in self.players:
            raise Exception("player already in game")
        
        # do
        self.players.append(player_id)

# test = Game.createGame(1)

# something = test.attribte_a #取值
# test.attribte_a = 123 #賦值

# something = test.attribte_b #取值
# test.attribte_b = 123 #賦值

# something = test.get_attribte_c() #取值
# test.set_attribte_c(123) #賦值

# something = test.attribte_d #取值
# test.attribte_d = 123 #賦值
