
from typing import Optional
from uno.usecase.game_repository import GameRepository
from uno.usecase.player_repository import PlayerRepository
from uno.model.player import Player
from .base_use_case import BaseUseCase, BaseUseCaseInput, BaseUseCaseOutput
from uno.model.game import Game

class JoinGameUseCaseInput(BaseUseCaseInput):
    game_id: int = 0
    player_id: int = 0

class JoinGameUseCaseOutput(BaseUseCaseOutput):
    game: Optional[Game] = None

class JoinGameUseCase(BaseUseCase):

    def __init__(self, gameRepo: GameRepository, playerRepo: PlayerRepository):
        # print("JoinGameUseCase.__init__", gameRepo, playerRepo)
        self.gameRepo = gameRepo
        self.playerRepo = playerRepo

    def execute(self, input: JoinGameUseCaseInput, output: JoinGameUseCaseOutput):

        try:

            # 查
            game_id = input.game_id
            game = self.gameRepo.get(game_id)

            if (game is None):
                raise Exception("Game not found")
            
            player_id = input.player_id
            player = self.playerRepo.get(player_id)
            if player is None:
                player = Player(player_id)
                self.playerRepo.save_or_update(player)
        
            # 改
            game.joinPlayer(player_id)

            # 存
            self.gameRepo.save_or_update(game)
            
            # 推？
            output.game = game
            output.isSuccess = True

        except Exception as e:
            output.error = e
            output.isSuccess = False

        return output