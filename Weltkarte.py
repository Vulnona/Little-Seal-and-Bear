import pygame
from pygame.locals import *

pygame.init()

#robbie is working
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

TILESIZE=20
MAPWIDTH=3
MAPHEIGHT=4

titlemap=[
    [GRASS, GRASS, HIGHGRASS],
    [WATER, GRASS, GRASS],
    [WATER, WATER, GRASS],
    [WATER, HIGHGRASS, GRASS]
]
