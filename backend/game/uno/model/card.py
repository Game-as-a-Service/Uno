
from enum import IntEnum, unique
from typing import List

@unique
class CardSymbol(IntEnum):
    Unknown = -1
    N0 = 0
    N1 = 1
    N2 = 2
    N3 = 3
    N4 = 4
    N5 = 5
    N6 = 6
    N7 = 7
    N8 = 8
    N9 = 9
    Skip = 10
    Reverse = 11
    DrawTwo = 12
    Wild = 13
    WildDrawFour = 14

@unique
class CardColor(IntEnum):
    Blue = 1
    Green = 2
    Red = 3
    Yellow = 4
    Wild = 5

SimpleCardColor = [CardColor.Blue, CardColor.Green, CardColor.Red, CardColor.Yellow]

@unique
class CardFunction(IntEnum):
    Nouse = 1
    Skip = 2
    Reverse = 3
    DrawTwo = 4
    DrawFour = 6

class Card:

    @staticmethod
    def allCard():
        result: List[Card] = []

        for color in SimpleCardColor:

            # 0 各 1
            result.append(Card(CardSymbol.N0, color, CardFunction.Nouse))

            # 0 ~ 9 Skip Reverse DrawTwo 各 2
            for _ in range(2):
                result.append(Card(CardSymbol.N1, color, CardFunction.Nouse))
                result.append(Card(CardSymbol.N2, color, CardFunction.Nouse))
                result.append(Card(CardSymbol.N3, color, CardFunction.Nouse))
                result.append(Card(CardSymbol.N4, color, CardFunction.Nouse))
                result.append(Card(CardSymbol.N5, color, CardFunction.Nouse))
                result.append(Card(CardSymbol.N6, color, CardFunction.Nouse))
                result.append(Card(CardSymbol.N7, color, CardFunction.Nouse))
                result.append(Card(CardSymbol.N8, color, CardFunction.Nouse))
                result.append(Card(CardSymbol.N9, color, CardFunction.Nouse))
                result.append(Card(CardSymbol.Skip, color, CardFunction.Skip))
                result.append(Card(CardSymbol.Reverse, color, CardFunction.Reverse))
                result.append(Card(CardSymbol.DrawTwo, color, CardFunction.DrawTwo))

        # Wild WildDrawFour 各 4
        for _ in range(4):
            result.append(Card(CardSymbol.Wild, CardColor.Wild, CardFunction.Nouse))
            result.append(Card(CardSymbol.WildDrawFour, CardColor.Wild, CardFunction.DrawFour))

        return result
   
    def __init__(self, symbol: CardSymbol, color: CardColor, function: CardFunction):
        
        self.number: CardSymbol = symbol
        self.color: CardColor = color
        self.function: CardFunction = function

        '''
    def reverse(turn):
        game.turn.reverse()

    def skip():
        a=game.turn[0]
        game.turn.pop([0])
        game.turn.append(a)

    def wild():
        pass

    def wildDrawFour:
        pass
        '''








    
