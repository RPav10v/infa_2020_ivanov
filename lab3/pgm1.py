import pygame
from pygame.draw import *

pygame.init()

FPS = 30

screen = pygame.display.set_mode((400, 400))

rect(screen, (200, 200, 200), (0, 0, 400, 400))

circle(screen, (255, 255, 0), (200, 200), 100)
rect(screen, (0, 0, 0), (150, 250, 100, 20))
circle(screen, (255, 0, 0), (150, 170), 25)
circle(screen, (0, 0, 0), (150, 170), 25, 2)
circle(screen, (0, 0, 0), (150, 170), 12)

circle(screen, (255, 0, 0), (250, 170), 20)
circle(screen, (0, 0, 0), (250, 170), 20, 2)
circle(screen, (0, 0, 0), (250, 170), 10)

polygon(screen, (0, 0, 0), [(100, 100), (190, 150), (185, 160), (95, 110), (100, 100)])
polygon(screen, (0, 0, 0), [(300, 100), (210, 150), (215, 160), (305, 110), (300, 100)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()