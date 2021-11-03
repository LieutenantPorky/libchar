import libchar
import pygame
from pygame.math import Vector2 as v
import pygame.locals as loc

libchar.setup("background.png")

star_2 = libchar.Character("star.png")
star_2.velocity = v(0.05,0.1)

def say_pos(self):
    print(self.position)
    self.kill()

star_2.event(loc.K_SPACE, say_pos)



while 1:
    star_2.rotate(0.1)
    libchar.update()
