
from uno.model.game import Game
from uno.usecase.game_repository import GameRepository

class StartGameUseCase:

    def __init__(self, gameRepo: GameRepository):
        self.gameRepo = gameRepo

    def execute(self, game_id: int, player_id: int):
        try:
            # 查
            game = self.gameRepo.get(game_id)
            
            if game is None:
                raise ValueError("Game not found")
                    
            # 改
            game.start(player_id)

            # 存
            self.gameRepo.save_or_update(game)

            # 推？
        except ValueError as e:
            print(e)

        except Exception as e:
            # pass
            print(e)

        return game