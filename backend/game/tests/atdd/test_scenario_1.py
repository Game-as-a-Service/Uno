
# pytest -s -q tests/atdd/test_scenario_1.py

# https://python-dependency-injector.ets-labs.org/tutorials/flask.html#tests

from typing import Optional, TypeVar
from flask import Flask
from flask.testing import FlaskClient
from uno.model.game import GameState
from uno.web.containers import Container
from uno.usecase.game_repository import GameRepository

T = TypeVar('T')
def cast_away_optional(arg: Optional[T]) -> T:
    assert arg is not None
    return arg

def test_scenario_1(client: FlaskClient, app: Flask):
    """
    建立遊戲房間
    玩家 101 加入遊戲房間
    玩家 102 加入遊戲房間
    玩家 101 開始遊戲
    玩家 101 出牌 3 次
    遊戲結束
    """
    container: Container = app.container # type: ignore
    gameRepository: GameRepository = container.gameRepository.provided()
    
    # 建立遊戲房間
    response = client.post("/game/create_game", json = {
        "game_id": -1,
    })
    assert response.json["isSuccess"] == True # type: ignore
    game_id = response.json["game_id"] # type: ignore
    game = cast_away_optional(gameRepository.get(game_id))

    assert game != None
    assert game.id == game_id

    # 玩家 101 加入遊戲房間
    response = client.post("/game/join_game", json = {
        "game_id": game_id,
        "player_id": 101,
    })
    assert response.json["isSuccess"] == True # type: ignore

    # 玩家 102 加入遊戲房間
    response = client.post("/game/join_game", json = {
        "game_id": game_id,
        "player_id": 102,
    })
    assert response.json["isSuccess"] == True # type: ignore

    # 玩家 101 開始遊戲
    response = client.post("/game/start_game", json = {
        "game_id": game_id,
        "player_id": 101,
    })
    assert response.json["isSuccess"] == True # type: ignore

    # 玩玩家 101 出牌 3 次
    count = 3
    for _ in range(count):
        response = client.post("/game/play_card", json = {
            "game_id": game_id,
            "player_id": 101,
            "index": 0,
        })
        assert response.json["isSuccess"] == True # type: ignore

    # 遊戲結束
    assert game.state == GameState.end