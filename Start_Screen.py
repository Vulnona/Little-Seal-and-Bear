import pygame, sys
from pygame.locals import *
import World_Map
import Helper
import os.path
import gui
from resources import Farben


class clsStartScreen(object):
    def __init__(self, screen, MODE, Status):
        self.screen=screen
        self.MODE=MODE
        self.Status=Status
        self.fonts = {
            'normal': Helper.load_font('celtic_gaelige.ttf', 19)
        }

    def draw(self):
        background=pygame.Rect(World_Map.MAPWIDTH * World_Map.TILESIZE, World_Map.MAPHEIGHT * World_Map.TILESIZE + 50, 400, 400)

        returnButton = gui.PygButton((10, 100, 80, 20),
                                     'Weiter',
                                     bgcolor=Farben.clsFarben.DARKRED, fgcolor=Farben.clsFarben.BRIGHT)
        returnButton.font = self.fonts['normal']
        newgameButton = gui.PygButton((100, 100, 80, 20),
                                     'Neues Spiel',
                                     bgcolor=Farben.clsFarben.DARKRED, fgcolor=Farben.clsFarben.BRIGHT)
        newgameButton.font = self.fonts['normal']
        saveButton = gui.PygButton((100, 200, 80, 20),
                                   'Speichern',
                                   bgcolor=Farben.clsFarben.DARKRED, fgcolor=Farben.clsFarben.BRIGHT)
        saveButton.font = self.fonts['normal']
        loadButton = gui.PygButton((200, 100, 80, 20),
                                     'Laden',
                                     bgcolor=Farben.clsFarben.DARKRED, fgcolor=Farben.clsFarben.BRIGHT)
        loadButton.font = self.fonts['normal']

        if self.Status:
            returnButton.draw(self.screen)
            saveButton.draw(self.screen)
        else:
            newgameButton.draw(self.screen)

        if os.path.isfile('savefile.dat'):
            loadButton.draw(self.screen)
        pygame.display.update()

        while self.whichMode()=="STARTSCREEN":
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if self.Status:
                    events = returnButton.handleEvent(event)
                    if 'click' in events:
                        self.MODE = "GAME"
                    events = saveButton.handleEvent(event)
                    if 'click' in events:
                        self.MODE = "SAVE"
                    if os.path.isfile('savefile.dat'):
                        events = loadButton.handleEvent(event)
                        if 'click' in events:
                            self.MODE = "LOAD"
                else:
                    events = newgameButton.handleEvent(event)
                    if 'click' in events:
                        self.MODE = "NEWGAME"
                    if os.path.isfile('savefile.dat'):
                        events = loadButton.handleEvent(event)
                        if 'click' in events:
                            self.MODE = "LOAD"

    def whichMode(self):
        return self.MODE