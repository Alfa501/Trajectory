import math
import pygame
from pygame.locals import *
from pygame import gfxdraw

size = 1024

distance = 100
velocity_bullet = 50 # m/s

time = 0
velocity = 100 # m/s
angle = 45 # degrees

pygame.init()
screen = pygame.display.set_mode((size,size))
clock = pygame.time.Clock()

def getxy(v, a, t):
    vx = v * math.cos(a*math.pi/180)
    vy = v * math.sin(a*math.pi/180)
    x = round(vx * t)
    y = round(vy * t)
    y = 512-round(y - 0.5 * 9.81 * t**2)
    print((x,y))
    return (x,y)

for i in range(100):
    screen.set_at(getxy(velocity, angle, time), ((255,255,255)))
    
    pygame.display.update() 
    clock.tick(10)
    time += 0.1

for event_var in pygame.event.get():
    if event_var.type == QUIT:
        pygame.quit()
    if event_var.type == MOUSEBUTTONDOWN:
        pygame.quit()
        continue
    if event_var.type == MOUSEMOTION:
        continue








# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# screen.set_at((cordx+many, cordy+pixels), xolor)
# xolor = (random.randint(0, 255), y, random.randint(0, 255))
# pygame.display.update() 
# 