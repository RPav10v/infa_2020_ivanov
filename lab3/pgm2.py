import pygame
from pygame.draw import *

pygame.init()

FPS = 30

screen = pygame.display.set_mode(((500, 700)))

#colors
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
BROWN = (51, 51, 0)
BROWN2 = (51, 25, 0)
YELLOW = (255, 255, 51)
BEZH = (224, 224, 224)
GRAY2 = (32, 32, 32)
GRAY3 = (64, 64, 64)
GRAY4 = (96, 96, 96)
GRAY5 = (26, 26, 26)
WHITE = (255, 255, 255)

#background
rect(screen, GRAY, (0, 0, 500, 300))
rect(screen, BLACK, (0, 300, 500, 700))

#cloud
ellipse(screen, GRAY5, (250, 152, 290, 45))

#building
rect(screen, BROWN, (20, 150, 300, 360))

#windows
n_windows = 3
x_left_window = 50
y_left_window = 380
width_window = 60
height_window = 80

for i in range(n_windows):
    if i != n_windows-1:
        rect(screen, BROWN2, (x_left_window, y_left_window, width_window, height_window))
        x_left_window += 90
    else:
        rect(screen, YELLOW, (x_left_window, y_left_window, width_window, height_window))

#windows2
n_windows2 = 4
x_left_window2 = 40
y_left_window2 = 150
width_window2 = 35
height_window2 = 140

for i in range(n_windows2):
    rect(screen, BEZH, (x_left_window2, y_left_window2, width_window2, height_window2))
    x_left_window2 += 75

#balcon
rect(screen, GRAY2, (0, 290, 340, 40))
rect(screen, GRAY2, (10, 245, 320, 15))
n_balks = 7
width_balk = 10
height_balk = 30
x_left_balk = 5
y_left_balk = 260
for i in range(n_balks):
    rect(screen, GRAY2, (x_left_balk, y_left_balk, width_balk, height_balk))
    x_left_balk += 53

#roof, clouds and moon
circle(screen, WHITE, (450, 54), 43)
rect(screen, GRAY2, (200, 60, 10, 70))
rect(screen, GRAY2, (80, 60, 10, 90))
ellipse(screen, GRAY3, (50, 48, 400, 55))

polygon(screen, BLACK, [(0, 150), (50, 120), (290, 120), (340, 150), (0, 150)])
rect(screen, GRAY2, (100, 50, 20, 90))
rect(screen, GRAY2, (270, 80, 10, 60))
ellipse(screen, GRAY4, (225, 28, 270, 45))
ellipse(screen, GRAY4, (320, 93, 270, 45))






pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()


