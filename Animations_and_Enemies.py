import Percentages
import World_Map
import pygame
import pyganim
import Helper
import character


class clsIconShowing(object):
    def __init__(self, window, Character):
        self.window = window
        self.Character = Character
        self._load_spritesheets()

    def _load_spritesheets(self):
        self.spritesheets = {
            'sealsprites': Helper.spritesheet('seal2.png'),
            'sealsprites2': Helper.spritesheet('seal.png'),
            'bearsprites': Helper.spritesheet('bear.png')
        }

    def draw(self, direction, player_Icon_Position):
        # a x b pixels of spritesheet
        a = 576 / 12
        b = 384 / 8
        if (isinstance(self.Character.get_Type(), character.animaltypes.clsBaer)):
            self.player_Sprite = self.spritesheets['bearsprites']
            if (isinstance(self.Character.get_Subtype(), character.animalsubtypes.White)):
                amod = 3
                bmod = 0
            elif (isinstance(self.Character.get_Subtype(), character.animalsubtypes.Grey)):
                amod = 3
                bmod = 4
            elif (isinstance(self.Character.get_Subtype(), character.animalsubtypes.Brown)):
                amod = 0
                bmod = 4
            if direction == "right":
                player_Icon = self.player_Sprite.image_at((a * amod, b * (bmod + 2), a, b), colorkey=(0, 0, 0))
            elif direction == "left":
                player_Icon = self.player_Sprite.image_at((a * amod, b * (bmod + 1), a, b), colorkey=(0, 0, 0))
            elif direction == "up":
                player_Icon = self.player_Sprite.image_at((a * amod, b * (bmod + 3), a, b), colorkey=(0, 0, 0))
            else:
                player_Icon = self.player_Sprite.image_at((a * amod, b * (bmod + 0), a, b), colorkey=(0, 0, 0))

            self.sprites_bear_right = []
            sprite_pos = 0
            for sprite_pos in range(3):
                bear_right = ((a * amod) + (sprite_pos * a), b * (bmod + 2), a, b)
                self.sprites_bear_right.append((bear_right))

            self.sprites_bear_left = []
            sprite_pos = 0
            for sprite_pos in range(3):
                bear_left = ((a * amod) + (sprite_pos * a), b * (bmod + 1), a, b)
                self.sprites_bear_left.append((bear_left))

            self.sprites_bear_up = []
            sprite_pos = 0
            for sprite_pos in range(3):
                bear_up = ((a * amod) + (sprite_pos * a), b * (bmod + 3), a, b)
                self.sprites_bear_up.append((bear_up))

            self.sprites_bear_down = []
            sprite_pos = 0
            for sprite_pos in range(3):
                bear_down = ((a * amod) + (sprite_pos * a), b * (bmod + 0), a, b)
                self.sprites_bear_down.append((bear_down))


        elif (isinstance(self.Character.get_Type(), character.animaltypes.clsRobbe)):
            self.player_Sprite = self.spritesheets['sealsprites']
            if (isinstance(self.Character.get_Subtype(), character.animalsubtypes.White)):
                amod = 0
                bmod = 0
            elif (isinstance(self.Character.get_Subtype(), character.animalsubtypes.Grey)):
                self.player_Sprite = self.spritesheets['sealsprites2']
                amod = 0
                bmod = 0
            elif (isinstance(self.Character.get_Subtype(), character.animalsubtypes.Brown)):
                amod = 0
                bmod = 4
            if direction == "right":
                player_Icon = self.player_Sprite.image_at((a * amod, b * (bmod + 2), a, b), colorkey=(0, 0, 0))
            elif direction == "left":
                player_Icon = self.player_Sprite.image_at((a * amod, b * (bmod + 1), a, b), colorkey=(0, 0, 0))
            elif direction == "up":
                player_Icon = self.player_Sprite.image_at((a * amod, b * (bmod + 3), a, b), colorkey=(0, 0, 0))
            else:
                player_Icon = self.player_Sprite.image_at((a * amod, b * (bmod + 0), a, b), colorkey=(0, 0, 0))

            self.sprites_seal_right = []
            sprite_pos = 0
            for sprite_pos in range(3):
                seal_right = (a * amod + (sprite_pos * a), b * (bmod + 2), a, b)
                self.sprites_seal_right.append((seal_right))

            self.sprites_seal_left = []
            sprite_pos = 0
            for sprite_pos in range(3):
                seal_left = (a * amod + (sprite_pos * a), b * (bmod + 1), a, b)
                self.sprites_seal_left.append((seal_left))

            self.sprites_seal_down = []
            sprite_pos = 0
            for sprite_pos in range(3):
                seal_down = (a * amod + (sprite_pos * a), b * (bmod + 0), a, b)
                self.sprites_seal_down.append((seal_down))

            self.sprites_seal_up = []
            sprite_pos = 0
            for sprite_pos in range(3):
                seal_up = (a * amod + (sprite_pos * a), b * (bmod + 3), a, b)
                self.sprites_seal_up.append((seal_up))
        player_Icon = pygame.transform.scale(player_Icon, (37, 37))

        self.window.blit(
            player_Icon, (
                player_Icon_Position[0] * World_Map.TILESIZE,
                (player_Icon_Position[1] * World_Map.TILESIZE)))


    def get_walk_Images(self, direction):
        if direction == 'right':
            if (isinstance(self.Character.get_Type(), character.animaltypes.clsBaer)):
                images = self.player_Sprite.images_at(
                    rects=self.sprites_bear_right, colorkey=[0, 0, 0])
            elif (isinstance(self.Character.get_Type(), character.animaltypes.clsRobbe)):
                images = self.player_Sprite.images_at(
                    rects=self.sprites_seal_right, colorkey=[0, 0, 0])
        elif direction == 'left':
            if (isinstance(self.Character.get_Type(), character.animaltypes.clsBaer)):
                images = self.player_Sprite.images_at(
                    rects=self.sprites_bear_left, colorkey=[0, 0, 0])
            elif (isinstance(self.Character.get_Type(), character.animaltypes.clsRobbe)):
                images = self.player_Sprite.images_at(
                    rects=self.sprites_seal_left, colorkey=[0, 0, 0])
        elif direction == 'down':
            if (isinstance(self.Character.get_Type(), character.animaltypes.clsBaer)):
                images = self.player_Sprite.images_at(
                    rects=self.sprites_bear_down, colorkey=[0, 0, 0])
            elif (isinstance(self.Character.get_Type(), character.animaltypes.clsRobbe)):
                images = self.player_Sprite.images_at(
                    rects=self.sprites_seal_down, colorkey=[0, 0, 0])
        elif direction == 'up':
            if (isinstance(self.Character.get_Type(), character.animaltypes.clsBaer)):
                images = self.player_Sprite.images_at(
                    rects=self.sprites_bear_up, colorkey=[0, 0, 0])
            elif (isinstance(self.Character.get_Type(), character.animaltypes.clsRobbe)):
                images = self.player_Sprite.images_at(
                    rects=self.sprites_seal_up, colorkey=[0, 0, 0])

        return images

