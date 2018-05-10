#robbie is working
import pygame
import pyganim
import random
import Helfer
from resources import Farben
from resources import Koordinaten

pygame.init()

TILESIZE = 40
MAPWIDTH = 15
MAPHEIGHT = 10
SURFACE = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE+50))

GRASS = 0
HIGHGRASS = 1
WIESENSNACK=2
BLÄTTERMISCHUNG=3
PUSTEBLUMENDESSERT=4
DIRT = 5
WATER = 6
NOTHING = 7
GRASSBUSH = 8
STONEHOLE = 9
GRASSFRAME = 10
LOWGRASS = 11
HOLE = 12
HILL1= 13
HILL2=14
HILL3=15
HILL4=16
MOREGRASS = 17
STONE = 18
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
CAVE = 40
WATERBORDERINNERCURVE = 41


tiles_Sprite = Helfer.spritesheet('tileset_32_32.png')
borders_Sprite = Helfer.spritesheet('borders.png')
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

textures={
    GRASS : grass_tile,
    HIGHGRASS : pygame.image.load('./resources/images/ressourcen/highgrasstexture.png').convert(),#needs renaming: darkgrass
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
    CAVE: cave,
    WATERBORDERINNERCURVE: water_border_inner_curve,
    STONECORNERLEFT: stone_corner_left,
    STONECORNERDOWN: stone_corner_down,
    STONECORNERCURVE: stone_corner_curve
}

#snippets
grasssnippet = grass_tile.convert()
grasssnippet = pygame.transform.scale(grasssnippet,(TILESIZE,TILESIZE))
highgrasssnippet = pygame.image.load('./resources/images/ressourcen/highgrasstexture.png').convert()
highgrasssnippet = pygame.transform.scale(highgrasssnippet,(TILESIZE,TILESIZE))

wiesensnacksnippet = pygame.image.load('./resources/images/ressourcen/wiesensnack.png')
wiesensnacksnippet = pygame.transform.scale(wiesensnacksnippet, (
Koordinaten.clsKoordinaten.SNACKSIZEX, Koordinaten.clsKoordinaten.SNACKSIZEY))
blättermischungsnippet = pygame.image.load('./resources/images/ressourcen/blattermischung.png')
blättermischungsnippet = pygame.transform.scale(blättermischungsnippet, (
Koordinaten.clsKoordinaten.SNACKSIZEX, Koordinaten.clsKoordinaten.SNACKSIZEY))
pusteblumendessertsnippet = pygame.image.load('./resources/images/ressourcen/dandelions.png')
pusteblumendessertsnippet = pygame.transform.scale(pusteblumendessertsnippet, (
Koordinaten.clsKoordinaten.SNACKSIZEX, Koordinaten.clsKoordinaten.SNACKSIZEY))

snippets=(grasssnippet,highgrasssnippet,wiesensnacksnippet,blättermischungsnippet,pusteblumendessertsnippet)

#resources
resources=[GRASS,STONE,DIRT,WATER]
collectableres=[GRASS,HIGHGRASS]
craftables=[WIESENSNACK,BLÄTTERMISCHUNG,PUSTEBLUMENDESSERT]

#collide
collide=[STONESTAND, HOLE, GRASSBUSH, TREE1, TREE2, TREE3]

#enterable
enterable=[CAVE, STONEHOLE]

#grasssorts
grasses=[LOWGRASS, MOREGRASS]

#inventory
inventory={
    GRASS:0,
    HIGHGRASS:0,
    WIESENSNACK:0,
    BLÄTTERMISCHUNG:0,
    PUSTEBLUMENDESSERT:0
}

#controls for crafting
controls = {
    WIESENSNACK:49,
    BLÄTTERMISCHUNG:50,
    PUSTEBLUMENDESSERT:51
}

#controls for feeding
feedcontrols = {
    WIESENSNACK:55,
    BLÄTTERMISCHUNG:56,
    PUSTEBLUMENDESSERT:57
}

