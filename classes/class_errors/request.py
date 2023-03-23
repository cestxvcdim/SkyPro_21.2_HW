class RequestError(Exception):
    def __init__(self, *args):
        if args:
            self.problem = args[0]
        else:
            self.problem = None
        self._length = 7
        self._wordlist = ["вернуть", "доставить"]

    @property
    def length(self):
        return self._length

    @property
    def wordlist(self):
        return self._wordlist

    def __str__(self):
        if self.problem and isinstance(self.problem, str):
            return f'Missed command word: {self.problem} not in {self.wordlist}'
        return f'Wrong length of request: {self.problem} should equal {self.length}'
