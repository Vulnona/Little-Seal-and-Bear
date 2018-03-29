#robbie is working
import pygame
from pygame.locals import *
import random


pygame.init()

GRASS=0
HIGHGRASS=1
WATER=3

GREEN=(0,255,0)
DARKGREEN=(34,139,34)
BLUE=(0,0,255)

#colours={
#    GRASS : GREEN,
#    HIGHGRASS: DARKGREEN,
#    WATER : BLUE
#}

textures={
    GRASS : pygame.image.load('grasstexture.png'),
    HIGHGRASS : pygame.image.load('highgrasstexture.png'),
    WATER : pygame.image.load('watertexture.png')
}

TILESIZE=60
MAPWIDTH=20
MAPHEIGHT=15

resources=[GRASS,HIGHGRASS,WATER]

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