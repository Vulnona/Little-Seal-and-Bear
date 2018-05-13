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
            'custom': Helfer.load_font('customfont.ttf', 19)
        }
        self.images = {
            'standard': Helfer.load_image('unknown.png'),
            'skills': {skill.id: Helfer.load_image('skills/' + skill.id + '.png') for skill in character.skills.ALL}
        }
    def interaktionen(self, charakter):
        #textbackground = pygame.Rect(80, 100, 100, 600)# textbackground: background for all craftable values, and collectable values
        actuallevel = self.fonts['normal'].render("Level: " + str(charakter.get_level()), 0, Farben.clsFarben.WHITE)
        exitButton = gui.PygButton((Koordinaten.clsKoordinaten.BUTTONPOSX,
                                    Koordinaten.clsKoordinaten.BUTTONPOSY,
                                    Koordinaten.clsKoordinaten.BUTTONWIDTH,
                                    Koordinaten.clsKoordinaten.BUTTONHEIGTH),
                                   'Zurück',
                                   bgcolor=Farben.clsFarben.DARKRED, fgcolor=Farben.clsFarben.BRIGHT)
        exitButton.font = self.fonts['normal']

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

        Position= 157
        for item in Weltkarte.craftables:
            textObjekt = pygame.font.Font('resources/fonts/celtic_gaelige.ttf', 19).render(str(
                Weltkarte.inventory[item]), True, Farben.clsFarben.WHITE, Farben.clsFarben.BLACK)
            self.screen.blit(
                textObjekt, (134+25, Position-20))
            Position += 45

        proceed=True
        while proceed:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if low_grass.rect.collidepoint(mouse_pos):
                        self.show_recipes(Weltkarte.LOWGRASS)
                    if high_grass.rect.collidepoint(mouse_pos):
                        self.show_recipes(Weltkarte.MOREGRASS)
                    if wiesen.rect.collidepoint(mouse_pos):
                        self.show_recipes(Weltkarte.WIESENSNACK)
                    if blaetter.rect.collidepoint(mouse_pos):
                        self.show_recipes(Weltkarte.BLÄTTERMISCHUNG)
                    if blumen.rect.collidepoint(mouse_pos):
                        self.show_recipes(Weltkarte.PUSTEBLUMENDESSERT)
                events = exitButton.handleEvent(event)
                if 'click' in events:
                    proceed = False
                else:
         #          pygame.draw.rect(self.screen, Farben.clsFarben.BLACK, textbackground)
                    CharakterAussehen.showAnimal(charakter, self.screen)
                    self.screen.blit(actuallevel,
                                     (Koordinaten.clsKoordinaten.ACTLVLPOSX, Koordinaten.clsKoordinaten.ACTLVLPOSY))
                    exitButton.draw(self.screen)

                    self.screen.blit(low_grass.image, low_grass.rect)
                    self.screen.blit(high_grass.image, high_grass.rect)
                    self.screen.blit(wiesen.image, wiesen.rect)
                    self.screen.blit(blaetter.image, blaetter.rect)
                    self.screen.blit(blumen.image, blumen.rect)


    def show_recipes(self, item):
        Background = pygame.Rect(Koordinaten.clsKoordinaten.BLACKBARSTART+60, Koordinaten.clsKoordinaten.BLACKBAREND,
                                 (Weltkarte.MAPWIDTH * Weltkarte.TILESIZE)-185,
                                   Weltkarte.MAPHEIGHT * Weltkarte.TILESIZE)
        pygame.draw.rect(self.screen, Farben.clsFarben.BLACK, Background)
        Position=250
        for y in Weltkarte.craftrecipes[item]:
            print(y, ':', Weltkarte.craftrecipes[item][y])
            print(Weltkarte.craftrecipes[item][y])
            snippetObjekt = Weltkarte.snippets[y]
            self.screen.blit(snippetObjekt, (Position, 400))
            textObjekt = pygame.font.Font('resources/fonts/celtic_gaelige.ttf', 19).render(str(
                Weltkarte.craftrecipes[item][y]), True, Farben.clsFarben.WHITE, Farben.clsFarben.BLACK)
            Position+=50
            self.screen.blit(
                textObjekt, (Position, 400))
            Position+=30

        pygame.display.update()
        #if (event.key == Weltkarte.controls[key]):
        #    if key in Weltkarte.craftrecipes:
        #        canBeMade = True
        #        for i in Weltkarte.craftrecipes[key]:
        #            if Weltkarte.craftrecipes[key][i] > Weltkarte.inventory[i]:
        #               canBeMade = False
        #              break
        #      if canBeMade == True:
        #         for i in Weltkarte.craftrecipes[key]:
        #            Weltkarte.inventory[i] -= Weltkarte.craftrecipes[key][i]
        #       Weltkarte.inventory[key]+=1

    #liste: buttons to be pressed for crafting and feeding
                    #liste=[0,0,0,1,2,3]
                    #listezwei=[0,0,0,7,8,9]
                    #placePosition = Koordinaten.clsKoordinaten.INVPLACEPOS
                    #for item in Weltkarte.craftables:
                        #displaying craft snippets
                     #   self.screen.blit(Weltkarte.snippets[item], (70, placePosition))
                      #  placePosition += 50
                       # textObjekt = self.fonts['normal'].render(str(Weltkarte.inventory.get(item)), True, Farben.clsFarben.WHITE,
                        #                                 Farben.clsFarben.BLACK)
                        #self.screen.blit(textObjekt, (115, placePosition - 50))
                        #placePosition += 50
                        #craftinglabel = self.fonts['custom'].render("Herstellen: Drücke " + str(liste[item]), False, Farben.clsFarben.GOLD)
                        #feedlabel = self.fonts['custom'].render("Füttern:  Drücke " + str(listezwei[item]), False, Farben.clsFarben.GOLD)
                        #self.screen.blit(craftinglabel, (105, craftbuttony-14))
                        #self.screen.blit(feedlabel, (105, craftbuttony-1))
                        #craftbuttony+=100

                    #if event.type == KEYDOWN:
                        #for key in Weltkarte.feedcontrols:
                        #    if (event.key == Weltkarte.feedcontrols[key]):
                                #print(Weltkarte.py.feedcontrols[key])
                                #print(event.key)
                                #print(Weltkarte.py.inventory[key])
                         #       leveltoohigh=False
                          #      if (event.key == 55 and int(character.Character.get_level(charakter))>=4):
                           #         leveltoohigh=True
                            #        print("Level zu hoch für Wiesensnack")
                             #   if (event.key == 56 and int(character.Character.get_level(charakter))>=8):
                              #      leveltoohigh=True
                               #     print("Level zu hoch für Blättermischung")
                                #if (Weltkarte.inventory[key]>=1 and leveltoohigh==False):
                                 #   Weltkarte.inventory[key]-=1
                                  #  print(character.Character.get_level(charakter))
                                   # character.Character.LevelUp(charakter)
                                    #print(character.Character.get_level(charakter))
                        #for key in Weltkarte.controls:
                        #    if (event.key == Weltkarte.controls[key]):
                        #        if key in Weltkarte.craftrecipes:
                        #            canBeMade = True
                        #            for i in Weltkarte.craftrecipes[key]:
                        #                if Weltkarte.craftrecipes[key][i] > Weltkarte.inventory[i]:
                         #                   canBeMade = False
                          #                  break
                          #          if canBeMade == True:
                           #             for i in Weltkarte.craftrecipes[key]:
                            #                Weltkarte.inventory[i] -= Weltkarte.craftrecipes[key][i]
                             #           Weltkarte.inventory[key]+=1

    def draw(self, charakter):
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
                        self.interaktionen(charakter)
                        visMode=True
                        interaktion=False

                pygame.display.update()
