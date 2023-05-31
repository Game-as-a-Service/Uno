
from typing import Any


class Player:

    '''def do_add_plus1(self, a: int, b: int) -> int:

        if (a < 0):
            return -1 #magic number # 隱喻
        
        return a + b
    
    def do_add_plus2(self, a: int, b: int) -> Any:

        # pre condition
        if (a < 0):
            return {
                'isSucess': False,
            }
        
        # ....

        return {
            'isSucess': True,
            'result': a + b,
        }
    
    def do_add_plus3(self, a: int, b: int) -> Any:

        # pre condition
        if (a < 0):
            raise Exception("a must > 0")
            # return
            print("after return")
            pass
        
        # ....

        return a + b
        '''
    
    def __init__(self, deck, playerstate )
        self.deck=deck
        self.playerstate=playerstate
        
    def unoState(deck:int, player_id):
        if game.players.deck.number == 1: