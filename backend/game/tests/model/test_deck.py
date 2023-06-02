
# pytest -q tests/model/test_deck.py

import pytest
from game.uno.model.deck import Deck
from game.uno.model.card import Card, CardSymbol, CardColor, CardFunction

def test_來比個大小():
    # Arrange
    deck_A = Deck(101, [Card(CardSymbol.N1, CardColor.Red, CardFunction.Nouse)])
    deck_B = Deck(101, [Card(CardSymbol.N8, CardColor.Red, CardFunction.Nouse)])
    deck_C = Deck(101, [Card(CardSymbol.N5, CardColor.Red, CardFunction.Nouse)])

    # Act
    result_BA = deck_B > deck_A
    result_BC = deck_B > deck_C

    # Assert
    assert result_BA == True
    assert result_BC == True