class Charakter(object):
    def __init__(self, animaltype, level):
        self.animaltype=animaltype
        self.level=level
    def getlevel(self):
        level=str(self.level)
        return level
