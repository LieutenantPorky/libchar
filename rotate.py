import libchar
import pygame
from pygame.math import Vector2 as vec


libchar.setup()
libchar.set_background("assets/background.png")

ball = libchar.Agent("assets/ball.png")
ball.move(vec(290, 100))
ball.set_velocity((0.2,0.2))
rotation = 0
while 1:
    rotation += 0.1
    ball.set_rotation(rotation)
    libchar.update(globals())
