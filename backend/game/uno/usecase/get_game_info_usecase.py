
from typing import List
from uno.usecase.game_repository import GameRepository
from uno.usecase.player_repository import PlayerRepository
from uno.usecase.deck_repository import DeckRepository

class GetGameInfoUseCase:
    def __init__(self, 
                 gameRepo: GameRepository,
                 playerRepo: PlayerRepository,
                 deckRepo: DeckRepository,        
        ):
        self.gameRepo = gameRepo
        self.playerRepo = playerRepo
        self.deckRepo = deckRepo

    def execute(self, game_id: int):
        
        result: List[str] = []
        game = self.gameRepo.get(game_id)
        if game is None:
            return result

        result.append(f'Game: {game}\n')
        
        for player_id in game.players:
            player = self.playerRepo.get(player_id)
            result.append(f'Player: {player}\n')

            deck = self.deckRepo.get_by_player_id(player_id)
            result.append(f'Deck: {deck}\n')

        return result