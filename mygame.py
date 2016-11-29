# Dig for gold
# Based on Whack-a-mole game using pygame by Kimberly Todd

from pygame import *
from pygame.sprite import *
from random import *

DELAY = 1000;            #Seed a timer to move sprite

bgcolor = (0,42,196)    #Color taken from background of sprite

class Car(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("myface.bmp").convert_alpha()
        self.rect = self.image.get_rect()

    # move gold to a new random location
    def move(self):
        randX = randint(0, 600)
        randY = randint(0, 400)
        self.rect.center = (randX,randY)


    # Did shovel/cursor collide the gold?
    def hit(self, target):
        return self.rect.colliderect(target)

    #The shovel sprite will move with the mousepointer
    def update(self):
        self.rect.center = mouse.get_pos()

class Distract(Car):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("poop.bmp").convert_alpha()
        self.rect = self.image.get_rect()


#main
init()

screen = display.set_mode((640, 480))
display.set_caption("Play Dodge 'Em!")

# hide the mouse cursor so we only see shovel
mouse.set_visible(False)

f = font.Font(None, 25)

# create the mole and shovel using the constructors
car = Car()
distract = Distract()
# creates a group of sprites so all can be updated at once
sprites = RenderPlain(car, distract)

hits = 0
time.set_timer(USEREVENT + 1, DELAY)

x = (display_width*0.45)
y = (display_height*0.8)

x_chng = 0

thing_strt_x =  random.randrange(0, display_width)
thing_strt_y = -600
thing_speed = 4
thing_width = 100
thing_height = 100
thing_count = 1
dodged = 0

# loop until user quits
while True:
    for event in event.get()
        e = event.get()
        if e.type == QUIT:
            quit()
            break

        elif e.type == KEYDOWN:
            if event.key == K_LEFT:
                # car goes left

            if e.type == K_RIGHT:
                # car goes right

                # reset timer
                time.set_timer(USEREVENT + 1, DELAY)
                
        elif e.type == USEREVENT + 1: # TIME has passed
            car.move()
            distract.move()

    # refill background color so that we can paint sprites in new locations
        screen.fill(bgcolor)
        t = f.render("Jackpot = " + str(hits), False, (0,0,0))
        screen.blit(t, (320, 0))        # draw text to screen.  Can you move it?

        # update and redraw sprites
        sprites.update()
        sprites.draw(screen)
        display.update()
