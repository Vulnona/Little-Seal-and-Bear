import pygame, sys
from pygame.locals import *
import Weltkarte
import CharakterForm


#colour resource: https://www.rapidtables.com/web/color/RGB_Color.html

DARK=(105,105,105)
BRIGHT=(255,248,220)
WHITE=(255,255,255)
BLACK=(0,0,0)

pygame.init()
SURFACE=pygame.display.set_mode((Weltkarte.MAPWIDTH*Weltkarte.TILESIZE, Weltkarte.MAPHEIGHT*Weltkarte.TILESIZE+50))
INVENTARFONT=pygame.font.Font('customfont.ttf',18)

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
            if(event.key==K_SPACE):
                currentTile=Weltkarte.tilemap[CharakterForm.POSITION[1]][CharakterForm.POSITION[0]]
                if(currentTile==Weltkarte.WATER or currentTile==Weltkarte.DIRT):
                    pass
                else:
                    Weltkarte.inventory[currentTile]+=1
                    Weltkarte.tilemap[CharakterForm.POSITION[1]][CharakterForm.POSITION[0]]=Weltkarte.DIRT
    for row in range(Weltkarte.MAPHEIGHT):
        for column in range(Weltkarte.MAPWIDTH):
            #pygame.draw.rect(SURFACE, Weltkarte.colours[Weltkarte.titlemap[row][column]], (column*Weltkarte.TILESIZE, row*Weltkarte.TILESIZE, Weltkarte.TILESIZE, Weltkarte.TILESIZE))
            SURFACE.blit(Weltkarte.textures[Weltkarte.tilemap[row][column]], (column*Weltkarte.TILESIZE, row*Weltkarte.TILESIZE))
    SURFACE.blit(CharakterForm.CHARACTER,(CharakterForm.POSITION[0]*Weltkarte.TILESIZE,CharakterForm.POSITION[1]*Weltkarte.TILESIZE))
    placePosition=50
    #SURFACE.blit(XXX)
    #https://stackoverflow.com/questions/37800894/what-is-surface-blit-function-in-python-what-does-it-do-how-it-works
    for item in Weltkarte.collectableres:
        SURFACE.blit(Weltkarte.snippets[item],(placePosition,Weltkarte.MAPHEIGHT*Weltkarte.TILESIZE+20))
        placePosition+=30
        textObjekt=INVENTARFONT.render(str(Weltkarte.inventory[item]),True,WHITE,BLACK)
        SURFACE.blit(textObjekt,(placePosition, Weltkarte.MAPHEIGHT * Weltkarte.TILESIZE + 20))
        placePosition+=50
    pygame.display.update()
