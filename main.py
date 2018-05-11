# Robbie likes: https://medium.com/@yvanscher/making-a-game-ai-with-deep-learning-963bb549b3d5
# Very nice: http://game-icons.net/
# TODO: die BG Tilemap kann glaube ich weg
# TODO: collect system überarbeiten, bubbles überarbeiten, 'schwarz'->'braun'


import pygame
import sys
import gui
import os
import logging
from pygame.locals import *
import pickle
import inspect
import pyganim
import StartingScreen
import Weltkarte
import Objekte
import Interaktion
import Wahrscheinlichkeiten
# import LevelupForm
from resources import Farben, Koordinaten
import run
import character
import Helfer


if 'SDL_VIDEO_WINDOW_POS' not in os.environ:
    # This makes the window centered on the screen
    os.environ['SDL_VIDEO_CENTERED'] = '1'

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
pygame.display.set_caption("Spiel ohne Namen")
pygame.display.set_icon(Helfer.load_image('icon.png'))
FPS = 60
fpsClock = pygame.time.Clock()
Charakter = character.Character()
MODE = "UNKNOWN"
player_Icon_Position = [0, 0]
Enemies = Objekte.cls_Enemies()
Enemies.fill_Enemies_list()
BackgroundTilemap = Weltkarte.clsTileMap()
NewTilemap = Weltkarte.clsTileMap()
# NewTilemap.randomTilemap()
NewTilemap.customTilemap()
NewTilemap.environment_customTilemap()


