#robbie is working
import pygame
import random
#import Helfer
from resources import Farben
from resources import Koordinaten

pygame.init()

TILESIZE = 40
MAPWIDTH = 15
MAPHEIGHT = 10
SURFACE = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE+50))

GRASS = 0
HIGHGRASS = 1
WIESENSNACK=2
BLÄTTERMISCHUNG=3
PUSTEBLUMENDESSERT=4
DIRT = 5
WATER = 6


textures={
    GRASS : pygame.image.load('./resources/images/ressourcen/grasstexture.png').convert(),
    HIGHGRASS : pygame.image.load('./resources/images/ressourcen/highgrasstexture.png').convert(),
    DIRT : pygame.image.load('./resources/images/ressourcen/dirttexture.png').convert(),
    WATER : pygame.image.load('./resources/images/ressourcen/watertexture.png').convert()
}

#snippets
grasssnippet = pygame.image.load('./resources/images/ressourcen/grasstexture.png').convert()
grasssnippet = pygame.transform.scale(grasssnippet,(TILESIZE,TILESIZE))
highgrasssnippet = pygame.image.load('./resources/images/ressourcen/highgrasstexture.png').convert()
highgrasssnippet = pygame.transform.scale(highgrasssnippet,(TILESIZE,TILESIZE))

wiesensnacksnippet = pygame.image.load('./resources/images/ressourcen/wiesensnack.png')
wiesensnacksnippet = pygame.transform.scale(wiesensnacksnippet, (
Koordinaten.clsKoordinaten.SNACKSIZEX, Koordinaten.clsKoordinaten.SNACKSIZEY))
blättermischungsnippet = pygame.image.load('./resources/images/ressourcen/blattermischung.png')
blättermischungsnippet = pygame.transform.scale(blättermischungsnippet, (
Koordinaten.clsKoordinaten.SNACKSIZEX, Koordinaten.clsKoordinaten.SNACKSIZEY))
pusteblumendessertsnippet = pygame.image.load('./resources/images/ressourcen/dandelions.png')
pusteblumendessertsnippet = pygame.transform.scale(pusteblumendessertsnippet, (
Koordinaten.clsKoordinaten.SNACKSIZEX, Koordinaten.clsKoordinaten.SNACKSIZEY))

snippets=(grasssnippet,highgrasssnippet,wiesensnacksnippet,blättermischungsnippet,pusteblumendessertsnippet)

#resources
resources=[GRASS,HIGHGRASS,DIRT,WATER]
collectableres=[GRASS,HIGHGRASS]
craftables=[WIESENSNACK,BLÄTTERMISCHUNG,PUSTEBLUMENDESSERT]

#inventory
inventory={
    GRASS:0,
    HIGHGRASS:0,
    WIESENSNACK:0,
    BLÄTTERMISCHUNG:0,
    PUSTEBLUMENDESSERT:0
}

#controls for crafting
controls = {
    WIESENSNACK:49,
    BLÄTTERMISCHUNG:50,
    PUSTEBLUMENDESSERT:51
}

#controls for feeding
feedcontrols = {
    WIESENSNACK:55,
    BLÄTTERMISCHUNG:56,
    PUSTEBLUMENDESSERT:57
}

#recipes for crafting
craftrecipes={
    WIESENSNACK : {GRASS : 5},
    BLÄTTERMISCHUNG: {HIGHGRASS : 2, WIESENSNACK: 1},
    PUSTEBLUMENDESSERT: {GRASS : 4, HIGHGRASS : 2, BLÄTTERMISCHUNG : 1}
}

#random map
tilemap = [[GRASS for i in range(MAPWIDTH)] for j in range(MAPHEIGHT)]
for k in range(MAPHEIGHT):
    for l in range(MAPWIDTH):
        randomint = random.randint(0, 20)
        if randomint == 0:
            tile = WATER
        elif randomint > 0 and randomint <= 5:
            tile = HIGHGRASS
        else:
            tile = GRASS
        tilemap[k][l] = tile

class clsInventory(object):
    def __init__(self, inventory):
        self.inventory=inventory
    def showInventory(self):
        print(inventory)
    def getInventory(self):
        return self.inventory

class clsTileMap(object):
    def __init__(self, tilemap):
        self.tilemap=tilemap
    def showTilemap(self):
        print(tilemap)
    def getTilemap(self):
        return self.tilemap
    def drawSnippets(screen):
        placePosition = 50
        for item in collectableres:
            screen.blit(
                snippets[item], (placePosition, MAPHEIGHT * TILESIZE + 5))
            placePosition += 50
            textObjekt = pygame.font.Font('resources/fonts/celtic_gaelige.ttf', 19).render(str(
                inventory[item]), True, Farben.clsFarben.WHITE, Farben.clsFarben.BLACK)
            screen.blit(
                textObjekt, (placePosition, MAPHEIGHT * TILESIZE + 5))
            placePosition += 50