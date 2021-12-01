#--------
#Pygame_Summative
#Graden_Rusk
#Nov_9_2021
#--------
#Credits
#Music from Kirill Belooussov
#sounds
#captaincrunch80
#----Info----#
import pygame
import random
import time
from os import path

#starting speeds
WIDTH = 800
HEIGHT = 600
FPS = 120
ball_speedy = 0
ball_speedx = 0

#sets the colorsheme
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED =  (255, 0, 0)
#dictionaries and the lists for the programs
Ball_y_speed = {'ball_speedy' : -3}
Ball_x_speed = {'ball_speedx' : -2}
Player_s = []
Player_2_s= []

#loads up images, music, and sounds.
pygame.mixer.init()
mobs = pygame.sprite.Group()
clock = pygame.time.Clock()
img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')
hit_sound = pygame.mixer.Sound(path.join(snd_dir, 'ping_pong_8bit_plop.ogg'))
pass_sound = pygame.mixer.Sound(path.join(snd_dir, 'ping_pong_8bit_peeeeeep.ogg'))
pygame.mixer.music.load(path.join(snd_dir, 'KB - Game Intro Menu Music.mp3'))
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(loops=-1)

font_name = pygame.font.match_font('Eras Demi ITC')#tells what format to print in
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
    

class Player(pygame.sprite.Sprite):#seats attributes for the first player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((16, 60))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH - 50
        self.rect.centery = HEIGHT / 2

    def update(self):
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.speedy = -8
        if keystate[pygame.K_DOWN]:
            self.speedy = 8
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.rect.bottom = 0
        if self.rect.bottom < 0:
            self.rect.top = HEIGHT

class Player_2(pygame.sprite.Sprite):#stes attributes for the 2nd player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((16, 60))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH - 750
        self.rect.centery = HEIGHT / 2

    def update(self):
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w]:
            self.speedy = -8
        if keystate[pygame.K_s]:
            self.speedy = 8
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.rect.bottom = 0
        if self.rect.bottom < 0:
            self.rect.top = HEIGHT

class Ball_1(pygame.sprite.Sprite):#sets attributs for the ball
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((16, 16))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2

    def update(self):
        hit_player = pygame.sprite.collide_rect(player, ball)#looking for ball hitting the pattles
        hit_player_2 = pygame.sprite.collide_rect(player_2, ball)
        if hit_player == False and hit_player_2 == False:
            if (ball.rect.centerx > 0) or (ball.rect.centerx < 700):
                ball_y = ball.rect.centery
                ball_x = ball.rect.centerx
                ball_time = pygame.time.get_ticks()
                ball_speedy = Move(ball_y, ball_x, HEIGHT, WIDTH, ball_time)
                new_ball_speedy = Ball_y_speed.get('ball_speedy')
                ball.rect.centery = ball.rect.centery + new_ball_speedy
                new_ball_speedx = Ball_x_speed.get('ball_speedx')
                ball.rect.centerx = ball.rect.centerx + new_ball_speedx
        if hit_player_2:
            hit_sound.play()
            Ball_x_speed.clear()
            Ball_x_speed['ball_speedx'] = (2)
            new_ball_speedx = Ball_x_speed.get('ball_speedx')
            ball.rect.centerx = ball.rect.centerx + new_ball_speedx
        if hit_player:
            hit_sound.play()
            Ball_x_speed.clear()
            Ball_x_speed['ball_speedx'] = (-2)
            new_ball_speedx = Ball_x_speed.get('ball_speedx')
            ball.rect.centerx = ball.rect.centerx + new_ball_speedx
