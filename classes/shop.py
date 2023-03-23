from classes.store import Store
from classes.class_errors.limit import LimitError
from utils import load_log


class Shop(Store):
    def __init__(self, items: dict[str, int], capacity=20):
        deleted_keys: list[str] = [k for k, v in items.items() if v == 0]
        for dk in deleted_keys:
            items.pop(dk)
        if (length := len(items.keys())) <= LimitError().limit:
            super().__init__(items, capacity)
        else:
            raise LimitError(length)

    def add(self, title: str, amount: int) -> None:
        keys = self._items.keys()
        if title not in keys and len(keys) == LimitError().limit:
            raise LimitError
        if amount <= self._capacity:
            self._items[title] = self._items.get(title, 0)
            self._items[title] += amount
            self._capacity -= amount
        else:
            print(load_log('shop/add'))
