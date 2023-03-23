class LimitError(Exception):
    def __init__(self, *args):
        if args:
            self.amount = args[0]
        else:
            self.amount = None
        self._limit = 4

    @property
    def limit(self):
        return self._limit

    def __str__(self):
        if self.amount:
            return f'Too many items: items amount({self.amount}) should less or equal max({self._limit})'
        return f'Reached maximum items limit: max({self._limit}) == items amount({self._limit})'
