import pygame, sys
from pygame.locals import *
import Weltkarte


#colour resource: https://www.rapidtables.com/web/color/RGB_Color.html


pygame.init()
surfacemap=pygame.display.set_mode((Weltkarte.MAPWIDTH*Weltkarte.TILESIZE, Weltkarte.MAPHEIGHT*Weltkarte.TILESIZE))


# surface = pygame.image.load('beispiel.png').convert()

pygame.display.set_caption("Beispiel")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    for column in range(Weltkarte.MAPWIDTH):
        for row in range(Weltkarte.MAPHEIGHT):
            pygame.draw.rect(surfacemap, Weltkarte.colours[Weltkarte.titlemap[row][column]], column*Weltkarte.TILESIZE, row*Weltkarte.TILESIZE, Weltkarte.TILESIZE, Weltkarte.TILESIZE)
    pygame.display.update()
