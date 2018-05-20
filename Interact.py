import pygame
import gui
import sys
from pygame.locals import *
from resources import Farben, Koordinaten
import World_Map
import character
import Character_Appearance
import Helper

class Bubble(object):

    def __init__(self, screen, skill, Position, active):
        self.screen = screen
        self.Position = Position #Starting with '0', max is 3 (because there are 4 fighting and 4 passive skills available overall)
        self.bubble_size = 18
        self.skill=skill
        self.active=active #in near of an enemy for fighting, enough temp values for fighting and non-fighting skills
        self._load_images()

    def _load_images(self):
        self.images = {
            'standard_active': Helper.load_image('skills/standard_active.png'),
            'standard_inactive': Helper.load_image('skills/standard_inactive.png'),
            'skills_active': {skill.id: Helper.load_image('skills/' + skill.id + '_active.png') for skill in character.skills.ACTIVE},
            'skills_inactive': {skill.id: Helper.load_image('skills/' + skill.id + '_inactive.png') for skill in character.skills.ACTIVE}
        }

    def draw_bubble(self):
        circle_x= 320 + (self.Position * World_Map.TILESIZE)
        circle_y= World_Map.MAPHEIGHT * World_Map.TILESIZE + 26
        circle=pygame.draw.circle(self.screen, Farben.clsFarben.BLACK,[circle_x,circle_y], self.bubble_size)

        if self.active:
            if self.skill!= 'standard':
                icon = self.images['skills_active'][self.skill]
            else:
                icon = self.images['standard_active']
        else:
            if self.skill!= 'standard':
                icon = self.images['skills_inactive'][self.skill]
            else:
                icon = self.images['standard_inactive']

        icon=pygame.transform.scale(
                    icon, (World_Map.TILESIZE, World_Map.TILESIZE))

        blit_icon_x=circle_x-20
        blit_icon_y=circle_y-20

        self.screen.blit(icon, (blit_icon_x, blit_icon_y))
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

    def fight_Skills_showing(self):
        pass

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
            amountStats = pygame.font.Font('resources/fonts/celtic_gaelige.ttf', 15).render(str(
                self.Charakter.get_status_temp(stats_string[stat])), True, Farben.clsFarben.WHITE,
                Farben.clsFarben.BLACK)
            slash = pygame.font.Font('resources/fonts/celtic_gaelige.ttf', 15).render(str("/"), True,
                                                                                                 Farben.clsFarben.WHITE,
                                                                                                 Farben.clsFarben.BLACK)
            textObjekt2 = pygame.font.Font('resources/fonts/celtic_gaelige.ttf', 15).render(str(
                self.Charakter.get_status_max(stats_string[stat])), True, Farben.clsFarben.WHITE,
                Farben.clsFarben.BLACK)
            self.screen.blit(
                amountStats, (15, placePosition))
            self.screen.blit(
                slash, (30, placePosition))
            self.screen.blit(
                textObjekt2, (35, placePosition))

            placePosition += 15


    def interaktionen(self):
        Background = pygame.Rect(Koordinaten.clsKoordinaten.BLACKBARSTART + 60,
                                 Koordinaten.clsKoordinaten.BLACKBAREND,
                                 (World_Map.MAPWIDTH * World_Map.TILESIZE) - 185,
                                 World_Map.MAPHEIGHT * World_Map.TILESIZE)
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
        low_grass.image = World_Map.snippets[1].convert_alpha()
        low_grass.rect = low_grass.image.get_rect()
        low_grass.rect.center = (134, Position)
        Position+=45
        high_grass = pygame.sprite.Sprite()
        high_grass.image = World_Map.snippets[2].convert_alpha()
        high_grass.rect = high_grass.image.get_rect()
        high_grass.rect.center = (134, Position)
        Position += 45
        wiesen = pygame.sprite.Sprite()
        wiesen.image = World_Map.snippets[3].convert_alpha()
        wiesen.rect = wiesen.image.get_rect()
        wiesen.rect.center = (134, Position)
        Position += 45
        blaetter = pygame.sprite.Sprite()
        blaetter.image = World_Map.snippets[4].convert_alpha()
        blaetter.rect = blaetter.image.get_rect()
        blaetter.rect.center = (134, Position)
        Position += 45
        blumen = pygame.sprite.Sprite()
        blumen.image = World_Map.snippets[5].convert_alpha()
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
                        canbeMade=self.check_Recipe_components(World_Map.LOWGRASS)
                        feed=self.check_Available(World_Map.LOWGRASS)
                        temp_Component=World_Map.LOWGRASS
                    elif high_grass.rect.collidepoint(mouse_pos):
                        canbeMade=self.check_Recipe_components(World_Map.MOREGRASS)
                        feed=self.check_Available(World_Map.MOREGRASS)
                        temp_Component = World_Map.MOREGRASS
                    elif wiesen.rect.collidepoint(mouse_pos):
                        canbeMade=self.check_Recipe_components(World_Map.WIESENSNACK)
                        feed = self.check_Available(World_Map.WIESENSNACK)
                        temp_Component = World_Map.WIESENSNACK
                    elif blaetter.rect.collidepoint(mouse_pos):
                        canbeMade=self.check_Recipe_components(World_Map.BLÄTTERMISCHUNG)
                        feed = self.check_Available(World_Map.BLÄTTERMISCHUNG)
                        temp_Component = World_Map.BLÄTTERMISCHUNG
                    elif blumen.rect.collidepoint(mouse_pos):
                        canbeMade=self.check_Recipe_components(World_Map.PUSTEBLUMENDESSERT)
                        feed = self.check_Available(World_Map.PUSTEBLUMENDESSERT)
                        temp_Component = World_Map.PUSTEBLUMENDESSERT
                if canbeMade:
                    events=produceButton.handleEvent(event)
                    if 'click' in events:
                        for i in World_Map.craftrecipes[temp_Component]:
                            World_Map.inventory[i] -= World_Map.craftrecipes[temp_Component][i]
                        World_Map.inventory[temp_Component]+=1

                        pygame.draw.rect(self.screen, Farben.clsFarben.BLACK, Background)
                        pygame.draw.rect(self.screen, Farben.clsFarben.BLACK, TextBackground)
                        canbeMade = self.check_Recipe_components(temp_Component)

                if feed:
                    events=feedButton.handleEvent(event)
                    if 'click' in events:
                        World_Map.inventory[temp_Component] -= 1
                        amount_exp=World_Map.experience_crafts[temp_Component]
                        self.Charakter.gain_experience(amount_exp)

                        pygame.draw.rect(self.screen, Farben.clsFarben.BLACK, Background)
                        pygame.draw.rect(self.screen, Farben.clsFarben.BLACK, TextBackground)
                        feed = self.check_Available(temp_Component)

                events = exitButton.handleEvent(event)
                if 'click' in events:
                    proceed = False

                Character_Appearance.showAnimal(self.Charakter, self.screen)
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
                for item in World_Map.craftables:
                    textObjekt = pygame.font.Font('resources/fonts/celtic_gaelige.ttf', 19).render(str(
                        World_Map.inventory[item]), True, Farben.clsFarben.WHITE, Farben.clsFarben.BLACK)
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
                                 (World_Map.MAPWIDTH * World_Map.TILESIZE) - 185,
                                 World_Map.MAPHEIGHT * World_Map.TILESIZE)
        pygame.draw.rect(self.screen, Farben.clsFarben.BLACK, Background)
        canbeMade=True
        Position=250
        for y in World_Map.craftrecipes[item]:
            #draws component needed
            snippetObjekt = World_Map.snippets[y]
            self.screen.blit(snippetObjekt, (Position, 405))
            #color indicated if player possesses the amount of ressources needed
            if World_Map.craftrecipes[item][y]<=World_Map.inventory[y]:
                Farbe=Farben.clsFarben.WHITE
            else:
                canbeMade=False
                Farbe=Farben.clsFarben.DARKRED
            #draws amount component needed
            textObjekt = pygame.font.Font('resources/fonts/celtic_gaelige.ttf', 19).render(str(
                World_Map.craftrecipes[item][y]), True, Farbe, Farben.clsFarben.BLACK)
            Position+=50
            self.screen.blit(
                textObjekt, (Position, 405))
            Position+=30

        pygame.display.update()
        return canbeMade

    def check_Available(self, item):
        feed=False
        if World_Map.inventory[item]>0:
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
                    Character_Appearance.showAnimal(charakter, self.screen)
                    if interaction:
                        self.interaktionen()
                        visMode=True
                        interaction=False

                pygame.display.update()