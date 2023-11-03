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
WIDTH, HEIGHT = 1200, 800
M, m = 10, 100
G = 100

## Inicialização do pygame

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

## Inicialização dos objetos

NeutronStar = particle((300, 400), M, 1, BLUE)
NeutronStar.v = vector(0, -10)
BlackHole = particle((600, 400), m, 1, GREY)
BlackHole.v = vector(0, 1)

while True:
    clock.tick(FPS)
    #screen.fill(BLACK)
    
    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            exit()
            
    raioVetor = BlackHole.r - NeutronStar.r
    r = raioVetor.mag()
    raioVetor.norm()
    fg = G*M*m / (r*r)
    F = raioVetor * (-fg)
    
    BlackHole.applyForce(F)
    NeutronStar.applyForce(F * (-1))
    BlackHole.move(DT)
    NeutronStar.move(DT)
    
    drawParticle(NeutronStar, screen)
    drawParticle(BlackHole, screen)
    drawCenterOfMass(NeutronStar, BlackHole, screen)
    
    pygame.display.update()