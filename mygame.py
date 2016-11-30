from pygame import *
from pygame.sprite import *
from random import *

DELAY = 1000; #Seed a timer to move sprite; [What does this do?]

bgcolor = (0,0,225)    

dispaly_h = 700
display_w = 500

class Car(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("racecar.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = display_w*0.45
        self.rect.y = dispaly_h*0.8

    def move(self, dx):
        x = self.rect.x
        x += dx
        self.rect.x = x

class Block(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("poop.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100

    def move(self):
        y = self.rect.y
        y += -10
        self.rect.y = y

init()

car = Car()
block = Block()
sprites = RenderPlain(car, block)

time.set_timer(USEREVENT + 1, DELAY)

crashed = False
while not crashed:
    for e in event.get():
        if e.type == KEYDOWN:
            if e.key == K_LEFT:
                car.move(dx = -10)
            if e.key == K_RIGHT:
                car.move(dx = 10)

        elif e.type == USEREVENT + 1:
            block.move()

    screen = display.set_mode((display_w, dispaly_h))
    display.set_caption("Dodge 'Em!")

    screen.fill(bgcolor)
    sprites.update()
    sprites.draw(screen)
    display.update()