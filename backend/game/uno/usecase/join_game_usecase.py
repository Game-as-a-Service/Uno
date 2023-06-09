
from uno.usecase.game_repository import GameRepository
from uno.usecase.player_repository import PlayerRepository
from uno.model.player import Player

class JoinGameUseCase:

    def __init__(self, gameRepo: GameRepository, playerRepo: PlayerRepository):
        self.gameRepo = gameRepo
        self.playerRepo = playerRepo

    def execute(self, game_id: int, player_id: int):
        # 查
        game = self.gameRepo.get(game_id)

        if (game is None):
            raise Exception("Game not found")
        player = self.playerRepo.get(player_id)
        if player is None:
            player = Player(player_id)
            self.playerRepo.save_or_update(player)
        
        # 改
        game.joinPlayer(player_id)

        # 存
        self.gameRepo.save_or_update(game)
        
        # 推？
        return game