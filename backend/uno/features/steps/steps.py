
# https://github.com/ictar/python-doc/blob/master/Testing/%E5%9C%A8Python%E4%B8%AD%E4%BD%BF%E7%94%A8Behave%E6%9D%A5%E5%BC%80%E5%A7%8B%E8%A1%8C%E4%B8%BA%E6%B5%8B%E8%AF%95.md

from behave import *
from src.usecase.create_game_usecase import CreateGameUseCase
from src.repository.game_repository_in_memory_impl import GameRepositoryInMemoryImpl
from src.model.game import Game

@given(u'遊戲編號: {id:d}')
def step_impl(context, id):
    context.gameId = id

@when(u'系統建立遊戲')
def step_impl(context):
    usecase = CreateGameUseCase(GameRepositoryInMemoryImpl())
    context.usecase = usecase
    usecase.execute(context.gameId)

@then(u'存在一個遊戲: {id:d}')
def step_impl(context, id):
    usecase: GameRepositoryInMemoryImpl = context.usecase
    game: Game = usecase.repository.get(context.gameId)
    assert game is not None
    assert game.id == id

