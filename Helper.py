import settings
import World_Map
import pygame
import os

#Repainting Tiles and Environment for Walking Animation

def repaint(BackgroundTilemap, NewTilemap, player_Icon_Position, nextPosition, window):
    toRepaintcurrentBG = World_Map.textures[
        BackgroundTilemap.getTilemap()[player_Icon_Position[1]][
            player_Icon_Position[0]]]
    toRepaintcurrentBG = pygame.transform.scale(toRepaintcurrentBG, (
        World_Map.TILESIZE, World_Map.TILESIZE))
    toRepaintcurrent = World_Map.textures[
        NewTilemap.getTilemap()[player_Icon_Position[1]][player_Icon_Position[0]]]
    toRepaintcurrent = pygame.transform.scale(toRepaintcurrent, (
        World_Map.TILESIZE, World_Map.TILESIZE))
    toRepaintcurrentenvironment = World_Map.environment[NewTilemap.getEnvironment(
    )[player_Icon_Position[1]][player_Icon_Position[0]]]
    toRepaintnextBG = World_Map.textures[
        BackgroundTilemap.getTilemap()[nextPosition[1]][nextPosition[0]]]
    toRepaintnextBG = pygame.transform.scale(toRepaintnextBG, (
        World_Map.TILESIZE, World_Map.TILESIZE))
    toRepaintnext = World_Map.textures[
        NewTilemap.getTilemap()[nextPosition[1]][nextPosition[0]]]
    toRepaintnext = pygame.transform.scale(toRepaintnext, (
        World_Map.TILESIZE, World_Map.TILESIZE))
    toRepaintnextenvironment = World_Map.environment[
        NewTilemap.getEnvironment()[nextPosition[1]][nextPosition[0]]]

    window.blit(toRepaintcurrentBG,
                (player_Icon_Position[0] * World_Map.TILESIZE,
                 player_Icon_Position[1] * World_Map.TILESIZE))
    window.blit(toRepaintcurrent,
                (player_Icon_Position[0] * World_Map.TILESIZE,
                 player_Icon_Position[1] * World_Map.TILESIZE))
    window.blit(toRepaintcurrentenvironment,
                (player_Icon_Position[0] * World_Map.TILESIZE,
                 player_Icon_Position[1] * World_Map.TILESIZE))
    window.blit(toRepaintnextBG,
                (nextPosition[0] * World_Map.TILESIZE,
                 nextPosition[1] * World_Map.TILESIZE))
    window.blit(toRepaintnext,
                (nextPosition[0] * World_Map.TILESIZE,
                 nextPosition[1] * World_Map.TILESIZE))
    window.blit(toRepaintnextenvironment,
                (nextPosition[0] * World_Map.TILESIZE,
                 nextPosition[1] * World_Map.TILESIZE))


# Resources, Images, Fonts Loading

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

#Spritesheets, taken from https://www.pygame.org/wiki/Spritesheet?parent=, converted to Python 3.x

class spritesheet(object):
    def __init__(self, filename):
        try:
            path=_get_resource_path('spritesheets', filename)
            self.sheet = pygame.image.load(path).convert_alpha()
        except pygame.error as message:
            print('Unable to load spritesheet image:'+ path)
            raise SystemExit(message)
    # Load a specific image from a specific rectangle
    def image_at(self, rectangle, colorkey = None):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
    # Load a whole bunch of images and return them as a list
    def images_at(self, rects, colorkey = None):
        "Loads multiple images, supply a list of coordinates"
        return [self.image_at(rect, colorkey) for rect in rects]
    # Load a whole strip of images
    def load_strip(self, rect, image_count, colorkey = None):
        "Loads a strip of images and returns them as a list"
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)


class SpriteStripAnim(object):
    """sprite strip animator
    This class provides an iterator (iter() and next() methods), and a
    __add__() method for joining strips which comes in handy when a
    strip wraps to the next row.
    """
    def __init__(self, filename, rect, count, colorkey=None, loop=False, frames=1):
        """construct a SpriteStripAnim
        filename, rect, count, and colorkey are the same arguments used
        by spritesheet.load_strip.
        loop is a boolean that, when True, causes the next() method to
        loop. If False, the terminal case raises StopIteration.
        frames is the number of ticks to return the same image before
        the iterator advances to the next image.
        """
        self.filename = filename
        ss = spritesheet.spritesheet(filename)
        self.images = ss.load_strip(rect, count, colorkey)
        self.i = 0
        self.loop = loop
        self.frames = frames
        self.f = frames

    def iter(self):
        self.i = 0
        self.f = self.frames
        return self

    def next(self):
        if self.i >= len(self.images):
            if not self.loop:
                raise StopIteration
            else:
                self.i = 0
        image = self.images[self.i]
        self.f -= 1
        if self.f == 0:
            self.i += 1
            self.f = self.frames
        return image

    def __add__(self, ss):
        self.images.extend(ss.images)
        return self