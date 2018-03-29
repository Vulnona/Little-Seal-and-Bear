import pygame, sys
from pygame.locals import *
import Weltkarte
import CharakterForm


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
        elif event.type==KEYDOWN:
            if(event.key==K_RIGHT and CharakterForm.POSITION[0]<Weltkarte.MAPWIDTH-1):
                CharakterForm.POSITION[0]+=1
            if(event.key==K_LEFT and CharakterForm.POSITION[0]>0):
                CharakterForm.POSITION[0]-=1
            if(event.key==K_DOWN and CharakterForm.POSITION[1]<Weltkarte.MAPHEIGHT-1):
                CharakterForm.POSITION[1]+=1
            if(event.key==K_UP and CharakterForm.POSITION[1]>0):
                CharakterForm.POSITION[1]-=1
    for row in range(Weltkarte.MAPHEIGHT):
        for column in range(Weltkarte.MAPWIDTH):
            #pygame.draw.rect(SURFACE, Weltkarte.colours[Weltkarte.titlemap[row][column]], (column*Weltkarte.TILESIZE, row*Weltkarte.TILESIZE, Weltkarte.TILESIZE, Weltkarte.TILESIZE))
            SURFACE.blit(Weltkarte.textures[Weltkarte.tilemap[row][column]], (column*Weltkarte.TILESIZE, row*Weltkarte.TILESIZE))
    SURFACE.blit(CharakterForm.CHARACTER,(CharakterForm.POSITION[0]*Weltkarte.TILESIZE,CharakterForm.POSITION[1]*Weltkarte.TILESIZE))
    pygame.display.update()
