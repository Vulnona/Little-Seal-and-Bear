import pygame
import gui
import sys
from pygame.locals import *
from resources import Farben, Koordinaten
import WorldMap
import character
import CharacterAppearance
import Helper

class Bubble(object):
    #SO nicht mehr notwendig, lieber unten in die anzeige blitten
    def __init__(self, screen, player_Icon_Position, bubble_position_x, bubble_position_y, attack_form, active):
        self.screen=screen
        self.bubble_position_x = bubble_position_x
        self.bubble_position_y = bubble_position_y
        self.bubble_size = 20
        self.player_Icon_Position=player_Icon_Position
        self.attack_form=attack_form
        self.active=active #in near of an enemy
        self._load_images()

    def _load_images(self):
        self.images = {
            'standard': Helper.load_image('unknown.png'),
            'skills': {skill.id: Helper.load_image('skills/' + skill.id + '.png') for skill in character.skills.ALL}
        }

    def draw_bubble(self):
    #BENÖTIGT ÜBERARBEITUNG
        circle_x= (self.player_Icon_Position[0] + self.bubble_position_x) * WorldMap.TILESIZE
        circle_y= (self.player_Icon_Position[1] + self.bubble_position_y) * WorldMap.TILESIZE

        if self.active==True:
            circle=pygame.draw.circle(self.screen, Farben.clsFarben.LIGHTGREY,[circle_x,circle_y], self.bubble_size)
        else: #not near an enemy
            circle=pygame.draw.circle(self.screen, Farben.clsFarben.DARKGREY, [circle_x, circle_y], self.bubble_size)

        if self.attack_form!="standard":
            icon = self.images['skills'][self.attack_form]
        else:
            icon = self.images['standard']
            icon=pygame.transform.scale(
                    icon, (WorldMap.TILESIZE, WorldMap.TILESIZE))

        #Positioning of the skill image on circle
        if self.bubble_position_x>0:
            blit_icon_x=circle_x-10
        else:
            blit_icon_x=circle_x-12
        if self.bubble_position_y>0:
            blit_icon_y=circle_y-10
        else:
            blit_icon_y=circle_y-8

        self.screen.blit(
            icon, (
                blit_icon_x, blit_icon_y
                )
        )
        pygame.display.update()
        return circle

