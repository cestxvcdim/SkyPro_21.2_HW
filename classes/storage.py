from abc import ABC, abstractmethod


class Storage(ABC):

    @abstractmethod
    def add(self, title: str, amount: int):
        pass

    @abstractmethod
    def remove(self, title: str, amount: int):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass
