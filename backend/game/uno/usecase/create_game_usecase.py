
from uno.model.game import Game
from uno.usecase.game_repository import GameRepository

class CreateGameUseCase:

    def __init__(self, gameRepo: GameRepository):
        self.gameRepo = gameRepo

    def execute(self, game_id: int):
        try:
            # 查
                    
            # 改
            game = self.gameRepo.get(game_id)
            if game is None:
                game = Game.createGame(game_id)
            # 存
            self.gameRepo.save_or_update(game)
            # 推？
        except ValueError as e:
            print(e)

        except Exception as e:
            # pass
            print(e)

        return game