#the ball moving function        
def Move(ball_y, ball_x, HEIGHT, WIDTH, ball_time):
    if ball_y >= HEIGHT:#checks for ball at height limits
        hit_sound.play()
        Ball_y_speed.clear()
        Ball_y_speed['ball_speedy'] = (-3)
        ball_speedy = -3
        return ball_speedy
    if ball_y <= 0:#checks of ball is at the height limits
        hit_sound.play()
        Ball_y_speed.clear()
        Ball_y_speed['ball_speedy'] = (3)
        ball_speedy = 3
        return ball_speedy
    if ball_x > WIDTH + 50:#checks if ball is off screen right
        pass_sound.play()# working here
        Player_s.append(1)
        time.sleep(1)
        ball.rect.centerx = WIDTH / 2
        ball.rect.centery = HEIGHT / 2
        return ball.rect.centerx and ball.rect.centery
    if ball_x < -50:#checks to see if the ball is off the screen to the left
        pass_sound.play()# working here
        Player_2_s.append(1)
        time.sleep(1)
        ball.rect.centerx = WIDTH / 2
        ball.rect.centery = HEIGHT / 2
        return ball.rect.centerx and ball.rect.centery
#start screen function
def show_go_screen():
    screen.blit(background, background_rect)
    draw_text(screen, "PING", 64, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, "Player 1 (left) use w and s, Player 2 (right) use up and down keys", 22,
              WIDTH / 2, HEIGHT / 2)
    draw_text(screen, "First to Three wins", 18, WIDTH / 2, HEIGHT * 5 / 8)
    draw_text(screen, "Press any key to begin", 18, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False
#the ending screen function
def End_screen():
    screen.blit(background, background_rect)
    draw_text(screen, "PING", 64, WIDTH / 2, HEIGHT / 4)
    if player_score >= 3:
        draw_text(screen, "Player 2 Loses!", 35,#calls the draw text function
              WIDTH / 2, HEIGHT / 2)
    if player_2_score >= 3:
        draw_text(screen, "Player 1 Wins!", 35,#and again here
              WIDTH / 2, HEIGHT / 2)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

pygame.init()#initialized pygam and music
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping")
clock = pygame.time.Clock()
background = pygame.image.load(path.join(img_dir, "fancy-court.png")).convert()#what the background will look like.
background_rect = background.get_rect()

all_sprites = pygame.sprite.Group()#adds all sprites to group
player = Player()
player_2 = Player_2()
ball = Ball_1()
mobs.add(ball)
all_sprites.add(player, player_2, ball)

running = True
game_over = True
while running:
    clock.tick(FPS)
    if game_over:
        show_go_screen()
        game_over = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player_score = sum(Player_s)
    player_2_score = sum(Player_2_s)
    if player_score >= 3 or player_2_score >= 3:
        End_screen()
    all_sprites.update()
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    draw_text(screen, str(player_2_score), 18, WIDTH / 2 + 50, 10)
    draw_text(screen, str(player_score), 18, WIDTH / 2 - 50, 10)
    pygame.display.flip()

pygame.quit()

#1. The difference between OOP and procedural coding is that you can write the code for the attributes of something, and if you have two
#things with attributes that will be close to the same you can run through the same code. for OOP when you code you only have to change
#little bits of the code to change an outcome, while with procedural coding you have to change almost everything on many lines. with OOP,
#you also name things differently like classes and methods, you also need to have an initialization at the start of the class.
#Also it takes self from what you start the class with and makes the attributes specifically for it.

#2. If my program was made in procedural coding it would take alot of functions for it to run, it would constantly be calling different functions,
#it wouls also be very slow because it would have to run through hundreds of lines of code. it would be very laggy. also it would take forever
#to code all of it and make it work properly. It would be really long and tedious to repeat all of the lines of code.

#3. The benefits of OOP is that you can reuse the same lines of code for the attributes to be given to different things, also you can make the
#amount of code shorter. You can also fix problems easier and faster because of the shorter code. you can also use sprites and make the program work
#better because of calling the update function. also you can reuse anything in any class that you need to.

#4. Some of the drawbacks of OOP is that it is confusing to learn at the start. it isn't for everybody as it doesn't neccesarily make sense off the bat
#second of all is that they usually take longer to run than procedural programs, and they may at some times even use more code than proceudral. some
#other drawbacks is that it can get very confusing the farhter you get into the code because it's hard to learn you can get confused easily.