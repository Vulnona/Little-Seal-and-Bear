#robbie is working
import pygame
import pyganim
import random
import Helper
from resources import Farben
from resources import Koordinaten

pygame.init()

TILESIZE = 40
MAPWIDTH = 15
MAPHEIGHT = 10
SURFACE = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE+50))

GRASSLAND = 0
LOWGRASS = 1
MOREGRASS = 2
WIESENSNACK=3
BLÄTTERMISCHUNG=4
PUSTEBLUMENDESSERT=5
DIRT = 6
WATER = 7
STONE = 8
NOTHING = 9
GRASSBUSH = 10
STONEHOLE = 11
HOLE = 12
HILL1= 13
HILL2=14
HILL3=15
HILL4=16
GRASSFRAME = 17
WATERBORDERINNERCURVE = 18
STONECORNERLEFT = 19
STONECORNERDOWN = 20
STONECORNERCURVE = 21
STONESTAND = 22
MINISTONE1= 23
MINISTONE2 = 24
STONEWATER = 25
ROSEWATER1 = 26
ROSEWATER2 = 27
WATERBORDERTOP = 28
DEADGRASS = 29
WATERBORDERCURVE = 30
LAKE1 = 31
LAKE2 = 32
LAKE3 = 33
LAKE4 = 34
TREE1 = 35
TREE2 = 36
TREE3 = 37
GRASSDECO = 38
STONEDECO = 39
CAVE1 = 40
CAVE2 = 41
CAVE3 = 42
CAVE4 = 43
FRUIT1 = 44
FRUIT2 = 45

fruit_Sprite = Helper.spritesheet('fruits.png')
tiles_Sprite = Helper.spritesheet('tileset_32_32.png')
borders_Sprite = Helper.spritesheet('borders.png')
craft_Sprites = Helper.spritesheet('flowers.png')
grass_tile = tiles_Sprite.image_at((193, 5505, 30, 30), colorkey=(0,0,0))
grass_tile = pygame.transform.scale(grass_tile, (40, 40))
stone_tile = tiles_Sprite.image_at((33, 8577, 30, 30), colorkey=(0,0,0))
stone_tile = pygame.transform.scale(stone_tile, (40, 40))
dirt_tile = tiles_Sprite.image_at((15, 2545, 64, 64), colorkey=(0,0,0))
dirt_tile = pygame.transform.scale(dirt_tile, (40,40))
water_tile = tiles_Sprite.image_at((26, 4701, 45, 45), colorkey=(0,0,0))
water_tile = pygame.transform.scale(water_tile, (40,40))
lake_1=tiles_Sprite.image_at((14, 4686, 33, 32), colorkey=(0,0,0))
lake_1=pygame.transform.scale(lake_1, (40,40))
lake_2=tiles_Sprite.image_at((14+33, 4686, 33, 32), colorkey=(0,0,0))
lake_2=pygame.transform.scale(lake_2, (40,40))
lake_3=tiles_Sprite.image_at((14, 4686+32, 33,32), colorkey=(0,0,0))
lake_3=pygame.transform.scale(lake_3, (40,40))
lake_4=tiles_Sprite.image_at((14+33, 4686+32, 33, 32), colorkey=(0,0,0))
lake_4=pygame.transform.scale(lake_4, (40,40))

