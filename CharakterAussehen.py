import pygame
import character

pygame.init()

def showAnimal(charakter, screen):
    if (str(charakter.gettype()==str(character.animaltypes.clsBaer))):
        if (int(charakter.level) < 4):
            image = pygame.image.load('babybear.png').convert()
            image = pygame.transform.scale(image, (300, 300))
            screen.blit(image, (200, 100))
        elif (int(charakter.level) >= 4 and int(charakter.level) <= 8):
            image = pygame.image.load('bearbig.png').convert()
            image = pygame.transform.scale(image, (300, 300))
            screen.blit(image, (200, 100))
        elif (int(charakter.level) > 8):
            image = pygame.image.load('bearfinallevel.png').convert()
            image = pygame.transform.scale(image, (300, 300))
            screen.blit(image, (200, 100))

    elif (str(charakter.gettype()==str(character.animaltypes.clsRobbe))):
        if (int(charakter.level) < 4):
            image = pygame.image.load('babyseal.png').convert()
            image = pygame.transform.scale(image, (300, 300))
            screen.blit(image, (200, 100))
        elif (int(charakter.level) >= 4 and int(charakter.level) <= 8):
            image = pygame.image.load('sealbig.png').convert()
            image = pygame.transform.scale(image, (300, 300))
            screen.blit(image, (200, 100))
        elif (int(charakter.level) > 8):
            image = pygame.image.load('sealfinallevel.png').convert()
            image = pygame.transform.scale(image, (300, 300))
            screen.blit(image, (200, 100))