#recipes for crafting
craftrecipes={
    WIESENSNACK : {GRASS : 5},
    BLÄTTERMISCHUNG: {HIGHGRASS : 2, WIESENSNACK: 1},
    PUSTEBLUMENDESSERT: {GRASS : 4, HIGHGRASS : 2, BLÄTTERMISCHUNG : 1}
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
        self.tilemap= [[GRASS for i in range(MAPWIDTH)] for j in range(MAPHEIGHT)]
        self.environment = [[NOTHING for i in range(MAPWIDTH)] for j in range(MAPHEIGHT)]
    def showTilemap(self):
        print(self.tilemap)
    def getTilemap(self):
        return self.tilemap
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
                    tile = GRASS
                self.tilemap[k][l] = tile
    def customTilemap(self):
        self.tilemap=[
            [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, STONE, STONE, STONE, STONE, STONE, STONE],
            [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, STONE, STONE, STONE, STONE, STONE, STONE],
            [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, STONE, STONE, STONE, STONE, STONE, STONE],
            [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
            [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
            [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, LAKE1, LAKE2, GRASS, GRASS, GRASS],
            [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, LAKE3, LAKE4, GRASS, GRASS, GRASS],
            [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
            [WATER, WATER, WATER, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
            [WATER, WATER, WATER, WATER, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
        ]
    def environment_customTilemap(self):
        self.environment=[
            [NOTHING, NOTHING, NOTHING, NOTHING, GRASSDECO, TREE2, NOTHING, NOTHING, NOTHING, STONECORNERLEFT, STONESTAND, STONEHOLE,
             NOTHING, MINISTONE2, NOTHING],
            [NOTHING, GRASSBUSH, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING, STONECORNERLEFT, NOTHING, MINISTONE1,
             STONESTAND, NOTHING, MINISTONE2],
            [GRASSDECO, NOTHING, NOTHING, NOTHING, HOLE, NOTHING, GRASSDECO, NOTHING, NOTHING, STONECORNERCURVE, STONECORNERDOWN, STONECORNERDOWN,
             STONECORNERDOWN, STONECORNERDOWN, STONECORNERDOWN],
            [LOWGRASS, LOWGRASS, LOWGRASS, NOTHING, GRASSDECO, NOTHING, TREE3, NOTHING, NOTHING, NOTHING, NOTHING, NOTHING,
             NOTHING, NOTHING, NOTHING],
            [MOREGRASS, MOREGRASS, GRASSBUSH, LOWGRASS, NOTHING, NOTHING, TREE3, TREE3, NOTHING, LOWGRASS, LOWGRASS, LOWGRASS,
             LOWGRASS, GRASSDECO, NOTHING],
            [MOREGRASS, LOWGRASS, LOWGRASS, NOTHING, NOTHING, GRASSDECO, NOTHING, NOTHING, LOWGRASS, LOWGRASS, NOTHING, NOTHING,
             LOWGRASS, MOREGRASS, TREE2],
            [LOWGRASS, LOWGRASS, LOWGRASS, LOWGRASS, HILL1, HILL3, NOTHING, GRASSDECO, NOTHING, LOWGRASS, NOTHING, ROSEWATER1,
             LOWGRASS, MOREGRASS, MOREGRASS],
            [LOWGRASS, LOWGRASS, LOWGRASS, LOWGRASS, HILL4, HILL2, NOTHING, NOTHING, NOTHING, GRASSBUSH, LOWGRASS, LOWGRASS,
             LOWGRASS, MOREGRASS, MOREGRASS],
            [WATERBORDERTOP, WATERBORDERTOP, WATERBORDERCURVE, LOWGRASS, LOWGRASS, NOTHING, NOTHING, NOTHING, CAVE, NOTHING, NOTHING, GRASSDECO,
             LOWGRASS, LOWGRASS, MOREGRASS],
            [ROSEWATER2, STONEWATER, WATERBORDERINNERCURVE, WATERBORDERCURVE, LOWGRASS, LOWGRASS, TREE2, NOTHING, NOTHING, STONEDECO, NOTHING, TREE1,
             MOREGRASS, HOLE, MOREGRASS]
        ]
    def drawSnippets(screen):
        placePosition = 50
        for item in collectableres:
            screen.blit(
                snippets[item], (placePosition, MAPHEIGHT * TILESIZE + 5))
            placePosition += 50
            textObjekt = pygame.font.Font('resources/fonts/celtic_gaelige.ttf', 19).render(str(
                inventory[item]), True, Farben.clsFarben.WHITE, Farben.clsFarben.BLACK)
            screen.blit(
                textObjekt, (placePosition, MAPHEIGHT * TILESIZE + 5))
            placePosition += 50