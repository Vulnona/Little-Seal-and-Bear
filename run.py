import logging
import pygame
import Build_Character
import sys
import os
import character


def run():
    pygame.init()
    logging.info('Initializing editor')
    g = Build_Character.Editor()
    logging.info('Running editor')

    while g.get_Mode() == "CREATE":
        g.update()
    return g.character


if __name__ == '__main__':
    run()
