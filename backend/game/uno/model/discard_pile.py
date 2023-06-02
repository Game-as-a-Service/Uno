
from typing import List
from .card import Card

class DiscardPile:

    def __init__(self, gameId: int, cardList: List[Card]):
        self.gameId: int = gameId
        self.cardList = cardList

    def addCard(self, card: Card) -> None:
        self.cardList.append(card)

    def isAccept(self, card: Card) -> bool:
        return True