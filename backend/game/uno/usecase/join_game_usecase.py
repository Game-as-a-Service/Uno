
from uno.usecase.game_repository import GameRepository
from uno.usecase.player_repository import PlayerRepository

class JoinGameUseCase:

    def __init__(self, gameRepo: GameRepository, playerRepo: PlayerRepository):
        self.GameRepository = gameRepo
        self.PlayerRepository = playerRepo

    def execute(self, game_id: int, player_id: int):
        # 查
        game = self.GameRepository.get(game_id)

        if (game is None):
            raise Exception("Game not found")
        
        # 改
        game.joinPlayer(player_id)

        # 存
        self.GameRepository.save_or_update(game)
        
        # 推？
        return game