stone_corner=tiles_Sprite.image_at((113, 4923, 31, 43), colorkey=(0,0,0))
stone_corner_curve=tiles_Sprite.image_at((113, 4944, 36, 32), colorkey=(0,0,0))
stone_corner_curve=pygame.transform.scale(stone_corner_curve, (40,40))
stone_corner = pygame.transform.scale(stone_corner, (40,40))
stone_corner_left = pygame.transform.rotate(stone_corner, 0)
stone_corner_down = pygame.transform.rotate(stone_corner, 90)
stone_deco = tiles_Sprite.image_at((226, 6243, 30, 29), colorkey=(0,0,0))
stone_stand = tiles_Sprite.image_at((202, 8303, 45, 31), colorkey=(0,0,0))
stone_stand = pygame.transform.scale(stone_stand, (40,40))
mini_stone_1 = tiles_Sprite.image_at((200, 6314, 21, 21), colorkey=(0,0,0))
mini_stone_1 = pygame.transform.scale(mini_stone_1, (40,40))
mini_stone_2 = tiles_Sprite.image_at((231, 6314, 21, 21), colorkey=(0,0,0))
mini_stone_2 = pygame.transform.scale(mini_stone_2, (20,20))
stone_in_water = tiles_Sprite.image_at((113, 4689, 32, 32), colorkey=(0,0,0))
stone_in_water = pygame.transform.scale(stone_in_water, (40,40))
rose_in_water_1 = tiles_Sprite.image_at((166,4646, 20, 19), colorkey=(0,0,0))
rose_in_water_2= tiles_Sprite.image_at((135,4648, 20, 19), colorkey=(0,0,0))
hole_in_grass = tiles_Sprite.image_at((208, 5327, 32, 32), colorkey=(0,0,0))
hole_in_grass = pygame.transform.scale(hole_in_grass, (40,40))
hill_grass_1 = tiles_Sprite.image_at((13, 5679, 35, 35),colorkey=(0,0,0))
hill_grass_1 = pygame.transform.scale(hill_grass_1, (40,40))
hill_grass_2 = tiles_Sprite.image_at((13+35, 5679+35, 35, 35), colorkey=(0,0,0))
hill_grass_2 = pygame.transform.scale(hill_grass_2, (40,40))
hill_grass_3 = tiles_Sprite.image_at((13+35, 5679, 35, 35), colorkey=(0,0,0))
hill_grass_3 = pygame.transform.scale(hill_grass_3, (40,40))
hill_grass_4 = tiles_Sprite.image_at((13, 5679+35, 35, 35), colorkey=(0,0,0))
hill_grass_4 = pygame.transform.scale(hill_grass_4, (40,40))

cave = tiles_Sprite.image_at((136, 6500, 56, 53), colorkey=(0,0,0))
cave = pygame.transform.scale(cave, (40,40))
cave_1 = tiles_Sprite.image_at((136, 6500, 28, 26), colorkey=(0,0,0))
cave_1 = pygame.transform.scale(cave_1, (40,40))
cave_2 = tiles_Sprite.image_at((136+28, 6500, 28, 26), colorkey=(0,0,0))
cave_2 = pygame.transform.scale(cave_2, (40,40))
cave_3 = tiles_Sprite.image_at((136+28, 6500+26, 28, 26), colorkey=(0,0,0))
cave_3 = pygame.transform.scale(cave_3, (40,40))
cave_4 = tiles_Sprite.image_at((136, 6500+26, 28, 26), colorkey=(0,0,0))
cave_4 = pygame.transform.scale(cave_4, (40,40))

water_border=tiles_Sprite.image_at((30, 4689, 40, 45), colorkey=(0,0,0))
water_border= pygame.transform.scale(water_border, (40,40))
water_border_top=pygame.transform.rotate(water_border, 0)
water_border_curve= tiles_Sprite.image_at((43, 4689, 36, 36), colorkey=(0,0,0))
water_border_curve=pygame.transform.scale(water_border_curve, (40,40))
water_border_inner_curve=tiles_Sprite.image_at((88, 4705, 40, 40),colorkey=(0,0,0))