class Spiel(object):

    def __init__(self, MODE, Charakter):
        self.MODE = MODE
        self.Charakter = Charakter
        self.window = Weltkarte.SURFACE
        self._load_fonts()
        self._load_images()
        self._load_spritesheets()

    def _load_fonts(self):
        logging.info('Loading fonts')
        self.fonts = {
            'normal': Helfer.load_font('celtic_gaelige.ttf', 19),
            'small': Helfer.load_font('celtic_gaelige.ttf', 14)
        }

    def _load_images(self):
        logging.info('Loading images')

        self.images = {
            'unknown': Helfer.load_image('unknown.png'),
            'player_icon': {
                'bear': Helfer.load_image('bearicon.png'),
                'seal': Helfer.load_image('sealicon.png')
            },
            'enemies': {
                'bug': Helfer.load_image('enemies/bug.png'),
                'bird': Helfer.load_image('enemies/bird.png'),
                'sawblade': Helfer.load_image('enemies/sawblade.png')
            },
            'buttons': {
                'yes': Helfer.load_image('buttons/yes.png'),
                'refresh': Helfer.load_image('buttons/refresh.png'),
                'exit': Helfer.load_image('buttons/exit.png'),
            }
        }

    def _load_spritesheets(self):
        logging.info('Loading Spritesheets')

        self.spritesheets = {
            'sealsprites': Helfer.spritesheet('seal2.png'),
            'bearsprites': Helfer.spritesheet('bear.png')
        }

    def spielen(self, MODE):
        if MODE == "STARTSCREEN":
            if self.Charakter.get_Name() is None:
                NewStartingScreen = StartingScreen.clsStartScreen(
                    self.window, MODE, False)
            else:
                NewStartingScreen = StartingScreen.clsStartScreen(
                    self.window, MODE, True)
            proceed = True
            while proceed:
                MODE = NewStartingScreen.draw()
                if MODE != "STARTSCREEN":
                    proceed = False
            return NewStartingScreen.whichMode()

        elif MODE == "UNKNOWN":
            logging.info('Game is in unknown mode: ' + MODE)
            MODE = "STARTSCREEN"
            return MODE

        elif MODE == "SAVE":
            with open('savefile.dat', 'wb') as f:
                pickle.dump([self.Charakter, Weltkarte.inventory],
                            f, protocol=2)
            logging.info('Game saved')
            MODE = "GAME"
            return MODE

        elif MODE == "LOAD":
            with open('savefile.dat', 'rb') as f:
                self.Charakter, Weltkarte.inventory = pickle.load(f)
            logging.info('Game loaded')
            MODE = "GAME"
            return MODE

        elif MODE == "NEWGAME":
            logging.info('Initializing new game')
            self.window.fill(Farben.clsFarben.BLACK)
            self.Charakter = run.run()
            pygame.display.update()
            MODE = "GAME"
            return MODE

        elif MODE == "GAME":
            global direction
            blackbar = pygame.Rect(Koordinaten.clsKoordinaten.BLACKBARSTART, Koordinaten.clsKoordinaten.BLACKBAREND,
                                   Weltkarte.MAPWIDTH * Weltkarte.TILESIZE,
                                   Weltkarte.MAPHEIGHT * Weltkarte.TILESIZE)

            characterButton = gui.PygButton((Koordinaten.clsKoordinaten.BUTTONPOSX,
                                             Koordinaten.clsKoordinaten.BUTTONPOSY,
                                             Koordinaten.clsKoordinaten.BUTTONWIDTH,
                                             Koordinaten.clsKoordinaten.BUTTONHEIGTH),
                                            'Charakter',
                                            bgcolor=Farben.clsFarben.DARKRED, fgcolor=Farben.clsFarben.BRIGHT)
            characterButton.font = self.fonts['small']
            direction = ""

            while True:
                pygame.display.update()
                for row in range(Weltkarte.MAPHEIGHT):
                    for column in range(Weltkarte.MAPWIDTH):
                        self.window.blit(Weltkarte.textures[BackgroundTilemap.getTilemap()[row][column]],
                                         (column * Weltkarte.TILESIZE, row * Weltkarte.TILESIZE))
                        self.window.blit(Weltkarte.textures[NewTilemap.getTilemap()[row][column]],
                                         (column * Weltkarte.TILESIZE, row * Weltkarte.TILESIZE))
                        self.window.blit(Weltkarte.environment[NewTilemap.getEnvironment()[row][column]],
                                         (column * Weltkarte.TILESIZE, row * Weltkarte.TILESIZE))
                pygame.draw.rect(
                    self.window, Farben.clsFarben.BLACK, blackbar)
                characterButton.draw(self.window)

                # a x b pixels of spritesheet
                a = 576 / 12
                b = 384 / 8
                if (isinstance(self.Charakter.get_type(), character.animaltypes.clsBaer)):
                    player_Sprite = self.spritesheets['bearsprites']
                    if(isinstance(self.Charakter.get_subtype(), character.animalsubtypes.Weiss)):
                        print('in condi')
                        amod = 3
                        bmod = 1
                    elif(isinstance(self.Charakter.get_subtype(), character.animalsubtypes.Grau)):
                        pass
                    elif(isinstance(self.Charakter.get_subtype(), character.animalsubtypes.Schwarz)):
                        pass
                    if direction == "right":
                        player_Icon = player_Sprite.image_at((a * amod, b * bmod * 2, a, b), colorkey=(0, 0, 0))
                    elif direction == "left":
                        player_Icon = player_Sprite.image_at((a * amod, b * bmod * 1, a, b), colorkey=(0, 0, 0))
                    elif direction == "up":
                        player_Icon = player_Sprite.image_at((a * amod, b * bmod * 3, a, b), colorkey=(0, 0, 0))
                    else:
                        player_Icon = player_Sprite.image_at((a * amod, b * bmod * 0, a, b), colorkey=(0, 0, 0))

                    sprites_bear_right_white = []
                    sprite_pos = 0
                    for sprite_pos in range(3):
                        bear_right = ((a * amod)+ (sprite_pos*a), b * 2, a, b)
                        sprites_bear_right_white.append((bear_right))

                    sprites_bear_left_white = []
                    sprite_pos = 0
                    for sprite_pos in range(3):
                        bear_left = ((a * amod) + (sprite_pos*a), b * bmod* 1, a, b)
                        sprites_bear_left_white.append((bear_left))

                    sprites_bear_up_white = []
                    sprite_pos = 0
                    for sprite_pos in range(3):
                        bear_up = ((a * amod) + (sprite_pos*a), b * bmod* 3, a, b)
                        sprites_bear_up_white.append((bear_up))

                    sprites_bear_down_white = []
                    sprite_pos = 0
                    for sprite_pos in range(3):
                        bear_down = ((a * amod) + (sprite_pos*a), b * bmod* 0, a, b)
                        sprites_bear_down_white.append((bear_down))


                elif(isinstance(self.Charakter.get_type(), character.animaltypes.clsRobbe)):
                    player_Sprite = self.spritesheets['sealsprites']
                    if direction == "right":
                        player_Icon = player_Sprite.image_at(
                            (a, b*2, a, b), colorkey=(0, 0, 0))
                    elif direction == "left":
                        player_Icon = player_Sprite.image_at(
                            (a, b, a, b), colorkey=(0, 0, 0))
                    elif direction == "up":
                        player_Icon = player_Sprite.image_at(
                            (a, b*3, a, b), colorkey=(0, 0, 0))
                    else:
                        player_Icon = player_Sprite.image_at(
                            (a, 0, a, b), colorkey=(0, 0, 0))

                    sprites_seal_right_white = []
                    sprite_pos = 0
                    for sprite_pos in range(3):
                        seal_right = (a*sprite_pos, b*2, a, b)
                        sprites_seal_right_white.append((seal_right))

                    sprites_seal_left_white = []
                    sprite_pos = 0
                    for sprite_pos in range(3):
                        seal_left = (a * sprite_pos, b, a, b)
                        sprites_seal_left_white.append((seal_left))

                    sprites_seal_down_white = []
                    sprite_pos = 0
                    for sprite_pos in range(3):
                        seal_down = (a*sprite_pos, 0, a, b)
                        sprites_seal_down_white.append((seal_down))

                    sprites_seal_up_white = []
                    sprite_pos = 0
                    for sprite_pos in range(3):
                        seal_up = (a*sprite_pos, b * 3, a, b)
                        sprites_seal_up_white.append((seal_up))
                player_Icon = pygame.transform.scale(player_Icon, (37,37))

                self.window.blit(
                    player_Icon, (
                         player_Icon_Position[0] * Weltkarte.TILESIZE,
                        (player_Icon_Position[1] * Weltkarte.TILESIZE)))

                # Generating and placing enemies
                for enemy in range(0, Enemies.get_Enemies_Anzahl()):
                    an_enemy = Enemies.get_Enemy(enemy)
                    if an_enemy.Art == "Käfer":
                        enemy_Icon = self.images['enemies']['bug']
                    elif an_enemy.Art == "Vogel":
                        enemy_Icon = self.images['enemies']['bird']
                    elif an_enemy.Art == "Kettensägenmensch":
                        enemy_Icon = self.images['enemies']['sawblade']
                    else:
                        enemy_Icon = self.images['unknown']
                    enemy_Icon = pygame.transform.scale(
                        enemy_Icon, (Weltkarte.TILESIZE, Weltkarte.TILESIZE))
                    enemy_Icon_Position = an_enemy.Position
                    self.window.blit(
                        enemy_Icon, (
                            enemy_Icon_Position[0] * Weltkarte.TILESIZE, enemy_Icon_Position[1] * Weltkarte.TILESIZE))

                # Snippets Showing
                Weltkarte.clsTileMap.drawSnippets(self.window)

                # Key and Mouse Input Handling
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()

                    #Button: 'Charakter'
                    events = characterButton.handleEvent(event)
                    if 'click' in events:
                        Charaktermenu = Interaktion.Menu(
                            self.window, self.Charakter)
                        Charaktermenu.draw(self.Charakter)

                    if event.type == KEYDOWN:
                        if (event.key == K_ESCAPE):
                            MODE = "STARTSCREEN"
                            return MODE
                        elif (event.key == K_RIGHT and player_Icon_Position[0] < Weltkarte.MAPWIDTH - 1):
                            if self.Charakter.get_status_temp('endu') <= 0:
                                print('Keine Energie mehr verfügbar')
                            else:
                                cont = True
                                nextTile = NewTilemap.getTilemap()[player_Icon_Position[1]
                                                                   ][player_Icon_Position[0]+1]
                                nextEnvironment = NewTilemap.getEnvironment()[player_Icon_Position[1]
                                                                              ][player_Icon_Position[0] + 1]
                                nextPosition = [
                                    player_Icon_Position[0]+1, player_Icon_Position[1]]
                                for enemy in range(0, Enemies.get_Enemies_Anzahl()):
                                    an_enemy = Enemies.get_Enemy(enemy)
                                    if nextPosition == an_enemy.Position:
                                        cont = False
                                currentEnvironment = NewTilemap.getEnvironment()[player_Icon_Position[1]
                                                                                 ][player_Icon_Position[0]]
                                for env in Weltkarte.enterable:
                                    if env == currentEnvironment:
                                        cont = False
                                if cont:
                                    for tile in Weltkarte.waterbehaviour:
                                        if tile == nextTile:
                                            if self.Charakter.has_skill(character.skills.SwimmingCharacterSkill):
                                                cont = True
                                                break
                                            else:
                                                cont = False
                                    if cont:
                                        for env in Weltkarte.enterable:
                                            if env == currentEnvironment:
                                                for env2 in Weltkarte.enterable:
                                                    if env == nextEnvironment:
                                                        cont = True
                                                        break
                                                    else:
                                                        cont = False
                                        for env in Weltkarte.collide:
                                            if env == nextEnvironment:
                                                cont = False
                                                break
                                        if cont:
                                            if(isinstance(self.Charakter.get_type(), character.animaltypes.clsBaer)):
                                                images = player_Sprite.images_at(
                                                    rects=sprites_bear_right_white, colorkey=[0, 0, 0])
                                            elif(isinstance(self.Charakter.get_type(), character.animaltypes.clsRobbe)):
                                                images = player_Sprite.images_at(
                                                    rects=sprites_seal_right_white, colorkey=[0, 0, 0])
                                            WalkAnim = pyganim.PygAnimation(
                                                [(images[0], 150), (images[1], 150), (images[2], 150)])
                                            WalkAnim.scale((37, 37))
                                            WalkAnim.play()
                                            walk = 0.0
                                            proceed = True
                                            while proceed:
                                                toRepaintcurrentBG = Weltkarte.textures[
                                                    BackgroundTilemap.getTilemap()[player_Icon_Position[1]][
                                                        player_Icon_Position[0]]]
                                                toRepaintcurrentBG = pygame.transform.scale(toRepaintcurrentBG, (
                                                    Weltkarte.TILESIZE, Weltkarte.TILESIZE))
                                                toRepaintcurrent = Weltkarte.textures[
                                                    NewTilemap.getTilemap()[player_Icon_Position[1]][player_Icon_Position[0]]]
                                                toRepaintcurrent = pygame.transform.scale(toRepaintcurrent, (
                                                    Weltkarte.TILESIZE, Weltkarte.TILESIZE))
                                                toRepaintcurrentenvironment = Weltkarte.environment[NewTilemap.getEnvironment(
                                                )[player_Icon_Position[1]][player_Icon_Position[0]]]
                                                toRepaintnextBG = Weltkarte.textures[
                                                    BackgroundTilemap.getTilemap()[nextPosition[1]][nextPosition[0]]]
                                                toRepaintnextBG = pygame.transform.scale(toRepaintnextBG, (
                                                    Weltkarte.TILESIZE, Weltkarte.TILESIZE))
                                                toRepaintnext = Weltkarte.textures[
                                                    NewTilemap.getTilemap()[nextPosition[1]][nextPosition[0]]]
                                                toRepaintnext = pygame.transform.scale(toRepaintnext, (
                                                    Weltkarte.TILESIZE, Weltkarte.TILESIZE))
                                                toRepaintnextenvironment = Weltkarte.environment[
                                                    NewTilemap.getEnvironment()[nextPosition[1]][nextPosition[0]]]

                                                self.window.blit(toRepaintcurrentBG,
                                                                 (player_Icon_Position[0] * Weltkarte.TILESIZE,
                                                                  player_Icon_Position[1] * Weltkarte.TILESIZE))
                                                self.window.blit(toRepaintcurrent,
                                                                 (player_Icon_Position[0] * Weltkarte.TILESIZE,
                                                                  player_Icon_Position[1] * Weltkarte.TILESIZE))
                                                self.window.blit(toRepaintcurrentenvironment,
                                                                 (player_Icon_Position[0] * Weltkarte.TILESIZE,
                                                                  player_Icon_Position[1] * Weltkarte.TILESIZE))
                                                self.window.blit(toRepaintnextBG,
                                                                 (nextPosition[0] * Weltkarte.TILESIZE,
                                                                  nextPosition[1] * Weltkarte.TILESIZE))
                                                self.window.blit(toRepaintnext,
                                                                 (nextPosition[0] * Weltkarte.TILESIZE,
                                                                  nextPosition[1] * Weltkarte.TILESIZE))
                                                self.window.blit(toRepaintnextenvironment,
                                                                 (nextPosition[0] * Weltkarte.TILESIZE,
                                                                  nextPosition[1] * Weltkarte.TILESIZE))

                                                WalkAnim.blit(self.window,
                                                              (player_Icon_Position[0] * Weltkarte.TILESIZE + walk,
                                                               (player_Icon_Position[1] * Weltkarte.TILESIZE)))
                                                pygame.display.update()
                                                walk += 1
                                                fpsClock.tick(FPS)
                                                if player_Icon_Position[0]*Weltkarte.TILESIZE + walk > (player_Icon_Position[0]+1)*Weltkarte.TILESIZE:
                                                    proceed = False
                                            direction = "right"
                                            player_Icon_Position[0] += 1
                                            self.Charakter.change_status_temp(
                                                'endu', '-')
                                            if self.Charakter.has_skill(character.skills.RunnerCharacterSkill):
                                                rand_int = Wahrscheinlichkeiten.haelftehaelfte()
                                                if rand_int:
                                                    self.Charakter.change_status_temp(
                                                        'endu', '+')
                        elif (event.key == K_LEFT and player_Icon_Position[0] > 0):
                            if self.Charakter.get_status_temp('endu') <= 0:
                                print('Keine Energie mehr verfügbar')
                            else:
                                cont = True
                                nextTile = NewTilemap.getTilemap()[player_Icon_Position[1]
                                                                   ][player_Icon_Position[0] - 1]
                                nextEnvironment = NewTilemap.getEnvironment()[player_Icon_Position[1]
                                                                              ][player_Icon_Position[0] - 1]
                                currentEnvironment = NewTilemap.getEnvironment()[player_Icon_Position[1]
                                                                                 ][player_Icon_Position[0]]
                                nextPosition = [
                                    player_Icon_Position[0] - 1, player_Icon_Position[1]]
                                for enemy in range(0, Enemies.get_Enemies_Anzahl()):
                                    an_enemy = Enemies.get_Enemy(enemy)
                                    if nextPosition == an_enemy.Position:
                                        cont = False
                                if cont:
                                    for env in Weltkarte.enterable:
                                        if env == currentEnvironment:
                                            for env2 in Weltkarte.enterable:
                                                if env2 == nextEnvironment:
                                                    cont = True
                                                    break
                                                else:
                                                    cont = False
                                    if cont:
                                        for tile in Weltkarte.waterbehaviour:
                                            if tile == nextTile:
                                                if self.Charakter.has_skill(character.skills.SwimmingCharacterSkill):
                                                    cont = True
                                                    break
                                                else:
                                                    cont = False
                                        if cont:
                                            for env in Weltkarte.collide:
                                                if env == nextEnvironment:
                                                    cont = False
                                                    break
                                            if cont:
                                                if (isinstance(self.Charakter.get_type(), character.animaltypes.clsBaer)):
                                                    images = player_Sprite.images_at(
                                                        rects=sprites_bear_left_white, colorkey=[0, 0, 0])
                                                elif (
                                                isinstance(self.Charakter.get_type(), character.animaltypes.clsRobbe)):
                                                    images = player_Sprite.images_at(
                                                        rects=sprites_seal_left_white, colorkey=[0, 0, 0])
                                                WalkAnim = pyganim.PygAnimation(
                                                    [(images[0], 150), (images[1], 150), (images[2], 150)])
                                                WalkAnim.scale((37, 37))
                                                WalkAnim.play()
                                                walk = 0.0
                                                proceed = True
                                                while proceed:
                                                    toRepaintcurrentBG = Weltkarte.textures[
                                                        BackgroundTilemap.getTilemap()[player_Icon_Position[1]][
                                                            player_Icon_Position[0]]]
                                                    toRepaintcurrentBG = pygame.transform.scale(toRepaintcurrentBG, (
                                                        Weltkarte.TILESIZE, Weltkarte.TILESIZE))
                                                    toRepaintcurrent = Weltkarte.textures[
                                                        NewTilemap.getTilemap()[player_Icon_Position[1]][
                                                            player_Icon_Position[0]]]
                                                    toRepaintcurrent = pygame.transform.scale(toRepaintcurrent, (
                                                        Weltkarte.TILESIZE, Weltkarte.TILESIZE))
                                                    toRepaintcurrentenvironment = Weltkarte.environment[
                                                        NewTilemap.getEnvironment()[player_Icon_Position[1]][
                                                            player_Icon_Position[0]]]
                                                    toRepaintnextBG = Weltkarte.textures[
                                                        BackgroundTilemap.getTilemap()[nextPosition[1]][nextPosition[0]]]
                                                    toRepaintnextBG = pygame.transform.scale(toRepaintnextBG, (
                                                        Weltkarte.TILESIZE, Weltkarte.TILESIZE))
                                                    toRepaintnext = Weltkarte.textures[
                                                        NewTilemap.getTilemap()[nextPosition[1]][nextPosition[0]]]
                                                    toRepaintnext = pygame.transform.scale(toRepaintnext, (
                                                        Weltkarte.TILESIZE, Weltkarte.TILESIZE))
                                                    toRepaintnextenvironment = Weltkarte.environment[
                                                        NewTilemap.getEnvironment()[nextPosition[1]][nextPosition[0]]]

                                                    self.window.blit(toRepaintcurrentBG,
                                                                     (player_Icon_Position[0] * Weltkarte.TILESIZE,
                                                                      player_Icon_Position[1] * Weltkarte.TILESIZE))
                                                    self.window.blit(toRepaintcurrent,
                                                                     (player_Icon_Position[0] * Weltkarte.TILESIZE,
                                                                      player_Icon_Position[1] * Weltkarte.TILESIZE))
                                                    self.window.blit(toRepaintcurrentenvironment,
                                                                     (player_Icon_Position[0] * Weltkarte.TILESIZE,
                                                                      player_Icon_Position[1] * Weltkarte.TILESIZE))
                                                    self.window.blit(toRepaintnextBG,
                                                                     (nextPosition[0] * Weltkarte.TILESIZE,
                                                                      nextPosition[1] * Weltkarte.TILESIZE))
                                                    self.window.blit(toRepaintnext,
                                                                     (nextPosition[0] * Weltkarte.TILESIZE,
                                                                      nextPosition[1] * Weltkarte.TILESIZE))
                                                    self.window.blit(toRepaintnextenvironment,
                                                                     (nextPosition[0] * Weltkarte.TILESIZE,
                                                                      nextPosition[1] * Weltkarte.TILESIZE))

                                                    WalkAnim.blit(self.window,
                                                                (player_Icon_Position[0] * Weltkarte.TILESIZE - walk,
                                                                (player_Icon_Position[1] * Weltkarte.TILESIZE)))
                                                    pygame.display.update()
                                                    walk += 1
                                                    fpsClock.tick(FPS)
                                                    if player_Icon_Position[0] * Weltkarte.TILESIZE - walk < (
                                                            player_Icon_Position[0] - 1) * Weltkarte.TILESIZE:
                                                        proceed = False
                                                direction = "left"
                                                player_Icon_Position[0] -= 1
                                                self.Charakter.change_status_temp(
                                                    'endu', '-')
                                                if self.Charakter.has_skill(character.skills.RunnerCharacterSkill):
                                                    rand_int = Wahrscheinlichkeiten.haelftehaelfte()
                                                    if rand_int:
                                                        self.Charakter.change_status_temp(
                                                            'endu', '+')
                                        else:
                                            break
                        elif (event.key == K_DOWN and player_Icon_Position[1] < Weltkarte.MAPHEIGHT - 1):
                            if self.Charakter.get_status_temp('endu') <= 0:
                                print('Keine Energie mehr verfügbar')
                            else:
                                cont = True
                                nextTile = NewTilemap.getTilemap()[player_Icon_Position[1]+1
                                                                   ][player_Icon_Position[0]]
                                nextEnvironment = NewTilemap.getEnvironment()[player_Icon_Position[1] + 1
                                                                              ][player_Icon_Position[0]]
                                nextPosition = [
                                    player_Icon_Position[0], player_Icon_Position[1]+1]
                                for enemy in range(0, Enemies.get_Enemies_Anzahl()):
                                    an_enemy = Enemies.get_Enemy(enemy)
                                    if nextPosition == an_enemy.Position:
                                        cont = False
                                for tile in Weltkarte.waterbehaviour:
                                    if tile == nextTile:
                                        if self.Charakter.has_skill(character.skills.SwimmingCharacterSkill):
                                            cont = True
                                            break
                                        else:
                                            cont = False
                                for env in Weltkarte.collide:
                                    if env == nextEnvironment:
                                        cont = False
                                        break
                                if cont:
                                    if (isinstance(self.Charakter.get_type(), character.animaltypes.clsBaer)):
                                        images = player_Sprite.images_at(
                                            rects=sprites_bear_down_white, colorkey=[0, 0, 0])
                                    elif (isinstance(self.Charakter.get_type(), character.animaltypes.clsRobbe)):
                                        images = player_Sprite.images_at(
                                            rects=sprites_seal_down_white, colorkey=[0, 0, 0])
                                    WalkAnim = pyganim.PygAnimation(
                                        [(images[0], 150), (images[1], 150), (images[2], 150)])
                                    WalkAnim.scale((37, 37))
                                    WalkAnim.play()
                                    walk = 0.0
                                    proceed = True
                                    while proceed:
                                        toRepaintcurrentBG = Weltkarte.textures[
                                            BackgroundTilemap.getTilemap()[player_Icon_Position[1]][
                                                player_Icon_Position[0]]]
                                        toRepaintcurrentBG = pygame.transform.scale(toRepaintcurrentBG, (
                                            Weltkarte.TILESIZE, Weltkarte.TILESIZE))
                                        toRepaintcurrent = Weltkarte.textures[
                                            NewTilemap.getTilemap()[player_Icon_Position[1]][player_Icon_Position[0]]]
                                        toRepaintcurrent = pygame.transform.scale(toRepaintcurrent, (
                                            Weltkarte.TILESIZE, Weltkarte.TILESIZE))
                                        toRepaintcurrentenvironment = Weltkarte.environment[
                                            NewTilemap.getEnvironment()[player_Icon_Position[1]][
                                                player_Icon_Position[0]]]
                                        toRepaintnextBG = Weltkarte.textures[
                                            BackgroundTilemap.getTilemap()[nextPosition[1]][nextPosition[0]]]
                                        toRepaintnextBG = pygame.transform.scale(toRepaintnextBG, (
                                            Weltkarte.TILESIZE, Weltkarte.TILESIZE))
                                        toRepaintnext = Weltkarte.textures[
                                            NewTilemap.getTilemap()[nextPosition[1]][nextPosition[0]]]
                                        toRepaintnext = pygame.transform.scale(toRepaintnext, (
                                            Weltkarte.TILESIZE, Weltkarte.TILESIZE))
                                        toRepaintnextenvironment = Weltkarte.environment[
                                            NewTilemap.getEnvironment()[nextPosition[1]][nextPosition[0]]]

                                        self.window.blit(toRepaintcurrentBG,
                                                         (player_Icon_Position[0] * Weltkarte.TILESIZE,
                                                          player_Icon_Position[1] * Weltkarte.TILESIZE))
                                        self.window.blit(toRepaintcurrent,
                                                         (player_Icon_Position[0] * Weltkarte.TILESIZE,
                                                          player_Icon_Position[1] * Weltkarte.TILESIZE))
                                        self.window.blit(toRepaintcurrentenvironment,
                                                         (player_Icon_Position[0] * Weltkarte.TILESIZE,
                                                          player_Icon_Position[1] * Weltkarte.TILESIZE))
                                        self.window.blit(toRepaintnextBG,
                                                         (nextPosition[0] * Weltkarte.TILESIZE,
                                                          nextPosition[1] * Weltkarte.TILESIZE))
                                        self.window.blit(toRepaintnext,
                                                         (nextPosition[0] * Weltkarte.TILESIZE,
                                                          nextPosition[1] * Weltkarte.TILESIZE))
                                        self.window.blit(toRepaintnextenvironment,
                                                         (nextPosition[0] * Weltkarte.TILESIZE,
                                                          nextPosition[1] * Weltkarte.TILESIZE))

                                        WalkAnim.blit(self.window,
                                                      (player_Icon_Position[0] * Weltkarte.TILESIZE,
                                                        (player_Icon_Position[1] * Weltkarte.TILESIZE) + walk))
                                        pygame.display.update()
                                        walk += 1
                                        fpsClock.tick(FPS)
                                        if player_Icon_Position[1] * Weltkarte.TILESIZE + walk > (
                                                player_Icon_Position[1] + 1) * Weltkarte.TILESIZE:
                                            proceed = False
                                    direction = "down"
                                    player_Icon_Position[1] += 1
                                    self.Charakter.change_status_temp(
                                        'endu', '-')
                                    if self.Charakter.has_skill(character.skills.RunnerCharacterSkill):
                                        rand_int = Wahrscheinlichkeiten.haelftehaelfte()
                                        if rand_int:
                                            self.Charakter.change_status_temp(
                                                'endu', '+')
                        elif (event.key == K_UP and player_Icon_Position[1] > 0):
                            if self.Charakter.get_status_temp('endu') <= 0:
                                print('Keine Energie mehr verfügbar')
                            else:
                                cont = True
                                nextTile = NewTilemap.getTilemap()[player_Icon_Position[1]-1
                                                                   ][player_Icon_Position[0]]
                                currentEnvironment = NewTilemap.getEnvironment()[player_Icon_Position[1]
                                                                                 ][player_Icon_Position[0]]
                                nextEnvironment = NewTilemap.getEnvironment()[player_Icon_Position[1]-1
                                                                              ][player_Icon_Position[0]]
                                nextPosition = [
                                    player_Icon_Position[0], player_Icon_Position[1]-1]
                                for enemy in range(0, Enemies.get_Enemies_Anzahl()):
                                    an_enemy = Enemies.get_Enemy(enemy)
                                    if nextPosition == an_enemy.Position:
                                        cont = False
                                for env in Weltkarte.enterable:
                                    if env == currentEnvironment:
                                        cont = False
                                if cont:
                                    if nextEnvironment == Weltkarte.STONEHOLE:
                                        if self.Charakter.has_skill(character.skills.SwimmingCharacterSkill):
                                            cont = True
                                            break
                                        else:
                                            cont = False
                                    for env in Weltkarte.collide:
                                        if env == nextEnvironment:
                                            cont = False
                                            break
                                    for tile in Weltkarte.waterbehaviour:
                                        if tile == nextTile:
                                            if self.Charakter.has_skill(character.skills.SwimmingCharacterSkill):
                                                cont = True
                                                break
                                            else:
                                                cont = False
                                    if cont:
                                        if (isinstance(self.Charakter.get_type(), character.animaltypes.clsBaer)):
                                            images = player_Sprite.images_at(
                                                rects=sprites_bear_up_white, colorkey=[0, 0, 0])
                                        elif (isinstance(self.Charakter.get_type(), character.animaltypes.clsRobbe)):
                                            images = player_Sprite.images_at(
                                                rects=sprites_seal_up_white, colorkey=[0, 0, 0])
                                        WalkAnim = pyganim.PygAnimation(
                                            [(images[0], 150), (images[1], 150), (images[2], 150)])
                                        WalkAnim.scale((37, 37))
                                        WalkAnim.play()
                                        walk = 0.0
                                        proceed = True
                                        while proceed:
                                            toRepaintcurrentBG = Weltkarte.textures[
                                                BackgroundTilemap.getTilemap()[player_Icon_Position[1]][
                                                    player_Icon_Position[0]]]
                                            toRepaintcurrentBG = pygame.transform.scale(toRepaintcurrentBG, (
                                                Weltkarte.TILESIZE, Weltkarte.TILESIZE))
                                            toRepaintcurrent = Weltkarte.textures[
                                                NewTilemap.getTilemap()[player_Icon_Position[1]][
                                                    player_Icon_Position[0]]]
                                            toRepaintcurrent = pygame.transform.scale(toRepaintcurrent, (
                                                Weltkarte.TILESIZE, Weltkarte.TILESIZE))
                                            toRepaintcurrentenvironment = Weltkarte.environment[
                                                NewTilemap.getEnvironment()[player_Icon_Position[1]][
                                                    player_Icon_Position[0]]]
                                            toRepaintnextBG = Weltkarte.textures[
                                                BackgroundTilemap.getTilemap()[nextPosition[1]][nextPosition[0]]]
                                            toRepaintnextBG = pygame.transform.scale(toRepaintnextBG, (
                                                Weltkarte.TILESIZE, Weltkarte.TILESIZE))
                                            toRepaintnext = Weltkarte.textures[
                                                NewTilemap.getTilemap()[nextPosition[1]][nextPosition[0]]]
                                            toRepaintnext = pygame.transform.scale(toRepaintnext, (
                                                Weltkarte.TILESIZE, Weltkarte.TILESIZE))
                                            toRepaintnextenvironment = Weltkarte.environment[
                                                NewTilemap.getEnvironment()[nextPosition[1]][nextPosition[0]]]

                                            self.window.blit(toRepaintcurrentBG,
                                                             (player_Icon_Position[0] * Weltkarte.TILESIZE,
                                                              player_Icon_Position[1] * Weltkarte.TILESIZE))
                                            self.window.blit(toRepaintcurrent,
                                                             (player_Icon_Position[0] * Weltkarte.TILESIZE,
                                                              player_Icon_Position[1] * Weltkarte.TILESIZE))
                                            self.window.blit(toRepaintcurrentenvironment,
                                                             (player_Icon_Position[0] * Weltkarte.TILESIZE,
                                                              player_Icon_Position[1] * Weltkarte.TILESIZE))
                                            self.window.blit(toRepaintnextBG,
                                                             (nextPosition[0] * Weltkarte.TILESIZE,
                                                              nextPosition[1] * Weltkarte.TILESIZE))
                                            self.window.blit(toRepaintnext,
                                                             (nextPosition[0] * Weltkarte.TILESIZE,
                                                              nextPosition[1] * Weltkarte.TILESIZE))
                                            self.window.blit(toRepaintnextenvironment,
                                                             (nextPosition[0] * Weltkarte.TILESIZE,
                                                              nextPosition[1] * Weltkarte.TILESIZE))
                                            WalkAnim.blit(self.window,
                                                          (player_Icon_Position[0] * Weltkarte.TILESIZE,
                                                           (player_Icon_Position[1] * Weltkarte.TILESIZE) + walk))
                                            pygame.display.update()
                                            walk -= 1
                                            fpsClock.tick(FPS)
                                            if player_Icon_Position[1] * Weltkarte.TILESIZE + walk < (
                                                    player_Icon_Position[1] - 1) * Weltkarte.TILESIZE:
                                                proceed = False
                                        direction = "up"
                                        player_Icon_Position[1] -= 1
                                        self.Charakter.change_status_temp(
                                            'endu', '-')
                                        if self.Charakter.has_skill(character.skills.RunnerCharacterSkill):
                                            rand_int = Wahrscheinlichkeiten.haelftehaelfte()
                                            if rand_int:
                                                self.Charakter.change_status_temp(
                                                    'endu', '+')
                        elif (event.key == K_SPACE):
                            currentTile = NewTilemap.getTilemap()[player_Icon_Position[1]
                                                                  ][player_Icon_Position[0]]
                            if (currentTile == Weltkarte.DIRT and self.Charakter.has_skill(character.skills.PlantingCharacterSkill)):
                                #NewTilemap.getTilemap()[player_Icon_Position[1]
                                #                        ][player_Icon_Position[0]] = Weltkarte.GRASS
                                NewTilemap.getEnvironment()[player_Icon_Position[1]
                                                            ][player_Icon_Position[0]] = Weltkarte.LOWGRASS
                                self.Charakter.change_status_temp('magic', '-')
                                break
                            elif currentTile == Weltkarte.GRASSLAND:
                                currentEnvironment = NewTilemap.getEnvironment()[player_Icon_Position[1]
                                                                                 ][player_Icon_Position[0]]
                                hasenv = False
                                for grass in Weltkarte.grasses:
                                    if grass == currentEnvironment:
                                        hasenv = True
                                if hasenv:
                                    # Fähigkeit Grasschlitzer: Chance auf doppelte Ressourcen
                                    if self.Charakter.has_skill(character.skills.GrasMovementCharacterSkill):
                                        rand_int = Wahrscheinlichkeiten.haelftehaelfte()
                                        if rand_int:
                                            Weltkarte.inventory[currentEnvironment] += 1
                                    # Sammeln
                                    Weltkarte.inventory[currentEnvironment]+=1
                                    NewTilemap.getEnvironment()[player_Icon_Position[1]
                                    ][player_Icon_Position[0]] = Weltkarte.DEADGRASS

                                else:
                                    Weltkarte.inventory[currentTile] += 1
                                    NewTilemap.getTilemap()[player_Icon_Position[1]
                                                            ][player_Icon_Position[0]] = Weltkarte.DIRT

                        elif (event.key == K_m):
                            # non-fighting skills
                            stealthSkill = False
                            healSkill = False
                            plantingSkill = False
                            saverSkill = False
                            if (self.Charakter.has_skill(character.skills.StealthCharacterSkill)):
                                stealthSkill = True
                            if (self.Charakter.has_skill(character.skills.MagicalHealCharacterSkill)):
                                healSkill = True
                            if (self.Charakter.has_skill(character.skills.PlantingCharacterSkill)):
                                plantingSkill = True
                            if (self.Charakter.has_skill(character.skills.SaversCharacterSkill)):
                                saverSkill = True
                            if stealthSkill == True:
                                enough_temp_value = False
                                if self.Charakter.get_status_temp('magic') > 1:
                                    enough_temp_value = True
                                bubble = Interaktion.Bubble(self.window, player_Icon_Position, -1,
                                                            -1, "stealth", enough_temp_value)
                                stealthbubble = bubble.draw_bubble()
                            if healSkill == True:
                                enough_temp_value = False
                                if self.Charakter.get_status_temp('magic') > 1:
                                    enough_temp_value = True
                                bubble = Interaktion.Bubble(self.window, player_Icon_Position, 2,
                                                            -1, "magical_heal", enough_temp_value)
                                healbubble = bubble.draw_bubble()
                            if plantingSkill == True:
                                enough_temp_value = False
                                if self.Charakter.get_status_temp('magic') > 1:
                                    currentTile = NewTilemap.getTilemap()[player_Icon_Position[1]
                                                                          ][player_Icon_Position[0]]
                                    if currentTile == Weltkarte.DIRT or currentTile == Weltkarte.GRASSLAND:
                                        enough_temp_value = True
                                bubble = Interaktion.Bubble(self.window, player_Icon_Position, -1,
                                                            2, "plant", enough_temp_value)
                                plantbubble = bubble.draw_bubble()
                            if saverSkill == True:
                                enough_temp_value = False
                                if self.Charakter.get_status_temp('endu') > 1:
                                    enough_temp_value = True
                                bubble = Interaktion.Bubble(self.window, player_Icon_Position, 2,
                                                            2, "robe", enough_temp_value)
                                saverbubble = bubble.draw_bubble()

                            if stealthSkill or healSkill or plantingSkill or saverSkill:
                                wait_for_click = True
                            else:
                                wait_for_click = False
                            # if character has one of the passive skills:
                            while wait_for_click:
                                for event in pygame.event.get():
                                    if event.type == QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == MOUSEBUTTONDOWN:
                                        if enough_temp_value == False:
                                            break
                                        elif enough_temp_value == True:
                                            mousepos = event.pos
                                            if stealthSkill:
                                                if stealthbubble.collidepoint(mousepos):
                                                    self.Charakter.change_status_temp(
                                                        'magic', '-')
                                            if healSkill:
                                                if healbubble.collidepoint(mousepos):
                                                    self.Charakter.change_status_temp(
                                                        'magic', '-')
                                                    self.Charakter.change_status_temp(
                                                        'endurance', '+')
                                                    self.Charakter.change_status_temp(
                                                        'health', '+')
                                            if plantingSkill:
                                                if plantbubble.collidepoint(mousepos):
                                                    currentTile = NewTilemap.getTilemap()[player_Icon_Position[1]
                                                                                          ][player_Icon_Position[0]]
                                                    if currentTile == Weltkarte.DIRT:
                                                        NewTilemap.getTilemap()[player_Icon_Position[1]
                                                                                ][player_Icon_Position[0]] = Weltkarte.GRASSLAND
                                                        self.Charakter.change_status_temp(
                                                            'magic', '-')
                                                    elif currentTile == Weltkarte.GRASSLAND:
                                                        NewTilemap.getTilemap()[player_Icon_Position[1]
                                                                                ][player_Icon_Position[0]] = Weltkarte.HIGHGRASS
                                                        self.Charakter.change_status_temp(
                                                            'magic', '-')
                                                    break

                                            if saverSkill:
                                                if saverbubble.collidepoint(mousepos):
                                                    self.Charakter.change_status_temp(
                                                        'endu', '-')
                                    elif event.type == KEYDOWN:
                                        if event.key == K_m:
                                            wait_for_click = False

                        elif(event.key == K_f):
                            # fighting skills
                            biteSkill = False  # MAGIC!
                            tailSkill = False
                            earthSkill = False
                            active = False
                            if(self.Charakter.has_skill(character.skills.BiteCharacterSkill)):
                                biteSkill = True
                            if(self.Charakter.has_skill(character.skills.TailCharacterSkill)):
                                tailSkill = True
                            if(self.Charakter.has_skill(character.skills.EarthquakeCharacterSkill)):
                                earthSkill = True
                            # Liste, in der alle den Spieler umgebenden Felder gespeichert sind, abhängig von dessen Position
                            Liste = []
                            Enemies_in_range = []
                            for tile_x in range(player_Icon_Position[0]-1, player_Icon_Position[0]+2):
                                for tile_y in range(player_Icon_Position[1] - 1, player_Icon_Position[1] + 2):
                                    to_append = [tile_x, tile_y]
                                    Liste.append(to_append)
                            for element in Liste:
                                for enemy in range(0, Enemies.get_Enemies_Anzahl()):
                                    an_enemy = Enemies.get_Enemy(enemy)
                                    if element == an_enemy.Position:
                                        active = True
                                        Enemies_in_range.append(an_enemy)

                            wait_for_click = True
                            while wait_for_click:
                                # pygame.display.update()
                                for event in pygame.event.get():
                                    if event.type == QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == MOUSEBUTTONDOWN:
                                        if active == False:
                                            break
                                        elif active == True:
                                            mousepos = event.pos
                                            if standardbubble.collidepoint(mousepos):
                                                for enemy in Enemies_in_range:
                                                    enemy_tile = NewTilemap.getTilemap()[enemy.Position[1]
                                                                                         ][enemy.Position[0]]
                                                    enemy.lower_Gesundheit(1)
                                                    enemy.damage_and_death_anim(
                                                        self.window, "damage", enemy_tile)
                                                    self.Charakter.change_status_temp(
                                                        'endu', '-')
                                                    if enemy.Gesundheit <= 0:
                                                        #    #resolution dpi noch fehlerhaft
                                                        enemy.damage_and_death_anim(
                                                            self.window, "death", enemy_tile)
                                                        Enemies.delete_from_list(
                                                            enemy)
                                                        Enemies_in_range.remove(
                                                            enemy)
                                                        enemy.__del__
                                                        if not Enemies_in_range:
                                                            active = False
                                                        break

                                            if biteSkill:
                                                if bitebubble.collidepoint(mousepos):
                                                    for enemy in Enemies_in_range:
                                                        enemy_tile = NewTilemap.getTilemap()[enemy.Position[1]
                                                                                             ][enemy.Position[0]]
                                                        enemy.lower_Gesundheit(
                                                            2)
                                                        enemy.damage_and_death_anim(
                                                            self.window, "damage", enemy_tile)
                                                        if enemy.Gesundheit <= 0:
                                                            #    #resolution dpi noch fehlerhaft
                                                            enemy.damage_and_death_anim(
                                                                self.window, "death", enemy_tile)
                                                            Enemies.delete_from_list(
                                                                enemy)
                                                            Enemies_in_range.remove(
                                                                enemy)
                                                            enemy.__del__
                                                            if not Enemies_in_range:
                                                                active = False
                                                            break
                                                    self.Charakter.change_status_temp(
                                                        'magic', '-')
                                            if tailSkill:
                                                if tailbubble.collidepoint(mousepos):
                                                    for enemy in Enemies_in_range:
                                                        enemy_tile = NewTilemap.getTilemap()[enemy.Position[1]
                                                                                             ][enemy.Position[0]]
                                                        enemy.lower_Gesundheit(
                                                            2)
                                                        enemy.damage_and_death_anim(
                                                            self.window, "damage", enemy_tile)
                                                        if enemy.Gesundheit <= 0:
                                                            #    #resolution dpi noch fehlerhaft
                                                            enemy.damage_and_death_anim(
                                                                self.window, "death", enemy_tile)
                                                            Enemies.delete_from_list(
                                                                enemy)
                                                            Enemies_in_range.remove(
                                                                enemy)
                                                            enemy.__del__
                                                            if not Enemies_in_range:
                                                                active = False
                                                            break
                                                    self.Charakter.change_status_temp(
                                                        'endu', '-')
                                            if earthSkill:
                                                if earthbubble.collidepoint(mousepos):
                                                    dirtimage = pygame.image.load(
                                                        './resources/images/ressourcen/dirttexture.png').convert()
                                                    dirtimage = pygame.transform.scale(dirtimage,
                                                                                       (Weltkarte.TILESIZE, Weltkarte.TILESIZE))
                                                    for tile in Liste:
                                                        # Exception handling fehlt: falls list index out of range, z.b. bei feinden direkt am spielrand
                                                        Weltkarte.NewTilemap.getTilemap()[tile[1]
                                                                                          ][tile[0]] = Weltkarte.DIRT
                                                        self.window.blit(dirtimage,
                                                                         (tile[0] * Weltkarte.TILESIZE, tile[1] * Weltkarte.TILESIZE))
                                                    self.window.blit(
                                                        player_Icon, (
                                                            player_Icon_Position[0] *
                                                            Weltkarte.TILESIZE,
                                                            player_Icon_Position[1] * Weltkarte.TILESIZE))
                                                    pygame.display.update()
                                                    fpsClock.tick(FPS)
                                                    for enemy in Enemies_in_range:
                                                        enemy_tile = NewTilemap.getTilemap()[enemy.Position[1]
                                                                                             ][enemy.Position[0]]
                                                        enemy.lower_Gesundheit(
                                                            Wahrscheinlichkeiten.wuerfel(5))
                                                        enemy.damage_and_death_anim(
                                                            self.window, "damage", enemy_tile)
                                                        if enemy.Gesundheit <= 0:
                                                            #    #resolution dpi noch fehlerhaft
                                                            enemy.damage_and_death_anim(
                                                                self.window, "death", enemy_tile)
                                                            Enemies.delete_from_list(
                                                                enemy)
                                                            Enemies_in_range.remove(
                                                                enemy)
                                                            enemy.__del__
                                                            if not Enemies_in_range:
                                                                active = False
                                                            break
                                                    self.Charakter.change_status_temp(
                                                        'endu', '-')
                                                    self.Charakter.change_status_temp(
                                                        'health', '-')

                                    elif event.type == KEYDOWN:
                                        if event.key == K_f:
                                            wait_for_click = False

                                    bubble = Interaktion.Bubble(self.window, player_Icon_Position, -1,
                                                                -1, "standard", active)
                                    standardbubble = bubble.draw_bubble()
                                    if biteSkill == True:
                                        bubble = Interaktion.Bubble(self.window, player_Icon_Position, 2,
                                                                    -1, "bite", active)
                                        bitebubble = bubble.draw_bubble()
                                    if tailSkill == True:
                                        bubble = Interaktion.Bubble(self.window, player_Icon_Position, -1,
                                                                    2, "tail", active)
                                        tailbubble = bubble.draw_bubble()
                                    if earthSkill == True:
                                        bubble = Interaktion.Bubble(self.window, player_Icon_Position, 2,
                                                                    2, "earthquake", active)
                                        earthbubble = bubble.draw_bubble()
                        elif (event.key == K_e):
                            # STAR = pygame.draw.lines(self.window, Farben.clsFarben.GOLD, 1, LevelupForm.Star, 3)
                            # self.window.blit(STAR, (CharakterForm.POSITION[0]*Weltkarte.py.TILESIZE,CharakterForm.POSITION[1]*Weltkarte.py.TILESIZE))
                            # pygame.draw.rect(self.window, Farben.clsFarben.BLACK, STAR, 2)
                            print(self.Charakter.get_status_max('health'))
                            print(self.Charakter.get_status_temp('health'))
                            print(self.Charakter.get_status_max('endu'))
                            print(self.Charakter.get_status_temp('endu'))


NeuesSpiel = Spiel(MODE, Charakter)
while True:
    MODE = NeuesSpiel.spielen(MODE)
