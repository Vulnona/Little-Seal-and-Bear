# http://usingpython.com/dl/StayAlive.py
import pygame
import sys
from pygame.locals import *
from resources import Farben, Koordinaten
import Weltkarte
import character
import CharakterAussehen
import Helfer


class Bubble(object):
    def __init__(self, screen, player_Icon_Position, bubble_position_x, bubble_position_y, attack_form, active):
        self.screen = screen
        self.bubble_position_x = bubble_position_x
        self.bubble_position_y = bubble_position_y
        self.bubble_size = 20
        self.player_Icon_Position = player_Icon_Position
        self.attack_form = attack_form
        self.active = active  # in near of an enemy
        self._load_images()

    def _load_images(self):
        self.images = {
            'standard': Helfer.load_image('unknown.png'),
            'skills': {skill.id: Helfer.load_image('skills/' + skill.id + '.png') for skill in character.skills.ALL}
        }

    def draw_bubble(self):

        circle_x = (
            self.player_Icon_Position[0] + self.bubble_position_x)*Weltkarte.TILESIZE
        circle_y = (
            self.player_Icon_Position[1] + self.bubble_position_y)*Weltkarte.TILESIZE

        if self.active:
            circle = pygame.draw.circle(self.screen, Farben.clsFarben.LIGHTGREY, [
                                        circle_x, circle_y], self.bubble_size)
        else:  # not near an enemy
            circle = pygame.draw.circle(self.screen, Farben.clsFarben.DARKGREY, [
                                        circle_x, circle_y], self.bubble_size)

        if self.attack_form != "standard":
            icon = self.images['skills'][self.attack_form]
        else:
            icon = self.images['standard']
            icon = pygame.transform.scale(
                icon, (Weltkarte.TILESIZE, Weltkarte.TILESIZE))

        # Positioning of the skill image on circle
        if self.bubble_position_x > 0:
            blit_icon_x = circle_x-10
        else:
            blit_icon_x = circle_x-12
        if self.bubble_position_y > 0:
            blit_icon_y = circle_y-10
        else:
            blit_icon_y = circle_y-8

        self.screen.blit(
            icon, (
                blit_icon_x, blit_icon_y
            )
        )
        pygame.display.update()
        return circle