empty = tiles_Sprite.image_at((193, 8473, 10, 10), colorkey=(0 , 0, 0))
empty = pygame.transform.scale(empty, (40,40))
grass_bush_tile = tiles_Sprite.image_at((200,8433, 50, 32), colorkey=(0 , 0, 0))
grass_bush_tile = pygame.transform.scale(grass_bush_tile, (40, 40))
stone_hole = tiles_Sprite.image_at((112, 8240, 64, 64), colorkey=(192, 166, 95))
stone_hole = pygame.transform.scale(stone_hole, (40, 40))
grass_frame = tiles_Sprite.image_at((16, 2096, 64, 62), colorkey=(0,0,0))
grass_frame = pygame.transform.scale(grass_frame, (40,40))
grass_deco = tiles_Sprite.image_at((126, 2853, 35, 35), colorkey=(0,0,0))

high_grass = tiles_Sprite.image_at((160, 2272, 32, 32), colorkey=(0,0,0))
high_grass = pygame.transform.scale(high_grass, (40, 40))
low_grass = tiles_Sprite.image_at((223, 2209, 32, 32), colorkey=(0,0,0))
low_grass = pygame.transform.scale(low_grass, (40, 40))
dead_grass = tiles_Sprite.image_at((97, 2853, 32, 32), colorkey=(0,0,0))

tree_1 = tiles_Sprite.image_at((195, 205, 57, 51), colorkey=(0,0,0))
tree_1 = pygame.transform.scale(tree_1, (40, 40))
tree_2 = tiles_Sprite.image_at((195, 263, 57, 51), colorkey=(0,0,0))
tree_2 = pygame.transform.scale(tree_2, (40, 40))
tree_3 = tiles_Sprite.image_at((195, 410, 64, 64), colorkey=(0,0,0))
tree_3 = pygame.transform.scale(tree_3, (40, 40))

fruit_1 = fruit_Sprite.image_at((0, 271, 70, 50), colorkey=(0,0,0))
fruit_1 = pygame.transform.scale(fruit_1, (20, 20))
fruit_2 = fruit_Sprite.image_at((195, 11, 57, 59), colorkey=(0,0,0))
fruit_2 = pygame.transform.scale(fruit_2, (20,20))


textures={
    GRASSLAND : grass_tile,
    STONE: stone_tile,
    DIRT : dirt_tile,
    WATER : water_tile,
    LAKE1: lake_1,
    LAKE2: lake_2,
    LAKE3: lake_3,
    LAKE4: lake_4
}

environment={
    NOTHING: empty,
    MINISTONE1: mini_stone_1,
    MINISTONE2: mini_stone_2,
    HOLE: hole_in_grass,
    HILL1: hill_grass_1,
    HILL2: hill_grass_2,
    HILL3: hill_grass_3,
    HILL4: hill_grass_4,
    GRASSDECO: grass_deco,
    STONESTAND: stone_stand,
    LOWGRASS: low_grass,
    MOREGRASS: high_grass,
    DEADGRASS: dead_grass,
    GRASSFRAME: grass_frame,
    GRASSBUSH: grass_bush_tile,
    STONEHOLE: stone_hole,
    STONEWATER: stone_in_water,
    ROSEWATER1: rose_in_water_1,
    ROSEWATER2: rose_in_water_2,
    WATERBORDERTOP: water_border_top,
    WATERBORDERCURVE: water_border_curve,
    TREE1: tree_1,
    TREE2: tree_2,
    TREE3: tree_3,
    STONEDECO: stone_deco,
    CAVE1: cave_1,
    CAVE2: cave_2,
    CAVE3: cave_3,
    CAVE4: cave_4,
    WATERBORDERINNERCURVE: water_border_inner_curve,
    STONECORNERLEFT: stone_corner_left,
    STONECORNERDOWN: stone_corner_down,
    STONECORNERCURVE: stone_corner_curve,
    FRUIT1: fruit_1,
    FRUIT2: fruit_2
}

