
# pytest -q tests/model/test_game.py

from game.uno.model.game import Game, GameState

def test_createGame():
    
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




    
