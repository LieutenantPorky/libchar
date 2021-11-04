
# First, we need to import both libchar and pygame
# While we're here, certain pygame modules - specifically Vector2 and
# locals (used to map keyboard buttons) will be used a lot, so I'm using
# the 'as' keyword to save them as a shorter alias

import libchar
import pygame
import pygame.locals as loc
from pygame.math import Vector2 as vec


# libchar.setup() sets up the game screen with a background
libchar.setup(init_background = "background.png")

# Since we'll be controlling the spaceship, let's make it a Character.
# Also, it's nicer to initialise it in the center of the screen.
spaceship = libchar.Character("spaceship.png",init_position = vec(640/2,400))

# Let's define a function to shoot a bullet. We'll then pair this function
# with a keypress event.
# Since we won't directly control the bullet, it makes sense to have it be an Agent.
# We just spawn it centered on the spaceship, and give it some velocity towards the top
# of the screen.
# The final step is to add a "bullet" tag to it.
def shoot(self):
    bullet = libchar.Agent("bullet.png")
    bullet.position = self.position + vec (12, 0)
    bullet.velocity = vec(0,-0.5)
    bullet.add_tag("bullet")

spaceship.event(loc.K_SPACE, shoot)

# Let's now create some aliens. Instead of doing this manually, a for loop will spawn however
# many aliens we want across the screen, and give them an initial push
# Since we'll also need to keep track of all the aliens, it makes sense to add them to an array
num_aliens = 6 
aliens = []
for i in range(num_aliens):
    new_alien = libchar.Agent("alien.png")
    new_alien.position =vec(100 * i, 0)
    new_alien.velocity = vec(0.2,0)
    aliens.append(new_alien)






# This is our actual game loop - this while statement will loop forever
while 1:

    # First, we need to deal with moving the spaceship.
    # pygame.key.get_pressed() returns a list of keys that are currently down
    pressed_keys = pygame.key.get_pressed()

    # If the a key is pressed and the spaceship is not on the left border, make it go left
    if pressed_keys[loc.K_a] and spaceship.position.x > 0:
        spaceship.velocity.x = -0.3

    # Ditto for d key and right
    elif pressed_keys[loc.K_d] and spaceship.position.x < 620:
        spaceship.velocity.x = 0.3

    # Otherwise, have it stay still
    else:
        spaceship.velocity.x = 0


    # Now, let's deal with the aliens. We want them to bounce horizontally across the screen,
    # Going down a bit every time they hit a wall
    for alien in aliens:

        if alien.position.x > 610:
            alien.move(vec(610, alien.position.y))
            alien.velocity.x *= -1
            alien.move(alien.position + vec(0,32))
     
        if alien.position.x < 0:
            alien.move(vec(0, alien.position.y))
            alien.velocity.x *= -1
            alien.move(alien.position + vec(0,32))
        
        # If an alien is being hit by a bullet, both the alien and the bullet should be destroyed
        # When creating bullets, we added a tag "bullet" to them. So all we need to do is
        # check if each alien is colliding with something with that tag, and then kill both
        # the alien and the agent it's collding with

        hit_bullet = alien.is_colliding_tag("bullet")
        if hit_bullet:
            aliens.remove(alien)
            hit_bullet.kill()
            alien.kill()
        
    libchar.update()
