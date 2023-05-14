
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
