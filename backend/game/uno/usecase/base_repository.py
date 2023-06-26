import abc
from typing import Optional, TypeVar, Generic

# 泛形
T = TypeVar('T')

class BaseRepository(Generic[T], metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def save_or_update(self, object: T) -> str:
        raise NotImplementedError("save_or_update not implemented")

    @abc.abstractmethod
    def get(self, id) -> Optional[T]:
        raise NotImplementedError("get not implemented")
    