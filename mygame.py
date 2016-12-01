from pygame import *
from pygame.sprite import *
from random import *

DELAY = 700; #Seed a timer to move sprite; [What does this do?]

#bgcolor = (0,0,225)    
bg_image = image.load("bcourt.bmp")


display_h = 716
display_w = 1261
#screen_rect = Rect((0,0), (display_w, display_h))

class Hoop(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("hoop.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = display_w*0.45
        self.rect.y = display_h*0.8

    #def move(self):
    #    x = self.rect.x
    #    self.rect.x = x

class Ball(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("ball.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100

    def move(self, dx):
        x = self.rect.x
        x += dx
        self.rect.x = x

    def move_down(self):
        y = self.rect.y
        y += 10
        self.rect.y = y

init()

hoop = Hoop()
ball = Ball()
sprites = RenderPlain(hoop, ball)

time.set_timer(USEREVENT + 1, DELAY)

f = font.Font(None, 25)

mixer.music.load("blobtales.wav")
mixer.music.play(-1)

crashed = False

swish = 0
while not crashed:
    for e in event.get():
        if e.type == KEYDOWN:
            
            if e.key == K_LEFT:
                ball.move(dx = -10)
            
            if e.key == K_RIGHT:
                ball.move(dx = 10)
                if ball.rect.x > (display_w-200):
                    crashed = True
            
            if e.key == K_q:
                #t = f.render("QUIT", False, (0,0,0)) # text not working
                #screen.blit(t, (320, 0))
                crashed = True

        #if e.type == USEREVENT + 1:
            #hoop.move()

        if hoop.rect.colliderect(ball.rect):
            swish += 1

    screen = display.set_mode((display_w, display_h))
    display.set_caption("Dodge 'Em!")

    t = f.render("Swishes = " + str(swish), False, (255,255,25))
    screen.blit(t, (320, 0))

    screen.blit(bg_image, (0,0))
    ball.move_down()

    #screen.fill(bgcolor)
    sprites.update()
    sprites.draw(screen)
    display.update()