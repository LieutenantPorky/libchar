import pygame


screen = None
background = None
dt = 0.1
dying = []
living = []
character_list = []
groups = {}
clock = None

frame = 0
gc_int = 40



def setup(width = 640, height=480, init_background = None):
    global screen
    global background
    global clock

    screen = pygame.display.set_mode((width,height))
    clock = pygame.time.Clock()
    if init_background:
        background = pygame.image.load(init_background).convert()
        screen.blit(background, (0,0))
    else:
        background = screen.copy()

    pygame.display.update()



class Agent:
    img = None
    img_original = None
    position = pygame.math.Vector2(0,0)
    velocity = pygame.math.Vector2(0,0)
    rotation = 0
    tags = []

    def __init__(self, image, init_position = None):
        self.img = pygame.image.load(image).convert_alpha()
        self.tags = []
        self.img_original = None
        self.velocity = pygame.math.Vector2(0,0)
        if init_position:
            self.position = init_position

        global living
        living.append(self)

    def move(self, newpos):
        self.clear()
        self.position = newpos
        self.draw()

    def step(self):
        global dt
        self.position += self.velocity * dt
    
    def set_rotation(self, angle):
        if not self.img_original:
            self.img_original = self.img.copy()

        self.rotation = angle
        self.img = pygame.transform.rotate(self.img_original, angle)

    def rotate(self, angle):
        self.rotation += angle
        self.set_rotation(self.rotation)

    def clear(self):
        global screen
        global background

        screen.blit(background, self.img.get_rect().move(self.position), self.img.get_rect().move(self.position))



    def draw(self):
        global screen
        screen.blit(self.img, self.img.get_rect().move(self.position))
    
    def kill(self):
        global dying, living, groups
        dying.append(self)
        living.remove(self)
        if len(self.tags):
            for i in self.tags:
                groups[i].remove(self)

    def get_rect(self):
        return self.img.get_rect().move(self.position)
    
    def is_colliding(self, other):
        return self.get_rect().colliderect(other.get_rect())
    
    def is_colliding_tag(self, test_tag):
        global groups
        if not test_tag in groups.keys():
            return None
        for i in groups[test_tag]:
            if self.is_colliding(i):
                return i
        return None


    def add_tag(self, tag):
        print("added tag")
        global groups
        if tag in self.tags:
            print(self.tags)
            return None
        self.tags.append(tag)
        
        if tag in groups:
            old = groups[tag]
            old.append(self)
            print(old)
            groups[tag] = old
        else:
            groups[tag] = [self]

    def remove_tag(self,tag):
        global groups
        if not tag in self.tags:
            return None
        groups[tag].remove(self)
        self.tags.remove(tag)


class Character(Agent):
    event_bindings = {}

    def __init__(self, image, init_position = None):
        super().__init__(image, init_position)
        global character_list
        character_list.append(self)
    
    def kill(self):
        global character_list
        character_list.remove(self)
        super().kill()
        
        
    def event(self, key, fn):
        self.event_bindings[key] = fn

    def pull_event(self, key):
        if key in self.event_bindings:
            self.event_bindings[key](self)




def obj_clean():
    global living
    size = pygame.display.get_window_size()
    for obj in living:
        if not obj in character_list:
            if (abs(obj.position.x) > size[0] * 2) or (abs(obj.position.y) > size[1] *2):
                obj.kill()



def update():
    
    for ev in pygame.event.get(eventtype = pygame.KEYDOWN):
        for char in character_list:
            char.pull_event(ev.key)



    global clock
    global dt
    global living
    global dying
    global frame
    dt = clock.tick()
    frame += 1

    if not frame % gc_int:
        obj_clean()
    for i in dying:
        i.clear()
        del i
    for i in living:
        i.clear()
    for i in living:
        i.step()
    for i in living:
        i.draw()
    pygame.display.update()
