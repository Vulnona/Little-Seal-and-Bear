import pygame
import gui
import sys
from pygame.locals import *
from resources import Farben, Koordinaten
import Weltkarte
import character
import CharakterAussehen
import Helfer

class Bubble(object):
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
            'standard': Helfer.load_image('unknown.png'),
            'skills': {skill.id: Helfer.load_image('skills/' + skill.id + '.png') for skill in character.skills.ALL}
        }

    def draw_bubble(self):
    #BENÖTIGT ÜBERARBEITUNG
        circle_x=(self.player_Icon_Position[0] + self.bubble_position_x)*Weltkarte.TILESIZE
        circle_y=(self.player_Icon_Position[1] + self.bubble_position_y)*Weltkarte.TILESIZE

        if self.active==True:
            circle=pygame.draw.circle(self.screen, Farben.clsFarben.LIGHTGREY,[circle_x,circle_y], self.bubble_size)
        else: #not near an enemy
            circle=pygame.draw.circle(self.screen, Farben.clsFarben.DARKGREY, [circle_x, circle_y], self.bubble_size)

        if self.attack_form!="standard":
            icon = self.images['skills'][self.attack_form]
        else:
            icon = self.images['standard']
            icon=pygame.transform.scale(
                    icon, (Weltkarte.TILESIZE, Weltkarte.TILESIZE))

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

