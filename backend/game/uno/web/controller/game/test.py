from uno.usecase.start_game_usecase import StartGameUseCase, StartGameUseCaseInput, StartGameUseCaseOutput
from uno.usecase.test_usecase import Testusecase
from dependency_injector.wiring import inject, Provide
from uno.web.containers import Container

@inject
def test2(usecase: Testusecase = Provide[Container.testUsecase]):
    print(type(usecase))
    output = usecase.execute()
    print(output)
    return output

