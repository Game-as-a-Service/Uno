
from typing import List
from uno.model.game import Game
from uno.usecase.game_repository import GameRepository
from typing import Optional

class GameRepositoryInMemoryImpl(GameRepository):

    data_list: List[Game] = []

    def save_or_update(self, game: Game):
        if not game in self.data_list:
            self.data_list.append(game)
        return game.id
    
    def get(self, id) -> Optional[Game] :
        for game in self.data_list:
            if game.id == id:
                return game
        return None
