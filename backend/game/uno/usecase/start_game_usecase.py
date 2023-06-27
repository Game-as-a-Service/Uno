

from uno.model.game import GameState
from uno.model.deck import Deck
from uno.model.card import Card, CardSymbol, CardColor, CardFunction
from uno.usecase.game_repository import GameRepository
from uno.usecase.deck_repository import DeckRepository
from .base_use_case import BaseUseCase, BaseUseCaseInput, BaseUseCaseOutput
from uno.model.game import Game

class StartGameUseCaseInput(BaseUseCaseInput):
    game_id: int = 0
    player_id: int = 0

class StartGameUseCaseOutput(BaseUseCaseOutput):
    game: Game = None

class StartGameUseCase(BaseUseCase):

    def __init__(self, 
                gameRepo: GameRepository,
                deckRepo: DeckRepository,         
        ):
        self.gameRepo = gameRepo
        self.deckRepo = deckRepo

    def execute(self, input: StartGameUseCaseInput, output: StartGameUseCaseOutput):
        try:
            # 查
            game_id = input.game_id
            game = self.gameRepo.get(game_id)
            
            if game is None:
                raise ValueError("Game not found")
            
            player_id = input.player_id
            # 改
            game.start(player_id)
            # TODO: 目前直接跳過抽牌動作
            game.state = GameState.playing
            # TODO: 直接給牌
            for player_id in game.players:
                deck = Deck(player_id, [
                    Card(CardSymbol.N1, CardColor.Red, CardFunction.Nouse),
                    Card(CardSymbol.N3, CardColor.Blue, CardFunction.Nouse),
                    Card(CardSymbol.N6, CardColor.Green, CardFunction.Nouse),
                ])
                self.deckRepo.save_or_update(deck)

            # 存
            self.gameRepo.save_or_update(game)

            # 推？
            output.game = game
            output.isSuccess = True

        except Exception as e:
            output.error = e
            output.isSuccess = False

        return output