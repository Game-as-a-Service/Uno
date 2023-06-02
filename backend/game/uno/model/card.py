from backend import game


class Card:
   
    def __init__(self, face:bool, cardCode:list, number, color, function):
        self._face = face  #正面背面 true為正面
        self._number=number
        self._color=color
        self._function=function
        self._cardCode = cardCode[A0,A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12, 
                                 B0,B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11,B12,
                                 C0,C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,C12,
                                 D0,D1,D2,D3,D4,D5,D6,D7,D8,D9,D10,D11,D12]
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








    
