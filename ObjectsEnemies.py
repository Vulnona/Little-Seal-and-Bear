import Percentages
import WorldMap
import pygame
import pyganim
import Helper
import character


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
                'bug': Helper.load_image('enemies/bug.png'),
                'bird': Helper.load_image('enemies/bird.png'),
                'sawblade': Helper.load_image('enemies/sawblade.png')
            }
        }
        self.spritesheets={
            'sealsprites': Helper.spritesheet('seal2.png'),
            'sealsprites2': Helper.spritesheet('seal.png'),
            'bearsprites': Helper.spritesheet('bear.png')
        }

    def show_Icon(self, screen):
        if self.Art == "Käfer":
            enemy_Icon=self.images['enemies']['bug']
        elif self.Art == "Vogel":
            enemy_Icon=self.images['enemies']['bird']
        elif self.Art == "Kettensägenmensch":
            enemy_Icon=self.images['enemies']['sawblade']
        enemy_Icon = pygame.transform.scale(
            enemy_Icon, (WorldMap.TILESIZE, WorldMap.TILESIZE))
        enemy_Icon_Position = self.Position
        screen.blit(
            enemy_Icon, (
                enemy_Icon_Position[0] * WorldMap.TILESIZE, enemy_Icon_Position[1] * WorldMap.TILESIZE))

    def choose_action(self, Tilemap, Player_Position, Charakter):

        currentTile = Tilemap.getTilemap()[self.Position[1]
        ][self.Position[0]]
        currentEnvironment = Tilemap.getEnvironment()[self.Position[1]
        ][self.Position[0]]
        #evaluate 'flee'

        #evaluate 'eat'
        if "fressen" in self.Verhalten:
            if currentTile == WorldMap.GRASSLAND or currentEnvironment == WorldMap.LOWGRASS or currentEnvironment == WorldMap.MOREGRASS:
                return "eat"
        if "obst" in self.Verhalten:
            if currentEnvironment==WorldMap.FRUIT1 or currentEnvironment==WorldMap.FRUIT2:
                return "eat"

        #Liste aller umliegenden Tiles# Liste aller benachbarten Tiles, keine 'negativen' Tilewerte (out of range der Map)
        Liste = []
        for tile_x in range(self.Position[0] - 1, self.Position[0] + 2):
            for tile_y in range(self.Position[1] - 1, self.Position[1] + 2):
                if tile_x >= 0 and tile_y >= 0:
                    if tile_x < WorldMap.MAPWIDTH and tile_y < WorldMap.MAPHEIGHT:
                        to_append = [tile_x, tile_y]
                        Liste.append(to_append)

        Surrounding = []
        for tile in Liste:
            tile_art = Tilemap.getTilemap()[tile[1]][tile[0]]
            if tile_art == WorldMap.GRASSLAND or tile_art == WorldMap.DIRT or tile_art == WorldMap.STONE:
                Surrounding.append(tile)

        # Possible Tiles berücksichtigt die Environment
        PossibleTiles = Surrounding[:]
        PreferedTiles = []
        for tile in Surrounding:
            tile_env = Tilemap.getEnvironment()[tile[1]][tile[0]]
            for env in WorldMap.collide:
                if env == tile_env:
                    PossibleTiles.remove(tile)
            for env in WorldMap.enterable:
                if env == tile_env:
                    PossibleTiles.remove(tile)
            if tile == Player_Position:
                if "angriff" in self.Verhalten or "feindlich" in self.Verhalten:
                    if Charakter.get_stealth_mode()==False:
                        return "attack"
                    else:
                        PossibleTiles.remove(tile)
            if tile_env == WorldMap.LOWGRASS or tile_env == WorldMap.MOREGRASS:
                if "fressen" in self.Verhalten:
                    PreferedTiles.append(tile)
            elif tile_env == WorldMap.FRUIT1 or tile_env == WorldMap.FRUIT2:
                if "obst" in self.Verhalten:
                    PreferedTiles.append(tile)

        if not PreferedTiles:
            if not PossibleTiles:
                return "stay"
            else:
                anzahl = len(PossibleTiles)
                if anzahl >1:
                    rand_int = Percentages.wuerfel(anzahl)
                    self.Position=PossibleTiles[rand_int-1]
                else:
                    self.Position=PossibleTiles[0]
                return "bewegt"
        else:
            anzahl = len(PreferedTiles)
            rand_int = Percentages.wuerfel(anzahl)
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

    # Movement
    # if act == "right":
    #    self.Position[0] += 1
    # elif act == "left":
    #    self.Position[0] -= 1
    # elif act == "down":
    #    self.Position[1] += 1
    # elif act == "up":
    #    self.Position[1] -= 1


    def Agieren(self, screen, Tilemap, Player_Direction, Player_Position, Charakter):

        #Decide action
        act=self.choose_action(Tilemap, Player_Position, Charakter)

        if act == "bewegt":
            pass
        elif act == "stay":
            pass
        elif act == "flee":
            #needs handling
            pass
        elif act == "attack":
            amount=1
            if self.Art=="Vogel":
                amount=Percentages.wuerfel(2)
            elif self.Art=="Kettensägenmensch":
                amount=Percentages.wuerfel(5)
            for i in range (amount):
                Charakter.change_status_temp('health', '-')
            if Charakter.get_status_temp('health')>0:
                self.damage_and_death_player(screen, Tilemap, "damage", Player_Direction, Player_Position, Charakter)
            else:
                self.damage_and_death_player(screen, Tilemap, "death", Player_Direction, Player_Position, Charakter)
        elif act == "eat":
            currenttile=Tilemap.getTilemap()[self.Position[1]
            ][self.Position[0]]
            currentenv=Tilemap.getEnvironment()[self.Position[1]
            ][self.Position[0]]
            if currentenv==WorldMap.MOREGRASS:
                Tilemap.getEnvironment()[self.Position[1]
                ][self.Position[0]]=WorldMap.LOWGRASS
            elif currentenv==WorldMap.LOWGRASS:
                Tilemap.getEnvironment()[self.Position[1]
                ][self.Position[0]] = WorldMap.DEADGRASS
            elif currentenv==WorldMap.FRUIT2 or currentenv==WorldMap.FRUIT1:
                Tilemap.getEnvironment()[self.Position[1]
                ][self.Position[0]] = WorldMap.NOTHING
            elif currenttile==WorldMap.GRASSLAND:
                Tilemap.getTilemap()[self.Position[1]
                ][self.Position[0]]=WorldMap.DIRT


    def init_Verhalten(self):

        if self.Art == "Käfer":
            self.add_Verhalten("fressen")
        if self.Art == "Vogel":
            self.add_Verhalten("feindlich")
            self.add_Verhalten("obst")
        if self.Art == "Kettensägenmensch":
            self.add_Verhalten("feindlich")
            self.add_Verhalten("angriff")


    def add_Verhalten(self, Verhalten):
        self.Verhalten.append(Verhalten)

    def delete_Verhalten(self, Verhalten):
        self.Verhalten.remove(Verhalten)

    def damage_and_death_player(self, screen, Tilemap, damage_or_death, player_direction, player_position, Charakter):

        Player_Environment = Tilemap.getEnvironment()[player_position[1]][player_position[0]]
        Player_Tile = Tilemap.getTilemap()[player_position[1]][player_position[0]]

        mainClock = pygame.time.Clock()
        # a x b pixels of spritesheet
        a = 576 / 12
        b = 384 / 8
        if (isinstance(Charakter.get_Type(), character.animaltypes.clsBaer)):
            player_Sprite = self.spritesheets['bearsprites']
            if (isinstance(Charakter.get_Subtype(), character.animalsubtypes.White)):
                amod = 3
                bmod = 0
            elif (isinstance(Charakter.get_Subtype(), character.animalsubtypes.Grey)):
                amod = 3
                bmod = 4
            elif (isinstance(Charakter.get_Subtype(), character.animalsubtypes.Brown)):
                amod = 0
                bmod = 4
            if player_direction == "right":
                player_Icon = player_Sprite.image_at((a * amod, b * (bmod + 2), a, b), colorkey=(0, 0, 0))
            elif player_direction == "left":
                player_Icon = player_Sprite.image_at((a * amod, b * (bmod + 1), a, b), colorkey=(0, 0, 0))
            elif player_direction == "up":
                player_Icon = player_Sprite.image_at((a * amod, b * (bmod + 3), a, b), colorkey=(0, 0, 0))
            else:
                player_Icon = player_Sprite.image_at((a * amod, b * (bmod + 0), a, b), colorkey=(0, 0, 0))
        elif (isinstance(Charakter.get_Type(), character.animaltypes.clsRobbe)):
            player_Sprite = self.spritesheets['sealsprites']
            if (isinstance(Charakter.get_Subtype(), character.animalsubtypes.White)):
                amod = 0
                bmod = 0
            elif (isinstance(Charakter.get_Subtype(), character.animalsubtypes.Grey)):
                player_Sprite = self.spritesheets['sealsprites2']
                amod = 0
                bmod = 0
            elif (isinstance(Charakter.get_Subtype(), character.animalsubtypes.Brown)):
                amod = 0
                bmod = 4
            if player_direction == "right":
                player_Icon = player_Sprite.image_at((a * amod, b * (bmod + 2), a, b), colorkey=(0, 0, 0))
            elif player_direction == "left":
                player_Icon = player_Sprite.image_at((a * amod, b * (bmod + 1), a, b), colorkey=(0, 0, 0))
            elif player_direction == "up":
                player_Icon = player_Sprite.image_at((a * amod, b * (bmod + 3), a, b), colorkey=(0, 0, 0))
            else:
                player_Icon = player_Sprite.image_at((a * amod, b * (bmod + 0), a, b), colorkey=(0, 0, 0))
        player_Icon = pygame.transform.scale(player_Icon, (WorldMap.TILESIZE, WorldMap.TILESIZE))
        tiles_Sprite = Helper.spritesheet('tileset_32_32.png')
        if Player_Tile == WorldMap.GRASSLAND:
            second = tiles_Sprite.image_at((193, 5505, 30, 30), colorkey=(0, 0, 0))
        elif Player_Tile == WorldMap.STONE:
            second = tiles_Sprite.image_at((33, 8577, 30, 30), colorkey=(0, 0, 0))
        elif Player_Tile == WorldMap.DIRT:
            second = tiles_Sprite.image_at((15, 2545, 64, 64), colorkey=(0, 0, 0))
        elif Player_Tile == WorldMap.WATER:
            second = tiles_Sprite.image_at((26, 4701, 45, 45), colorkey=(0, 0, 0))
        second = pygame.transform.scale(
            second, (WorldMap.TILESIZE, WorldMap.TILESIZE))
        third = WorldMap.environment[Player_Environment]
        deathAnim = pyganim.PygAnimation([(player_Icon, 10), (second, 10), (third, 10)])
        i = 0
        if damage_or_death == "damage":
            m = 10
        elif damage_or_death == "death":
            m = 40

        deathAnim.play()

        for i in range(m):
            deathAnim.blit(
                screen, (player_position[0] * WorldMap.TILESIZE, player_position[1] * WorldMap.TILESIZE))
            pygame.display.update()
            mainClock.tick(30)
            i -= 1
        if damage_or_death == "death":
            screen.blit(
                second, (player_position[0] * WorldMap.TILESIZE, player_position[1] * WorldMap.TILESIZE))
            screen.blit(
                third, (player_position[0] * WorldMap.TILESIZE, player_position[1] * WorldMap.TILESIZE))
        elif damage_or_death == "damage":
            screen.blit(
                third, (player_position[0] * WorldMap.TILESIZE, player_position[1] * WorldMap.TILESIZE))
            screen.blit(
                player_Icon, (player_position[0] * WorldMap.TILESIZE, player_position[1] * WorldMap.TILESIZE))

    def damage_and_death_anim(self, screen, damage_or_death, enemy_tile_Art, enemy_environment=WorldMap.NOTHING):
        mainClock = pygame.time.Clock()
        if self.Art == "Käfer":
            first = Helper.load_image('enemies/bug.png')
        if self.Art == "Vogel":
            first = Helper.load_image('enemies/bird.png')
        if self.Art == "Kettensägenmensch":
            first = Helper.load_image('enemies/sawblade.png')
        first = pygame.transform.scale(
            first, (WorldMap.TILESIZE, WorldMap.TILESIZE))

        tiles_Sprite = Helper.spritesheet('tileset_32_32.png')
        if enemy_tile_Art == WorldMap.GRASSLAND:
            second = tiles_Sprite.image_at((193, 5505, 30, 30), colorkey=(0, 0, 0))
        elif enemy_tile_Art == WorldMap.STONE:
            second = tiles_Sprite.image_at((33, 8577, 30, 30), colorkey=(0,0,0))
        elif enemy_tile_Art == WorldMap.DIRT:
            second = tiles_Sprite.image_at((15, 2545, 64, 64), colorkey=(0,0,0))
        elif enemy_tile_Art == WorldMap.WATER:
            second = tiles_Sprite.image_at((26, 4701, 45, 45), colorkey=(0,0,0))
        second = pygame.transform.scale(
            second, (WorldMap.TILESIZE, WorldMap.TILESIZE))
        third = WorldMap.environment[enemy_environment]
        deathAnim = pyganim.PygAnimation([(first, 10), (second, 10), (third, 10)])
        i = 0
        if damage_or_death == "damage":
            m = 10
        elif damage_or_death == "death":
            m = 40

        deathAnim.play()

        for i in range(m):
            deathAnim.blit(
                screen, (self.Position[0] * WorldMap.TILESIZE, self.Position[1] * WorldMap.TILESIZE))
            pygame.display.update()
            mainClock.tick(30)
            i -= 1
        if damage_or_death == "death":
            screen.blit(
                second, (self.Position[0] * WorldMap.TILESIZE, self.Position[1] * WorldMap.TILESIZE))
            screen.blit(
                third, (self.Position[0] * WorldMap.TILESIZE, self.Position[1] * WorldMap.TILESIZE))
        elif damage_or_death == "damage":
            screen.blit(
                third, (self.Position[0] * WorldMap.TILESIZE, self.Position[1] * WorldMap.TILESIZE))
            screen.blit(
                first, (self.Position[0] * WorldMap.TILESIZE, self.Position[1] * WorldMap.TILESIZE))

    def generate_Enemy(self, Tilemap):
        rand_int = Percentages.wuerfel(10)
        if rand_int <= 5:
            Art = "Käfer"
            healthmodifier=Percentages.wuerfel(6)
            Gesundheit = 5+healthmodifier
        elif (rand_int >= 5 and rand_int <= 9):
            Art = "Vogel"
            healthmodifier=Percentages.wuerfel(12)
            Gesundheit = 10+healthmodifier
        elif rand_int == 10:
            Art = "Kettensägenmensch"
            healthmodifier=Percentages.wuerfel(30)
            Gesundheit = 30+healthmodifier

        Position=self.generatePosition()
        # Can just spawn on Dirt, Grassland and Stone:
        acceptableValue=False
        while not acceptableValue:
            if Tilemap.getTilemap()[Position[1]][Position[0]]== WorldMap.STONE or Tilemap.getTilemap()[Position[1]][Position[0]] == WorldMap.GRASSLAND\
                    or Tilemap.getTilemap()[Position[1]][Position[0]]== WorldMap.DIRT:
                acceptableValue=True
            else:
                Position=self.generatePosition()

        enemy = cls_Enemy(Art, Gesundheit, Position)
        return enemy

    def generatePosition(self):
        # Can't spawn at [0,0], starting with '1'
        Position = [int((Percentages.wuerfel(WorldMap.MAPWIDTH - 1))),
                    int((Percentages.wuerfel(WorldMap.MAPHEIGHT - 1)))]
        return Position

    def __del__(self):
        pass

    def lower_Gesundheit(self, Anzahl):
        self.Gesundheit -= Anzahl


class cls_Enemies(object):

    def __init__(self, Enemies=[]):
        self.enemies = Enemies

    def fill_Enemies_list(self, Tilemap):
        # Max Enemies: 6
        rand_int = Percentages.wuerfel(Wuerfelseiten=5)
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
