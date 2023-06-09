from uno.usecase.game_repository import GameRepository
from uno.usecase.deck_repository import DeckRepository
from uno.model.game import GameState

class PlayCardUsecase:

    def __init__(self,
                 gameRepo: GameRepository,
                 deckRepo: DeckRepository,
                 ):
        self.gameRepo = gameRepo
        self.deckRepo = deckRepo

    def execute(self, game_id: int , player_id: int, card_index: int):
        
        # 查
        game = self.gameRepo.get(game_id)
        deck = self.deckRepo.get_by_player_id(player_id)

        if (deck is None):
            raise Exception("deck not found")
        
        # 改
        deck.useCard(card_index)
        if len(deck.cardList) == 0:
             game.state = GameState.end

        # 存
        self.gameRepo.save_or_update(game)
        self.deckRepo.save_or_update(deck)
        
        # 推？
        return game