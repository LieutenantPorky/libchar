import libchar
import pygame
import pygame.locals as loc
from pygame.math import Vector2 as vec


libchar.setup(init_background = "background.png")

spaceship = libchar.Character("spaceship.png")
spaceship.position.x = 640/2
spaceship.position.y = 400


def shoot(self):
    bullet = libchar.Agent("bullet.png")
    bullet.position = self.position + vec (12, 0)
    bullet.velocity = vec(0,-0.5)
    bullet.add_tag("bullet")

spaceship.event(loc.K_SPACE, shoot)


num_aliens = 6 
aliens = []
for i in range(num_aliens):
    new_alien = libchar.Agent("alien.png")
    new_alien.position =vec(100 * i, 0)
    new_alien.velocity = vec(0.2,0)
    aliens.append(new_alien)







while 1:
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[loc.K_a] and spaceship.position.x > 0:
        spaceship.velocity.x = -0.3
    elif pressed_keys[loc.K_d] and spaceship.position.x < 620:
        spaceship.velocity.x = 0.3
    else:
        spaceship.velocity.x = 0

    
    for alien in aliens:

        if alien.position.x > 610:
            alien.move(vec(610, alien.position.y))
            alien.velocity.x *= -1
            alien.move(alien.position + vec(0,32))
     
        if alien.position.x < 0:
            alien.move(vec(0, alien.position.y))
            alien.velocity.x *= -1
            alien.move(alien.position + vec(0,32))
        
        hit = alien.is_colliding_tag("bullet")
        if hit:
            aliens.remove(alien)
            hit.kill()
            alien.kill()
        
    libchar.update()
