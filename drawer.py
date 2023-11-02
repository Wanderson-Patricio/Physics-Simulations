from line import line
from particle import particle
from pygame import display, draw

WHITE = (255, 255, 255)

def drawLine(line : line, screen : display) -> None:
    draw.line(screen, WHITE, (line.a.r.x, line.a.r.y), (line.b.r.x, line.b.r.y), line.size)
    
def drawParticle(p : particle, screen : display) -> None:
    draw.circle(screen, p.color, (p.r.x, p.r.y), p.size)
