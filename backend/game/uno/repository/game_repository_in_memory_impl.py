
from typing import List
from uno.model.game import GameState
from uno.model.game import Game
from uno.model.game_repository import GameRepository
from typing import Optional

class GameRepositoryInMemoryImpl(GameRepository):

    data_list: List[Game] = []

    def save_or_update(self, game: Game):
        if not game in self.data_list:
            self.data_list.append(game)
        return game.id
    
    def get(self, game_id) -> Optional[Game] :
        for game in self.data_list:
            if game.id == game_id:
                return game
        return None
    
    def find_waiting_game(self) -> List[Game]:

        aList = self.data_list
        result_list = []
        for data in aList:
            if data.state == GameState.waiting:
                result_list.append(data)

        # tdd 直接開發
        # function programming / object programming

        return [game for game in self.data_list if game.state == GameState.waiting]
