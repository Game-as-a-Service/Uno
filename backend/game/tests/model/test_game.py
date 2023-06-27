
# pytest -q tests/model/test_game.py

import pytest
from game.uno.model.card import Card, CardColor, CardFunction, CardSymbol
from game.uno.model.deck import Deck
from game.uno.model.draw_pile import Drawpile
from game.uno.model.game import Game, GameState

def test_創立遊戲():
    
    # Arrange
    id = 1

    # Act
    game = Game.createGame(id)

    # Assert
    assert game.id == id
    assert game.state == GameState.waiting


def test_頭一個玩家加入():
        
    # Arrange
    game_id = 1
    game = Game.createGame(game_id)
    player_id = 101

    # Act
    game.joinPlayer(player_id)

    # Assert
    assert len(game.players) == 1
    assert game.state == GameState.waiting
    assert game.host == player_id


def test_有第二個人加入():

    # Arrange > given
    game_id = 2
    game = Game.createGame(game_id)
    player_id_A = 101
    game.joinPlayer(player_id_A)
    player_id_B = 102
    
    # Act > when
    game.joinPlayer(player_id_B)

    # Assert > then
    assert len(game.players) == 2
    assert game.state == GameState.waiting
    assert game.host == player_id_A

def test_重複的玩家加入():

    # Arrange > given
    game_id = 1
    game = Game.createGame(game_id)
    player_id_A = 101
    game.joinPlayer(player_id_A)

    # raise Exception("player already in game") # 產生錯誤

    # Act > when
    with pytest.raises(Exception) as exception_info:
        game.joinPlayer(player_id_A)
    
    #Then    
    assert exception_info.value.args[0] == "player already in game"

    # 如果沒有發生錯誤 則這個測試 竟然也不會報錯
    # try:
    #     game.joinPlayer(player_id_A)
    # except Exception as exception_info:
    #     # 因為 有 raise 才會跑到這一行 
    #     assert str(exception_info) == "player already in game"

def test_第11人():
     # Arrange > given
    game_id = 2
    game = Game.createGame(game_id)
    player_id_A = 101
    player_id_B = 102
    player_id_C = 103
    player_id_D = 104
    player_id_E = 105
    player_id_F = 106
    player_id_G = 107
    player_id_H = 108
    player_id_I = 109
    player_id_J = 110
    player_id_K = 111
    game.joinPlayer(player_id_A)
    game.joinPlayer(player_id_B)
    game.joinPlayer(player_id_C)
    game.joinPlayer(player_id_D)
    game.joinPlayer(player_id_E)
    game.joinPlayer(player_id_F)
    game.joinPlayer(player_id_G)
    game.joinPlayer(player_id_H)
    game.joinPlayer(player_id_I)
    game.joinPlayer(player_id_J)

    # Act > when
    with pytest.raises(Exception) as exception_info:
        game.joinPlayer(player_id_K)

    #Then
    assert exception_info.value.args[0] == "too many players"

    # try:
    #     game.joinPlayer(player_id_K)
    # except Exception as exception_info:
    #     assert exception_info.value.args[0] == "too many players"

def test_遊戲是等待中才能加入():
    #Arrange > given
    game_id = 2
    game = Game.createGame(game_id)
    game.state = GameState.waiting
    player_id_A = 101
    player_id_B = 102
    player_id_C = 103
    game.joinPlayer(player_id_A)
    game.joinPlayer(player_id_B)

    #Act > when
    game.joinPlayer(player_id_C)
        
    #then
    assert len(game.players) == 3
    assert game.state == GameState.waiting


def test_非等待中狀態不能加入():
    #Arrange > given
    game_id = 2
    game = Game.createGame(game_id)
    player_id_A = 101
    player_id_B = 102
    player_id_C = 103
    game.joinPlayer(player_id_A)
    game.joinPlayer(player_id_B)
    game.state = GameState.playing

    #Act > when
    with pytest.raises(Exception) as exception_info:
        game.joinPlayer(player_id_C)

    #then
    assert exception_info.value.args[0] == "Game is beginning"

def test_只有房主能開始遊戲():
    #Arrange > given
    game_id = 2
    game = Game.createGame(game_id)
    game.state = GameState.waiting
    player_id_A = 101
    player_id_B = 102
    player_id_C = 103
    game.joinPlayer(player_id_A)
    game.host == player_id_A
    game.joinPlayer(player_id_B)
    game.joinPlayer(player_id_C)

    #Act > when
    game.start(player_id_A)

    #then
    assert game.state==GameState.preparing

    
def test_非房主不能開始遊戲():
    #Arrange > given
    game_id = 2
    game = Game.createGame(game_id)
    game.state = GameState.waiting
    player_id_A = 101
    player_id_B = 102
    game.joinPlayer(player_id_A)
    game.host == player_id_A
    game.joinPlayer(player_id_B)

    #Act > when
    
    with pytest.raises(Exception) as exception_info:
        game.start(player_id_B)

    #then
    assert exception_info.value.args[0] == "Players access deny"



def test_1個人不能玩遊戲():
    #Arrange > given
    game_id = 2
    game = Game.createGame(game_id)
    game.state = GameState.waiting
    player_id_A = 101
    game.joinPlayer(player_id_A)
    game.host == player_id_A

    #Act > when
    with pytest.raises(Exception) as exception_info:
        game.start(player_id_A)

    #then
    assert exception_info.value.args[0] == "Players not enough"

'''
# 這個 example 還沒修正根本無法寫測試
def test_點數最大優先出牌():
    game_id = 2
    game = Game.createGame(game_id)
    game.players==3
    player_id_A = 101
    player_id_B = 102
    player_id_C = 103
    game.joinPlayer(player_id_A)
    game.joinPlayer(player_id_B)
    game.joinPlayer(player_id_C)
    game.state = GameState.preparing
    game.turn.append(player_id_A)
    game.players[0] == 1
    game.players[1] == 8
    game.players[2] == 5

    #Act > when   玩家B 先開始遊戲
    game.turn[0] == game.players[1]
    
    
    
    #then 可以翻開第一張牌
    assert drawpile.shuffleCard(cardcode)  
    assert game.host == player_id_A
    assert game.state == GameState.playing
    assert game.turn == game.players[1]
'''

def test_決定第一玩家():
    # Arrange
    game_id = 2
    game = Game.createGame(game_id)
    game.state = GameState.preparing
    game.players = [101, 102, 103]
    deck_A = Deck(101, [Card(CardSymbol.N1, CardColor.Red, CardFunction.Nouse)])
    deck_B = Deck(102, [Card(CardSymbol.N8, CardColor.Red, CardFunction.Nouse)])
    deck_C = Deck(103, [Card(CardSymbol.N5, CardColor.Red, CardFunction.Nouse)])

    # Act
    game.decideFirstPlayer([deck_A, deck_B, deck_C])

    # Assert
    assert game.turnPlayerId == 102

def test_只有一個人抽牌():
    # Arrange
    game_id = 2
    game = Game.createGame(game_id)
    game.state = GameState.preparing
    game.players = [101, 102, 103]
    deck_A = Deck(101, [Card(CardSymbol.N1, CardColor.Red, CardFunction.Nouse)])
    deck_B = Deck(102, [])
    deck_C = Deck(103, [])
    
    # Act
    new_card = Card(CardSymbol.N8, CardColor.Red, CardFunction.Nouse)
    deck_B.addCard(new_card)
    game.decideFirstPlayer([deck_A, deck_B, deck_C])

    # Assert
    assert game.turnPlayerId == 0