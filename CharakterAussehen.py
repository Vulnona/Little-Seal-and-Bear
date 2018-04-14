import pygame
import CharakterWerte

pygame.init()

def showAnimal(charakter, screen):
    if CharakterWerte.Charakter.gettype(charakter) == "baer":
        if int(CharakterWerte.Charakter.getlevel(charakter)) < 4:
            image = pygame.image.load('babybear.png').convert()
            image = pygame.transform.scale(image, (300, 300))
            screen.blit(image, (200, 100))
        elif int(charakter.level) >= 4 and int(charakter.level) <= 8:
            image = pygame.image.load('bearbig.png').convert()
            image = pygame.transform.scale(image, (300, 300))
            screen.blit(image, (200, 100))
        elif int(charakter.level) > 8:
            image = pygame.image.load('bearfinallevel.png').convert()
            image = pygame.transform.scale(image, (300, 300))
            screen.blit(image, (200, 100))

    else:
        pass