class Menu(object):
    def __init__(self, screen, charakter):
        self.screen = screen
        self.charakter = charakter
        self.fonts = {
            'normal': Helfer.load_font('celtic_gaelige.ttf', 19),
            'custom': Helfer.load_font('customfont.ttf', 19)
        }

    def interaktionen(self, charakter):
        proceed = True
        while proceed:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                else:
                    # textbackground: background for all craftable values, and collectable values
                    textbackground = pygame.Rect(80, 100, 100, 600)
                    pygame.draw.rect(
                        self.screen, Farben.clsFarben.BLACK, textbackground)

                    CharakterAussehen.showAnimal(charakter, self.screen)

                    actuallevel = self.fonts['custom'].render(
                        "Level: " + str(charakter.get_level()), 0, Farben.clsFarben.WHITE)
                    self.screen.blit(actuallevel,
                                     (Koordinaten.clsKoordinaten.ACTLVLPOSX, Koordinaten.clsKoordinaten.ACTLVLPOSY))

                    craftlabel = self.fonts['custom'].render(
                        "Craftables: ", 0, Farben.clsFarben.WHITE)
                    exitlabel = self.fonts['custom'].render(
                        "Zurück", 0, Farben.clsFarben.WHITE)
                    craftbuttonx = 100
                    craftbuttony = 200
                    exitbutton = pygame.Rect(Koordinaten.clsKoordinaten.BUTTONPOSX, Koordinaten.clsKoordinaten.BUTTONPOSY,
                                             Koordinaten.clsKoordinaten.BUTTONWIDTH, Koordinaten.clsKoordinaten.BUTTONWIDTH)
                    # @andre: falsche Größe exitbutton
                    pygame.draw.rect(
                        self.screen, Farben.clsFarben.DARKRED, exitbutton)
                    self.screen.blit(craftlabel, (
                        Koordinaten.clsKoordinaten.INVCRAFTPOSX, Koordinaten.clsKoordinaten.INVCRAFTPOSY))
                    self.screen.blit(exitlabel, (
                        Koordinaten.clsKoordinaten.BUTTONPOSX, Koordinaten.clsKoordinaten.BUTTONPOSY, Koordinaten.clsKoordinaten.BUTTONWIDTH, Koordinaten.clsKoordinaten.BUTTONWIDTH))
                    # @Andre: falsche Position des Labels exitlabel
                    placePosition = Koordinaten.clsKoordinaten.INVPLACEPOS
                    placePositioncoll = 50
                    for item in Weltkarte.collectableres:
                        self.screen.blit(Weltkarte.snippets[item],
                                         (placePositioncoll, Weltkarte.MAPHEIGHT * Weltkarte.TILESIZE + 20))
                        placePositioncoll += 30
                        textObjekt = self.fonts['custom'].render(str(Weltkarte.inventory[item]), False, Farben.clsFarben.WHITE,
                                                                 Farben.clsFarben.BLACK)
                        self.screen.blit(
                            textObjekt, (placePositioncoll, Weltkarte.MAPHEIGHT * Weltkarte.TILESIZE + 20))
                        placePositioncoll += 50

                    # liste: buttons to be pressed for crafting and feeding
                    liste = [0, 0, 1, 2, 3]
                    listezwei = [0, 0, 7, 8, 9]

                    for item in Weltkarte.craftables:
                        # displaying craft snippets
                        self.screen.blit(
                            Weltkarte.snippets[item], (120, placePosition))
                        placePosition += 60
                        textObjekt = self.fonts['custom'].render(str(Weltkarte.inventory.get(item)), True, Farben.clsFarben.WHITE,
                                                                 Farben.clsFarben.BLACK)
                        self.screen.blit(textObjekt, (100, placePosition - 40))
                        placePosition += 40
                        craftinglabel = self.fonts['custom'].render(
                            "Herstellen: Drücke " + str(liste[item]), False, Farben.clsFarben.GOLD)
                        feedlabel = self.fonts['custom'].render(
                            "Füttern:  Drücke " + str(listezwei[item]), False, Farben.clsFarben.GOLD)
                        self.screen.blit(
                            craftinglabel, (craftbuttonx + 5, craftbuttony - 14))
                        self.screen.blit(
                            feedlabel, (craftbuttonx+5, craftbuttony-1))
                        craftbuttony += 100
                    if event.type == MOUSEBUTTONDOWN:
                        mousepos = event.pos
                        if exitbutton.collidepoint(mousepos):
                            proceed = False
                    if event.type == KEYDOWN:
                        for key in Weltkarte.feedcontrols:
                            if (event.key == Weltkarte.feedcontrols[key]):
                                # print(Weltkarte.feedcontrols[key])
                                # print(event.key)
                                # print(Weltkarte.inventory[key])
                                leveltoohigh = False
                                if (event.key == 55 and int(character.Character.get_level(charakter)) >= 4):
                                    leveltoohigh = True
                                    print("Level zu hoch für Wiesensnack")
                                if (event.key == 56 and int(character.Character.get_level(charakter)) >= 8):
                                    leveltoohigh = True
                                    print("Level zu hoch für Blättermischung")

                                if (Weltkarte.inventory[key] >= 1 and not leveltoohigh):
                                    Weltkarte.inventory[key] -= 1
                                    print(
                                        character.Character.get_level(charakter))
                                    character.Character.LevelUp(charakter)
                                    print(
                                        character.Character.get_level(charakter))
                        for key in Weltkarte.controls:
                            if (event.key == Weltkarte.controls[key]):
                                if key in Weltkarte.craftrecipes:
                                    canBeMade = True
                                    for i in Weltkarte.craftrecipes[key]:
                                        if Weltkarte.craftrecipes[key][i] > Weltkarte.inventory[i]:
                                            canBeMade = False
                                            break
                                    if canBeMade:
                                        for i in Weltkarte.craftrecipes[key]:
                                            Weltkarte.inventory[i] -= Weltkarte.craftrecipes[key][i]
                                            # Weltkarte.inventorycrafts[key] += 1
                                        # print(Weltkarte.inventory[key])
                                        Weltkarte.inventory[key] += 1
                                        # print(Weltkarte.inventory[key])

    def draw(self, screen, charakter):
        BG = pygame.Rect(45, 75, 500, 500)
        exitbutton = pygame.Rect(Koordinaten.clsKoordinaten.BUTTONPOSX, Koordinaten.clsKoordinaten.BUTTONPOSY,
                                 Koordinaten.clsKoordinaten.BUTTONWIDTH, Koordinaten.clsKoordinaten.BUTTONHEIGTH)
        feedbutton = pygame.Rect(Koordinaten.clsKoordinaten.FEEDBUTTONPOSX, Koordinaten.clsKoordinaten.FEEDBUTTONPOSY,
                                 Koordinaten.clsKoordinaten.BUTTONWIDTH, Koordinaten.clsKoordinaten.BUTTONHEIGTH)
        label = self.fonts['custom'].render(
            "Zurück", 1, Farben.clsFarben.WHITE)
        feedlabel = self.fonts['custom'].render(
            "Füttern", 1, Farben.clsFarben.WHITE)
        proceed = True
        while proceed:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                else:
                    pygame.draw.rect(self.screen, Farben.clsFarben.BLACK, BG)
                    pygame.draw.rect(
                        self.screen, Farben.clsFarben.DARKRED, exitbutton)
                    self.screen.blit(label, (
                        Koordinaten.clsKoordinaten.CHARSHEETPOSX, Koordinaten.clsKoordinaten.CHARSHEETPOSY))
                    pygame.draw.rect(
                        self.screen, Farben.clsFarben.DARKRED, feedbutton)
                    self.screen.blit(feedlabel, (
                        Koordinaten.clsKoordinaten.FEEDLBLPOSX, Koordinaten.clsKoordinaten.FEEDLBLPOSY))

                    CharakterAussehen.showAnimal(charakter, self.screen)

                    if event.type == MOUSEBUTTONDOWN:
                        mousepos = event.pos
                        if exitbutton.collidepoint(mousepos):
                            proceed = False
                        if feedbutton.collidepoint(mousepos):
                            self.interaktionen(charakter)

                pygame.display.update()
