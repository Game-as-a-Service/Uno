
import abc
from enum import IntEnum, unique
from typing import Any, Optional
class BaseUseCaseInput(metaclass=abc.ABCMeta):
    """ command 輸入 """

    pass

class BaseUseCaseOutput(metaclass=abc.ABCMeta):
    """ command 輸出 """

    isSuccess: Optional[bool] = None
    """ command 是否成功 預設為 None 未知 """

    error = Exception('Unknown error')
    """ command 錯誤原因 """

class BaseUseCase(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def execute(self, input: Any, output: Any):
        """ 執行 command """
        raise NotImplementedError("execute not implemented")
    