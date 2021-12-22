import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 200
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
x = 100
y = 100
r = 50
dx = 1
dy = 1
def click(event):
    print(x, y, r)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
A = []
n = 0

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            A = pygame.mouse.get_pos()
            x1 = A[0]
            y1 = A[1]
            if ((x1-x)**2 + (y1-y)**2)**0.5 <= r:
                print('goal')
                n+=1
            else:
                print('miss')
    x += dx
    y += dy

    circle(screen, RED, (x, y), r)
    if x >= 1150 or x < 50:
        dx *= -1
    if y >= 850 or y < 50:
        dy *= -1
    pygame.display.update()
    screen.fill(BLACK)
pygame.quit()
print('Количество очков', n)