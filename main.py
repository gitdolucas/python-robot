import pygame
from random import randint
import numpy as np
from math import atan2, pi, exp, cos, sin, floor, sqrt
import robot

# COLORS
BLACK = (0, 0, 0)  # background
GREY = (50, 50, 50)  # sensors
WHITE = (255, 255, 255)  # ant
YELLOW = (255, 191, 0)  # nest
GREEN = (0, 255, 0)  # food
RED = (255, 0, 0)  # trail - to nest
BLUE = (0, 0, 255)  # trail - to food

# CLOCK
CLOCK_SPEED = 50

# GRID
X_DIMENSION = 350
Y_DIMENSION = 350
RECT_SIZE = 1

# SCREEN SIZE
WIDTH = X_DIMENSION * RECT_SIZE
HEIGHT = Y_DIMENSION * RECT_SIZE

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), vsync=1)

# GENERAL METHODS


def mod(x, y):
    return sqrt(x ** 2 + y ** 2)


def getSensor(tx, ty, sx, sy, t, vx, vy):
    t = atan2(vy, vx)
    s1x = (cos(t) * robot.S1[0] - sin(t) * robot.S1[1]) * sx + tx
    s1y = (sin(t) * robot.S1[0] + cos(t) * robot.S1[1]) * sy + ty
    s2x = (cos(t) * robot.S2[0] - sin(t) * robot.S2[1]) * sx + tx
    s2y = (sin(t) * robot.S2[0] + cos(t) * robot.S2[1]) * sy + ty

    s1 = imp.get_at((floor(s1x), floor(s1y)))
    s2 = imp.get_at((floor(s2x), floor(s2y)))
    return (s1, s2)


def drawRobot(tx, ty, sx, sy, t, vx, vy):
    t = atan2(vy, vx)

    for segment in robot.SEGMENTOS:

        [p1x, p1y] = robot.PONTOS[segment[0]]
        [p2x, p2y] = robot.PONTOS[segment[1]]

        r1x = (cos(t) * p1x - sin(t) * p1y) * sx + tx
        r1y = (sin(t) * p1x + cos(t) * p1y) * sy + ty
        r2x = (cos(t) * p2x - sin(t) * p2y) * sx + tx
        r2y = (sin(t) * p2x + cos(t) * p2y) * sy + ty

        pygame.draw.line(SCREEN, YELLOW, (r1x, r1y), (r2x, r2y), 2)


# UTIL TO CREATE A MATRIX WITH DIMENSION SIZE
def GenerateMatrix():
    return [[0 for j in range(Y_DIMENSION)] for i in range(X_DIMENSION)]

# UTIL TO DRAW A RECT AT AN ESPECIFIC POSITION WITH AN ESPECIFIC COLOR


def DrawRect(position, color):
    # position must be in screen domain size (and not matrix domain)
    # ie. x * RECT_SIZE
    pygame.draw.rect(SCREEN, color, pygame.Rect(
        position[0], position[1], RECT_SIZE, RECT_SIZE))


def degToRad(deg):
    return deg * pi / 180


class Robo:
    def __init__(self, position):
        self.position = position


imp = pygame.image.load("./pista.png").convert()
# print(imp.get_at())
pygame.init()
CLOCK = pygame.time.Clock()
IS_SIMULATION_RUNNING = True  # APPLICATION CONTROL VARIABLE

vx = 1
vy = 1
px = 1
py = 1
dt = 1 / 10

while IS_SIMULATION_RUNNING:

    SCREEN.fill(BLACK)
    SCREEN.blit(imp, (0, 0))

    # EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            IS_SIMULATION_RUNNING = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                vx = 0
                vy = 0
            if event.key == pygame.K_LEFT:
                vx -= 1
            if event.key == pygame.K_RIGHT:
                vx += 1
            if event.key == pygame.K_UP:
                vy -= 1
            if event.key == pygame.K_DOWN:
                vy += 1

    if not IS_SIMULATION_RUNNING:
        break

    drawRobot((X_DIMENSION / 2) + px, (Y_DIMENSION / 2) +
              py, 2, 2, pi / 4, vx, vy)
    if getSensor((X_DIMENSION / 2) + px, (Y_DIMENSION / 2) + py, 2, 2, pi / 4, vx, vy)[0] == (255, 255, 255, 255):
        vx -= 1
        vy -= 1
    if getSensor((X_DIMENSION / 2) + px, (Y_DIMENSION / 2) + py, 2, 2, pi / 4, vx, vy)[1] == (255, 255, 255, 255):
        vx += 1
        vy += 1

    # DRAW CURRENT MATRIX STATUSES
    for i in range(0, X_DIMENSION):
        for j in range(0, Y_DIMENSION):
            pass

    CLOCK.tick(CLOCK_SPEED)
    pygame.display.update()
    px = px + vx * dt
    py = py + vy * dt

pygame.quit()
