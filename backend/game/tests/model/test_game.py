
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


def test_joinGame():
        
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
