
# pytest -q tests/model/test_card.py

import pytest
from game.uno.model.card import Card, CardSymbol, SimpleCardColor, NumberCardSymbol

def test_所有的牌數量():

    # Arrange

    # Act
    cardList = Card.allCard()

    # Assert
    # https://service.mattel.com//instruction_sheets/GYH69-Eng.pdf
    for color in SimpleCardColor:
        cardInColor = list(filter(lambda card: card.color == color, cardList))
        numberCardInColor = list(filter(lambda card: card.symbol in NumberCardSymbol, cardInColor))
        assert len(numberCardInColor) == 19

        drawTwoCardInColor = list(filter(lambda card: card.symbol == CardSymbol.DrawTwo, cardInColor))
        assert len(drawTwoCardInColor) == 2

        reverseCardInColor = list(filter(lambda card: card.symbol == CardSymbol.Reverse, cardInColor))
        assert len(reverseCardInColor) == 2

        skipCardInColor = list(filter(lambda card: card.symbol == CardSymbol.Skip, cardInColor))
        assert len(skipCardInColor) == 2

    wildCard = list(filter(lambda card: card.symbol == CardSymbol.Wild, cardList))
    assert len(wildCard) == 8

    wildDrawFourCard = list(filter(lambda card: card.symbol == CardSymbol.WildDrawFour, cardList))
    assert len(wildDrawFourCard) == 4

    assert len(cardList) == 112