from classes.class_errors.request import RequestError
from classes.store import Store
from classes.shop import Shop


class Request:
    VEN = 'You should put number in amount, not string'
    VEI = 'This item is not available for any actions'

    def __init__(self, req_str: str):
        req = req_str.split()
        if req[0] not in RequestError().wordlist:
            raise RequestError(req[0])
        if len(req) != RequestError().length:
            raise RequestError(len(req))
        if not req[1].isdigit():
            raise ValueError(self.VEN)
        self._cmd_word = req[0]
        self._from: str = req[4]
        self._to: str = req[6]
        self._amount: int = int(req[1])
        self._product: str = req[2]

    def __repr__(self):
        return f'from = "{self._from}",\n' \
               f'to = "{self._to}",\n' \
               f'amount = {self._amount},\n' \
               f'product = "{self._product}"'

    @property
    def to(self):
        return self._to

    @property
    def amount(self):
        return self._amount

    @property
    def product(self):
        return self._product

    def is_incorrect(self, shop_obj: Shop, store_obj: Store):
        match self._cmd_word:
            case 'доставить':
                if self._product not in store_obj.get_items():
                    raise ValueError(self.VEI)
                return False
            case 'вернуть':
                if self._product not in shop_obj.get_items():
                    raise ValueError(self.VEI)
                return False
