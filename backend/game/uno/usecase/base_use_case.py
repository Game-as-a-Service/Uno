
import abc

class BaseUseCaseInput(metaclass=abc.ABCMeta):
    """ command 輸入 """

    pass

class BaseUseCaseOutput(metaclass=abc.ABCMeta):
    """ command 輸出 """
    
    @abc.abstractmethod
    def onSuccess(self):
        """ command 執行成功 """
        raise NotImplementedError("onSuccess not implemented")
    
    @abc.abstractmethod
    def onError(self):
        """ command 執行失敗 """
        raise NotImplementedError("onError not implemented")

class BaseUseCase(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def execute(self, input: BaseUseCaseInput, output: BaseUseCaseOutput):
        """ 執行 command """
        raise NotImplementedError("execute not implemented")
    