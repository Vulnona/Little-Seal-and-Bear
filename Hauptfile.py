from math import pow, sqrt

class clsRechteck(object):
    def __init__(self, a, b):
        self.kanteA = a
        self.kanteB = b

    def setKanteA(self, a):
        self.kanteA = a

    def setKanteB(self, b):
        self.kanteB = b

    def getKanteA(self):
        return self.kanteA

    def getKanteB(self):
        return self.kanteB

    def getKanteC(self):
        cQuadrat = pow(self.kanteA, 2) + (self.kanteB ** 2)
        kanteC = sqrt(cQuadrat)

        return kanteC

    def getFlaeche(self):
        if (self.kanteA > 0) and (self.kanteB > 0):
            return (self.kanteA * self.kanteB) / 2
        else:
            return 0