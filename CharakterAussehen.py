import pygame
import character

pygame.init()


def showAnimal(charakter, screen):
    if (isinstance(charakter.get_type(), character.animaltypes.clsBaer)):
        if (int(charakter.level) < 4):
            image = pygame.image.load(
                './resources/images/animalstages/babybear.png').convert()
            image = pygame.transform.scale(image, (300, 300))
            screen.blit(image, (200, 100))
        elif (int(charakter.level) >= 4 and int(charakter.level) <= 8):
            if (str(charakter.get_subtype())==character.animalsubtypes.Weiss):
                image = pygame.image.load(
                    './resources/images/animalstages/bear_white_adult.png').convert()
                image = pygame.transform.scale(image, (300, 300))
            elif (str(charakter.get_subtype())==character.animalsubtypes.Grau):
                image = pygame.image.load(
                    './resources/images/animalstages/bear_grey_adult.png').convert()
                image = pygame.transform.scale(image, (300, 300))
            elif (str(charakter.get_subtype())==character.animalsubtypes.Schwarz):
                image = pygame.image.load(
                    './resources/images/animalstages/bear_brown_adult.png').convert()
                image = pygame.transform.scale(image, (300, 300))
            screen.blit(image, (200, 100))
        elif (int(charakter.level) > 8):
            if (str(charakter.get_subtype())==character.animalsubtypes.Weiss):
                image = pygame.image.load(
                    './resources/images/animalstages/bear_white_final.png').convert()
                image = pygame.transform.scale(image, (300, 300))
            elif (str(charakter.get_subtype())==character.animalsubtypes.Grau):
                image = pygame.image.load(
                    './resources/images/animalstages/bear_grey_final.png').convert()
                image = pygame.transform.scale(image, (300, 300))
            elif (str(charakter.get_subtype())==character.animalsubtypes.Schwarz):
                image = pygame.image.load(
                    './resources/images/animalstages/bear_brown_final.png').convert()
                image = pygame.transform.scale(image, (300, 300))
            screen.blit(image, (200, 100))
    elif (isinstance(charakter.get_type(), character.animaltypes.clsRobbe)):
        if (int(charakter.level) < 4):
            image = pygame.image.load(
                './resources/images/animalstages/babyseal.png').convert()
            image = pygame.transform.scale(image, (300, 300))
            screen.blit(image, (200, 100))
        elif (int(charakter.level) >= 4 and int(charakter.level) <= 8):
            if (str(charakter.get_subtype())==character.animalsubtypes.Weiss):
                image = pygame.image.load(
                    './resources/images/animalstages/seal_white_adult.png').convert()
                image = pygame.transform.scale(image, (300, 300))
            elif (str(charakter.get_subtype())==character.animalsubtypes.Grau):
                image = pygame.image.load(
                    './resources/images/animalstages/seal_grey_adult.png').convert()
                image = pygame.transform.scale(image, (300, 300))
            elif (str(charakter.get_subtype())==character.animalsubtypes.Schwarz):
                image = pygame.image.load(
                    './resources/images/animalstages/seal_brown_adult.png').convert()
                image = pygame.transform.scale(image, (300, 300))
            screen.blit(image, (200, 100))
        elif (int(charakter.level) > 8):
            if (str(charakter.get_subtype())==character.animalsubtypes.Weiss):
                image = pygame.image.load(
                    './resources/images/animalstages/seal_white_final.png').convert()
                image = pygame.transform.scale(image, (300, 300))
            elif (str(charakter.get_subtype())==character.animalsubtypes.Grau):
                image = pygame.image.load(
                    './resources/images/animalstages/seal_grey_final.png').convert()
                image = pygame.transform.scale(image, (300, 300))
            elif (str(charakter.get_subtype())==character.animalsubtypes.Schwarz):
                image = pygame.image.load(
                    './resources/images/animalstages/seal_brown_final.png').convert()
                image = pygame.transform.scale(image, (300, 300))
            screen.blit(image, (200, 100))
