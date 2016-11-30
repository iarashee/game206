from pygame import *
from pygame.sprite import *
from random import *

DELAY = 1000; #Seed a timer to move sprite; [What does this do?]

bgcolor = (0,0,225)    

class Car(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("racecar.bmp").convert_alpha()
        self.rect = self.image.get_rect()

        def move(self):
            x = 200
            y = 200
            self.rect.center = (x, y)

    # move gold to a new random location
    #def move_up(self):
        #x_change = randint(0, 600)

        #self.rect.center = (randX,randY)

    #The shovel sprite will move with the mousepointer
    #def update(self):
        self.rect.center = mouse.get_pos()

class Block(Car):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("poop.bmp").convert_alpha()
        self.rect = self.image.get_rect()

while True:
    e = event.poll()
    if e.type == KEYDOWN:
        if e.key == K_LEFT:
            x = x - 5
            car.move()

screen = display.set_mode((640, 480))
display.set_caption("Dodge 'Em!")

screen.fill(bgcolor)

car = Car()
block = Block()

car_s = RenderPlain(car)
block_s = RenderPlain(block)

car_s.update()
block_s.update()

car_s.draw(screen)
block_s.draw(screen)

display.update()