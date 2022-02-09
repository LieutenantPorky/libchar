import libchar
import pygame
import pygame.locals as loc
from pygame.math import Vector2 as vec

libchar.setup()
ground = libchar.Agent("assets/grass.png")
ground.move((libchar.screen.get_width()/2, libchar.screen.get_height() - ground.get_height()/2))
ground.add_tag("platform")

platform = libchar.Agent("assets/small_platform.png")
platform.move((libchar.screen.get_width()/2, libchar.screen.get_height() - 100))
platform.add_tag("platform")

slime = libchar.Character("assets/slime.png")
slime.move((libchar.screen.get_width()/2, 100))


gravity = 0.005
max_speed_v = 0.8
max_speed_h = 0.6
horizontal_acc = 0.2
brake_acc = 0.02
jump_speed = -1
can_jump = False

def K_space():
    global can_jump
    if can_jump:
        slime.velocity.y = jump_speed
        can_jump = False

def K_a():
    if slime.velocity.x > - max_speed_h:
        slime.velocity.x -= horizontal_acc * libchar.dt

def K_d():
    if slime.velocity.x < max_speed_h:
        slime.velocity.x += horizontal_acc * libchar.dt

while 1:
    colliding_ground = slime.is_colliding_tag("platform")
    if colliding_ground:
        can_jump = True
        if slime.velocity.y > 0:
            slime.velocity.y = 0
            slime.move((slime.position.x, colliding_ground.position.y - colliding_ground.get_height() / 2 - slime.get_height() /2))
    else:
        slime.velocity.y += gravity * libchar.dt
        if slime.velocity.y > max_speed_v:
            slime.velocity.y = max_speed_v

    if abs(slime.velocity.x) <= brake_acc * libchar.dt:
        slime.velocity.x = 0
    else:
        slime.velocity.x -= slime.velocity.x/abs(slime.velocity.x) * brake_acc * libchar.dt



    libchar.update(globals())
