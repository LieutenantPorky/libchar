import libchar
import pygame
from pygame.math import Vector2 as vec


libchar.setup()


ball = libchar.Agent("assets/ball.png")
ball.move(vec(290, 100))


platform = libchar.Agent("assets/platform.png")
platform.move(vec(210,400))


while 1:
    
    ball.velocity.y += 0.01

    if ball.is_colliding(platform):
        ball.velocity.y = -1 * abs(ball.velocity.y)

    libchar.update(globals())