class clsAnimation(object):
    def __init__(self, screen, player_position):
        self.screen = screen
        self._load_spritesheets()
        self.player_position = player_position

    def _load_spritesheets(self):
        self.spritesheets={
            'stealth': Helper.spritesheet('smokeSpritesheet.png'),
            'savers': Helper.spritesheet('shield.png'),
            'plant': Helper.spritesheet('planting.png'),
            'heal': Helper.spritesheet('heal.png')
        }


    def magic_Anim(self, magic, Tilemap = None):

        if magic == 'stealth':
            self.stealth_Anim()

        elif magic == 'savers':
            self.savers_Anim()

        elif magic == 'heal':
            self.heal_Anim()

        elif magic == 'plant':
            self.plant_Anim(Tilemap)

    def stealth_Anim(self):
        i1 = self.spritesheets['stealth'].image_at((0, 0, 231, 263), colorkey=(0,0,0))
        i2 = self.spritesheets['stealth'].image_at((249, 0, 231, 263), colorkey=(0, 0, 0))
        i3 = self.spritesheets['stealth'].image_at((509, 0, 231, 263), colorkey=(0, 0, 0))
        i4 = self.spritesheets['stealth'].image_at((770, 0, 231, 263), colorkey=(0, 0, 0))
        i5 = self.spritesheets['stealth'].image_at((1021, 0, 231, 263), colorkey=(0, 0, 0))
        i6 = self.spritesheets['stealth'].image_at((1280, 0, 231, 263), colorkey=(0, 0, 0))
        i7 = self.spritesheets['stealth'].image_at((0, 270, 231, 263), colorkey=(0, 0, 0))
        i8 = self.spritesheets['stealth'].image_at((249, 270, 231, 263), colorkey=(0, 0, 0))
        i9 = self.spritesheets['stealth'].image_at((509, 270, 231, 263), colorkey=(0, 0, 0))
        i10 = self.spritesheets['stealth'].image_at((770, 270, 231, 263), colorkey=(0, 0, 0))
        i11 = self.spritesheets['stealth'].image_at((1021, 270, 231, 263), colorkey=(0, 0, 0))
        i12 = self.spritesheets['stealth'].image_at((1280, 270, 231, 263), colorkey=(0, 0, 0))

        mainClock = pygame.time.Clock()
        stealthAnimation = pyganim.PygAnimation([(i1, 10), (i2, 10), (i3, 10), (i4, 10), (i5, 10), (i6, 10),
                                                   # (i7, 10), (i8, 10), (i9, 10), (i10, 10), (i11, 10),
                                                 (i12, 10)])
                                                    #, (i11, 10), (i10, 10), (i9, 10)
                                                    #, (i8, 10), (i7, 10), (i6, 10), (i5, 10), (i4, 10)
                                                    #, (i3, 10), (i2, 10)])
        stealthAnimation.scale((World_Map.TILESIZE, World_Map.TILESIZE))
        stealthAnimation.play()

        for i in range(10):
            stealthAnimation.blit(
                self.screen, (self.player_position[0] * World_Map.TILESIZE, self.player_position[1] * World_Map.TILESIZE))
            pygame.display.update()
            mainClock.tick(30)
            i -= 1

    def savers_Anim(self):
        i1 = self.spritesheets['savers'].image_at((0, 0, 192, 192), colorkey=(0, 0, 0))
        i2 = self.spritesheets['savers'].image_at((192, 0, 192, 192), colorkey=(0, 0, 0))
        i3 = self.spritesheets['savers'].image_at((384, 0, 192, 192), colorkey=(0, 0, 0))
        i4 = self.spritesheets['savers'].image_at((576, 0, 192, 192), colorkey=(0, 0, 0))
        i5 = self.spritesheets['savers'].image_at((771, 0, 192, 192), colorkey=(0, 0, 0))
        i6 = self.spritesheets['savers'].image_at((0, 192, 192, 192), colorkey=(0, 0, 0))
        i7 = self.spritesheets['savers'].image_at((192, 192, 192, 192), colorkey=(0, 0, 0))
        i8 = self.spritesheets['savers'].image_at((384, 192, 192, 192), colorkey=(0, 0, 0))
        i9 = self.spritesheets['savers'].image_at((576, 192, 192, 192), colorkey=(0, 0, 0))
        i10 = self.spritesheets['savers'].image_at((771, 192, 192, 192), colorkey=(0, 0, 0))
        i11 = self.spritesheets['savers'].image_at((0, 384, 192, 192), colorkey=(0, 0, 0))
        i12 = self.spritesheets['savers'].image_at((192, 384, 192, 192), colorkey=(0, 0, 0))
        i13 = self.spritesheets['savers'].image_at((384, 384, 192, 192), colorkey=(0, 0, 0))
        i14 = self.spritesheets['savers'].image_at((576, 384, 192, 192), colorkey=(0, 0, 0))
        i15 = self.spritesheets['savers'].image_at((771, 384, 192, 192), colorkey=(0, 0, 0))
        i16 = self.spritesheets['savers'].image_at((0, 576, 192, 192), colorkey=(0, 0, 0))
        i17 = self.spritesheets['savers'].image_at((192, 576, 192, 192), colorkey=(0, 0, 0))
        i18 = self.spritesheets['savers'].image_at((384, 576, 192, 192), colorkey=(0, 0, 0))
        i19 = self.spritesheets['savers'].image_at((576, 576, 192, 192), colorkey=(0, 0, 0))
        i20 = self.spritesheets['savers'].image_at((771, 576, 192, 192), colorkey=(0, 0, 0))
        i21 = self.spritesheets['savers'].image_at((0, 771, 192, 192), colorkey=(0, 0, 0))
        i22 = self.spritesheets['savers'].image_at((192, 771, 192, 192), colorkey=(0, 0, 0))
        i23 = self.spritesheets['savers'].image_at((384, 771, 192, 192), colorkey=(0, 0, 0))
        i24 = self.spritesheets['savers'].image_at((576, 771, 192, 192), colorkey=(0, 0, 0))
        i25 = self.spritesheets['savers'].image_at((771, 771, 192, 192), colorkey=(0, 0, 0))


        mainClock = pygame.time.Clock()
        saversAnimation = pyganim.PygAnimation([(i1, 10), (i2, 10), (i3, 10), (i4, 10), (i5, 10), (i6, 10),
                                                (i7, 10), (i8, 10), (i9, 10), (i10, 10), (i11, 10), (i12, 10)
                                                   , (i13, 10), (i14, 10), (i15, 10), (i16, 10),
                                                (i17, 10), (i18, 10), (i19, 10), (i20, 10), (i21, 10), (i22, 10)
                                                   , (i23, 10), (i24, 10), (i25, 10)])

        saversAnimation.scale((World_Map.TILESIZE, World_Map.TILESIZE))
        saversAnimation.play()

        for i in range(10):
            saversAnimation.blit(
                self.screen, (self.player_position[0] * World_Map.TILESIZE, self.player_position[1] * World_Map.TILESIZE))
            pygame.display.update()
            mainClock.tick(30)
            i -= 1

    def heal_Anim(self):
        i1 = self.spritesheets['heal'].image_at((0, 0, 192, 192), colorkey=(0, 0, 0))
        i2 = self.spritesheets['heal'].image_at((192, 0, 192, 192), colorkey=(0, 0, 0))
        i3 = self.spritesheets['heal'].image_at((384, 0, 192, 192), colorkey=(0, 0, 0))
        i4 = self.spritesheets['heal'].image_at((576, 0, 192, 192), colorkey=(0, 0, 0))
        i5 = self.spritesheets['heal'].image_at((771, 0, 192, 192), colorkey=(0, 0, 0))
        i6 = self.spritesheets['heal'].image_at((0, 192, 192, 192), colorkey=(0, 0, 0))
        i7 = self.spritesheets['heal'].image_at((192, 192, 192, 192), colorkey=(0, 0, 0))
        i8 = self.spritesheets['heal'].image_at((384, 192, 192, 192), colorkey=(0, 0, 0))
        i9 = self.spritesheets['heal'].image_at((576, 192, 192, 192), colorkey=(0, 0, 0))
        i10 = self.spritesheets['heal'].image_at((771, 192, 192, 192), colorkey=(0, 0, 0))
        i11 = self.spritesheets['heal'].image_at((0, 384, 192, 192), colorkey=(0, 0, 0))
        i12 = self.spritesheets['heal'].image_at((192, 384, 192, 192), colorkey=(0, 0, 0))
        i13 = self.spritesheets['heal'].image_at((384, 384, 192, 192), colorkey=(0, 0, 0))

        mainClock = pygame.time.Clock()
        healAnimation = pyganim.PygAnimation([(i1, 10), (i2, 10), (i3, 10), (i4, 10), (i5, 10), (i6, 10),
                                                (i7, 10), (i8, 10), (i9, 10), (i10, 10), (i11, 10), (i12, 10),
                                                (i13, 10)])

        healAnimation.scale((World_Map.TILESIZE, World_Map.TILESIZE))
        healAnimation.play()

        for i in range(10):
            healAnimation.blit(
                self.screen, (self.player_position[0] * World_Map.TILESIZE, self.player_position[1] * World_Map.TILESIZE))
            pygame.display.update()
            mainClock.tick(30)
            i -= 1

    def plant_Anim(self, Tilemap):

        currentTile = Tilemap.getTilemap()[self.player_position[1]][self.player_position[0]]
        if currentTile == 0:
            currentTile = World_Map.grass_tile
        else:
            currentTile = World_Map.dirt_tile
        currentEnvironment = Tilemap.getEnvironment()[self.player_position[1]][self.player_position[0]]
        currentEnvironment = World_Map.environment[currentEnvironment]

        i1 = self.spritesheets['plant'].image_at((0, 0, 192, 192), colorkey=(0, 0, 0))
        i2 = self.spritesheets['plant'].image_at((192, 0, 192, 192), colorkey=(0, 0, 0))
        i3 = self.spritesheets['plant'].image_at((384, 0, 192, 192), colorkey=(0, 0, 0))
        i4 = self.spritesheets['plant'].image_at((576, 0, 192, 192), colorkey=(0, 0, 0))
        i5 = self.spritesheets['plant'].image_at((771, 0, 192, 192), colorkey=(0, 0, 0))
        i6 = self.spritesheets['plant'].image_at((0, 192, 192, 192), colorkey=(0, 0, 0))
        i7 = self.spritesheets['plant'].image_at((192, 192, 192, 192), colorkey=(0, 0, 0))
        i8 = self.spritesheets['plant'].image_at((384, 192, 192, 192), colorkey=(0, 0, 0))
        i9 = self.spritesheets['plant'].image_at((576, 192, 192, 192), colorkey=(0, 0, 0))
        i10 = self.spritesheets['plant'].image_at((771, 192, 192, 192), colorkey=(0, 0, 0))
        i11 = self.spritesheets['plant'].image_at((0, 384, 192, 192), colorkey=(0, 0, 0))
        i12 = self.spritesheets['plant'].image_at((192, 384, 192, 192), colorkey=(0, 0, 0))
        i13 = self.spritesheets['plant'].image_at((384, 384, 192, 192), colorkey=(0, 0, 0))
        i14 = self.spritesheets['plant'].image_at((576, 384, 192, 192), colorkey=(0, 0, 0))
        i15 = self.spritesheets['plant'].image_at((771, 384, 192, 192), colorkey=(0, 0, 0))
        i16 = self.spritesheets['plant'].image_at((0, 576, 192, 192), colorkey=(0, 0, 0))
        i17 = self.spritesheets['plant'].image_at((192, 576, 192, 192), colorkey=(0, 0, 0))
        i18 = self.spritesheets['plant'].image_at((384, 576, 192, 192), colorkey=(0, 0, 0))
        i19 = self.spritesheets['plant'].image_at((576, 576, 192, 192), colorkey=(0, 0, 0))
        i20 = self.spritesheets['plant'].image_at((771, 576, 192, 192), colorkey=(0, 0, 0))
        i21 = self.spritesheets['plant'].image_at((0, 771, 192, 192), colorkey=(0, 0, 0))
        i22 = self.spritesheets['plant'].image_at((192, 771, 192, 192), colorkey=(0, 0, 0))
        i23 = self.spritesheets['plant'].image_at((384, 771, 192, 192), colorkey=(0, 0, 0))
        i24 = self.spritesheets['plant'].image_at((576, 771, 192, 192), colorkey=(0, 0, 0))
        i25 = self.spritesheets['plant'].image_at((771, 771, 192, 192), colorkey=(0, 0, 0))


        mainClock = pygame.time.Clock()
        plantAnimation = pyganim.PygAnimation([(i1, 10), (i2, 10), (i3, 10), (i4, 10), (i5, 10), (currentTile, 10), (i6, 10),
                                              (i7, 10), (i8, 10), (currentTile, 10), (i9, 10), (i10, 10), (i11, 10), (currentTile, 10),
                                               (i12, 10), (i13, 10), (i14, 10), (currentTile, 10), (i15, 10), (i16, 10), (i17, 10),
                                               (currentEnvironment, 10), (i18, 10), (i19, 10), (currentTile, 10), (currentEnvironment, 10),
                                               (i20, 10), (i21, 10), (i22, 10), (currentTile, 10), (currentEnvironment, 10), (i23, 10), (i24, 10),
                                               (i25, 10), (currentTile, 10), (currentEnvironment, 10)])

        plantAnimation.scale((World_Map.TILESIZE, World_Map.TILESIZE))
        plantAnimation.play()

        for i in range(10):
            plantAnimation.blit(
                self.screen, (self.player_position[0] * World_Map.TILESIZE, self.player_position[1] * World_Map.TILESIZE))
            pygame.display.update()
            mainClock.tick(30)
            i -= 1

