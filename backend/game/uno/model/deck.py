import json
from typing import List
from .uno_error import UnoError
from .card import Card

class Deck:

    def __init__(self, playerId: int, cardList: List[Card]):
        self.playerId: int = playerId
        self.cardList = cardList

    def __str__(self):
        result = {}
        result["playerId"] = self.playerId

        result["cardList"] = ""
        for card in self.cardList:
            result["cardList"] += f",{card}"
        
        return json.dumps(result)

    def __gt__(self, other):
        if isinstance(other, Deck):
            return self.cardList[0].symbol > other.cardList[0].symbol
        else:
            raise UnoError(f"cannot compare(>) Deck and {type(other)}")
        
    def addCard(self, card: Card) -> None:
        self.cardList.append(card)

    def useCard(self, index: int) -> Card:
        return self.cardList.pop(index)
