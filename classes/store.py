from classes.storage import Storage
from utils import load_log


class Store(Storage):
    def __init__(self, items: dict[str, int], capacity=100):
        deleted_keys: list[str] = [k for k, v in items.items() if v == 0]
        for dk in deleted_keys:
            items.pop(dk)
        self._items = items
        self._capacity = capacity

    def add(self, title: str, amount: int) -> None:
        if amount <= self._capacity:
            self._items[title] = self._items.get(title, 0)
            self._items[title] += amount
            self._capacity -= amount
        else:
            print(load_log('store/add'))

    def remove(self, title: str, amount: int) -> None:
        if title not in self._items.keys():
            raise KeyError(title)
        if 0 < amount <= (item := self._items[title]):
            self._items[title] = item
            self._items[title] -= amount
            self._capacity += amount
        else:
            print(load_log('rmv/error'))
        if not self._items[title]:
            self._items.pop(title)

    def get_free_space(self) -> int:
        return self._capacity - sum(self._items.values())

    def get_items(self) -> dict[str, int]:
        return self._items

    def get_unique_items_count(self) -> int:
        return len([v for v in self._items.values() if v == 1])
