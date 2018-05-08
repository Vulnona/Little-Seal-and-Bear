import random


class BaseSubtype:
    def __str__(self):
        return self.name


class Schwarz(BaseSubtype):
    id = 'schwarz'
    name = 'Schwarz'


class Grau(BaseSubtype):
    id = 'grau'
    name = 'Grau'


class Weiss(BaseSubtype):
    id = 'weiss'
    name = 'Weiss'


ALL = [
    Schwarz,
    Weiss,
    Grau
]


def pick_random():
    return random.choice(ALL)
