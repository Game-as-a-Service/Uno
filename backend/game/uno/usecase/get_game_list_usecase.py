
from typing import List
from uno.usecase.game_repository import GameRepository
from .base_use_case import BaseUseCase, BaseUseCaseInput, BaseUseCaseOutput
from uno.model.game import Game
from typing import Optional

class GetGameListUseCaseInput(BaseUseCaseInput):
    pass

class GetGameListUseCaseOutput(BaseUseCaseOutput):
    game_list: List[Game] = []

class GetGameListUseCase(BaseUseCase):
    def __init__(self, 
            gameRepo: GameRepository,
        ):
        self.gameRepo = gameRepo

    def execute(self, input: GetGameListUseCaseInput, output: GetGameListUseCaseOutput):

        try:
            # 查
            game_list = self.gameRepo.get_all()

            # 改
            # 存
            # 推？
            output.game_list = game_list
            output.isSuccess = True
        
        except Exception as e:
            output.error = e
            output.isSuccess = False

        return output