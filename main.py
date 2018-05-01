# Robbie likes: https://medium.com/@yvanscher/making-a-game-ai-with-deep-learning-963bb549b3d5
# Very nice: http://game-icons.net/

import pygame, sys, os
import logging
from pygame.locals import *
import pickle
import inspect
import StartingScreen
import Weltkarte
import Interaktion
#import LevelupForm
from resources import Farben, Koordinaten
import charaktereditor
import CharakterAussehen
import run
import character
import Helfer


if 'SDL_VIDEO_WINDOW_POS' not in os.environ:
    os.environ['SDL_VIDEO_CENTERED'] = '1'  # This makes the window centered on the screen

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

Charakter=character.Character()
MODE = "UNKNOWN"
player_Icon_Position = [0,0]

class Spiel(object):

    def __init__(self, MODE, Charakter):
        self.MODE=MODE
        self.Charakter=Charakter

        self.window = pygame.display.set_mode(
            (Weltkarte.MAPWIDTH * Weltkarte.TILESIZE, Weltkarte.MAPHEIGHT * Weltkarte.TILESIZE + 50))
        self.fonts = {
            'normal': Helfer.load_font('celtic_gaelige.ttf', 19)
        }

    def spielen(self, MODE):
        if MODE=="STARTSCREEN":
            if self.Charakter.get_Name()==None:
                NewStartingScreen = StartingScreen.clsStartScreen(self.window, MODE, False)
            else:
                NewStartingScreen = StartingScreen.clsStartScreen(self.window, MODE, True)
            NewStartingScreen.draw(self.window)
            pygame.display.update()
            MODE = NewStartingScreen.whichMode()
            return MODE

        elif MODE=="UNKNOWN":
            logging.info('Game is in unknown mode: ' + MODE)
            MODE="STARTSCREEN"
            return MODE

        elif MODE=="SAVE":
            with open('savefile.dat', 'wb') as f:
                pickle.dump([self.Charakter, Weltkarte.inventory], f, protocol=2)
            logging.info('Game saved')
            MODE="GAME"
            return MODE

        elif MODE=="LOAD":
            with open('savefile.dat', 'rb') as f:
                self.Charakter, Weltkarte.inventory = pickle.load(f)
            logging.info('Game loaded')
            MODE="GAME"
            return MODE

        elif MODE=="NEWGAME":
            logging.info('Initializing new game')
            self.window.fill(Farben.clsFarben.BLACK)
            self.Charakter=run.run()
            pygame.display.update()
            MODE="GAME"
            return MODE

        elif MODE=="GAME":
            blackbar = pygame.Rect(Koordinaten.clsKoordinaten.BLACKBARSTART, Koordinaten.clsKoordinaten.BLACKBAREND,
                                   Weltkarte.MAPWIDTH * Weltkarte.TILESIZE,
                                   Weltkarte.MAPHEIGHT * Weltkarte.TILESIZE)
            while True:
                pygame.display.update()

                for row in range(Weltkarte.MAPHEIGHT):
                    for column in range(Weltkarte.MAPWIDTH):
                        self.window.blit(Weltkarte.textures[Weltkarte.tilemap[row][column]],
                                     (column * Weltkarte.TILESIZE, row * Weltkarte.TILESIZE))
                        pygame.draw.rect(self.window, Farben.clsFarben.BLACK, blackbar)

                player_Icon = Helfer.load_image('unknown.png')
                player_Icon = pygame.transform.scale(player_Icon, (Weltkarte.TILESIZE, Weltkarte.TILESIZE))

                #if (isinstance(self.Charakter.get_type(), character.animaltypes.clsBaer)): #doesnt work :(
                if(str(self.Charakter.get_type())==str(character.animaltypes.clsBaer)):
                    player_Icon = Helfer.load_image('bearicon.png')
                    player_Icon = pygame.transform.scale(player_Icon, (Weltkarte.TILESIZE, Weltkarte.TILESIZE))

                elif (str(self.Charakter.get_type()) == str(character.animaltypes.clsRobbe)):
                    player_Icon = Helfer.load_image('sealicon.png')
                    player_Icon = pygame.transform.scale(player_Icon, (Weltkarte.TILESIZE, Weltkarte.TILESIZE))

                self.window.blit(
                    player_Icon, (
                    player_Icon_Position[0]*Weltkarte.TILESIZE,player_Icon_Position[1]*Weltkarte.TILESIZE))

                placePosition = 50
                for item in Weltkarte.collectableres:
                    self.window.blit(Weltkarte.snippets[item], (placePosition, Weltkarte.MAPHEIGHT * Weltkarte.TILESIZE + 20))
                    placePosition += 30
                    textObjekt = self.fonts['normal'].render(str(Weltkarte.inventory[item]), True, Farben.clsFarben.WHITE,Farben.clsFarben.BLACK)
                    self.window.blit(textObjekt, (placePosition, Weltkarte.MAPHEIGHT * Weltkarte.TILESIZE + 20))
                    placePosition += 50

                interagierenbutton = pygame.Rect(Koordinaten.clsKoordinaten.BUTTONPOSX,
                                                 Koordinaten.clsKoordinaten.BUTTONPOSY,
                                                 Koordinaten.clsKoordinaten.BUTTONWIDTH,
                                                 Koordinaten.clsKoordinaten.BUTTONHEIGTH)

                pygame.draw.rect(self.window, Farben.clsFarben.DARKRED, interagierenbutton)
                label = self.fonts['normal'].render("Charakter", 1, Farben.clsFarben.WHITE)
                self.window.blit(label, (Koordinaten.clsKoordinaten.CHARSHEETPOSX, Koordinaten.clsKoordinaten.CHARSHEETPOSY))

                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == MOUSEBUTTONDOWN:
                        mousepos = event.pos
                        if interagierenbutton.collidepoint(mousepos):
                            Charaktermenu = Interaktion.Menu(self.window, self.Charakter)
                            Charaktermenu.draw(self.window, self.Charakter)
                    elif event.type == KEYDOWN:
                        if (event.key == K_ESCAPE):
                            MODE="STARTSCREEN"
                            return MODE
                        elif (event.key == K_RIGHT and player_Icon_Position[0] < Weltkarte.MAPWIDTH - 1):
                            nextTile = Weltkarte.tilemap[player_Icon_Position[1]][player_Icon_Position[0]+1]
                            if nextTile==Weltkarte.WATER:
                                if self.Charakter.has_skill(character.skills.MagicalHealCharacterSkill):
                                    print("In magi condi")
                                    player_Icon_Position[0] += 1
                                else:
                                    pass
                        elif (event.key == K_LEFT and player_Icon_Position[0] > 0):
                            nextTile = Weltkarte.tilemap[player_Icon_Position[1]][player_Icon_Position[0] + 1]
                            if nextTile == Weltkarte.WATER:
                                if self.Charakter.has_skill(character.skills.MagicalHealCharacterSkill):
                                    print("In magi condi")
                                    player_Icon_Position[0] -= 1
                                else:
                                    pass
                        elif (event.key == K_DOWN and player_Icon_Position[1] < Weltkarte.MAPHEIGHT - 1):
                            nextTile = Weltkarte.tilemap[player_Icon_Position[1]][player_Icon_Position[0] + 1]
                            if nextTile == Weltkarte.WATER:
                                if self.Charakter.has_skill(character.skills.MagicalHealCharacterSkill):
                                    print("In magi condi")
                                    player_Icon_Position[1] += 1
                                else:
                                    pass
                        elif (event.key == K_UP and player_Icon_Position[1] > 0):
                            nextTile = Weltkarte.tilemap[player_Icon_Position[1]][player_Icon_Position[0] + 1]
                            if nextTile == Weltkarte.WATER:
                                if self.Charakter.has_skill(character.skills.MagicalHealCharacterSkill):
                                    print("In magi condi")
                                    player_Icon_Position[1] -= 1
                                else:
                                    pass
                        elif (event.key == K_SPACE):
                            currentTile = Weltkarte.tilemap[player_Icon_Position[1]][player_Icon_Position[0]]
                            if (currentTile == Weltkarte.WATER or currentTile == Weltkarte.DIRT):
                                print("Not collectable")
                            else:
                                Weltkarte.inventory[currentTile] += 1
                                Weltkarte.tilemap[player_Icon_Position[1]][player_Icon_Position[0]] = Weltkarte.DIRT
                        elif (event.key == K_e):
                            # STAR = pygame.draw.lines(self.window, Farben.clsFarben.GOLD, 1, LevelupForm.Star, 3)
                            # self.window.blit(STAR, (CharakterForm.POSITION[0]*Weltkarte.TILESIZE,CharakterForm.POSITION[1]*Weltkarte.TILESIZE))
                            #pygame.draw.rect(self.window, Farben.clsFarben.BLACK, STAR, 2)
                            pass



Charakter=character.Character()
MODE = "UNKNOWN"
NeuesSpiel=Spiel(MODE,Charakter)
while True:
    MODE=NeuesSpiel.spielen(MODE)