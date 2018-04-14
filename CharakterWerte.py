class Charakter(object):
    def __init__(self, animaltype, level):
        self.animaltype=animaltype
        self.level=level
    def getlevel(self):
        level=str(self.level)
        return level
    def gettype(self):
        type=str(self.animaltype)
        return type
    def LevelUp(self):
        self.level=self.level+1
