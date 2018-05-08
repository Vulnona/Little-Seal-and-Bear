from random import randint


def haelftehaelfte(object):
    rand_int = randint(0, 1)
    if rand_int == 0:
        return False
    if rand_int == 1:
        return True


def wuerfel(Wuerfelseiten):
    rand_int = randint(1, Wuerfelseiten)
    return rand_int
