import Wahrscheinlichkeiten
import Weltkarte
import pygame
import pyganim
import Helfer

GRASS = 0
HIGHGRASS = 1
DIRT = 5
WATER = 6


class cls_Enemy(object):

    def __init__(self, Art="Unbekannt", Gesundheit=1, Position=[0, 0]):
        self.Art = Art
        self.Gesundheit = Gesundheit
        self.Position = Position
        self.Verhalten = []
        self.init_Verhalten()

    def init_Verhalten(self):
        self.add_Verhalten("feindlich")
        if self.Art == "Käfer":
            self.add_Verhalten("fressen")
        if self.Art == "Vogel":
            self.add_Verhalten("obst")
        if self.Art == "Kettensägenmensch":
            self.add_Verhalten("angriff")

    def add_Verhalten(self, Verhalten):
        self.Verhalten.append(Verhalten)

    def damage_and_death_anim(self, screen, damage_or_death, enemy_tile_Art):
        mainClock = pygame.time.Clock()
        if self.Art == "Käfer":
            first = Helfer.load_image('enemies/bug.png')
        if self.Art == "Vogel":
            first = Helfer.load_image('enemies/bird.png')
        if self.Art == "Kettensägenmensch":
            first = Helfer.load_image('enemies/sawblade.png')
        first = pygame.transform.scale(
            first, (Weltkarte.TILESIZE, Weltkarte.TILESIZE))

        tiles_Sprite = Helfer.spritesheet('tileset_32_32.png')
        if enemy_tile_Art == Weltkarte.GRASSLAND:
            second = tiles_Sprite.image_at((193, 5505, 30, 30), colorkey=(0, 0, 0))
        elif enemy_tile_Art == Weltkarte.STONE:
            second = tiles_Sprite.image_at((33, 8577, 30, 30), colorkey=(0,0,0))
        elif enemy_tile_Art == Weltkarte.DIRT:
            second = tiles_Sprite.image_at((15, 2545, 64, 64), colorkey=(0,0,0))
        elif enemy_tile_Art == Weltkarte.WATER:
            second = tiles_Sprite.image_at((26, 4701, 45, 45), colorkey=(0,0,0))
        second = pygame.transform.scale(
            second, (Weltkarte.TILESIZE, Weltkarte.TILESIZE))

        deathAnim = pyganim.PygAnimation([(first, 10), (second, 10)])
        i = 0
        if damage_or_death == "damage":
            m = 10
        elif damage_or_death == "death":
            m = 40

        deathAnim.play()

        for i in range(m):
            deathAnim.blit(
                screen, (self.Position[0]*Weltkarte.TILESIZE, self.Position[1]*Weltkarte.TILESIZE))
            pygame.display.update()
            mainClock.tick(30)
            i -= 1

        if damage_or_death == "death":
            screen.blit(
                second, (self.Position[0]*Weltkarte.TILESIZE, self.Position[1]*Weltkarte.TILESIZE))
        elif damage_or_death == "damage":
            screen.blit(
                first, (self.Position[0] * Weltkarte.TILESIZE, self.Position[1] * Weltkarte.TILESIZE))

    def generate_Enemy(self):
        rand_int = Wahrscheinlichkeiten.wuerfel(10)
        if rand_int <= 5:
            Art = "Käfer"  # für später: Frisst Gras weg
            Gesundheit = 2
        elif (rand_int >= 5 and rand_int <= 9):
            Art = "Vogel"  # für später: frisst Äpfel/Gesundheitsboni weg
            Gesundheit = 5
        elif rand_int == 10:
            Art = "Kettensägenmensch"
            Gesundheit = 10
        # Can't spawn at [0,0], starting with '1'
        Position = [int((Wahrscheinlichkeiten.wuerfel(Weltkarte.MAPWIDTH-1))),
                    int((Wahrscheinlichkeiten.wuerfel(Weltkarte.MAPHEIGHT-1)))]

        enemy = cls_Enemy(Art, Gesundheit, Position)
        return enemy

    def __del__(self):
        print('deleted')

    def lower_Gesundheit(self, Anzahl):
        self.Gesundheit -= Anzahl

    def change_Position(self):
        pass


class cls_Enemies(object):

    def __init__(self, Enemies=[]):
        self.enemies = Enemies

    def fill_Enemies_list(self):
        # Max Enemies: 6
        rand_int = Wahrscheinlichkeiten.wuerfel(Wuerfelseiten=5)
        start_int = 0
        while rand_int >= start_int:
            new_enemy = cls_Enemy()
            self.enemies.append(new_enemy.generate_Enemy())
            rand_int -= 1

    def delete_from_list(self, input_enemy):
        for enemy in range(0, self.get_Enemies_Anzahl()):
            an_enemy = self.get_Enemy(enemy)
            if an_enemy == input_enemy:
                self.enemies.remove(an_enemy)
                break

    def get_Enemies_Liste(self):
        return self.enemies

    def get_Enemies_Anzahl(self):
        return len(self.enemies)

    def get_Enemy(self, Zahl):
        return self.enemies[Zahl]
