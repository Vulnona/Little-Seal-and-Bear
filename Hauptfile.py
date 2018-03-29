import pygame, sys
from pygame.locals import *
import Weltkarte


#colour resource: https://www.rapidtables.com/web/color/RGB_Color.html


pygame.init()
SURFACE=pygame.display.set_mode((Weltkarte.MAPWIDTH*Weltkarte.TILESIZE, Weltkarte.MAPHEIGHT*Weltkarte.TILESIZE))


# surface = pygame.image.load('beispiel.png').convert()

pygame.display.set_caption("Beispiel")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    for row in range(Weltkarte.MAPHEIGHT):
        for column in range(Weltkarte.MAPWIDTH):
            #pygame.draw.rect(SURFACE, Weltkarte.colours[Weltkarte.titlemap[row][column]], (column*Weltkarte.TILESIZE, row*Weltkarte.TILESIZE, Weltkarte.TILESIZE, Weltkarte.TILESIZE))
            SURFACE.blit(Weltkarte.textures[Weltkarte.tilemap[row][column]], (column*Weltkarte.TILESIZE, row*Weltkarte.TILESIZE))
    pygame.display.update()
