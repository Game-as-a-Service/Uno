
from typing import List
from uno.usecase.game_repository import GameRepository
from uno.usecase.player_repository import PlayerRepository
from uno.usecase.deck_repository import DeckRepository
from .base_use_case import BaseUseCase, BaseUseCaseInput, BaseUseCaseOutput
from uno.model.game import Game
from uno.model.player import Player
from uno.model.deck import Deck
from typing import Optional

class GetGameInfoUseCaseInput(BaseUseCaseInput):
    game_id: int = 0

class GetGameInfoUseCaseOutput(BaseUseCaseOutput):
    game: Optional[Game] = None
    player_list: List[Player] = []
    deck_list: List[Deck] = []

class GetGameInfoUseCase(BaseUseCase):
    def __init__(self, 
                 gameRepo: GameRepository,
                 playerRepo: PlayerRepository,
                 deckRepo: DeckRepository,        
        ):
        self.gameRepo = gameRepo
        self.playerRepo = playerRepo
        self.deckRepo = deckRepo

    def execute(self, input: GetGameInfoUseCaseInput, output: GetGameInfoUseCaseOutput):
        
        try:
            # 查
            game_id = input.game_id
            game = self.gameRepo.get(game_id)
        
            if game is not None:

                player_list: List[Player] = []
                deck_list: List[Deck] = []
                for player_id in game.players:
                    player = self.playerRepo.get(player_id)
                    player_list.append(player)

                    deck = self.deckRepo.get_by_player_id(player_id)
                    deck_list.append(deck)

                output.game = game
                output.player_list = player_list
                output.deck_list = deck_list
            # 改
            # 存
            # 推？
            output.isSuccess = True

        except Exception as e:
            output.error = e
            output.isSuccess = False

        return output