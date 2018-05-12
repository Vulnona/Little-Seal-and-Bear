import random


class BaseSubtype:
    def __str__(self):
        return self.name


class Brown(BaseSubtype):
    id = 'brown'
    name = 'Braun'


class Grey(BaseSubtype):
    id = 'grey'
    name = 'Grau'


class White(BaseSubtype):
    id = 'white'
    name = 'Weiss'


ALL = [
    Brown,
    White,
    Grey
]


def pick_random():
    return random.choice(ALL)
