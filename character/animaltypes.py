import random


class BaseType:
    def __str__(self):
        return self.name


class clsBaer(BaseType):
    id = 'bear'
    name = 'Bär'


class clsRobbe(BaseType):
    id = 'seal'
    name = 'Robbe'


ALL = [
    clsBaer,
    clsRobbe
]


def pick_random():
    return random.choice(ALL)
