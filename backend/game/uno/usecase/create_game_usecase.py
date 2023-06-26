
from uno.model.game import Game
from typing import Optional
from uno.usecase.game_repository import GameRepository
from .base_use_case import BaseUseCase, BaseUseCaseInput, BaseUseCaseOutput

class CreateGameUseCaseInput(BaseUseCaseInput):
    game_id: int = 0

class CreateGameUseCaseOutput(BaseUseCaseOutput):
    game: Optional[Game] = None

class CreateGameUseCase(BaseUseCase):

    def __init__(self, gameRepo: GameRepository):
        # print("CreateGameUseCase.__init__", gameRepo)
        self.gameRepo = gameRepo

    def execute(self, input: CreateGameUseCaseInput, output: CreateGameUseCaseOutput):

        try:
            # 查
            game = self.gameRepo.get(input.game_id)
                    
            # 改
            if game is None:
                game = Game.createGame(input.game_id)

            # 存
            self.gameRepo.save_or_update(game)

            # 推？
            output.game = game
            output.isSuccess = True

        except Exception as e:
            output.error = e
            output.isSuccess = False

        return output

