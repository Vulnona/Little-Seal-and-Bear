import logging
import pygame
import Build_Character


def run_Character_Builder():
    pygame.init()
    logging.info('Initializing editor')
    g = Build_Character.Editor()
    logging.info('Running editor')

    while g.get_Mode() == "CREATE":
        g.update()
    return g.character

