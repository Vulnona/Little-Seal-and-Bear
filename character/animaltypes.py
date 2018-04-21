import random

class BaseType:
    def __str__(self):
        return self.name

class clsBaer(BaseType):
    id = 'baer'
    name = 'Bär'

class clsRobbe(BaseType):
    id = 'robbe'
    name = 'Robbe'

ALL = [
    clsBaer,
    clsRobbe
]

def pick_random():
    """Zufallsgenerierte Tierart..."""
    return random.choice(ALL)
