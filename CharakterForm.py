# here, the character is drawn...
# https://www.pygame.org/docs/ref/draw.html
import pygame
import Weltkarte


CHARACTER=pygame.image.load('characterbear.png')
CHARACTER=pygame.transform.scale(CHARACTER,(Weltkarte.TILESIZE,Weltkarte.TILESIZE))
POSITION=[0,0]


