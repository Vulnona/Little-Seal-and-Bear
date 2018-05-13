import Wahrscheinlichkeiten
import Weltkarte
import pygame
import pyganim
import Helfer


class cls_Enemy(object):

    def __init__(self, Art="Unbekannt", Gesundheit=1, Position=[0, 0]):
        self.Art = Art
        self.Gesundheit = Gesundheit
        self.Position = Position
        self.Verhalten = []
        self.init_Verhalten()
        self._load_images()

    def _load_images(self):
        self.images={
            'enemies': {
                'bug': Helfer.load_image('enemies/bug.png'),
                'bird': Helfer.load_image('enemies/bird.png'),
                'sawblade': Helfer.load_image('enemies/sawblade.png')
            }
        }

    def show_Icon(self, screen):
        if self.Art == "Käfer":
            enemy_Icon=self.images['enemies']['bug']
        elif self.Art == "Vogel":
            enemy_Icon=self.images['enemies']['bird']
        elif self.Art == "Kettensägenmensch":
            enemy_Icon=self.images['enemies']['sawblade']
        enemy_Icon = pygame.transform.scale(
            enemy_Icon, (Weltkarte.TILESIZE, Weltkarte.TILESIZE))
        enemy_Icon_Position = self.Position
        screen.blit(
            enemy_Icon, (
                enemy_Icon_Position[0] * Weltkarte.TILESIZE, enemy_Icon_Position[1] * Weltkarte.TILESIZE))

    def choose_action(self, Tilemap, Player_Position):
        PossibleAction=["right", "left", "up", "down", "stay", "attack", "eat"] #right, left, up, down, stay, fight
        #eat_value=0
        stay_value=0
        #attack_value=0

        currentTile = Tilemap.getTilemap()[self.Position[1]
        ][self.Position[0]]
        currentEnvironment = Tilemap.getEnvironment()[self.Position[1]
        ][self.Position[0]]

        #evaluate 'eat'
        if "fressen" in self.Verhalten:
            if currentTile == Weltkarte.GRASSLAND or currentEnvironment == Weltkarte.LOWGRASS or currentEnvironment == Weltkarte.MOREGRASS:
                if currentTile==Weltkarte.GRASSLAND:
                    return "eat"
                if currentEnvironment == Weltkarte.LOWGRASS:
                    return "eat"
                if currentEnvironment == Weltkarte.MOREGRASS:
                    return "eat"
            else:
                #eat_value=-1
                PossibleAction.remove("eat")
        if "obst" in self.Verhalten:
            if currentEnvironment==Weltkarte.FRUIT1 or currentEnvironment==Weltkarte.FRUIT2:
                return "eat"
            else:
                #eat_value=-1
                PossibleAction.remove("eat")

        #Liste aller umliegenden Tiles# Liste aller benachbarten Tiles, keine 'negativen' Tilewerte (out of range der Map)
        Liste = []
        for tile_x in range(self.Position[0] - 1, self.Position[0] + 2):
            for tile_y in range(self.Position[1] - 1, self.Position[1] + 2):
                if tile_x >= 0 and tile_y >= 0:
                    if tile_x < Weltkarte.MAPWIDTH and tile_y < Weltkarte.MAPHEIGHT:
                        to_append = [tile_x, tile_y]
                        Liste.append(to_append)

        Surrounding = []
        for tile in Liste:
            tile_art = Tilemap.getTilemap()[tile[1]][tile[0]]
            if tile_art == Weltkarte.GRASSLAND or tile_art == Weltkarte.DIRT or tile_art == Weltkarte.STONE:
                Surrounding.append(tile)

        # Possible Tiles berücksichtigt die Environment
        PossibleTiles = Surrounding[:]
        PreferedTiles = []
        for tile in Surrounding:
            tile_env = Tilemap.getEnvironment()[tile[1]][tile[0]]
            print(tile_env)
            for env in Weltkarte.collide:
                if env == tile_env:
                    PossibleTiles.remove(tile)
            for env in Weltkarte.enterable:
                if env == tile_env:
                    PossibleTiles.remove(tile)
            if tile == Player_Position:
                if "angriff" in self.Verhalten:
                    #attack_value+=90
                    print('attack act')
                    return "attack"
                if "feindlich" in self.Verhalten:
                    #attack_value+=55
                    print('attack act')
                    return "attack"
                else:
                    attack_value=1
            if tile_env == Weltkarte.LOWGRASS or tile_env == Weltkarte.MOREGRASS:
                if "fressen" in self.Verhalten:
                    PreferedTiles.append(tile)
            elif tile_env == Weltkarte.FRUIT1 or tile_env == Weltkarte.FRUIT2:
                if "obst" in self.Verhalten:
                    PreferedTiles.append(tile)


        print('possible tiles:')
        print(PossibleTiles)
        print('prefered tiles:')
        print(PreferedTiles)
        #print(attack_value)

        if not PreferedTiles:
            if not PossibleTiles:
                return "stay"
            else:
                print('chosen: possible list')
                anzahl = len(PossibleTiles)
                if anzahl >1:
                    rand_int = Wahrscheinlichkeiten.wuerfel(anzahl)
                    self.Position=PossibleTiles[rand_int-1]
                else:
                    self.Position=PossibleTiles[0]
                return "bewegt"
        else:
            print('chosen: prefered list')
            anzahl = len(PreferedTiles)
            rand_int = Wahrscheinlichkeiten.wuerfel(anzahl)
            self.Position=PreferedTiles[rand_int-1]
            return "bewegt"


        #action = "down"
        #return action
        # Spieler steht auf einem Feld, auf dem er angegriffen werden kann und befindet sich in Reichweite

        #evaluate 'right'
        #right_value = 0
        #nextTile = Tilemap.getTilemap()[self.Position[1]
        #][self.Position[0] + 1]
        #nextEnvironment = Tilemap.getEnvironment()[self.Position[1]
        #][self.Position[0] + 1]
        #if self.Position < Weltkarte.MAPWIDTH - 1:
        #    right_value = -1
        #for env in Weltkarte.collide:
        #    if env == nextEnvironment:
        #        right_value = -1
        #for env in Weltkarte.enterable:
        #    if env == nextEnvironment:
        #        right_value = -1
        #for tile in Weltkarte.waterbehaviour:
        #    # Enemy ist bereits im Wasser:
        #    if currentTile == tile:
        #        if nextTile == Weltkarte.GRASSLAND or Weltkarte.DIRT or Weltkarte.STONE:
        #            right_value = 99
        #        else:
        #            right_value = 50
        #        break
        #    else:
        #        if nextTile == tile:
        #            right_value = -1
        #keine Ausschlusskriterien zugetroffen:
        #if right_value >= 0:
        #    if "fressen" in self.Verhalten:
        #        if nextTile == Weltkarte.GRASSLAND or nextEnvironment == Weltkarte.LOWGRASS or nextEnvironment == Weltkarte.MOREGRASS:
        #            right_value += 49
        #        else:
         #           right_value += 0
          #  if "obst" in self.Verhalten:
           #     Obst_Liste=[]
            #    for row in range(Weltkarte.MAPHEIGHT):
             #       for column in range(Weltkarte.MAPWIDTH):
              #          if Tilemap.getEnvironment[row][column]==Weltkarte.MOREGRASS:
               #             Koordinaten=[row][column]
                #            Obst_Liste.append(Koordinaten)
                ##kein 'Obst' auf der Map
                #if not Obst_Liste:
                 #   right_value += 25
                #else:
                #Vergleich Liste: self.Position mit gespeicherten Koordinaten
                  #  Diff=[]
                 #   for obst in Obst_Liste:
                   #     if self.Position[0]>obst[0]:
                    #        xdiff = self.Position[0]-obst[0]
                     #       if self.Position[1]>obst[1]:
                      #          ydiff = self.Position[1]-obst[1]
                       #     else:
                        #        ydiff = obst[1] - self.Position[1]
                        #else:
                         #   xdiff = obst[0]-self.Position[0]
                          #  if self.Position[1]>obst[1]:
                           #     ydiff = self.Position[1]-obst[1]
                            #else:
                             #   ydiff = obst[1] - self.Position[1]
                        #diff=[xdiff, ydiff]
                        #Diff.append(diff)

                   # print(sorted(Diff))
                   # Diff = sorted(Diff)
                   # destination = Diff[0] #lowest value
                   # print(destination)
                    #if (destination[0] destination[0]+=1):
                    #    pass

        #else:
         #   PossibleAction.remove("r")


        #evaluate 'left'
        #nextTile = Tilemap.getTilemap()[self.Position[1]
        #][self.Position[0] - 1]
        #nextEnvironment = Tilemap.getEnvironment()[self.Position[1]
        #][self.Position[0] - 1]

        #evaluate 'down'
        #nextTile = Tilemap.getTilemap()[self.Position[1] + 1
        #                                ][self.Position[0]]
        #nextEnvironment = Tilemap.getEnvironment()[self.Position[1] + 1
        #                                           ][self.Position[0]]

        #evaluate 'up':
        #nextTile = Tilemap.getTilemap()[self.Position[1] - 1
        #                                ][self.Position[0]]
        #nextEnvironment = Tilemap.getEnvironment()[self.Position[1] - 1
        #                                           ][self.Position[0]]



    def Agieren(self, Tilemap, Player_Position):

        #Decide action
        act=self.choose_action(Tilemap, Player_Position)

        #Movement
        #if act == "right":
        #    self.Position[0] += 1
        #elif act == "left":
        #    self.Position[0] -= 1
        #elif act == "down":
        #    self.Position[1] += 1
        #elif act == "up":
        #    self.Position[1] -= 1
        if act == "bewegt":
            pass
        elif act == "stay":
            pass
        elif act == "attack":
            pass
        elif act == "eat":
            currenttile=Tilemap.getTilemap()[self.Position[1]
            ][self.Position[0]]
            currentenv=Tilemap.getEnvironment()[self.Position[1]
            ][self.Position[0]]
            if currentenv==Weltkarte.MOREGRASS:
                Tilemap.getEnvironment()[self.Position[1]
                ][self.Position[0]]=Weltkarte.LOWGRASS
            elif currentenv==Weltkarte.LOWGRASS:
                Tilemap.getEnvironment()[self.Position[1]
                ][self.Position[0]] = Weltkarte.DEADGRASS
            elif currentenv==Weltkarte.FRUIT2 or currentenv==Weltkarte.FRUIT1:
                Tilemap.getEnvironment()[self.Position[1]
                ][self.Position[0]] = Weltkarte.NOTHING
            elif currenttile==Weltkarte.GRASSLAND:
                Tilemap.getTilemap()[self.Position[1]
                ][self.Position[0]]=Weltkarte.DIRT


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

    def damage_and_death_anim(self, screen, damage_or_death, enemy_tile_Art, enemy_environment=Weltkarte.NOTHING):
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

        third = Weltkarte.environment[enemy_environment]

        deathAnim = pyganim.PygAnimation([(first, 10), (second, 10), (third, 10)])
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
        screen.blit(
            third, (self.Position[0] * Weltkarte.TILESIZE, self.Position[1] * Weltkarte.TILESIZE))

    def generate_Enemy(self, Tilemap):
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

        Position=self.generatePosition()
        # Can just spawn on Dirt, Grassland and Stone:
        acceptableValue=False
        while not acceptableValue:
            if Tilemap.getTilemap()[Position[1]][Position[0]]== Weltkarte.STONE or Tilemap.getTilemap()[Position[1]][Position[0]] == Weltkarte.GRASSLAND\
                    or Tilemap.getTilemap()[Position[1]][Position[0]]== Weltkarte.DIRT:
                acceptableValue=True
            else:
                Position=self.generatePosition()

        enemy = cls_Enemy(Art, Gesundheit, Position)
        return enemy

    def generatePosition(self):
        # Can't spawn at [0,0], starting with '1'
        Position = [int((Wahrscheinlichkeiten.wuerfel(Weltkarte.MAPWIDTH - 1))),
                    int((Wahrscheinlichkeiten.wuerfel(Weltkarte.MAPHEIGHT - 1)))]
        return Position

    def __del__(self):
        print('deleted')

    def lower_Gesundheit(self, Anzahl):
        self.Gesundheit -= Anzahl

    def change_Position(self):
        pass


class cls_Enemies(object):

    def __init__(self, Enemies=[]):
        self.enemies = Enemies

    def fill_Enemies_list(self, Tilemap):
        # Max Enemies: 6
        rand_int = Wahrscheinlichkeiten.wuerfel(Wuerfelseiten=5)
        start_int = 0
        while rand_int >= start_int:
            new_enemy = cls_Enemy()
            self.enemies.append(new_enemy.generate_Enemy(Tilemap))
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
