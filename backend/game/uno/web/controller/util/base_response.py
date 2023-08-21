
import abc
from enum import IntEnum, unique
from typing import Any

@unique
class PresentType(IntEnum):

    unknown = 0
    """ 未知 """

    web = 1
    """ 網頁 """

    json = 2
    """ json """

class BasePresenter(metaclass=abc.ABCMeta):

    presentType = PresentType.unknown

    def detectPresentType(self, aDict: dict):
        """ 從物件中查找 presentType key: present """

        present = aDict.get("present")
        if present == "web":
            self.presentType = PresentType.web
        else:
            self.presentType = PresentType.json

    @abc.abstractmethod
    def presentWeb(self) -> Any:
        """ 將結果轉換成網頁格式 """
        raise NotImplementedError("presentWeb not implemented")
    
    @abc.abstractmethod
    def presentJson(self) -> Any:
        """ 將結果轉換成 anguler 格式 """
        raise NotImplementedError("presentJson not implemented")
    
    def present(self) -> Any:
        """ 將結果轉換成任何格式 """
        if self.presentType == PresentType.web:
            return self.presentWeb()
        elif self.presentType == PresentType.json:
            return self.presentJson()
        else:
            raise NotImplementedError("present not implemented unknown")
