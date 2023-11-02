import pygame
from pygame.locals import *
import os
import sys
from math import pi, sin, cos

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
diretorio_pai = os.path.join(diretorio_atual, '..')
sys.path.append(diretorio_pai)

from particle import particle
from vetor import vector
from drawer import *

pygame.init()

## Inicialização dos atributos iniciais do programa

FPS = 120
DT = 10/FPS
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 600, 800

angle = 10*(pi / 180)
v_angle = 0
len = 500
g = 10
mass = 10
Fg = vector(0, mass*g)

pivot = particle((WIDTH/2, 0), 1, 5, BLACK, True)
p = particle((WIDTH/2 + len * sin(angle), len * cos(angle)), mass, 20, RED, False)
l = line(pivot, p, 2)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

counter = 0

while True:
    clock.tick(FPS)
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            exit()
            
    seno = (p.r.x - pivot.r.x) / len
    cosseno = (p.r.y) / len
    
    tracao = mass * g * cosseno + ( mass * (p.v.mag() ** 2) )/ len
    T = vector(-tracao * seno, - tracao * cosseno)
    p.applyForce(Fg + T)
    p.move(DT)
            
    drawLine(l, screen)
    drawParticle(p, screen)
    
    pygame.display.update()