#snippets
grasssnippet = grass_tile.convert()
grasssnippet = pygame.transform.scale(grasssnippet,(TILESIZE,TILESIZE))
lowgrasssnippet = low_grass.convert()
lowgrasssnippet = pygame.transform.scale(lowgrasssnippet,(TILESIZE,TILESIZE))
highgrasssnippet = high_grass.convert()
highgrasssnippet = pygame.transform.scale(highgrasssnippet,(TILESIZE,TILESIZE))
wiesensnacksnippet = craft_Sprites.image_at((33, 135, 35, 30), colorkey=(0,0,0))
wiesensnacksnippet = pygame.transform.scale(wiesensnacksnippet, (TILESIZE,TILESIZE))
blättermischungsnippet = craft_Sprites.image_at((254, 129, 35, 33), colorkey=(0,0,0))
blättermischungsnippet = pygame.transform.scale(blättermischungsnippet, (TILESIZE,TILESIZE))
pusteblumendessertsnippet = craft_Sprites.image_at((223, 128, 34, 31), colorkey=(0,0,0))
pusteblumendessertsnippet = pygame.transform.scale(pusteblumendessertsnippet, (TILESIZE, TILESIZE))

snippets=(grasssnippet,lowgrasssnippet,highgrasssnippet,wiesensnacksnippet,blättermischungsnippet,pusteblumendessertsnippet)

#resources
resources=[GRASSLAND, STONE, DIRT, WATER]
collectableres=[GRASSLAND, LOWGRASS, MOREGRASS]
craftables=[LOWGRASS, MOREGRASS, WIESENSNACK,BLÄTTERMISCHUNG,PUSTEBLUMENDESSERT]

#needs swimming
waterbehaviour=[WATER, LAKE2, LAKE1, LAKE3, LAKE4]

#collide
collide=[STONESTAND, HOLE, GRASSBUSH, TREE1, TREE2, TREE3, CAVE1, CAVE2, HILL1, HILL2, HILL3, HILL4]

#enterable
enterable=[CAVE3, CAVE4, STONEHOLE]

#grasssorts
grasses=[LOWGRASS, MOREGRASS]

#inventory
inventory={
    GRASSLAND:0,
    LOWGRASS: 0,
    MOREGRASS:0,
    WIESENSNACK:0,
    BLÄTTERMISCHUNG:0,
    PUSTEBLUMENDESSERT:0
}

#recipes for crafting
craftrecipes={
    LOWGRASS : {GRASSLAND : 5},
    MOREGRASS: {GRASSLAND : 3, LOWGRASS : 4},
    WIESENSNACK : {MOREGRASS : 2},
    BLÄTTERMISCHUNG: {LOWGRASS : 2, WIESENSNACK: 1},
    PUSTEBLUMENDESSERT: {GRASSLAND : 2, MOREGRASS : 2, BLÄTTERMISCHUNG : 1}
}


#exp per component
experience_crafts={
    LOWGRASS: 50,
    MOREGRASS: 250,
    WIESENSNACK: 510,
    BLÄTTERMISCHUNG: 620,
    PUSTEBLUMENDESSERT: 1160
}

class clsInventory(object):
    def __init__(self, inventory):
        self.inventory=inventory
    def showInventory(self):
        print(inventory)
    def getInventory(self):
        return self.inventory

