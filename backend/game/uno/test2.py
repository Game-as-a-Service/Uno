
from model.player import Player

def player1do():
    p = Player()
    result = p.do_add_plus2(-1, 2)
    print(result)
    return result

def player2do():
    p = Player()
    result = p.do_add_plus2(-1, 2)
    print(result)
    return result

def allPlayerDo():

    result1 = player1do()
    if result1['isSucess'] == False:
        return False
    
    result2 = player2do()
    if result2['isSucess'] == False:
        return False
    
    return True

allPlayerDo() # 錯誤總管