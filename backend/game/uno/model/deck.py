from typing import List
from .card import Card

class Deck:

    def __init__(self, playerId: int, cardList: List[Card]):
        self.playerId: int = playerId
        self.cardList = cardList

    def __gt__(self, other):
        if isinstance(other, Deck):
            return self.cardList[0].symbol > other.cardList[0].symbol
        else:
            raise Exception("cannot compare(>) Deck and {}".format(type(other)))
        
    def addCard(self, card: Card) -> None:
        self.cardList.append(card) 
