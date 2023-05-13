
from uno.model.game import Game
from uno.model.game_repository import GameRepository

class CreateGameUseCase:

    def __init__(self, repository: GameRepository):
        self.repository = repository

    def execute(self, game_id: int):
        game = Game.createGame(game_id)
        self.repository.save_or_update(game)
