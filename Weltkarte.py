#robbie is working
import pygame
from pygame.locals import *
import random
import Koordinaten


pygame.init()
TILESIZE = 20
MAPWIDTH = 30
MAPHEIGHT = 20
SURFACE = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE+50))


GRASS = 0
HIGHGRASS = 1
DIRT = 2
WATER = 3
WIESENSNACK = 0
BLÄTTERMISCHUNG = 1
PUSTEBLUMENDESSERT = 2

allresources = {GRASS:0, HIGHGRASS:1, DIRT:2, WATER:3}
allcraftables = {WIESENSNACK:0, BLÄTTERMISCHUNG:1, PUSTEBLUMENDESSERT:2}

#colours={
#    GRASS : GREEN,
#    HIGHGRASS: DARKGREEN,
#    WATER : BLUE
#}

textures={
    GRASS : pygame.image.load('grasstexture.png').convert(),
    HIGHGRASS : pygame.image.load('highgrasstexture.png').convert(),
    DIRT : pygame.image.load('dirttexture.jpg').convert(),
    WATER : pygame.image.load('watertexture.png').convert()
}

grasssnippet = pygame.image.load('grasstexture.png').convert()
grasssnippet = pygame.transform.scale(grasssnippet,(20,20))
highgrasssnippet = pygame.image.load('highgrasstexture.png').convert()
highgrasssnippet = pygame.transform.scale(highgrasssnippet,(20,20))


wiesensnacksnippet = pygame.image.load('wiesensnack.png')
wiesensnacksnippet = pygame.transform.scale(wiesensnacksnippet,(Koordinaten.clsKoordinaten.SNACKSIZEX, Koordinaten.clsKoordinaten.SNACKSIZEY))
blättermischungsnippet = pygame.image.load('blattermischung.png')
blättermischungsnippet = pygame.transform.scale(blättermischungsnippet, (Koordinaten.clsKoordinaten.SNACKSIZEX, Koordinaten.clsKoordinaten.SNACKSIZEY))
pusteblumendessertsnippet = pygame.image.load('dandelions.png')
pusteblumendessertsnippet = pygame.transform.scale(pusteblumendessertsnippet, (Koordinaten.clsKoordinaten.SNACKSIZEX, Koordinaten.clsKoordinaten.SNACKSIZEY))


snippets=(grasssnippet,highgrasssnippet)
craftsnippets=(wiesensnacksnippet,blättermischungsnippet,pusteblumendessertsnippet)

resources=[GRASS,HIGHGRASS,DIRT,WATER]
collectableres=[GRASS,HIGHGRASS]
craftables=[WIESENSNACK,BLÄTTERMISCHUNG,PUSTEBLUMENDESSERT]

inventory={
    GRASS:0,
    HIGHGRASS:0
}
inventorycrafts={
    WIESENSNACK:0,
    BLÄTTERMISCHUNG:0,
    PUSTEBLUMENDESSERT:0
}

controls = {
    WIESENSNACK:49,
    BLÄTTERMISCHUNG:50,
    PUSTEBLUMENDESSERT:51
}

craftrecipes={
    WIESENSNACK : {GRASS : 5},
    BLÄTTERMISCHUNG: {GRASS: 4, HIGHGRASS: 2},
    PUSTEBLUMENDESSERT: {GRASS : 2, HIGHGRASS: 8}
}

#titlemap=[
#    [GRASS, GRASS, HIGHGRASS],
#    [WATER, GRASS, GRASS],
#    [WATER, WATER, GRASS],
#    [WATER, HIGHGRASS, GRASS]
#]

tilemap=[[GRASS for i in range(MAPWIDTH)]for j in range(MAPHEIGHT)]

for k in range(MAPHEIGHT):
    for l in range(MAPWIDTH):
        randomint=random.randint(0,20)
        if randomint==0:
            tile=WATER
        elif randomint>=0 and randomint<=5:
            tile=HIGHGRASS
        else:
            tile=GRASS

        tilemap[k][l]=tile