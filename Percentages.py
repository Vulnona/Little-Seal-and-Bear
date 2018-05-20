from random import randint


def halfhalf():
    rand_int = randint(0, 1)
    if rand_int == 0:
        return False
    if rand_int == 1:
        return True


def dice(Wuerfelseiten):
    rand_int = randint(1, Wuerfelseiten)
    return rand_int
