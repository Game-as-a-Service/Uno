
from typing import Optional
from uno.model.player import Player
from uno.usecase.game_repository import GameRepository
from uno.usecase.player_repository import PlayerRepository
from .base_use_case import BaseUseCase, BaseUseCaseInput, BaseUseCaseOutput
from uno.model.game import Game

class CheckPlayerUsecaseInput(BaseUseCaseInput):
    player_id: int = 0

class CheckPlayerUsecaseOutput(BaseUseCaseOutput):
    game: Optional[Game] = None
    player: Optional[Player] = None 

class CheckPlayerUsecase(BaseUseCase):

    def __init__(self, gameRepo: GameRepository, playerRepo: PlayerRepository):
        self.gameRepo = gameRepo
        self.playerRepo = playerRepo

    def execute(self, input: CheckPlayerUsecaseInput, output: CheckPlayerUsecaseOutput):
        try:
            # 查
            player_id = input.player_id
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

            # 推？
            game = self.gameRepo.findPlayerInGame(player.id)
            output.game = game
            output.player = player
            output.isSuccess = True

        except Exception as e:
            output.error = e
            output.isSuccess = False

        return output