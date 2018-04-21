import settings
import pygame
import os

#Resources, Images, Fonts Loading

def _get_resource_path(res_type, filename):
    path = os.path.join(settings.RESOURCES_ROOT, res_type, filename)
    if not os.path.isfile(path):
        raise ValueError('The file ' + path + ' doesn\'t exist')
    return path


def load_image(filename):
    path = _get_resource_path('images', filename)
    return pygame.image.load(path).convert_alpha()


def load_font(filename, size):
    path = _get_resource_path('fonts', filename)
    return pygame.font.Font(path, size)
