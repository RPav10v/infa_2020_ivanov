import pygame
from pygame.draw import *

pygame.init()

FPS = 30
width = 500
height = 700
screen = pygame.display.set_mode(((width, height)))

# colors
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


def draw_image(surface, width, height):
    """
    Рисует картину с домом.
    """
    # landscape
    x_landscape = 0
    y_landscape = 0.428 * height
    width_landscape = width
    height_landscape = height - y_landscape
    draw_landscape(surface, x_landscape, y_landscape, width_landscape, height_landscape, BLACK)

    # sky
    x_sky = 0
    y_sky = 0
    width_sky = width
    height_sky = y_landscape
    draw_sky(surface, x_sky, y_sky, width_sky, height_sky, GRAY)

    # cloud_alone
    x_cloud_alone = x_sky + 250
    y_cloud_alone = y_sky + 152
    width_cloud_alone = 290
    height_cloud_alone = 45
    draw_cloud(screen, x_cloud_alone, y_cloud_alone, width_cloud_alone, height_cloud_alone, GRAY5)

    # walls
    x_walls = 0.04 * width
    y_walls = 0.2143 * height
    width_walls = 0.6 * width
    height_walls = 0.5143 * height
    draw_walls(surface, x_walls, y_walls, width_walls, height_walls, BROWN)

    # first_floor_windows
    n_first_floor_windows = 3
    x_left_window = x_walls + 0.1 * width_walls
    y_left_window = y_walls + 230
    width_window = 0.2 * width_walls
    height_window = 0.222 * height_walls
    step = 0.3 * width_walls
    for window_x in range(n_first_floor_windows):
        if window_x != n_first_floor_windows - 1:
            draw_first_floor_windows(surface, x_left_window, y_left_window, width_window, height_window, BROWN2)
            x_left_window += step
        else:
            draw_first_floor_windows(surface, x_left_window, y_left_window, width_window, height_window, YELLOW)

    # second_floor_windows
    n_second_floor_windows = 4
    x_left_window2 = x_walls + 0.0666 * width_walls
    y_left_window2 = y_walls
    width_window2 = 0.1166 * width_walls
    height_window2 = 0.3888 * height_walls
    step = 0.25 * width_walls
    for window2_x in range(n_second_floor_windows):
        draw_second_floor_windows(surface, x_left_window2, y_left_window2, width_window2, height_window2, BEZH)
        x_left_window2 += step

    # balcony
    n_balks = 7
    otstup = 20
    x_balcony = x_walls - otstup
    y_balcony = y_walls + 0.2638 * height_walls
    width_balcony = width_walls + 2 * otstup
    height_balcony = 0.2361 * height_walls
    draw_balcony(surface, x_balcony, y_balcony, width_balcony, height_balcony, n_balks, GRAY2)

    # roof
    x_roof = x_balcony
    y_roof = y_walls
    width_roof = width_balcony
    height_roof = 0.0833 * height_walls
    draw_roof(surface, x_roof, y_roof, width_roof, height_roof, BLACK)

    # draw_moon
    diameter_moon = 86
    x_moon = 0.9 * width
    y_moon = 0.077 * height
    draw_moon(surface, x_moon, y_moon, diameter_moon, WHITE)

    # tubes1
    x_tube1 = x_sky + 80
    y_tube1 = y_sky + 60
    width_tube1 = 10
    height_tube1 = 90
    draw_tubes(surface, x_tube1, y_tube1, width_tube1, height_tube1, GRAY2)

    x_tube2 = x_sky + 200
    y_tube2 = y_sky + 60
    width_tube2 = 10
    height_tube2 = 70
    draw_tubes(surface, x_tube2, y_tube2, width_tube2, height_tube2, GRAY2)

    # clouds
    x_cloud1 = x_sky + 50
    y_cloud1 = y_sky + 48
    width_cloud1 = 400
    height_cloud1 = 55
    draw_cloud(screen, x_cloud1, y_cloud1, width_cloud1, height_cloud1, GRAY3)

    x_cloud2 = x_sky + 225
    y_cloud2 = y_sky + 28
    width_cloud2 = 270
    height_cloud2 = 45
    draw_cloud(screen, x_cloud2, y_cloud2, width_cloud2, height_cloud2, GRAY4)

    x_cloud3 = x_sky + 320
    y_cloud3 = y_sky + 93
    width_cloud3 = 270
    height_cloud3 = 45
    draw_cloud(screen, x_cloud3, y_cloud3, width_cloud3, height_cloud3, GRAY4)

    # tubes2
    draw_tubes(surface, 100, 50, 20, 90, GRAY2)
    draw_tubes(surface, 270, 80, 10, 60, GRAY2)


