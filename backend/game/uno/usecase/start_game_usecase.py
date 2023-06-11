

from uno.model.game import GameState
from uno.model.deck import Deck
from uno.model.card import Card, CardSymbol, CardColor, CardFunction
from uno.usecase.game_repository import GameRepository
from uno.usecase.deck_repository import DeckRepository
class StartGameUseCase:

    def __init__(self, 
                gameRepo: GameRepository,
                deckRepo: DeckRepository,         
        ):
        self.gameRepo = gameRepo
        self.deckRepo = deckRepo

    def execute(self, game_id: int, host_id: int):
        try:
            # 查
            game = self.gameRepo.get(game_id)
            
            if game is None:
                raise ValueError("Game not found")
                    
            # 改
            game.start(host_id)
            # TODO: 目前直接跳過抽牌動作
            game.state = GameState.playing
            # TODO: 直接給牌
            for player_id in game.players:
                deck = Deck(player_id, [Card(CardSymbol.N1, CardColor.Red, CardFunction.Nouse)])
                self.deckRepo.save_or_update(deck)

            # 存
            self.gameRepo.save_or_update(game)

            # 推？
        except ValueError as e:
            print(e)

        except Exception as e:
            # pass
            print(e)

        return game