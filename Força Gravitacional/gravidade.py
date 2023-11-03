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

## Inicialização dos atributos iniciais do programa

FPS = 120
DT = 10/FPS
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREY = (48, 45, 45)
WIDTH, HEIGHT = 1000, 800
M, m = 1000, 1
G = 100

## Inicialização do pygame

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

## Inicialização dos objetos

Earth = particle((WIDTH/2, HEIGHT/2), M, 50, BLUE, True)
centerX, centerY = Earth.r.x, Earth.r.y
rocket = particle((700, HEIGHT/2), m, 6, GREY)
rocket.v = vector(5, -20)


while True:
    clock.tick(FPS)
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            exit()
            
    raioVetor = rocket.r - Earth.r
    r = raioVetor.mag()
    raioVetor.norm()
    fg = G*M*m / (r*r)
    F = raioVetor * (-fg)
    
    rocket.applyForce(F)
    rocket.move(DT)
    
    drawParticle(Earth, screen)
    drawParticle(rocket, screen)
    
    pygame.display.update()