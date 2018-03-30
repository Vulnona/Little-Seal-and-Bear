import pygame, sys
from pygame.locals import *
import Weltkarte
import CharakterForm
import Interaktion
import LevelupForm


#colour resource: https://www.rapidtables.com/web/color/RGB_Color.html

DARK=(105,105,105)
BRIGHT=(255,248,220)
WHITE=(255,255,255)
BLACK=(0,0,0)
GOLD = (255, 215,   0)
DARKRED = (139, 0, 0)


pygame.init()
SURFACE=pygame.display.set_mode((Weltkarte.MAPWIDTH*Weltkarte.TILESIZE, Weltkarte.MAPHEIGHT*Weltkarte.TILESIZE+50))
INVENTARFONT=pygame.font.Font('customfont.ttf',18)

# surface = pygame.image.load('beispiel.png').convert()

pygame.display.set_caption("Bärenspiel")
blackbar=pygame.Rect(0,400,Weltkarte.MAPWIDTH*Weltkarte.TILESIZE,Weltkarte.MAPHEIGHT*Weltkarte.TILESIZE)
interagierenbutton = pygame.Rect(480, 420, 80, 20)

while True:
    for row in range(Weltkarte.MAPHEIGHT):
        for column in range(Weltkarte.MAPWIDTH):
            #pygame.draw.rect(SURFACE, Weltkarte.colours[Weltkarte.titlemap[row][column]], (column*Weltkarte.TILESIZE, row*Weltkarte.TILESIZE, Weltkarte.TILESIZE, Weltkarte.TILESIZE))
            SURFACE.blit(Weltkarte.textures[Weltkarte.tilemap[row][column]], (column*Weltkarte.TILESIZE, row*Weltkarte.TILESIZE))
            pygame.draw.rect(SURFACE, [0, 0, 0], blackbar)
    SURFACE.blit(CharakterForm.CHARACTER,(CharakterForm.POSITION[0]*Weltkarte.TILESIZE,CharakterForm.POSITION[1]*Weltkarte.TILESIZE))
    placePosition=50
    for item in Weltkarte.collectableres:
        SURFACE.blit(Weltkarte.snippets[item],(placePosition,Weltkarte.MAPHEIGHT*Weltkarte.TILESIZE+20))
        placePosition+=30
        textObjekt=INVENTARFONT.render(str(Weltkarte.inventory[item]),True,WHITE,BLACK)
        SURFACE.blit(textObjekt,(placePosition, Weltkarte.MAPHEIGHT * Weltkarte.TILESIZE + 20))
        placePosition+=50

    pygame.draw.rect(SURFACE, [255, 0, 0], interagierenbutton)
    label = INVENTARFONT.render("Charakter", 1, (0, 0, 0))
    SURFACE.blit(label, (495, 420))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==MOUSEBUTTONDOWN:
            mousepos=event.pos
            if interagierenbutton.collidepoint(mousepos):
                #Interaktion.AgierenMenu(SURFACE,Weltkarte.MAPHEIGHT,Weltkarte.MAPWIDTH)
                Charaktermenu=Interaktion.Menu(SURFACE)
                Charaktermenu.draw(SURFACE)
                #Charaktermenu = Interaktion.Menu(SURFACE)

                #Charaktermenu.draw(SURFACE)
                #pygame.display.update()

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
            if(event.key==K_e):
                STAR = pygame.draw.lines(SURFACE, GOLD, 1, LevelupForm.Star, 3)
                #SURFACE.blit(STAR, (CharakterForm.POSITION[0]*Weltkarte.TILESIZE,CharakterForm.POSITION[1]*Weltkarte.TILESIZE))
                pygame.draw.rect(SURFACE, (0,0,0), STAR, 2)
    pygame.display.update()
