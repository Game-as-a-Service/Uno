
# pytest -q tests/model/test_game.py

import pytest
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
    with pytest.raises(Exception) as e:
        game.joinPlayer(player_id_K)

    #Then
    assert str(e) == "too many players"

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
    game.state = GameState.playing
    player_id_A = 101
    player_id_B = 102
    player_id_C = 103
    game.joinPlayer(player_id_A)
    game.joinPlayer(player_id_B)

    #Act > when
    with pytest.raises(Exception) as e:
        game.joinPlayer(player_id_C)

    #then
    assert str(e) == "Game is beginning"

