import logging
import pygame
import charaktereditor
import sys
import os
import character


def run():
    if 'SDL_VIDEO_WINDOW_POS' not in os.environ:
        os.environ['SDL_VIDEO_CENTERED'] = '1' # This makes the window centered on the screen

    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%d/%m/%Y %H:%M:%S',
        stream=sys.stdout
    )

    logging.getLogger().setLevel(logging.INFO)

    logging.info('Initializing PyGame/{} (with SDL/{})'.format(
        pygame.version.ver,
        '.'.join(str(v) for v in pygame.get_sdl_version())
    ))

    pygame.init()

    logging.info('Initializing editor')
    g = charaktereditor.Editor()

    logging.info('Running editor')

    while g.get_Mode()=="CREATE":
        g.update()
    #save character ausserhalb des sheets und übergeben fehlt noch


if __name__ == '__main__':
    run()
