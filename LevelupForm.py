import pygame
# maybe a star?
# pygame.draw.polygon
# for Andre

pygame.init()
pygame.display.init()
screen = pygame.display.set_mode((100, 100), 0, 0)
gold = (255, 215,   0)
darkred = (139, 0, 0)

pygame.display.set_caption("Screentitle")

# six 
pointlist = [(55, 20), (75, 80), (20, 40), (80, 40), (35, 80)]
pygame.draw.lines(screen, gold, 1, pointlist, 3)

# six inverse
# pointlist = [(45, 80), (25, 20), (80, 60), (20, 60), (65, 20)]
# pygame.draw.lines(screen, darkred, 1, pointlist, 3)


pygame.display.update()
