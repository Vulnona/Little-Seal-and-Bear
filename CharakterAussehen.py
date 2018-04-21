import pygame
import character

pygame.init()

def showAnimal(charakter, screen):
    print(str(charakter.gettype()))
    if (str(charakter.gettype())==str(character.animaltypes.clsBaer)):
        if (int(charakter.level) < 4):
            image = pygame.image.load('./resources/images/animalstages/babybear.png').convert()
            image = pygame.transform.scale(image, (300, 300))
            screen.blit(image, (200, 100))
        elif (int(charakter.level) >= 4 and int(charakter.level) <= 8):
            image = pygame.image.load('./resources/images/animalstages/bearbig.png').convert()
            image = pygame.transform.scale(image, (300, 300))
            screen.blit(image, (200, 100))
        elif (int(charakter.level) > 8):
            image = pygame.image.load('./resources/images/animalstages/bearfinallevel.png').convert()
            image = pygame.transform.scale(image, (300, 300))
            screen.blit(image, (200, 100))
    elif (str(charakter.gettype())==str(character.animaltypes.clsRobbe)):
        if (int(charakter.level) < 4):
            image = pygame.image.load('./resources/images/animalstages/babyseal.png').convert()
            image = pygame.transform.scale(image, (300, 300))
            screen.blit(image, (200, 100))
        elif (int(charakter.level) >= 4 and int(charakter.level) <= 8):
            image = pygame.image.load('./resources/images/animalstages/sealbig.png').convert()
            image = pygame.transform.scale(image, (300, 300))
            screen.blit(image, (200, 100))
        elif (int(charakter.level) > 8):
            image = pygame.image.load('./resources/images/animalstages/sealfinallevel.png').convert()
            image = pygame.transform.scale(image, (300, 300))
            screen.blit(image, (200, 100))