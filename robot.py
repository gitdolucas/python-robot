from math import cos, sin, pi
L = 20
C = 20
WL = 10
WC = 14
ALPHA = pi / 12
DS = 20
R1 = (L / 2, C / 2)
R2 = (-L / 2, C / 2)
R3 = (-L / 2, -C / 2)
R4 = (L / 2, -C / 2)
W11 = (-WC / 2, L/2 + WL)
W12 = (-WC / 2, L/2)
W13 = (WC / 2, L/2)
W14 = (WC / 2, L/2 + WL)

W21 = (-WC / 2, -L/2)
W22 = (-WC / 2, -L/2 - WL)
W23 = (WC / 2, -L/2 - WL)
W24 = (WC / 2, -L/2)

S1 = (DS * cos(ALPHA), DS * sin(ALPHA))
S2 = (DS * cos(-ALPHA), DS * sin(-ALPHA))

O = (0, 0)
PONTOS = [R1, R2, R3, R4, W11, W12, W13, W14, W21, W22, W23, W24, O, S1, S2]

SEGMENTOS = ((0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7),
             (7, 4), (8, 9), (9, 10), (10, 11), (11, 8), (12, 13), (12, 14))