class clsInteract(object):
    def __init__(self, screen, Charakter):
        self.screen=screen
        self.Charakter=Charakter
        self._load_fonts()
        self._load_images()

    def _load_fonts(self):
        self.fonts = {
            'normal': Helper.load_font('celtic_gaelige.ttf', 19),
            'big': Helper.load_font('celtic_gaelige.ttf', 23),
            'small': Helper.load_font('celtic_gaelige.ttf', 13),
            'custom': Helper.load_font('customfont.ttf', 19)
        }

    def _load_images(self):
        self.images = {
            'stats': {
                'health': Helper.load_image('stats/health.png'),
                'endurance': Helper.load_image('stats/endurance.png'),
                'magic': Helper.load_image('stats/magic.png')
            }
        }

    def stats_showing(self):
        background=pygame.Rect(0, 400, 50, 50)
        pygame.draw.rect(self.screen, Farben.clsFarben.BLACK, background)
        health = self.images['stats']['health']
        health = pygame.transform.scale(health, (15, 15))
        endurance = self.images['stats']['endurance']
        endurance = pygame.transform.scale(endurance, (15, 15))
        magic = self.images['stats']['magic']
        magic = pygame.transform.scale(magic, (15, 15))
        stats = (health, endurance, magic)
        stats_string = ("health", "endu", "magic")
        placePosition = 400
        for stat in range(3):
            self.screen.blit(
                stats[stat], (0, placePosition))
            # placePosition += 10
            textObjekt = pygame.font.Font('resources/fonts/celtic_gaelige.ttf', 15).render(str(
                self.Charakter.get_status_temp(stats_string[stat])), True, Farben.clsFarben.WHITE,
                Farben.clsFarben.BLACK)
            abgrenzungObjekt = pygame.font.Font('resources/fonts/celtic_gaelige.ttf', 15).render(str("/"), True,
                                                                                                 Farben.clsFarben.WHITE,
                                                                                                 Farben.clsFarben.BLACK)
            textObjekt2 = pygame.font.Font('resources/fonts/celtic_gaelige.ttf', 15).render(str(
                self.Charakter.get_status_max(stats_string[stat])), True, Farben.clsFarben.WHITE,
                Farben.clsFarben.BLACK)
            self.screen.blit(
                textObjekt, (15, placePosition))
            self.screen.blit(
                abgrenzungObjekt, (30, placePosition))
            self.screen.blit(
                textObjekt2, (35, placePosition))

            placePosition += 15


    def interaktionen(self):
        Background = pygame.Rect(Koordinaten.clsKoordinaten.BLACKBARSTART + 60,
                                 Koordinaten.clsKoordinaten.BLACKBAREND,
                                 (WorldMap.MAPWIDTH * WorldMap.TILESIZE) - 185,
                                 WorldMap.MAPHEIGHT * WorldMap.TILESIZE)
        TextBackground = pygame.Rect(55, 100, 150, 280)
        exitButton = gui.PygButton((Koordinaten.clsKoordinaten.BUTTONPOSX,
                                    Koordinaten.clsKoordinaten.BUTTONPOSY,
                                    Koordinaten.clsKoordinaten.BUTTONWIDTH,
                                    Koordinaten.clsKoordinaten.BUTTONHEIGTH),
                                   'Zurück',
                                   bgcolor=Farben.clsFarben.DARKRED, fgcolor=Farben.clsFarben.BRIGHT)
        exitButton.font = self.fonts['normal']
        feedButton = gui.PygButton((60, 410,
                                    Koordinaten.clsKoordinaten.BUTTONWIDTH - 20,
                                    Koordinaten.clsKoordinaten.BUTTONHEIGTH),
                                   'Füttern',
                                   bgcolor=Farben.clsFarben.DARKRED, fgcolor=Farben.clsFarben.BRIGHT)
        feedButton.font = self.fonts['small']
        produceButton = gui.PygButton((150, 410,
                                       Koordinaten.clsKoordinaten.BUTTONWIDTH - 20,
                                       Koordinaten.clsKoordinaten.BUTTONHEIGTH),
                                      'Erschaffen',
                                      bgcolor=Farben.clsFarben.DARKRED, fgcolor=Farben.clsFarben.BRIGHT)
        produceButton.font = self.fonts['small']
        Position=187
        low_grass = pygame.sprite.Sprite()
        low_grass.image = WorldMap.snippets[1].convert_alpha()
        low_grass.rect = low_grass.image.get_rect()
        low_grass.rect.center = (134, Position)
        Position+=45
        high_grass = pygame.sprite.Sprite()
        high_grass.image = WorldMap.snippets[2].convert_alpha()
        high_grass.rect = high_grass.image.get_rect()
        high_grass.rect.center = (134, Position)
        Position += 45
        wiesen = pygame.sprite.Sprite()
        wiesen.image = WorldMap.snippets[3].convert_alpha()
        wiesen.rect = wiesen.image.get_rect()
        wiesen.rect.center = (134, Position)
        Position += 45
        blaetter = pygame.sprite.Sprite()
        blaetter.image = WorldMap.snippets[4].convert_alpha()
        blaetter.rect = blaetter.image.get_rect()
        blaetter.rect.center = (134, Position)
        Position += 45
        blumen = pygame.sprite.Sprite()
        blumen.image = WorldMap.snippets[5].convert_alpha()
        blumen.rect = wiesen.image.get_rect()
        blumen.rect.center = (134, Position)

        canbeMade=False
        feed=False
        proceed=True
        while proceed:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if low_grass.rect.collidepoint(mouse_pos):
                        canbeMade=self.check_Recipe_components(WorldMap.LOWGRASS)
                        feed=self.check_Available(WorldMap.LOWGRASS)
                        temp_Component=WorldMap.LOWGRASS
                    elif high_grass.rect.collidepoint(mouse_pos):
                        canbeMade=self.check_Recipe_components(WorldMap.MOREGRASS)
                        feed=self.check_Available(WorldMap.MOREGRASS)
                        temp_Component = WorldMap.MOREGRASS
                    elif wiesen.rect.collidepoint(mouse_pos):
                        canbeMade=self.check_Recipe_components(WorldMap.WIESENSNACK)
                        feed = self.check_Available(WorldMap.WIESENSNACK)
                        temp_Component = WorldMap.WIESENSNACK
                    elif blaetter.rect.collidepoint(mouse_pos):
                        canbeMade=self.check_Recipe_components(WorldMap.BLÄTTERMISCHUNG)
                        feed = self.check_Available(WorldMap.BLÄTTERMISCHUNG)
                        temp_Component = WorldMap.BLÄTTERMISCHUNG
                    elif blumen.rect.collidepoint(mouse_pos):
                        canbeMade=self.check_Recipe_components(WorldMap.PUSTEBLUMENDESSERT)
                        feed = self.check_Available(WorldMap.PUSTEBLUMENDESSERT)
                        temp_Component = WorldMap.PUSTEBLUMENDESSERT
                if canbeMade:
                    events=produceButton.handleEvent(event)
                    if 'click' in events:
                        for i in WorldMap.craftrecipes[temp_Component]:
                            WorldMap.inventory[i] -= WorldMap.craftrecipes[temp_Component][i]
                        WorldMap.inventory[temp_Component]+=1

                        pygame.draw.rect(self.screen, Farben.clsFarben.BLACK, Background)
                        pygame.draw.rect(self.screen, Farben.clsFarben.BLACK, TextBackground)
                        canbeMade = self.check_Recipe_components(temp_Component)

                if feed:
                    events=feedButton.handleEvent(event)
                    if 'click' in events:
                        WorldMap.inventory[temp_Component] -= 1
                        amount_exp=WorldMap.experience_crafts[temp_Component]
                        self.Charakter.gain_experience(amount_exp)

                        pygame.draw.rect(self.screen, Farben.clsFarben.BLACK, Background)
                        pygame.draw.rect(self.screen, Farben.clsFarben.BLACK, TextBackground)
                        feed = self.check_Available(temp_Component)

                events = exitButton.handleEvent(event)
                if 'click' in events:
                    proceed = False

                CharacterAppearance.showAnimal(self.Charakter, self.screen)
                actuallevel = self.fonts['big'].render("Level: " + str(self.Charakter.get_Level()), 0,
                                                       Farben.clsFarben.WHITE)
                self.screen.blit(actuallevel,
                                 (Koordinaten.clsKoordinaten.ACTLVLPOSX, Koordinaten.clsKoordinaten.ACTLVLPOSY))
                exp_bar = self.fonts['normal'].render(str(self.Charakter.get_experience()) + "/" + str(self.Charakter.exp_needed_for_Level_Up()),
                                                      0, Farben.clsFarben.WHITE)
                self.screen.blit(exp_bar,
                                 (Koordinaten.clsKoordinaten.ACTLVLPOSX, Koordinaten.clsKoordinaten.ACTLVLPOSY+25))

                #craft items and their number available
                Position = 187
                for item in WorldMap.craftables:
                    textObjekt = pygame.font.Font('resources/fonts/celtic_gaelige.ttf', 19).render(str(
                        WorldMap.inventory[item]), True, Farben.clsFarben.WHITE, Farben.clsFarben.BLACK)
                    self.screen.blit(
                        textObjekt, (134 + 25, Position - 20))
                    Position += 45

                self.screen.blit(low_grass.image, low_grass.rect)
                self.screen.blit(high_grass.image, high_grass.rect)
                self.screen.blit(wiesen.image, wiesen.rect)
                self.screen.blit(blaetter.image, blaetter.rect)
                self.screen.blit(blumen.image, blumen.rect)

                exitButton.draw(self.screen)
                if canbeMade:
                    produceButton.draw(self.screen)
                if feed:
                    feedButton.draw(self.screen)

                self.stats_showing()
                pygame.display.update()

    def check_Recipe_components(self, item):
        Background = pygame.Rect(Koordinaten.clsKoordinaten.BLACKBARSTART + 60, Koordinaten.clsKoordinaten.BLACKBAREND,
                                 (WorldMap.MAPWIDTH * WorldMap.TILESIZE) - 185,
                                 WorldMap.MAPHEIGHT * WorldMap.TILESIZE)
        pygame.draw.rect(self.screen, Farben.clsFarben.BLACK, Background)
        canbeMade=True
        Position=250
        for y in WorldMap.craftrecipes[item]:
            #draws component needed
            snippetObjekt = WorldMap.snippets[y]
            self.screen.blit(snippetObjekt, (Position, 405))
            #color indicated if player possesses the amount of ressources needed
            if WorldMap.craftrecipes[item][y]<=WorldMap.inventory[y]:
                Farbe=Farben.clsFarben.WHITE
            else:
                canbeMade=False
                Farbe=Farben.clsFarben.DARKRED
            #draws amount component needed
            textObjekt = pygame.font.Font('resources/fonts/celtic_gaelige.ttf', 19).render(str(
                WorldMap.craftrecipes[item][y]), True, Farbe, Farben.clsFarben.BLACK)
            Position+=50
            self.screen.blit(
                textObjekt, (Position, 405))
            Position+=30

        pygame.display.update()
        return canbeMade

    def check_Available(self, item):
        feed=False
        if WorldMap.inventory[item]>0:
            feed=True
        return feed

    def draw_MainMenu(self, charakter):
        BG = pygame.Rect(55, 75, 500, 500) #BACKGROUND
        exitButton = gui.PygButton((Koordinaten.clsKoordinaten.BUTTONPOSX,
                                    Koordinaten.clsKoordinaten.BUTTONPOSY,
                                    Koordinaten.clsKoordinaten.BUTTONWIDTH,
                                    Koordinaten.clsKoordinaten.BUTTONHEIGTH),
                                   'Zurück',
                                   bgcolor=Farben.clsFarben.DARKRED, fgcolor=Farben.clsFarben.BRIGHT)
        exitButton.font = self.fonts['normal']
        feedButton = gui.PygButton((Koordinaten.clsKoordinaten.FEEDBUTTONPOSX,
                                    Koordinaten.clsKoordinaten.FEEDBUTTONPOSY,
                                    Koordinaten.clsKoordinaten.BUTTONWIDTH,
                                    Koordinaten.clsKoordinaten.BUTTONHEIGTH),
                                   'Füttern',
                                   bgcolor=Farben.clsFarben.DARKRED, fgcolor=Farben.clsFarben.BRIGHT)
        feedButton.font = self.fonts['normal']

        interaction=False
        proceed = True
        visMode = True
        while proceed:
            feedButton.visible=visMode
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                events = exitButton.handleEvent(event)
                if 'click' in events:
                    proceed = False
                events = feedButton.handleEvent(event)
                if 'click' in events:
                    visMode = not visMode
                    interaction=True
                else:
                    pygame.draw.rect(self.screen, Farben.clsFarben.BLACK, BG)
                    feedButton.draw(self.screen)
                    exitButton.draw(self.screen)
                    CharacterAppearance.showAnimal(charakter, self.screen)
                    if interaction:
                        self.interaktionen()
                        visMode=True
                        interaction=False

                pygame.display.update()