class BaseType:
    def __str__(self):
        return self.name

class clsBug(BaseType):
    id = 'bug'
    name = 'Käfer'

class clsBird(BaseType):
    id = 'bird'
    name = 'Vogel'

class clsSawblade(BaseType):
    id = 'sawblade'
    name = "Kettensägenmensch"


class cls_Enemy(object):

    def __init__(self, Type=None, Health=1, Position=[0, 0]):
        self.Type = Type
        self.Health = Health
        self.Position = Position
        self.Behaviour = []
        self.init_Behaviour()
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
        if isinstance(self.Type, clsBug):
            enemy_Icon=self.images['enemies']['bug']
        elif isinstance(self.Type, clsBird):
            enemy_Icon=self.images['enemies']['bird']
        elif isinstance(self.Type, clsSawblade):
            enemy_Icon=self.images['enemies']['sawblade']
        enemy_Icon = pygame.transform.scale(
            enemy_Icon, (World_Map.TILESIZE, World_Map.TILESIZE))
        enemy_Icon_Position = self.Position
        screen.blit(
            enemy_Icon, (
                enemy_Icon_Position[0] * World_Map.TILESIZE, enemy_Icon_Position[1] * World_Map.TILESIZE))

    def choose_action(self, Tilemap, Player_Position, Charakter):

        currentTile = Tilemap.getTilemap()[self.Position[1]
        ][self.Position[0]]
        currentEnvironment = Tilemap.getEnvironment()[self.Position[1]
        ][self.Position[0]]
        #evaluate 'flee'
        if "flee" in self.Behaviour:
            pass

        #evaluate 'eat'
        if "grassfood" in self.Behaviour:
            if currentTile == World_Map.GRASSLAND or currentEnvironment == World_Map.LOWGRASS or currentEnvironment == World_Map.MOREGRASS:
                return "eat"
        if "vegetables" in self.Behaviour:
            if currentEnvironment==World_Map.FRUIT1 or currentEnvironment==World_Map.FRUIT2:
                return "eat"

        #Liste aller umliegenden Tiles# Liste aller benachbarten Tiles, keine 'negativen' Tilewerte (out of range der Map)
        Liste = []
        for tile_x in range(self.Position[0] - 1, self.Position[0] + 2):
            for tile_y in range(self.Position[1] - 1, self.Position[1] + 2):
                if tile_x >= 0 and tile_y >= 0:
                    if tile_x < World_Map.MAPWIDTH and tile_y < World_Map.MAPHEIGHT:
                        to_append = [tile_x, tile_y]
                        Liste.append(to_append)

        Surrounding = []
        for tile in Liste:
            tile_art = Tilemap.getTilemap()[tile[1]][tile[0]]
            if tile_art == World_Map.GRASSLAND or tile_art == World_Map.DIRT or tile_art == World_Map.STONE:
                Surrounding.append(tile)

        # Possible Tiles berücksichtigt die Environment
        PossibleTiles = Surrounding[:]
        PreferedTiles = []
        for tile in Surrounding:
            tile_env = Tilemap.getEnvironment()[tile[1]][tile[0]]
            for env in World_Map.collide:
                if env == tile_env:
                    PossibleTiles.remove(tile)
            for env in World_Map.enterable:
                if env == tile_env:
                    PossibleTiles.remove(tile)
            if tile == Player_Position:
                if "aggressive" in self.Behaviour or "hostile" in self.Behaviour:
                    if Charakter.get_stealth_mode()==False:
                        return "attack"
                    else:
                        PossibleTiles.remove(tile)
            if tile_env == World_Map.LOWGRASS or tile_env == World_Map.MOREGRASS:
                if "grassfood" in self.Behaviour:
                    PreferedTiles.append(tile)
            elif tile_env == World_Map.FRUIT1 or tile_env == World_Map.FRUIT2:
                if "vegetables" in self.Behaviour:
                    PreferedTiles.append(tile)

        if not PreferedTiles:
            if not PossibleTiles:
                return "stay"
            else:
                anzahl = len(PossibleTiles)
                if anzahl >1:
                    rand_int = Percentages.dice(anzahl)
                    self.Position=PossibleTiles[rand_int-1]
                else:
                    self.Position=PossibleTiles[0]
                return "bewegt"
        else:
            anzahl = len(PreferedTiles)
            rand_int = Percentages.dice(anzahl)
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
            if isinstance(self.Type, clsBird):
                amount=Percentages.dice(2)
            elif isinstance(self.Type, clsSawblade):
                amount=Percentages.dice(5)
            if Charakter.savers:
                if amount > 1:
                    loweramount = Percentages.dice(amount)
                    amount -= loweramount
                else:
                    check = Percentages.halfhalf()
                    if check:
                        amount = 0
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
            if currentenv==World_Map.MOREGRASS:
                Tilemap.getEnvironment()[self.Position[1]
                ][self.Position[0]]=World_Map.LOWGRASS
            elif currentenv==World_Map.LOWGRASS:
                Tilemap.getEnvironment()[self.Position[1]
                ][self.Position[0]] = World_Map.DEADGRASS
            elif currentenv==World_Map.FRUIT2 or currentenv==World_Map.FRUIT1:
                Tilemap.getEnvironment()[self.Position[1]
                ][self.Position[0]] = World_Map.NOTHING
            elif currenttile==World_Map.GRASSLAND:
                Tilemap.getTilemap()[self.Position[1]
                ][self.Position[0]]=World_Map.DIRT

    def init_Behaviour(self):
        if isinstance(self.Type, clsBug):
            self.add_Behaviour("grassfood")
        if isinstance(self.Type, clsBird):
            self.add_Behaviour("hostile")
            self.add_Behaviour("vegetables")
        if isinstance(self.Type, clsSawblade):
            self.add_Behaviour("hostile")
            self.add_Behaviour("aggressive")

    def add_Behaviour(self, Verhalten):
        self.Behaviour.append(Verhalten)

    def delete_Behaviour(self, Verhalten):
        self.Behaviour.remove(Verhalten)

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
        player_Icon = pygame.transform.scale(player_Icon, (World_Map.TILESIZE, World_Map.TILESIZE))
        tiles_Sprite = Helper.spritesheet('tileset_32_32.png')
        if Player_Tile == World_Map.GRASSLAND:
            second = tiles_Sprite.image_at((193, 5505, 30, 30), colorkey=(0, 0, 0))
        elif Player_Tile == World_Map.STONE:
            second = tiles_Sprite.image_at((33, 8577, 30, 30), colorkey=(0, 0, 0))
        elif Player_Tile == World_Map.DIRT:
            second = tiles_Sprite.image_at((15, 2545, 64, 64), colorkey=(0, 0, 0))
        elif Player_Tile == World_Map.WATER:
            second = tiles_Sprite.image_at((26, 4701, 45, 45), colorkey=(0, 0, 0))
        second = pygame.transform.scale(
            second, (World_Map.TILESIZE, World_Map.TILESIZE))
        third = World_Map.environment[Player_Environment]
        deathAnim = pyganim.PygAnimation([(player_Icon, 10), (second, 10), (third, 10)])
        i = 0
        if damage_or_death == "damage":
            m = 10
        elif damage_or_death == "death":
            m = 40

        deathAnim.play()

        for i in range(m):
            deathAnim.blit(
                screen, (player_position[0] * World_Map.TILESIZE, player_position[1] * World_Map.TILESIZE))
            pygame.display.update()
            mainClock.tick(30)
            i -= 1
        if damage_or_death == "death":
            screen.blit(
                second, (player_position[0] * World_Map.TILESIZE, player_position[1] * World_Map.TILESIZE))
            screen.blit(
                third, (player_position[0] * World_Map.TILESIZE, player_position[1] * World_Map.TILESIZE))
        elif damage_or_death == "damage":
            screen.blit(
                third, (player_position[0] * World_Map.TILESIZE, player_position[1] * World_Map.TILESIZE))
            screen.blit(
                player_Icon, (player_position[0] * World_Map.TILESIZE, player_position[1] * World_Map.TILESIZE))

    def damage_and_death_anim(self, screen, damage_or_death, enemy_tile_Art, enemy_environment=World_Map.NOTHING):
        mainClock = pygame.time.Clock()
        if isinstance(self.Type, clsBug):
            first = self.images['enemies']['bug']
        elif isinstance(self.Type, clsBird):
            first = self.images['enemies']['bird']
        elif isinstance(self.Type, clsSawblade):
            first = self.images['enemies']['sawblade']
        first = pygame.transform.scale(
            first, (World_Map.TILESIZE, World_Map.TILESIZE))

        tiles_Sprite = Helper.spritesheet('tileset_32_32.png')
        if enemy_tile_Art == World_Map.GRASSLAND:
            second = tiles_Sprite.image_at((193, 5505, 30, 30), colorkey=(0, 0, 0))
        elif enemy_tile_Art == World_Map.STONE:
            second = tiles_Sprite.image_at((33, 8577, 30, 30), colorkey=(0,0,0))
        elif enemy_tile_Art == World_Map.DIRT:
            second = tiles_Sprite.image_at((15, 2545, 64, 64), colorkey=(0,0,0))
        elif enemy_tile_Art == World_Map.WATER:
            second = tiles_Sprite.image_at((26, 4701, 45, 45), colorkey=(0,0,0))
        second = pygame.transform.scale(
            second, (World_Map.TILESIZE, World_Map.TILESIZE))
        third = World_Map.environment[enemy_environment]
        deathAnim = pyganim.PygAnimation([(first, 10), (second, 10), (third, 10)])
        i = 0
        if damage_or_death == "damage":
            m = 10
        elif damage_or_death == "death":
            m = 40

        deathAnim.play()

        for i in range(m):
            deathAnim.blit(
                screen, (self.Position[0] * World_Map.TILESIZE, self.Position[1] * World_Map.TILESIZE))
            pygame.display.update()
            mainClock.tick(30)
            i -= 1
        if damage_or_death == "death":
            screen.blit(
                second, (self.Position[0] * World_Map.TILESIZE, self.Position[1] * World_Map.TILESIZE))
            screen.blit(
                third, (self.Position[0] * World_Map.TILESIZE, self.Position[1] * World_Map.TILESIZE))
        elif damage_or_death == "damage":
            screen.blit(
                third, (self.Position[0] * World_Map.TILESIZE, self.Position[1] * World_Map.TILESIZE))
            screen.blit(
                first, (self.Position[0] * World_Map.TILESIZE, self.Position[1] * World_Map.TILESIZE))

    def generate_Enemy(self, Tilemap):
        rand_int = Percentages.dice(10)
        if rand_int <= 5:
            Art = clsBug()
            healthmodifier=Percentages.dice(6)
            health = 5+healthmodifier
        elif (rand_int >= 5 and rand_int <= 9):
            Art = clsBird()
            healthmodifier=Percentages.dice(12)
            health = 10+healthmodifier
        elif rand_int == 10:
            Art = clsSawblade()
            healthmodifier=Percentages.dice(30)
            health = 30+healthmodifier

        Position=self.generatePosition()
        # Can just spawn on Dirt, Grassland and Stone:
        acceptableValue=False
        while not acceptableValue:
            if Tilemap.getTilemap()[Position[1]][Position[0]]== World_Map.STONE or Tilemap.getTilemap()[Position[1]][Position[0]] == World_Map.GRASSLAND\
                    or Tilemap.getTilemap()[Position[1]][Position[0]]== World_Map.DIRT:
                acceptableValue=True
            else:
                Position=self.generatePosition()

        enemy = cls_Enemy(Art, health, Position)
        return enemy

    def generatePosition(self):
        # Can't spawn at [0,0], starting with '1'
        Position = [int((Percentages.dice(World_Map.MAPWIDTH - 1))),
                    int((Percentages.dice(World_Map.MAPHEIGHT - 1)))]
        return Position

    def __del__(self):
        pass

    def lower_Health(self, amount):
        self.Health -= amount


class cls_Enemies(object):

    def __init__(self, Enemies=[]):
        self.enemies = Enemies

    def fill_Enemies_list(self, Tilemap):
        # Max Enemies: 6
        rand_int = Percentages.dice(Wuerfelseiten=5)
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
