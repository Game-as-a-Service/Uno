from uno.usecase.game_repository import GameRepository
from uno.usecase.deck_repository import DeckRepository
from uno.model.game import GameState
from .base_use_case import BaseUseCase, BaseUseCaseInput, BaseUseCaseOutput
from uno.model.game import Game
class PlayCardUsecaseInput(BaseUseCaseInput):
    game_id: int
    player_id: int
    index: int

class PlayCardUsecaseOutput(BaseUseCaseOutput):
    game: Game = None

class PlayCardUsecase(BaseUseCase):

    def __init__(self,
                 gameRepo: GameRepository,
                 deckRepo: DeckRepository,
                 ):
        self.gameRepo = gameRepo
        self.deckRepo = deckRepo

    def execute(self, input: PlayCardUsecaseInput, output: PlayCardUsecaseOutput):
        
        try:
            # 查
            game_id = input.game_id
            game = self.gameRepo.get(game_id)

            player_id = input.player_id
            deck = self.deckRepo.get_by_player_id(player_id)

            if (deck is None):
                raise Exception("deck not found")
            
            # 改
            card_index = input.index
            deck.useCard(card_index)
            if len(deck.cardList) == 0:
                game.state = GameState.end

            # 存
            self.gameRepo.save_or_update(game)
            self.deckRepo.save_or_update(deck)
        
            # 推？
            output.game = game
            output.isSuccess = True

        except Exception as e:
            output.error = e
            output.isSuccess = False

        return output