from random import shuffle
from typing import List
from .card import Card

class Drawpile:

    def __init__(self, gameId: int, cardList: List[Card]):
        self.gameId: int = gameId
        self.cardList: List[Card] = cardList

    def addCardList(self, cardList: List[Card]) -> None:
        self.cardList.extend(cardList)

    def shuffleCard(self) -> None:
        shuffle(self.cardList)

    def draw(self) -> Card:
        return self.cardList.pop(0)