class clsTileMap(object):
    def __init__(self):
        self.tilemap= [[GRASSLAND for i in range(MAPWIDTH)] for j in range(MAPHEIGHT)]
        self.environment = [[NOTHING for i in range(MAPWIDTH)] for j in range(MAPHEIGHT)]
    def showTilemap(self):
        print(self.tilemap)
    def getTilemap(self):
        return self.tilemap
    def getEnvironment(self):
        return self.environment
    def getEnvironment(self):
        return self.environment
    def randomTilemap(self):
        for k in range(MAPHEIGHT):
            for l in range(MAPWIDTH):
                randomint = random.randint(0, 20)
                if randomint == 0:
                    tile = WATER
                elif randomint > 0 and randomint <= 5:
                    tile = STONE
                else:
                    tile = GRASSLAND
                self.tilemap[k][l] = tile
    def customTilemap(self):
        self.tilemap=[
            [GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, STONE, STONE, STONE, STONE, STONE, STONE],
            [GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, STONE, STONE, STONE, STONE, STONE, STONE],
            [GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, STONE, STONE, STONE, STONE, STONE, STONE],
            [GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND],
            [GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND],
            [GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, LAKE1, LAKE2, GRASSLAND, GRASSLAND, GRASSLAND],
            [GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, LAKE3, LAKE4, GRASSLAND, GRASSLAND, GRASSLAND],
            [GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND],
            [WATER, WATER, WATER, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND],
            [WATER, WATER, WATER, WATER, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND, GRASSLAND],
        ]
    def environment_customTilemap(self):
        self.environment=[
            [NOTHING, NOTHING, NOTHING, NOTHING, GRASSDECO, TREE2, NOTHING, NOTHING, FRUIT2, STONECORNERLEFT, STONESTAND, STONEHOLE,
             NOTHING, MINISTONE2, NOTHING],
            [NOTHING, GRASSBUSH, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, STONECORNERLEFT, NOTHING, MINISTONE1,
             STONESTAND, NOTHING, MINISTONE2],
            [GRASSDECO, NOTHING, NOTHING, NOTHING, HOLE, NOTHING, GRASSDECO, NOTHING, NOTHING, STONECORNERCURVE, STONECORNERDOWN, STONECORNERDOWN,
             STONECORNERDOWN, STONECORNERDOWN, STONECORNERDOWN],
            [LOWGRASS, LOWGRASS, LOWGRASS, NOTHING, GRASSDECO, NOTHING, TREE3, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING,
             NOTHING, NOTHING, NOTHING],
            [MOREGRASS, MOREGRASS, GRASSBUSH, LOWGRASS, NOTHING, NOTHING, TREE3, TREE3, NOTHING, LOWGRASS, LOWGRASS, LOWGRASS,
             LOWGRASS, GRASSDECO, FRUIT1],
            [MOREGRASS, LOWGRASS, LOWGRASS, NOTHING, NOTHING, GRASSDECO, NOTHING, NOTHING, LOWGRASS, LOWGRASS, NOTHING, NOTHING,
             LOWGRASS, MOREGRASS, TREE2],
            [LOWGRASS, LOWGRASS, LOWGRASS, LOWGRASS, HILL1, HILL3, NOTHING, GRASSDECO, NOTHING, LOWGRASS, NOTHING, ROSEWATER1,
             LOWGRASS, MOREGRASS, MOREGRASS],
            [LOWGRASS, LOWGRASS, LOWGRASS, LOWGRASS, HILL4, HILL2, NOTHING, CAVE1, CAVE2, GRASSBUSH, LOWGRASS, LOWGRASS,
             LOWGRASS, MOREGRASS, MOREGRASS],
            [WATERBORDERTOP, WATERBORDERTOP, WATERBORDERCURVE, LOWGRASS, LOWGRASS, FRUIT2, NOTHING, CAVE4, CAVE3, NOTHING, NOTHING, GRASSDECO,
             LOWGRASS, LOWGRASS, MOREGRASS],
            [ROSEWATER2, STONEWATER, WATERBORDERINNERCURVE, WATERBORDERCURVE, LOWGRASS, LOWGRASS, TREE1, NOTHING, NOTHING, STONEDECO, NOTHING, TREE2,
             MOREGRASS, HOLE, MOREGRASS]
        ]
    def drawSnippets(screen):
        placePosition = 70
        for item in collectableres:
            screen.blit(
                snippets[item], (placePosition, MAPHEIGHT * TILESIZE + 5))
            placePosition += 40
            textObjekt = pygame.font.Font('resources/fonts/celtic_gaelige.ttf', 19).render(str(
                inventory[item]), True, Farben.clsFarben.WHITE, Farben.clsFarben.BLACK)
            screen.blit(
                textObjekt, (placePosition+5, MAPHEIGHT * TILESIZE + 5))
            placePosition += 40