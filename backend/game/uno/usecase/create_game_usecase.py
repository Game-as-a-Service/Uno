
from uno.model.game import Game
from uno.usecase.game_repository import GameRepository

class CreateGameUseCase:

    def __init__(self, repository: GameRepository):
        self.repository = repository

    def execute(self, game_id: int):
        try:
            # 查
                    
            # 改
            game = Game.createGame(game_id)
            # 存
            self.repository.save_or_update(game)
            # 推？
        except ValueError as e:
            print(e)

        except Exception as e:
            # pass
            print(e)