def draw_landscape(surface, x, y, width, height, color):
    """
    Рисует землю.
    surface - объект pygame.Surface
    x, y - координаты верхнего левого угла
    width, height - ширина, высота изображения
    color - цвет, заданный в формате, подходящем для pygame.Color
    """
    rect(surface, color, (x, y, width, height))


def draw_sky(surface, x, y, width, height, color):
    """
    Рисует небо.
    surface - объект pygame.Surface
    x, y - координаты верхнего левого угла
    width, height - ширина, высота изображения
    color - цвет, заданный в формате, подходящем для pygame.Color
    """
    rect(surface, color, (x, y, width, height))


def draw_walls(surface, x, y, width, height, color):
    """
    Рисует стены дома.
    surface - объект pygame.Surface
    x, y - координаты верхнего левого угла
    width, height - ширина, высота изображения
    color - цвет, заданный в формате, подходящем для pygame.Color
    """
    rect(surface, color, (x, y, width, height))


def draw_first_floor_windows(surface, x, y, width, height, color):
    """
    Рисует окна первого этажа дома.
    surface - объект pygame.Surface
    x, y - координаты верхнего левого угла
    width, height - ширина, высота изображения
    color - цвет, заданный в формате, подходящем для pygame.Color
    """
    rect(surface, color, (x, y, width, height))


def draw_second_floor_windows(surface, x, y, width, height, color):
    """
    Рисует окна второго этажа дома.
    surface - объект pygame.Surface
    x, y - координаты верхнего левого угла
    width, height - ширина, высота изображения
    color - цвет, заданный в формате, подходящем для pygame.Color
    """
    rect(surface, color, (x, y, width, height))


def draw_balcony(surface, x, y, width, height, n_balks, color):
    """
    Рисует балкон дома.
    surface - объект pygame.Surface
    x, y - координаты верхнего левого угла
    width, height - ширина, высота изображения
    color - цвет, заданный в формате, подходящем для pygame.Color
    """
    rect(surface, color, (x, y + 45, width, height * 0.5))
    rect(surface, color, (x + 10, y, width * 0.941, height * 0.1875))
    width_balk = 0.029 * width
    height_balk = 0.4 * height
    x_left_balk = x + 5
    y_left_balk = y + 15
    step = 0.1558 * width
    for i in range(n_balks):
        rect(surface, color, (x_left_balk, y_left_balk, width_balk, height_balk))
        x_left_balk += step


def draw_roof(surface, x, y, width, height, color):
    """
    Рисует крышу дома.
    surface - объект pygame.Surface
    x, y - координаты верхнего левого угла
    width, height - ширина, высота изображения
    color - цвет, заданный в формате, подходящем для pygame.Color
    """
    polygon(surface, color, [(x, y), (0.15 * width, y - height), (0.85 * width, y - height), (width, y), (x, y)])


def draw_tubes(surface, x, y, width, height, color):
    """
    Рисует трубу на крыше дома.
    surface - объект pygame.Surface
    x, y - координаты верхнего левого угла
    width, height - ширина, высота изображения
    color - цвет, заданный в формате, подходящем для pygame.Color
    """
    rect(surface, color, (x, y, width, height))


def draw_moon(surface, x, y, size, color):
    """
    Рисует луну.
    surface - объект pygame.Surface
    x, y - координаты верхнего левого угла
    size - диаметр луны
    color - цвет, заданный в формате, подходящем для pygame.Color
    """
    circle(surface, color, (x, y), size // 2)


def draw_cloud(surface, x, y, width, height, color):
    """
    Рисует облако.
    surface - объект pygame.Surface
    x, y - координаты верхнего левого угла
    width, height - ширина, высота изображения
    color - цвет, заданный в формате, подходящем для pygame.Color
    """
    ellipse(surface, color, (x, y, width, height))


draw_image(screen, 500, 700)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()