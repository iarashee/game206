from pygame import *
from pygame.sprite import *
from random import *

DELAY = 1200; #Seed a timer to move sprite; [What does this do?]

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

    def move(self, dx):
        x = self.rect.x
        x += dx
        self.rect.x = x

class Ball(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("ball.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = randint(10, display_h-10)
        self.rect.y = 100

    def move_down(self):
        y = self.rect.y
        y += 10
        self.rect.y = y

    def reset(self):
        self.rect.x = randint(10, display_h-10)
        self.rect.y = 100

init()

hoop = Hoop()
ball = Ball()
sprites = RenderPlain(hoop, ball)

time.set_timer(USEREVENT + 1, DELAY)

f = font.Font(None, 25)

mixer.music.load("blobtales.wav")
mixer.music.play(-1)

crashed = False
game_off = False

swoosh = 0
while not crashed:
    for e in event.get():
        if e.type == KEYDOWN:
            
            if e.key == K_LEFT:
                hoop.move(dx = -20)
            
            if e.key == K_RIGHT:
                hoop.move(dx = 20)
                if hoop.rect.x > (display_w-200):
                    crashed = True
            
            if e.key == K_q:
                t = f.render("QUIT", False, (0,0,0)) # text not working
                screen.blit(t, (320, 0))
                crashed = True

        #if e.type == USEREVENT + 1:
            #hoop.move()
        
        if hoop.rect.colliderect(ball.rect):
            mixer.Sound("swoosh.wav").play()
            swoosh += 1
            ball.reset()

        if swoosh > 5: ## Fix!! Needs to increase speed
            DELAY -= 50

        if ball.rect.y >= (display_h - 5):
            t6 = f.render("Hit Bottom, Game Done", False, (0,0,0))
            screen.blit(t6, (200, 350))
            game_off = True

    screen = display.set_mode((display_w, display_h))
    display.set_caption("Basketball!")
    screen.blit(bg_image, (0,0))

    t1 = f.render("Baskets = " + str(swoosh), False, (0,0,0))
    t2 = f.render("q = Quit", False, (0,0,0))
    t3 = f.render("Directions: Catch the basketballs. Balls move down faster over time. You lose when you miss.", False, (0,0,0))
    t4 = f.render(str(DELAY), False, (0,0,0))
    t5 = f.render(str(ball.rect.y), False, (0,0,0))
    
    screen.blit(t1, (100, 100))
    screen.blit(t2, (100, 150))
    screen.blit(t3, (100, 200))
    screen.blit(t4, (100, 250))
    screen.blit(t5, (100, 300))
    
    
    while not game_off:
        ball.move_down()

    #screen.fill(bgcolor)
    sprites.update()
    sprites.draw(screen)
    display.update()