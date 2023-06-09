
from typing import Generic, List, TypeVar
from typing import Optional

# 泛形
T = TypeVar('T')

class BaseRepositoryInMemoryImpl(Generic[T]):

    def __init__(self):
        self.object_list: List[T] = []

    def save_or_update(self, object: T):
        if not object in self.object_list:
            self.object_list.append(object)
        return getattr(object, "id")
    
    def get(self, id) -> Optional[T] :
        for object in self.object_list:
            if getattr(object, "id") == id:
                return object
        return None