
from typing import Optional
from uno.model.player import Player
from uno.usecase.game_repository import GameRepository
from uno.usecase.player_repository import PlayerRepository

class CheckPlayerUsecase:

    def __init__(self, gameRepo: GameRepository, playerRepo: PlayerRepository ):
        self.gameRepo = gameRepo
        self.playerRepo = playerRepo

    def execute(self, player_id: int):
        try:
            # 查
            player: Optional[Player] = None
            if player_id >= 0:
                player = self.playerRepo.get(player_id)
                
            # 改
            if player is None:
                target_id = player_id
                if target_id < 0:
                    target_id = self.playerRepo.getMaxId()
                player = Player(target_id)

            # 存
            self.playerRepo.save_or_update(player)

            # 查
            game = self.gameRepo.findPlayerInGame(player.id)

        except Exception as e:
            # pass
            print("error", e)

        return {
            "game": game,
            "player": player,
        }