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

TAMANHO_SETA = 10

# GENERAL METHODS
def somar_vetores(v1, v2):
    return [v1[0]+v2[0], v1[1]+v2[1]]

# Converte um ângulo em graus para radianos
def rad(angulo):
    return angulo*pi/180

# Desenha um vetor v na tela
def desenhar_vetor(p, v, cor=(WHITE)):
    # Desenha a linha do vetor
    pygame.draw.line(SCREEN, cor, p, somar_vetores(p,v))
    
    # Desenha a seta do vetor
    
    theta = atan2(v[1],v[0])
    #print(f"Theta: {theta}")
    #print(f"V: {v}",end="\n\n")

    # Cálculo das setas do vetor v
    s1 = (v[0]+TAMANHO_SETA * cos(3*pi/4+theta), v[1] + TAMANHO_SETA * sin(3*pi/4+theta))
    s2 = (v[0]+TAMANHO_SETA * cos(5*pi/4+theta), v[1] + TAMANHO_SETA * sin(5*pi/4+theta))

    # Desenhar as setas
    pygame.draw.line(SCREEN, cor, somar_vetores(p,v), somar_vetores(p,s1))
    pygame.draw.line(SCREEN, cor, somar_vetores(p,v), somar_vetores(p,s2))
    

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


def drawRobot(tx, ty, sx, sy, theta, rpme, rpmd):
    CENTRO = (tx,ty)
    CE = [0, -(robot.L+robot.WL)/2]
    CD = [0, +(robot.L+robot.WL)/2]
    ve = rpme * 2 * pi * robot.WC/2
    vd = rpmd * 2 * pi * robot.WC/2
    PE = [ve, -(robot.L+robot.WL)/2]
    PD = [vd, +(robot.L+robot.WL)/2]
    d_ed = [PE[0]-PD[0], PE[1]-PD[1]] 

    v_ve = [PE[0]-CE[0], PE[1]-CE[1]]
    v_vd = [PD[0]-CD[0], PD[1]-CD[1]]

    n0 = [-d_ed[1], d_ed[0]]
    n1 = [d_ed[1], -d_ed[0]]
    
    #CE = somar_vetores(CE,translacao)
    #CD = somar_vetores(CD,translacao)
    #PE = somar_vetores(PE,translacao)
    #PD = somar_vetores(PD,translacao)

    #desenhar_vetor(CE,v_ve)
    #desenhar_vetor(CD,v_vd)

    for segment in robot.SEGMENTOS:

        [p1x, p1y] = robot.PONTOS[segment[0]]
        [p2x, p2y] = robot.PONTOS[segment[1]]

        r1x = (cos(theta) * p1x - sin(theta) * p1y) * sx + tx
        r1y = (sin(theta) * p1x + cos(theta) * p1y) * sy + ty
        r2x = (cos(theta) * p2x - sin(theta) * p2y) * sx + tx
        r2y = (sin(theta) * p2x + cos(theta) * p2y) * sy + ty

        pygame.draw.line(SCREEN, YELLOW, (r1x, r1y), (r2x, r2y), 1)

    tCDx = (cos(theta) * CD[0] - sin(theta) * CD[1]) + tx
    tCDy = (sin(theta) * CD[0] + cos(theta) * CD[1]) + ty

    tCEx = (cos(theta) * CE[0] - sin(theta) * CE[1]) + tx
    tCEy = (sin(theta) * CE[0] + cos(theta) * CE[1]) + ty

    tCE = [tCEx, tCEy]
    tCD = [tCDx, tCDy]

    tv_vex = (cos(theta) * v_ve[0] - sin(theta) * v_ve[1])
    tv_vey = (sin(theta) * v_ve[0] + cos(theta) * v_ve[1])
    tv_ve = (tv_vex, tv_vey)

    tv_vdx = (cos(theta) * v_vd[0] - sin(theta) * v_vd[1])
    tv_vdy = (sin(theta) * v_vd[0] + cos(theta) * v_vd[1])
    tv_vd = (tv_vdx, tv_vdy)

    tn0x = (cos(theta) * n0[0] - sin(theta) * n0[1])
    tn0y = (sin(theta) * n0[0] + cos(theta) * n0[1])
    tn0 = (tn0x, tn0y)

    tn1x = (cos(theta) * n1[0] - sin(theta) * n1[1])
    tn1y = (sin(theta) * n1[0] + cos(theta) * n1[1])
    tn1 = (tn1x, tn1y)

    tdx = (cos(theta) * d_ed[0] - sin(theta) * d_ed[1])
    tdy = (sin(theta) * d_ed[0] + cos(theta) * d_ed[1])
    td = (tdx, tdy)

    desenhar_vetor(tCE,tv_ve)
    desenhar_vetor(tCD,tv_vd)
    desenhar_vetor(CENTRO,tn0)
    desenhar_vetor(CENTRO,tn1)
    desenhar_vetor(CENTRO,td)

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

    drawRobot(WIDTH/2, HEIGHT/2, 1, 1, 0, 3, 2)
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
    #px = px + vx * dt
    #py = py + vy * dt

pygame.quit()
