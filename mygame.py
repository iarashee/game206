from pygame import *
from pygame.sprite import *
from random import *

DELAY = 1000; # Delay
   
bg_image = image.load("bcourt.bmp") # Load background image

display_h = 716 # Display height
display_w = 1261 # Display width


class Hoop(Sprite): # Hoop sprite
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("hoop.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = display_w*0.45
        self.rect.y = display_h*0.8

    def move(self, dx): # Move hoop
        x = self.rect.x
        x += dx
        self.rect.x = x

class Ball(Sprite): # Ball sprite
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("ball.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = randint(15, display_w-15)
        self.rect.y = 5

    def move_down(self, dy): # Move ball down
        y = self.rect.y
        y += dy
        self.rect.y = y

    def reset(self): # Return ball to top after scoring
        self.rect.x = randint(10, display_h-10)
        self.rect.y = 100

init()

print ("Name: Ibrahim A. Rasheed")
print ("Game: Catch the Basketball")
print ("Reference: Colleen: gold_game.py, shiv6146: https://github.com/shiv6146/Dodge-It")

hoop = Hoop()
ball = Ball()
sprites = RenderPlain(hoop, ball)

time.set_timer(USEREVENT + 1, DELAY)

f = font.Font(None, 25)
big_f = font.Font(None, 75)

mixer.music.load("blobtales.wav") # Background music
mixer.music.play(-1)

crashed = False
game_off = False
score = 0 # Score
while not crashed:
    while not game_off:
        for e in event.get(): # Key down events
            if e.type == KEYDOWN:
                
                if e.key == K_LEFT:
                    hoop.move(dx = -27)
                
                if e.key == K_RIGHT:
                    hoop.move(dx = 27)
            
        if hoop.rect.colliderect(ball.rect): # Add score if collision
            mixer.Sound("swoosh.wav").play() # Sound if score
            score += 1
            ball.reset()

        if score >= 0: # Increase speed
            ball.move_down(dy = 6)
        if score >= 2: 
            ball.move_down(dy = 6.10)
        if score > 5:
            ball.move_down(dy = 6.20)    
        if score > 7:
            ball.move_down(dy = 6.30)
        if score > 10:
            ball.move_down(dy = 6.5)


        if hoop.rect.x <= -45: # Restrict hoop from leaving screen left
            hoop.rect.x = -45

        if hoop.rect.x >= (display_w-300): # Restrict hoop from leaving scren right
            hoop.rect.x = (display_w-300)

        screen = display.set_mode((display_w, display_h)) # Create window
        display.set_caption("Basketball!")
        screen.blit(bg_image, (0,0))

        # Multiple screen texts to display
        t1 = big_f.render("Score = " + str(score), False, (0,0,0))
        t2 = f.render("q = Quit", True, (0,0,0))
        t3 = f.render("Directions: 1) Catch the basketballs. 2) Balls begin moving faster after 2. 3) You lose when you miss.", False, (0,0,0))
        
        screen.blit(t1, (100, 100))
        screen.blit(t2, (100, 150))
        screen.blit(t3, (100, 200))


        #Updates
        sprites.update()
        sprites.draw(screen)
        t6 = big_f.render("Hit Bottom, Game Done", False, (0,0,0))
        t = big_f.render("QUIT", False, (0,0,0))
        
        if ball.rect.y >= (display_h - 20):
            screen.blit(t6, (200, 250))
            game_off = True
        
        for e in event.get():
            if e.type == KEYDOWN:
                if e.key == K_q:
                    screen.blit(t, (200, 250))
                    game_off = True

        display.update()