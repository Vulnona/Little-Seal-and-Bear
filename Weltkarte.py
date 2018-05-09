#robbie is working
import pygame
import pyganim
import random
import Helfer
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
NOTHING = 7
GRASSBUSH = 8


tiles_Sprite = Helfer.spritesheet('tileset_32_32.png')
grass_tile = tiles_Sprite.image_at((32, 8544, 32, 32), colorkey=(0 , 0, 0))
grass_tile = pygame.transform.scale(grass_tile, (40, 40))
empty = tiles_Sprite.image_at((193, 8473, 10, 10), colorkey=(0 , 0, 0))
empty = pygame.transform.scale(empty, (40,40))
grass_bush_tile = tiles_Sprite.image_at((200,8433, 55, 32), colorkey=(0 , 0, 0))
grass_bush_tile = pygame.transform.scale(grass_bush_tile, (40, 40))

textures={
    #GRASS : pygame.image.load('./resources/images/ressourcen/grasstexture.png').convert(),
    GRASS : grass_tile,
    HIGHGRASS : pygame.image.load('./resources/images/ressourcen/highgrasstexture.png').convert(),
    DIRT : pygame.image.load('./resources/images/ressourcen/dirttexture.png').convert(),
    WATER : pygame.image.load('./resources/images/ressourcen/watertexture.png').convert()
}

environment={
    NOTHING: empty,
    GRASSBUSH: grass_bush_tile
}

#snippets
grasssnippet = grass_tile.convert()
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

class clsInventory(object):
    def __init__(self, inventory):
        self.inventory=inventory
    def showInventory(self):
        print(inventory)
    def getInventory(self):
        return self.inventory

class clsTileMap(object):
    def __init__(self):
        self.tilemap= [[GRASS for i in range(MAPWIDTH)] for j in range(MAPHEIGHT)]
        self.environment = [[NOTHING for i in range(MAPWIDTH)] for j in range(MAPHEIGHT)]
    def showTilemap(self):
        print(self.tilemap)
    def getTilemap(self):
        return self.tilemap
    def getEnvironment(self):
        return self.environment
    def randomTilemap(self):
        for k in range(MAPHEIGHT):
            for l in range(MAPWIDTH):
                randomint = random.randint(0, 20)
                if randomint == 0:
                    tile = WATER
                elif randomint > 0 and randomint <= 5:
                    tile = HIGHGRASS
                else:
                    tile = GRASS
                self.tilemap[k][l] = tile
    def customTilemap(self):
        self.tilemap=[
            [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
            [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
            [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
            [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
            [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
            [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
            [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
            [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
            [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
            [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
        ]
    def environment_customTilemap(self):
        self.environment=[
            [NOTHING, GRASSBUSH, NOTHING, NOTHING, NOTHING,NOTHING, NOTHING, NOTHING, NOTHING, NOTHING,NOTHING, NOTHING,
             NOTHING, NOTHING, NOTHING],
            [NOTHING, GRASSBUSH, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING,
             NOTHING, NOTHING, NOTHING],
            [NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING,
             NOTHING, NOTHING, NOTHING],
            [NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING,
             NOTHING, NOTHING, NOTHING],
            [NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING,
             NOTHING, NOTHING, NOTHING],
            [NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING,
             NOTHING, NOTHING, NOTHING],
            [NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING,
             NOTHING, NOTHING, NOTHING],
            [NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING,
             NOTHING, NOTHING, NOTHING],
            [NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING,
             NOTHING, NOTHING, NOTHING],
            [NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING,
             NOTHING, NOTHING, NOTHING]
        ]
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