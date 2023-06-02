from typing import List
from card import Card

class Deck:

    def __init__(self, player: int, cardList: List[Card]):
        self.player: int = player
        self.cardList = cardList
