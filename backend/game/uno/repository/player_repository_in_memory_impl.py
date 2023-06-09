
from typing import List
from uno.model.player import Player
from uno.usecase.player_repository import PlayerRepository
from typing import Optional

class PlayerRepositoryInMemoryImpl(PlayerRepository):

    data_list: List[Player] = []

    def save_or_update(self, player: Player):
        if not player in self.data_list:
            self.data_list.append(player)
        return player.id
    
    def get(self, id) -> Optional[Player] :
        for player in self.data_list:
            if player.id == id:
                return player
        return None
