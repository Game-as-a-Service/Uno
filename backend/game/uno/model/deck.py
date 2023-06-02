from typing import List
from .card import Card

class Deck:

    def __init__(self, player: int, cardList: List[Card]):
        self.player: int = player
        self.cardList = cardList

    def __gt__(self, other):
        if isinstance(other, Deck):
            return self.cardList[0].symbol > other.cardList[0].symbol
        else:
            raise Exception("cannot compare(>) Deck and {}".format(type(other)))
