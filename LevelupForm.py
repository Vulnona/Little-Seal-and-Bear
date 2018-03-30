import Hauptfile
import Weltkarte
import random


class Star(object):
    def __init__(self, zackzahl, farbe, groesse, screen):
        self.Zackenzahl = zackzahl
        self.Farbe = farbe
        self.Groesse = groesse
        self.screen = screen

    def get_zackenanzahl(self):
        pass

    def set_zackenanzahl(self):
        pass

    def get_koordinaten(self):
        loc = Hauptfile.currentTile

    def set_koordinaten(self):
        loc

    centerptx = Weltkarte.TILESIZE / 2
    centerpty = Weltkarte.TILESIZE / 2
    startpunktx = centerptx + (centerptx / 2)
    startpunkty = centerpty + (centerpty / 2)
    winkel = zackzahl / 360                       # wtf to get zackenzahl?

    for i <= zackzahl:

        i++


    pointlist = [(startpunktx, startpunkty), ()]

    def Sternbewegung(self, screen):
        screen.blit(textures(Star).convert_alpha(), (Posx,Posy))
        #stern bewegt sich nach oben/unten
        Posy+=1

        if Posy>Weltkarte.MAPWIDTH*Weltkarte.TILESIZE:
            Posx=random.randint(0,Weltkarte.MAPHEIGHT*Weltkarte.TILESIZE)
            Posy=-200
# pygame.display.set_caption("Screentitle")

    # pointlists for different stars
    # inverse
    # septa
    # octa

# six inverse
# pointlist = [(45, 80), (25, 20), (80, 60), (20, 60), (65, 20)]
# pygame.draw.lines(screen, darkred, 1, pointlist, 3)


# pygame.display.update()
