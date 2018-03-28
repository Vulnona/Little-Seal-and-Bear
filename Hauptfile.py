import pygame, sys
import Weltkarte

#colour resource: https://www.rapidtables.com/web/color/RGB_Color.html


pygame.init()
surfacemap=pygame.display.set_mode((Weltkarte.MAPWIDTH*Weltkarte.TILESIZE, Weltkarte.MAPHEIGHT*Weltkarte.TILESIZE))


surface = pygame.image.load('beispiel.png').convert()

pygame.display.set_caption("Beispiel")

