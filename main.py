# Robbie likes: https://medium.com/@yvanscher/making-a-game-ai-with-deep-learning-963bb549b3d5
# Very nice: http://game-icons.net/
# TODO: enemies correct walking
# BUG: enemy can walk on player position
# TODO: magic -> animation, recoloration!
# IDEA: Winterschlafvorbereitung treffen
# @ANDRE: Seal images (animalstages) without logo, spritesheets transparent


import pygame
import sys
import gui
import os
import logging
from pygame.locals import *
import pickle
import inspect
import pyganim
import Start_Screen
import World_Map
import Animations_and_Enemies
import Interact
import Percentages
from resources import Farben, Koordinaten
import Character_Builder
import character
import Helper


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
pygame.display.set_icon(Helper.load_image('icon.png'))
FPS = 60
fpsClock = pygame.time.Clock()
Charakter = character.Character()
MODE = "UNKNOWN"


class Spiel(object):

    def __init__(self, MODE, Charakter):
        self.MODE = MODE
        self.Charakter = Charakter
        self.window = World_Map.SURFACE
        self._load_fonts()
        self._load_images()
        self._load_spritesheets()
        self.BackgroundTilemap = World_Map.clsTileMap()
        self.NewTilemap = World_Map.clsTileMap()
        # NewTilemap.randomTilemap()
        self.NewTilemap.customTilemap()
        self.NewTilemap.environment_customTilemap()
        self.Enemies = Animations_and_Enemies.cls_Enemies()
        self.Enemies.fill_Enemies_list(self.NewTilemap)
        self.player_Icon_Position = [0, 0]

    def _load_fonts(self):
        logging.info('Loading fonts')
        self.fonts = {
            'normal': Helper.load_font('celtic_gaelige.ttf', 19),
            'small': Helper.load_font('celtic_gaelige.ttf', 14)
        }

    def _load_images(self):
        logging.info('Loading images')

        self.images = {
            'buttons': {
                'yes': Helper.load_image('buttons/yes.png'),
                'refresh': Helper.load_image('buttons/refresh.png'),
                'exit': Helper.load_image('buttons/exit.png'),
            }
        }

    def _load_spritesheets(self):
        logging.info('Loading Spritesheets')

        self.spritesheets = {
            'sealsprites': Helper.spritesheet('seal2.png'),
            'sealsprites2': Helper.spritesheet('seal.png'),
            'bearsprites': Helper.spritesheet('bear.png')
        }

    def play(self, MODE):
        if MODE == "STARTSCREEN":
            if self.Charakter.get_Name() is None:
                NewStartingScreen = Start_Screen.clsStartScreen(
                    self.window, MODE, False)
            else:
                NewStartingScreen = Start_Screen.clsStartScreen(
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
                pickle.dump([self.Charakter, World_Map.inventory, self.NewTilemap, self.player_Icon_Position],
                            f, protocol=2)
            logging.info('Game saved')
            MODE = "GAME"
            return MODE

        elif MODE == "LOAD":
            with open('savefile.dat', 'rb') as f:
                self.Charakter, World_Map.inventory, self.NewTilemap, self.player_Icon_Position = pickle.load(f)
            logging.info('Game loaded')
            MODE = "GAME"
            return MODE

        elif MODE == "NEWGAME":
            logging.info('Initializing new game')
            self.window.fill(Farben.clsFarben.BLACK)
            self.Charakter = Character_Builder.run_Character_Builder()
            pygame.display.update()
            MODE = "GAME"
            return MODE

        elif MODE == "GAMEOVER":
            self.window.fill(Farben.clsFarben.BLACK)
            GameOverAnim = pyganim.PygAnimation('./resources/gameover.gif')
            GameOverAnim.scale((600,450))
            GameOverAnim.play()
            mainClock = pygame.time.Clock()

            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                GameOverAnim.blit(self.window, (10, 10))
                mainClock.tick(FPS)
                pygame.display.update()

        elif MODE == "GAME":
            global direction
            blackbar = pygame.Rect(Koordinaten.clsKoordinaten.BLACKBARSTART, Koordinaten.clsKoordinaten.BLACKBAREND,
                                   World_Map.MAPWIDTH * World_Map.TILESIZE,
                                   World_Map.MAPHEIGHT * World_Map.TILESIZE)

            characterButton = gui.PygButton((Koordinaten.clsKoordinaten.BUTTONPOSX,
                                             Koordinaten.clsKoordinaten.BUTTONPOSY,
                                             Koordinaten.clsKoordinaten.BUTTONWIDTH,
                                             Koordinaten.clsKoordinaten.BUTTONHEIGTH),
                                            'Charakter',
                                            bgcolor=Farben.clsFarben.DARKRED, fgcolor=Farben.clsFarben.BRIGHT)
            characterButton.font = self.fonts['small']
            direction = ""
            time_begin = pygame.time.get_ticks()
            milli_seconds_to_pass = 40000

            Charaktermenu = Interact.clsInteract(
                self.window, self.Charakter)

            #for testing purposes
            self.Charakter.set_Skill(character.skills.PlantingCharacterSkill)
            self.Charakter.set_Skill(character.skills.EarthquakeCharacterSkill)
            self.Charakter.set_Skill(character.skills.StealthCharacterSkill)
            self.Charakter.set_Skill(character.skills.SaversCharacterSkill)
            self.Charakter.set_Skill(character.skills.MagicalHealCharacterSkill)

            while True:

                if self.Charakter.get_status_temp('health')<=0:
                    MODE = "GAMEOVER"
                    return MODE
                pygame.display.update()
                for row in range(World_Map.MAPHEIGHT):
                    for column in range(World_Map.MAPWIDTH):
                        self.window.blit(World_Map.textures[self.BackgroundTilemap.getTilemap()[row][column]],
                                         (column * World_Map.TILESIZE, row * World_Map.TILESIZE))
                        self.window.blit(World_Map.textures[self.NewTilemap.getTilemap()[row][column]],
                                         (column * World_Map.TILESIZE, row * World_Map.TILESIZE))
                        self.window.blit(World_Map.environment[self.NewTilemap.getEnvironment()[row][column]],
                                         (column * World_Map.TILESIZE, row * World_Map.TILESIZE))
                pygame.draw.rect(
                    self.window, Farben.clsFarben.BLACK, blackbar)
                characterButton.draw(self.window)

                #icon showing
                Player_Icon=Animations_and_Enemies.clsIconShowing(self.window, self.Charakter)
                Player_Icon.draw(direction, self.player_Icon_Position)
                # For animating magic
                MagicAnimator = Animations_and_Enemies.clsAnimation(self.window, self.player_Icon_Position)

                # Generating and placing enemies
                for enemy in range(0, self.Enemies.get_Enemies_Anzahl()):
                    an_enemy = self.Enemies.get_Enemy(enemy)
                    an_enemy.show_Icon(self.window)

                # Character Stats Showing
                Charaktermenu.stats_showing()

                # Snippets Showing
                World_Map.clsTileMap.drawSnippets(self.window)

                #Time Handling for time-based events
                actual_time = pygame.time.get_ticks()
                if (actual_time - time_begin) > milli_seconds_to_pass:
                    if self.Charakter.get_status_temp('endu')<self.Charakter.get_status_max('endu'):
                        self.Charakter.change_status_temp('endu', '+')
                    time_begin = actual_time

                # Key and Mouse Input Handling
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    #Button: 'Charakter'
                    events = characterButton.handleEvent(event)
                    if 'click' in events:
                        Charaktermenu.draw_MainMenu(self.Charakter)

                    if event.type == KEYDOWN:
                        if (event.key == K_ESCAPE):
                            MODE = "STARTSCREEN"
                            return MODE
                        elif (event.key == K_RIGHT and self.player_Icon_Position[0] < World_Map.MAPWIDTH - 1):
                            cont = True
                            if self.Charakter.get_status_temp('magic') <= 0:
                                if self.Charakter.get_stealth_mode():
                                    self.Charakter.set_stealth_mode(False)
                            if self.Charakter.get_status_temp('endu') <= 0:
                                if self.Charakter.get_savers_mode():
                                    self.Charakter.set_savers_mode(False)

                            nextTile = self.NewTilemap.getTilemap()[self.player_Icon_Position[1]
                                                               ][self.player_Icon_Position[0]+1]
                            nextEnvironment = self.NewTilemap.getEnvironment()[self.player_Icon_Position[1]
                                                                          ][self.player_Icon_Position[0] + 1]
                            nextPosition = [
                                self.player_Icon_Position[0]+1, self.player_Icon_Position[1]]
                            for enemy in range(0, self.Enemies.get_Enemies_Anzahl()):
                                an_enemy = self.Enemies.get_Enemy(enemy)
                                if nextPosition == an_enemy.Position:
                                    cont = False
                            currentEnvironment = self.NewTilemap.getEnvironment()[self.player_Icon_Position[1]
                                                                             ][self.player_Icon_Position[0]]
                            for env in World_Map.enterable:
                                if env == currentEnvironment:
                                    for env2 in World_Map.enterable:
                                        if env2 == nextEnvironment:
                                            cont = True
                                            break
                                        else:
                                            cont = False
                            if nextEnvironment == World_Map.CAVE4:
                                cont = False
                            if cont:
                                for tile in World_Map.waterbehaviour:
                                    if tile == nextTile:
                                        if self.Charakter.has_Skill(character.skills.SwimmingCharacterSkill):
                                            cont = True
                                            break
                                        else:
                                            cont = False
                                if cont:
                                    for env in World_Map.enterable:
                                        if env == currentEnvironment:
                                            for env2 in World_Map.enterable:
                                                if env2 == nextEnvironment:
                                                    cont = True
                                                    break
                                                else:
                                                    cont = False
                                    for env in World_Map.collide:
                                        if env == nextEnvironment:
                                            cont = False
                                            break
                                    if cont:
                                        if self.Charakter.get_status_temp('health')>0:
                                            images = Player_Icon.get_walk_Images('right')
                                            WalkAnim = pyganim.PygAnimation(
                                                [(images[0], 150), (images[1], 150), (images[2], 150)])
                                            WalkAnim.scale((37, 37))
                                            WalkAnim.play()
                                            walk = 0.0
                                            proceed = True
                                            while proceed:
                                                Helper.repaint(self.BackgroundTilemap, self.NewTilemap, self.player_Icon_Position, nextPosition, self.window)
                                                WalkAnim.blit(self.window,
                                                              (self.player_Icon_Position[0] * World_Map.TILESIZE + walk,
                                                               (self.player_Icon_Position[1] * World_Map.TILESIZE)))
                                                pygame.display.update()
                                                walk += 1
                                                fpsClock.tick(FPS)
                                                if self.player_Icon_Position[0]*World_Map.TILESIZE + walk > (self.player_Icon_Position[0] + 1)*World_Map.TILESIZE:
                                                    proceed = False
                                            direction = "right"
                                            self.player_Icon_Position[0] += 1
                                            if self.Charakter.get_stealth_mode():
                                                MagicAnimator.magic_Anim('stealth')
                                                self.Charakter.change_status_temp(
                                                    'magic', '-')
                                            if self.Charakter.get_savers_mode():
                                                MagicAnimator.magic_Anim('savers')
                                                self.Charakter.change_status_temp(
                                                    'endu', '-')
                                            if self.Charakter.has_Skill(character.skills.RunnerCharacterSkill):
                                                rand_int = Percentages.halfhalf()
                                                if rand_int:
                                                    self.Charakter.change_status_temp(
                                                        'endu', '+')
                                            Player_Icon.draw(direction, self.player_Icon_Position)
                                            for enemy in self.Enemies.get_Enemies_Liste():
                                                enemy.Agieren(self.window, self.NewTilemap, direction,
                                                              self.player_Icon_Position, self.Charakter)
                        elif (event.key == K_LEFT and self.player_Icon_Position[0] > 0):
                            cont = True
                            if self.Charakter.get_status_temp('magic') <= 0:
                                if self.Charakter.get_stealth_mode():
                                    self.Charakter.set_stealth_mode(False)
                            if self.Charakter.get_status_temp('endu') <= 0:
                                if self.Charakter.get_savers_mode():
                                    self.Charakter.set_savers_mode(False)

                            nextTile = self.NewTilemap.getTilemap()[self.player_Icon_Position[1]
                                                               ][self.player_Icon_Position[0] - 1]
                            nextEnvironment = self.NewTilemap.getEnvironment()[self.player_Icon_Position[1]
                                                                          ][self.player_Icon_Position[0] - 1]
                            currentEnvironment = self.NewTilemap.getEnvironment()[self.player_Icon_Position[1]
                                                                             ][self.player_Icon_Position[0]]
                            nextPosition = [
                                self.player_Icon_Position[0] - 1, self.player_Icon_Position[1]]
                            for enemy in range(0, self.Enemies.get_Enemies_Anzahl()):
                                an_enemy = self.Enemies.get_Enemy(enemy)
                                if nextPosition == an_enemy.Position:
                                    cont = False
                            if cont:
                                for env in World_Map.enterable:
                                    if env == currentEnvironment:
                                        for env2 in World_Map.enterable:
                                            if env2 == nextEnvironment:
                                                cont = True
                                                break
                                            else:
                                                cont = False
                                if nextEnvironment == World_Map.CAVE3:
                                    cont = False

                                if cont:
                                    for tile in World_Map.waterbehaviour:
                                        if tile == nextTile:
                                            if self.Charakter.has_Skill(character.skills.SwimmingCharacterSkill):
                                                cont = True
                                                break
                                            else:
                                                cont = False
                                    if cont:
                                        for env in World_Map.collide:
                                            if env == nextEnvironment:
                                                cont = False
                                                break
                                        if cont:
                                            if self.Charakter.get_status_temp('health') > 0:
                                                images = Player_Icon.get_walk_Images('left')
                                                WalkAnim = pyganim.PygAnimation(
                                                    [(images[0], 150), (images[1], 150), (images[2], 150)])
                                                WalkAnim.scale((37, 37))
                                                WalkAnim.play()
                                                walk = 0.0
                                                proceed = True
                                                while proceed:
                                                    Helper.repaint(self.BackgroundTilemap, self.NewTilemap, self.player_Icon_Position,
                                                                   nextPosition, self.window)
                                                    WalkAnim.blit(self.window,
                                                                  (self.player_Icon_Position[0] * World_Map.TILESIZE - walk,
                                                                   (self.player_Icon_Position[1] * World_Map.TILESIZE)))
                                                    pygame.display.update()
                                                    walk += 1
                                                    fpsClock.tick(FPS)
                                                    if self.player_Icon_Position[0] * World_Map.TILESIZE - walk < (
                                                            self.player_Icon_Position[0] - 1) * World_Map.TILESIZE:
                                                        proceed = False
                                                direction = "left"
                                                self.player_Icon_Position[0] -= 1
                                                if self.Charakter.get_stealth_mode():
                                                    MagicAnimator.magic_Anim('stealth')
                                                    self.Charakter.change_status_temp(
                                                        'magic', '-')
                                                if self.Charakter.get_savers_mode():
                                                    MagicAnimator.magic_Anim('savers')
                                                    self.Charakter.change_status_temp(
                                                        'endu', '-')
                                                if self.Charakter.has_Skill(character.skills.RunnerCharacterSkill):
                                                    rand_int = Percentages.halfhalf()
                                                    if rand_int:
                                                        self.Charakter.change_status_temp(
                                                            'endu', '+')
                                                Player_Icon.draw(direction, self.player_Icon_Position)
                                                for enemy in self.Enemies.get_Enemies_Liste():
                                                    enemy.Agieren(self.window, self.NewTilemap, direction,
                                                                  self.player_Icon_Position, self.Charakter)

                        elif (event.key == K_DOWN and self.player_Icon_Position[1] < World_Map.MAPHEIGHT - 1):
                            cont = True
                            if self.Charakter.get_status_temp('magic') <= 0:
                                if self.Charakter.get_stealth_mode():
                                    self.Charakter.set_stealth_mode(False)
                            if self.Charakter.get_status_temp('endu') <= 0:
                                if self.Charakter.get_savers_mode():
                                    self.Charakter.set_savers_mode(False)

                            nextTile = self.NewTilemap.getTilemap()[self.player_Icon_Position[1]+1
                                                               ][self.player_Icon_Position[0]]
                            nextEnvironment = self.NewTilemap.getEnvironment()[self.player_Icon_Position[1] + 1
                                                                          ][self.player_Icon_Position[0]]
                            nextPosition = [
                                self.player_Icon_Position[0], self.player_Icon_Position[1]+1]
                            for enemy in range(0, self.Enemies.get_Enemies_Anzahl()):
                                an_enemy = self.Enemies.get_Enemy(enemy)
                                if nextPosition == an_enemy.Position:
                                    cont = False
                            for tile in World_Map.waterbehaviour:
                                if tile == nextTile:
                                    if self.Charakter.has_Skill(character.skills.SwimmingCharacterSkill):
                                        cont = True
                                        break
                                    else:
                                        cont = False
                            for env in World_Map.collide:
                                if env == nextEnvironment:
                                    cont = False
                                    break
                            if cont:
                                if self.Charakter.get_status_temp('health') > 0:
                                    images = Player_Icon.get_walk_Images('down')
                                    WalkAnim = pyganim.PygAnimation(
                                        [(images[0], 150), (images[1], 150), (images[2], 150)])
                                    WalkAnim.scale((37, 37))
                                    WalkAnim.play()
                                    walk = 0.0
                                    proceed = True
                                    while proceed:
                                        Helper.repaint(self.BackgroundTilemap, self.NewTilemap, self.player_Icon_Position,
                                                       nextPosition, self.window)
                                        WalkAnim.blit(self.window,
                                                      (self.player_Icon_Position[0] * World_Map.TILESIZE,
                                                       (self.player_Icon_Position[1] * World_Map.TILESIZE) + walk))
                                        pygame.display.update()
                                        walk += 1
                                        fpsClock.tick(FPS)
                                        if self.player_Icon_Position[1] * World_Map.TILESIZE + walk > (
                                                self.player_Icon_Position[1] + 1) * World_Map.TILESIZE:
                                            proceed = False
                                    direction = "down"
                                    self.player_Icon_Position[1] += 1
                                    if self.Charakter.get_stealth_mode():
                                        MagicAnimator.magic_Anim('stealth')
                                        self.Charakter.change_status_temp(
                                            'magic', '-')
                                    if self.Charakter.get_savers_mode():
                                        MagicAnimator.magic_Anim('savers')
                                        self.Charakter.change_status_temp(
                                            'endu', '-')
                                    if self.Charakter.has_Skill(character.skills.RunnerCharacterSkill):
                                        rand_int = Percentages.halfhalf()
                                        if rand_int:
                                            self.Charakter.change_status_temp(
                                                'endu', '+')
                                    Player_Icon.draw(direction, self.player_Icon_Position)
                                    for enemy in self.Enemies.get_Enemies_Liste():
                                        enemy.Agieren(self.window, self.NewTilemap, direction,
                                                      self.player_Icon_Position, self.Charakter)
                        elif (event.key == K_UP and self.player_Icon_Position[1] > 0):
                            cont = True
                            if self.Charakter.get_status_temp('magic') <= 0:
                                if self.Charakter.get_stealth_mode():
                                    self.Charakter.set_stealth_mode(False)
                            if self.Charakter.get_status_temp('endu') <= 0:
                                if self.Charakter.get_savers_mode():
                                    self.Charakter.set_savers_mode(False)

                            nextTile = self.NewTilemap.getTilemap()[self.player_Icon_Position[1]-1
                                                               ][self.player_Icon_Position[0]]
                            currentEnvironment = self.NewTilemap.getEnvironment()[self.player_Icon_Position[1]
                                                                             ][self.player_Icon_Position[0]]
                            nextEnvironment = self.NewTilemap.getEnvironment()[self.player_Icon_Position[1]-1
                                                                          ][self.player_Icon_Position[0]]
                            nextPosition = [
                                self.player_Icon_Position[0], self.player_Icon_Position[1]-1]
                            for enemy in range(0, self.Enemies.get_Enemies_Anzahl()):
                                an_enemy = self.Enemies.get_Enemy(enemy)
                                if nextPosition == an_enemy.Position:
                                    cont = False
                            for env in World_Map.enterable:
                                if env == currentEnvironment:
                                    cont = False
                            if cont:
                                if nextEnvironment == World_Map.STONEHOLE:
                                    if self.Charakter.has_Skill(character.skills.SwimmingCharacterSkill):
                                        cont = True
                                        break
                                    else:
                                        cont = False
                                for env in World_Map.collide:
                                    if env == nextEnvironment:
                                        cont = False
                                        break
                                for tile in World_Map.waterbehaviour:
                                    if tile == nextTile:
                                        if self.Charakter.has_Skill(character.skills.SwimmingCharacterSkill):
                                            cont = True
                                            break
                                        else:
                                            cont = False
                                if cont:
                                    if self.Charakter.get_status_temp('health') > 0:
                                        images = Player_Icon.get_walk_Images('up')
                                        WalkAnim = pyganim.PygAnimation(
                                            [(images[0], 150), (images[1], 150), (images[2], 150)])
                                        WalkAnim.scale((37, 37))
                                        WalkAnim.play()
                                        walk = 0.0
                                        proceed = True
                                        while proceed:
                                            Helper.repaint(self.BackgroundTilemap, self.NewTilemap, self.player_Icon_Position,
                                                           nextPosition, self.window)
                                            WalkAnim.blit(self.window,
                                                          (self.player_Icon_Position[0] * World_Map.TILESIZE,
                                                           (self.player_Icon_Position[1] * World_Map.TILESIZE) + walk))
                                            pygame.display.update()
                                            walk -= 1
                                            fpsClock.tick(FPS)
                                            if self.player_Icon_Position[1] * World_Map.TILESIZE + walk < (
                                                    self.player_Icon_Position[1] - 1) * World_Map.TILESIZE:
                                                proceed = False
                                        direction = "up"
                                        self.player_Icon_Position[1] -= 1
                                        if self.Charakter.get_stealth_mode() == True:
                                            MagicAnimator.magic_Anim('stealth')
                                            self.Charakter.change_status_temp(
                                                'magic', '-')
                                        if self.Charakter.get_savers_mode():
                                            MagicAnimator.magic_Anim('savers')
                                            self.Charakter.change_status_temp(
                                                'endu', '-')
                                        if self.Charakter.has_Skill(character.skills.RunnerCharacterSkill):
                                            rand_int = Percentages.halfhalf()
                                            if rand_int:
                                                self.Charakter.change_status_temp(
                                                    'endu', '+')
                                        Player_Icon.draw(direction, self.player_Icon_Position)
                                        for enemy in self.Enemies.get_Enemies_Liste():
                                            enemy.Agieren(self.window, self.NewTilemap, direction,
                                                          self.player_Icon_Position, self.Charakter)
                        elif (event.key == K_SPACE):
                            currentTile = self.NewTilemap.getTilemap()[self.player_Icon_Position[1]
                                                                  ][self.player_Icon_Position[0]]
                            currentEnvironment = self.NewTilemap.getEnvironment()[self.player_Icon_Position[1]
                                                                    ][self.player_Icon_Position[0]]

                            #hasenv: True bei Gras, False wenn kein Gras
                            hasenv = False
                            for grass in World_Map.grasses:
                                if grass == currentEnvironment:
                                    hasenv = True
                            if (currentTile == World_Map.DIRT and self.Charakter.has_Skill(character.skills.PlantingCharacterSkill) and self.Charakter.get_status_temp('magic')>0):
                                # DIRT mit irgendeiner Grassorte [nur möglich nach Planting Skill..]
                                if currentTile == World_Map.DIRT and hasenv == True:
                                    World_Map.inventory[currentEnvironment] += 1
                                    self.NewTilemap.getEnvironment()[self.player_Icon_Position[1]
                                    ][self.player_Icon_Position[0]] = World_Map.DEADGRASS
                                    for enemy in self.Enemies.get_Enemies_Liste():
                                        enemy.Agieren(self.window, self.NewTilemap, direction, self.player_Icon_Position,
                                                      self.Charakter)
                                # DIRT ohne Gras, ohne totes Gras: wird wieder Grassland
                                if currentEnvironment != World_Map.DEADGRASS and hasenv == False:
                                    self.NewTilemap.getTilemap()[self.player_Icon_Position[1]
                                    ][self.player_Icon_Position[0]] = World_Map.GRASSLAND
                                    self.Charakter.change_status_temp(
                                        'magic', '-')
                                # DIRT mit totem Gras: totes Gras wird niedriges Gras
                                elif currentEnvironment == World_Map.DEADGRASS:
                                    self.NewTilemap.getEnvironment()[self.player_Icon_Position[1]
                                    ][self.player_Icon_Position[0]] = World_Map.LOWGRASS
                                    self.Charakter.change_status_temp(
                                        'magic', '-')
                                    for enemy in self.Enemies.get_Enemies_Liste():
                                        enemy.Agieren(self.window, self.NewTilemap, direction, self.player_Icon_Position,
                                                      self.Charakter)
                                if self.Charakter.get_stealth_mode():
                                    MagicAnimator.magic_Anim('stealth')
                                    self.Charakter.change_status_temp(
                                        'magic', '-')
                                if self.Charakter.get_savers_mode():
                                    MagicAnimator.magic_Anim('savers')
                                    self.Charakter.change_status_temp(
                                        'endu', '-')
                                MagicAnimator.magic_Anim('plant', self.NewTilemap)
                                Charaktermenu.stats_showing()
                                for enemy in self.Enemies.get_Enemies_Liste():
                                    enemy.Agieren(self.window, self.NewTilemap, direction, self.player_Icon_Position,
                                                  self.Charakter)
                                break
                            elif currentTile == World_Map.GRASSLAND:
                                if hasenv:
                                    # Fähigkeit Grasschlitzer: Chance auf doppelte Ressourcen
                                    if self.Charakter.has_Skill(character.skills.GrasMovementCharacterSkill):
                                        rand_int = Percentages.halfhalf()
                                        if rand_int:
                                            World_Map.inventory[currentEnvironment] += 1
                                    # Sammeln
                                    World_Map.inventory[currentEnvironment]+=1
                                    self.NewTilemap.getEnvironment()[self.player_Icon_Position[1]
                                    ][self.player_Icon_Position[0]] = World_Map.DEADGRASS
                                #kein Gras drauf, wird Dirt:
                                else:
                                    if self.Charakter.has_Skill(character.skills.GrasMovementCharacterSkill):
                                        rand_int = Percentages.halfhalf()
                                        if rand_int:
                                            World_Map.inventory[currentTile] += 1
                                    World_Map.inventory[currentTile] += 1
                                    self.NewTilemap.getTilemap()[self.player_Icon_Position[1]
                                                            ][self.player_Icon_Position[0]] = World_Map.DIRT
                                if self.Charakter.get_stealth_mode():
                                    MagicAnimator.magic_Anim('stealth')
                                    self.Charakter.change_status_temp(
                                        'magic', '-')
                                if self.Charakter.get_savers_mode():
                                    MagicAnimator.magic_Anim('savers')
                                    self.Charakter.change_status_temp(
                                        'endu', '-')
                                self.Charakter.change_status_temp('endu', '-')
                                Player_Icon.draw(direction, self.player_Icon_Position)
                                Charaktermenu.stats_showing()
                                for enemy in self.Enemies.get_Enemies_Liste():
                                    enemy.Agieren(self.window, self.NewTilemap, direction, self.player_Icon_Position,
                                                  self.Charakter)
                        elif (event.key == K_m):
                            Skills = []
                            # non-fighting skills
                            stealthSkill = False
                            healSkill = False
                            plantingSkill = False
                            saverSkill = False
                            if (self.Charakter.has_Skill(character.skills.StealthCharacterSkill)):
                                stealthSkill = True
                                Skills.append('stealth')
                            if (self.Charakter.has_Skill(character.skills.MagicalHealCharacterSkill)):
                                healSkill = True
                                Skills.append('magical_heal')
                            if (self.Charakter.has_Skill(character.skills.PlantingCharacterSkill)):
                                plantingSkill = True
                                Skills.append('plant')
                            if (self.Charakter.has_Skill(character.skills.SaversCharacterSkill)):
                                saverSkill = True
                                Skills.append('robe')

                            if stealthSkill or healSkill or plantingSkill or saverSkill:
                                wait_for_click = True
                            else:
                                wait_for_click = False
                            clicked = False
                            # if character has one of the passive skills:
                            while wait_for_click:
                                pygame.display.update()
                                for event in pygame.event.get():
                                    if event.type == QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == MOUSEBUTTONDOWN:
                                        if not enough_temp_value:
                                            break
                                        elif enough_temp_value:
                                            mousepos = event.pos
                                            if stealthSkill:
                                                if stealthbubble.collidepoint(mousepos):
                                                    if not self.Charakter.get_stealth_mode():
                                                        self.Charakter.change_status_temp(
                                                            'magic', '-')
                                                        self.Charakter.set_stealth_mode(True)
                                                        MagicAnimator.magic_Anim('stealth')
                                                        clicked = True
                                                    else:
                                                        self.Charakter.set_stealth_mode(False)
                                            if healSkill:
                                                if healbubble.collidepoint(mousepos):
                                                    MagicAnimator.magic_Anim('heal')
                                                    self.Charakter.change_status_temp(
                                                        'magic', '-')
                                                    self.Charakter.change_status_temp(
                                                        'endurance', '+')
                                                    self.Charakter.change_status_temp(
                                                        'health', '+')
                                                    clicked = True
                                            if plantingSkill:
                                                if plantbubble.collidepoint(mousepos):
                                                    currentTile = self.NewTilemap.getTilemap()[self.player_Icon_Position[1]
                                                                                          ][self.player_Icon_Position[0]]
                                                    currentEnvironment = self.NewTilemap.getEnvironment()[self.player_Icon_Position[1]
                                                    ][self.player_Icon_Position[0]]

                                                    if currentTile == World_Map.DIRT:
                                                        if currentEnvironment != World_Map.DEADGRASS:
                                                            self.NewTilemap.getTilemap()[self.player_Icon_Position[1]
                                                            ][self.player_Icon_Position[0]] = World_Map.GRASSLAND
                                                            self.Charakter.change_status_temp(
                                                                'magic', '-')
                                                        elif currentEnvironment == World_Map.DEADGRASS:
                                                            self.NewTilemap.getEnvironment()[self.player_Icon_Position[1]
                                                                                        ][self.player_Icon_Position[0]] = World_Map.LOWGRASS
                                                            self.Charakter.change_status_temp(
                                                                'magic', '-')
                                                        clicked = True

                                                    elif currentTile == World_Map.GRASSLAND:
                                                        if currentEnvironment == World_Map.LOWGRASS:
                                                            self.NewTilemap.getEnvironment()[self.player_Icon_Position[1]
                                                                                    ][self.player_Icon_Position[0]] = World_Map.MOREGRASS
                                                            self.Charakter.change_status_temp(
                                                                'magic', '-')
                                                        # auf dem Grassland ist entweder nichts oder ein Dekoitem
                                                        else:
                                                            self.NewTilemap.getEnvironment()[self.player_Icon_Position[1]
                                                            ][self.player_Icon_Position[0]] = World_Map.LOWGRASS
                                                            self.Charakter.change_status_temp(
                                                                'magic', '-')
                                                    MagicAnimator.magic_Anim('plant', self.NewTilemap)
                                                    clicked = True

                                            if saverSkill:
                                                if saverbubble.collidepoint(mousepos):
                                                    if not self.Charakter.get_savers_mode():
                                                        MagicAnimator.magic_Anim('savers')
                                                        self.Charakter.change_status_temp(
                                                            'endu', '-')
                                                        self.Charakter.set_savers_mode(True)
                                                        clicked = True
                                                    else:
                                                        self.Charakter.set_savers_mode(False)
                                            if clicked:
                                                for enemy in self.Enemies.get_Enemies_Liste():
                                                    enemy.Agieren(self.window, self.NewTilemap, direction,
                                                                  self.player_Icon_Position, self.Charakter)
                                                Player_Icon.draw(direction, self.player_Icon_Position)
                                                Charaktermenu.stats_showing()
                                                pygame.display.update()
                                                fpsClock.tick(FPS)
                                                clicked = False
                                    elif event.type == KEYDOWN:
                                        if event.key == K_m:
                                            wait_for_click = False

                                    if stealthSkill:
                                        enough_temp_value = False
                                        if self.Charakter.get_status_temp('magic') >= 1:
                                            enough_temp_value = True
                                        for i in [i for i, x in enumerate(Skills) if x == 'stealth']:
                                            bubble = Interact.Bubble(self.window, 'stealth', i, enough_temp_value)
                                        stealthbubble = bubble.draw_bubble()
                                    if healSkill:
                                        enough_temp_value = False
                                        if self.Charakter.get_status_temp('magic') >= 1:
                                            enough_temp_value = True
                                        for i in [i for i, x in enumerate(Skills) if x == 'magical_heal']:
                                            bubble = Interact.Bubble(self.window, 'magical_heal', i, enough_temp_value)
                                        healbubble = bubble.draw_bubble()
                                    if plantingSkill:
                                        enough_temp_value = False
                                        if self.Charakter.get_status_temp('magic') >= 1:
                                            currentTile = self.NewTilemap.getTilemap()[self.player_Icon_Position[1]
                                            ][self.player_Icon_Position[0]]
                                            currentEnvironment = self.NewTilemap.getEnvironment()[self.player_Icon_Position[1]
                                            ][self.player_Icon_Position[0]]
                                            hasenv = False
                                            for grass in World_Map.grasses:
                                                if grass == currentEnvironment:
                                                    hasenv = True
                                            # Skill möglich, wenn Dirt ohne Gras vorhanden ist
                                            if currentTile == World_Map.DIRT and hasenv == False:
                                                enough_temp_value = True
                                            # Skill möglich, wenn Grassland vorhanden ist, auf dem kein hohes Gras wächst
                                            elif currentTile == World_Map.GRASSLAND and currentEnvironment != World_Map.MOREGRASS:
                                                if currentEnvironment == World_Map.LOWGRASS or currentEnvironment == World_Map.DEADGRASS \
                                                        or currentEnvironment == World_Map.GRASSDECO:
                                                    enough_temp_value = True
                                        for i in [i for i, x in enumerate(Skills) if x == 'plant']:
                                            bubble = Interact.Bubble(self.window, 'plant', i, enough_temp_value)
                                        plantbubble = bubble.draw_bubble()
                                    if saverSkill:
                                        enough_temp_value = False
                                        if self.Charakter.get_status_temp('endu') >= 1:
                                            enough_temp_value = True
                                        for i in [i for i, x in enumerate(Skills) if x == 'robe']:
                                            bubble = Interact.Bubble(self.window, 'robe', i, enough_temp_value)
                                        saverbubble = bubble.draw_bubble()

                        elif(event.key == K_f):
                            # fighting skills
                            Skills=[]

                            Surrounding_Tiles = []
                            Enemies_in_range = []
                            for tile_x in range(self.player_Icon_Position[0]-1, self.player_Icon_Position[0]+2):
                                for tile_y in range(self.player_Icon_Position[1] - 1, self.player_Icon_Position[1] + 2):
                                    to_append = [tile_x, tile_y]
                                    Surrounding_Tiles.append(to_append)
                            for element in Surrounding_Tiles:
                                for enemy in range(0, self.Enemies.get_Enemies_Anzahl()):
                                    an_enemy = self.Enemies.get_Enemy(enemy)
                                    if element == an_enemy.Position:
                                        Enemies_in_range.append(an_enemy)

                            standardSkill = True
                            if self.Charakter.get_status_temp('endu')>=1 and Enemies_in_range:
                                standard_attack_active = True
                            else:
                                standard_attack_active = False
                            Skills.append('standard')

                            if (self.Charakter.has_Skill(character.skills.BiteCharacterSkill)):
                                biteSkill = True
                                if self.Charakter.get_status_temp('magic')>=1 and Enemies_in_range:
                                    bite_attack_active = True
                                else:
                                    bite_attack_active = False
                                Skills.append('bite')
                            else:
                                biteSkill = False
                            if (self.Charakter.has_Skill(character.skills.TailCharacterSkill)):
                                tailSkill = True
                                if self.Charakter.get_status_temp('endu')>=1 and Enemies_in_range:
                                    tail_attack_active = True
                                else:
                                    tail_attack_active = False
                                Skills.append('tail')
                            else:
                                tailSkill = False
                            if (self.Charakter.has_Skill(character.skills.EarthquakeCharacterSkill)):
                                earthSkill = True
                                if self.Charakter.get_status_temp('endu')>=1 and Enemies_in_range:
                                    earth_attack_active = True
                                else:
                                    earth_attack_active = False
                                Skills.append('earthquake')
                            else:
                                earthSkill = False

                            wait_for_click = True
                            clicked = False
                            while wait_for_click:
                                pygame.display.update()
                                for event in pygame.event.get():
                                    if event.type == QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == MOUSEBUTTONDOWN:
                                        mousepos = event.pos
                                        if standard_attack_active:
                                            if standardbubble.collidepoint(mousepos):
                                                for enemy in Enemies_in_range:
                                                    enemy_tile = self.NewTilemap.getTilemap()[enemy.Position[1]
                                                                                         ][enemy.Position[0]]
                                                    enemy_environment = self.NewTilemap.getEnvironment()[enemy.Position[1]
                                                    ][enemy.Position[0]]
                                                    mod=int(self.Charakter.get_str())
                                                    if mod>0:
                                                        attackmodifier=Percentages.dice(mod)
                                                    else:
                                                        attackmodifier=0
                                                    enemy.lower_Health(1 + attackmodifier)
                                                    self.Charakter.change_status_temp('endu', '-')
                                                    clicked = True
                                        if biteSkill:
                                            if bite_attack_active:
                                                if bitebubble.collidepoint(mousepos):
                                                    for enemy in Enemies_in_range:
                                                        enemy_tile = self.NewTilemap.getTilemap()[enemy.Position[1]
                                                                                             ][enemy.Position[0]]
                                                        enemy_environment = self.NewTilemap.getEnvironment()[enemy.Position[1]
                                                        ][enemy.Position[0]]
                                                        mod = int(self.Charakter.get_str())
                                                        if mod > 0:
                                                            attackmodifier = Percentages.dice(mod)
                                                        else:
                                                            attackmodifier = 0
                                                        enemy.lower_Health(
                                                            2+attackmodifier)
                                                        self.Charakter.change_status_temp('magic', '-')
                                                        clicked = True
                                        if tailSkill:
                                            if tail_attack_active:
                                                if tailbubble.collidepoint(mousepos):
                                                    for enemy in Enemies_in_range:
                                                        enemy_tile = self.NewTilemap.getTilemap()[enemy.Position[1]
                                                                                             ][enemy.Position[0]]
                                                        enemy_environment = self.NewTilemap.getEnvironment()[enemy.Position[1]
                                                        ][enemy.Position[0]]
                                                        mod = int(self.Charakter.get_str())
                                                        if mod > 0:
                                                            attackmodifier = Percentages.dice(mod)
                                                        else:
                                                            attackmodifier = 0
                                                        enemy.lower_Health(
                                                            2+attackmodifier)
                                                        self.Charakter.change_status_temp('endu', '-')
                                                        clicked = True
                                        if earthSkill:
                                            if earth_attack_active:
                                                if earthbubble.collidepoint(mousepos):
                                                    #needed for blitting late
                                                    tiles_Sprite = Helper.spritesheet('tileset_32_32.png')
                                                    dirt_tile = tiles_Sprite.image_at((15, 2545, 64, 64),
                                                                                      colorkey=(0, 0, 0))
                                                    dirt_tile = pygame.transform.scale(dirt_tile, (40, 40))

                                                    #stores just Gras tiles around character
                                                    Surrounding = []
                                                    for tile in Surrounding_Tiles:
                                                        if tile[0] >= 0 and tile[1] >= 0:
                                                            tile_art= self.NewTilemap.getTilemap()[tile[1]][tile[0]]
                                                            if tile_art == World_Map.GRASSLAND or tile_art == World_Map.DIRT:
                                                                Surrounding.append(tile)

                                                    for tile in Surrounding:
                                                        #GRAS to DIRT
                                                        self.NewTilemap.getTilemap()[tile[1]][tile[0]] = World_Map.DIRT
                                                        environment = self.NewTilemap.getEnvironment()[tile[1]][tile[0]]
                                                        collide=False
                                                        for env in World_Map.collide:
                                                            if environment == env:
                                                                collide=True
                                                        for env in World_Map.enterable:
                                                            if environment == env:
                                                                collide=True
                                                        if collide==False:
                                                            #all non-collideables to NOTHING
                                                            self.NewTilemap.getEnvironment()[tile[1]][tile[0]] = World_Map.NOTHING

                                                        self.window.blit(dirt_tile,
                                                                         (tile[0] * World_Map.TILESIZE,
                                                                          tile[1] * World_Map.TILESIZE))

                                                        if collide:
                                                            self.window.blit(World_Map.environment[environment],
                                                                             (tile[0] * World_Map.TILESIZE, tile[1] * World_Map.TILESIZE))
                                                        Player_Icon.draw(direction, self.player_Icon_Position)
                                                        #redraw all enemies on map:
                                                        for enemy in range(0, self.Enemies.get_Enemies_Anzahl()):
                                                            an_enemy = self.Enemies.get_Enemy(enemy)
                                                            an_enemy.show_Icon(self.window)
                                                        pygame.display.update()
                                                        fpsClock.tick(FPS)

                                                    for enemy in Enemies_in_range:
                                                        enemy_tile = self.NewTilemap.getTilemap()[enemy.Position[1]
                                                                                             ][enemy.Position[0]]
                                                        enemy_environment = self.NewTilemap.getEnvironment()[enemy.Position[1]
                                                        ][enemy.Position[0]]

                                                        if enemy.Position in Surrounding:
                                                            mod = int(self.Charakter.get_str())
                                                            if mod > 0:
                                                                attackmodifier = Percentages.dice(mod)
                                                            else:
                                                                attackmodifier = 0
                                                            enemy.lower_Health(
                                                                Percentages.dice(5 + attackmodifier))
                                                            self.Charakter.change_status_temp(
                                                                'endu', '-')
                                                            self.Charakter.change_status_temp(
                                                                'health', '-')
                                                            clicked = True

                                        if clicked:
                                            enemy.damage_and_death_anim(
                                                self.window, "damage", enemy_tile, enemy_environment)
                                            if not "hostile" in enemy.Behaviour:
                                                enemy.add_Behaviour("hostile")
                                            if enemy.Health <= 0:
                                                enemy.damage_and_death_anim(
                                                    self.window, "death", enemy_tile, enemy_environment)
                                                self.Enemies.delete_from_list(
                                                    enemy)
                                                Enemies_in_range.remove(
                                                    enemy)
                                                enemy.__del__
                                                if not Enemies_in_range:
                                                    active = False
                                            clicked = False

                                        for enemy in self.Enemies.get_Enemies_Liste():
                                            enemy.Agieren(self.window, self.NewTilemap, direction,
                                                          self.player_Icon_Position, self.Charakter)
                                            Charaktermenu.stats_showing()
                                    elif event.type == KEYDOWN:
                                        if event.key == K_f:
                                            wait_for_click = False

                                    #Drawing the Skills
                                    bubble = Interact.Bubble(self.window, 'standard', 0, standard_attack_active)
                                    standardbubble = bubble.draw_bubble()
                                    if biteSkill:
                                        for i in [i for i, x in enumerate(Skills) if x == 'bite']:
                                            bubble = Interact.Bubble(self.window, 'bite', i, bite_attack_active)
                                        bitebubble = bubble.draw_bubble()
                                    if tailSkill:
                                        for i in [i for i, x in enumerate(Skills) if x == 'tail']:
                                            bubble = Interact.Bubble(self.window, 'tail', i, tail_attack_active)
                                        tailbubble = bubble.draw_bubble()
                                    if earthSkill:
                                        for i in [i for i, x in enumerate(Skills) if x == 'earthquake']:
                                            bubble = Interact.Bubble(self.window, 'earthquake', i, earth_attack_active)
                                        earthbubble = bubble.draw_bubble()

                        elif (event.key == K_e):
                            #collect fruits and vegetables
                            currentEnvironment = self.NewTilemap.getEnvironment()[self.player_Icon_Position[1]
                            ][self.player_Icon_Position[0]]
                            if currentEnvironment==World_Map.FRUIT1 or currentEnvironment==World_Map.FRUIT2:
                                self.NewTilemap.getEnvironment()[self.player_Icon_Position[1]
                                ][self.player_Icon_Position[0]]=World_Map.NOTHING
                                for i in range (10):
                                    self.Charakter.change_status_temp('magic', '+')
                                    self.Charakter.change_status_temp('health', '+')
                                Charaktermenu.stats_showing()


NewGame = Spiel(MODE, Charakter)
while True:
    MODE = NewGame.play(MODE)