class Menu(object):
    def __init__(self, screen, charakter):
        self.screen=screen
        self.charakter=charakter
        self.fonts = {
            'normal': Helfer.load_font('celtic_gaelige.ttf', 19),
            'big': Helfer.load_font('celtic_gaelige.ttf', 23),
            'small': Helfer.load_font('celtic_gaelige.ttf', 13),
            'custom': Helfer.load_font('customfont.ttf', 19)
        }

    def interaktionen(self):
        Background = pygame.Rect(Koordinaten.clsKoordinaten.BLACKBARSTART + 60,
                                 Koordinaten.clsKoordinaten.BLACKBAREND,
                                 (Weltkarte.MAPWIDTH * Weltkarte.TILESIZE) - 185,
                                 Weltkarte.MAPHEIGHT * Weltkarte.TILESIZE)
        TextBackground = pygame.Rect(55, 125, 150, 280)
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
        Position=157
        low_grass = pygame.sprite.Sprite()
        low_grass.image = Weltkarte.snippets[1].convert_alpha()
        low_grass.rect = low_grass.image.get_rect()
        low_grass.rect.center = (134, Position)
        Position+=45
        high_grass = pygame.sprite.Sprite()
        high_grass.image = Weltkarte.snippets[2].convert_alpha()
        high_grass.rect = high_grass.image.get_rect()
        high_grass.rect.center = (134, Position)
        Position += 45
        wiesen = pygame.sprite.Sprite()
        wiesen.image = Weltkarte.snippets[3].convert_alpha()
        wiesen.rect = wiesen.image.get_rect()
        wiesen.rect.center = (134, Position)
        Position += 45
        blaetter = pygame.sprite.Sprite()
        blaetter.image = Weltkarte.snippets[4].convert_alpha()
        blaetter.rect = blaetter.image.get_rect()
        blaetter.rect.center = (134, Position)
        Position += 45
        blumen = pygame.sprite.Sprite()
        blumen.image = Weltkarte.snippets[5].convert_alpha()
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
                        canbeMade=self.check_Recipe_components(Weltkarte.LOWGRASS)
                        feed=self.check_Available(Weltkarte.LOWGRASS)
                        temp_Component=Weltkarte.LOWGRASS
                    elif high_grass.rect.collidepoint(mouse_pos):
                        canbeMade=self.check_Recipe_components(Weltkarte.MOREGRASS)
                        feed=self.check_Available(Weltkarte.MOREGRASS)
                        temp_Component = Weltkarte.MOREGRASS
                    elif wiesen.rect.collidepoint(mouse_pos):
                        canbeMade=self.check_Recipe_components(Weltkarte.WIESENSNACK)
                        feed = self.check_Available(Weltkarte.WIESENSNACK)
                        temp_Component = Weltkarte.WIESENSNACK
                    elif blaetter.rect.collidepoint(mouse_pos):
                        canbeMade=self.check_Recipe_components(Weltkarte.BLÄTTERMISCHUNG)
                        feed = self.check_Available(Weltkarte.BLÄTTERMISCHUNG)
                        temp_Component = Weltkarte.BLÄTTERMISCHUNG
                    elif blumen.rect.collidepoint(mouse_pos):
                        canbeMade=self.check_Recipe_components(Weltkarte.PUSTEBLUMENDESSERT)
                        feed = self.check_Available(Weltkarte.PUSTEBLUMENDESSERT)
                        temp_Component = Weltkarte.PUSTEBLUMENDESSERT
                if canbeMade:
                    events=produceButton.handleEvent(event)
                    if 'click' in events:
                        for i in Weltkarte.craftrecipes[temp_Component]:
                            Weltkarte.inventory[i] -= Weltkarte.craftrecipes[temp_Component][i]
                        Weltkarte.inventory[temp_Component]+=1

                        pygame.draw.rect(self.screen, Farben.clsFarben.BLACK, Background)
                        pygame.draw.rect(self.screen, Farben.clsFarben.BLACK, TextBackground)
                        canbeMade = self.check_Recipe_components(temp_Component)

                if feed:
                    events=feedButton.handleEvent(event)
                    if 'click' in events:
                        Weltkarte.inventory[temp_Component] -= 1
                        amount_exp=Weltkarte.experience_crafts[temp_Component]
                        self.charakter.gain_experience(amount_exp)

                        pygame.draw.rect(self.screen, Farben.clsFarben.BLACK, Background)
                        pygame.draw.rect(self.screen, Farben.clsFarben.BLACK, TextBackground)
                        feed = self.check_Available(temp_Component)

                events = exitButton.handleEvent(event)
                if 'click' in events:
                    proceed = False


                CharakterAussehen.showAnimal(self.charakter, self.screen)
                actuallevel = self.fonts['big'].render("Level: " + str(self.charakter.get_level()), 0,
                                                       Farben.clsFarben.WHITE)
                self.screen.blit(actuallevel,
                                 (Koordinaten.clsKoordinaten.ACTLVLPOSX, Koordinaten.clsKoordinaten.ACTLVLPOSY))
                Position = 157
                for item in Weltkarte.craftables:
                    textObjekt = pygame.font.Font('resources/fonts/celtic_gaelige.ttf', 19).render(str(
                        Weltkarte.inventory[item]), True, Farben.clsFarben.WHITE, Farben.clsFarben.BLACK)
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
                pygame.display.update()

    def check_Recipe_components(self, item):
        Background = pygame.Rect(Koordinaten.clsKoordinaten.BLACKBARSTART+60, Koordinaten.clsKoordinaten.BLACKBAREND,
                                 (Weltkarte.MAPWIDTH * Weltkarte.TILESIZE)-185,
                                   Weltkarte.MAPHEIGHT * Weltkarte.TILESIZE)
        pygame.draw.rect(self.screen, Farben.clsFarben.BLACK, Background)
        canbeMade=True
        Position=250
        for y in Weltkarte.craftrecipes[item]:
            #draws component needed
            snippetObjekt = Weltkarte.snippets[y]
            self.screen.blit(snippetObjekt, (Position, 405))
            #color indicated if player possesses the amount of ressources needed
            if Weltkarte.craftrecipes[item][y]<=Weltkarte.inventory[y]:
                Farbe=Farben.clsFarben.WHITE
            else:
                canbeMade=False
                Farbe=Farben.clsFarben.DARKRED
            #draws amount component needed
            textObjekt = pygame.font.Font('resources/fonts/celtic_gaelige.ttf', 19).render(str(
                Weltkarte.craftrecipes[item][y]), True, Farbe, Farben.clsFarben.BLACK)
            Position+=50
            self.screen.blit(
                textObjekt, (Position, 405))
            Position+=30

        pygame.display.update()
        return canbeMade

    def check_Available(self, item):
        feed=False
        if Weltkarte.inventory[item]>0:
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

        interaktion=False
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
                    interaktion=True
                else:
                    pygame.draw.rect(self.screen, Farben.clsFarben.BLACK, BG)
                    feedButton.draw(self.screen)
                    exitButton.draw(self.screen)
                    CharakterAussehen.showAnimal(charakter, self.screen)
                    if interaktion:
                        self.interaktionen()
                        visMode=True
                        interaktion=False

                pygame.display.update()
