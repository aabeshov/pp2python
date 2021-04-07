import pygame
import random , time
from pygame.locals import *

pygame.init()
FPS = pygame.time.Clock()

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
SPEED = 1

bg = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
COLORROAD = (139,191,251)
PURPLE = (140,0,168)
done = False
bg.fill(WHITE)
pygame.display.set_caption("NEON STREETRACING ULTIMATE X")

SCORE = 0
font = pygame.font.SysFont("ComicSans",35)
font2 = pygame.font.SysFont("ComicSans",50)
font3 = pygame.font.SysFont("ComicSans",45)

background = pygame.image.load("background1.png")

deadscene =pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.SRCALPHA)
deadscene.fill((128,128,128)) #Gray Color
deadscene.set_alpha(200)
money = []
RectForScore = pygame.Surface((200,40), pygame.SRCALPHA)
RectForScore.set_alpha(150)
RectForScore.fill((BLACK))

class GameObject(object):
    def __init__(self, x=10, y=10, color=(255, 255, 255), speed=8):
        self.x = x
        self.y = y
        self.color = color
        self.up = True
        self.down = False
        self.left = False
        self.right = False
        self.speed = speed
        self.hero = False

    def direction(self, right=False, left=False, down=False, up=False):
        self.right = right
        self.left = left
        self.up = up
        self.down = down

    def move(self):
        if self.right:
            self.x += self.speed
        elif self.left:
            self.x -= self.speed

    def fall(self):
        pass


font = pygame.font.Font("justicehalf.ttf",35)
font2 = pygame.font.Font("justicehalf.ttf",65)
font3 = pygame.font.Font("justicehalf.ttf",45)




class Rectangle(GameObject):
    def __init__(self, x=10, y=10, color=(255, 255, 255), width=30, height=30, speed=8):
        GameObject.__init__(self, x, y, color)
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        pygame.draw.rect(
            bg, self.color, (self.x, self.y, self.width, self.height))
        # hitbox draw
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        # pygame.draw.rect(
        #     win, [0, 255, 0], (self.x, self.y, self.width, self.height), 1)

    def fall(self):
        if not self.hero:
            self.y += self.speed
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("po_naexali.png")
        self.image = pygame.transform.scale(self.image,(40,80))
        self.surf = pygame.Surface((50, 80))
        self.rect = self.surf.get_rect(center = (random.randint(240, SCREEN_WIDTH-240)
                                               ,0))   
 
      def move(self,):
        
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > SCREEN_HEIGHT+50):
            self.rect.top = 0
            self.rect.center = (random.randint(240, 560), 0)
 
      def draw(self, Surface):
        Surface.blit(self.image, self.rect) 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("player.png")
        self.image = pygame.transform.scale(self.image,(40,90))
        self.surf = pygame.Surface((50, 100))
        self.rect = self.surf.get_rect(center = (400
                                               ,750)) 
        
 
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        #if self.rect.top > 0:
            #if pressed_keys[K_UP]:
                #self.rect.move_ip(0, -3)
        #if self.rect.bottom < SCREEN_HEIGHT:    
            #if pressed_keys[K_DOWN]:
                #self.rect.move_ip(0,3)
         
        if self.rect.left > 200:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-8,0)
        if self.rect.right < SCREEN_WIDTH-200:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(8, 0)

 
    def draw(self, Surface):
        Surface.blit(self.image, self.rect)     
class Coin(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Coin.png")
        self.image = pygame.transform.scale(self.image,(20,20))
        self.surf = pygame.Surface((50, 80))
        self.rect = self.surf.get_rect(center = (random.randint(230, SCREEN_WIDTH-230)
                                               ,0))   
 
      def move(self,):
        global SCORE
        self.rect.move_ip(0,4)
        if (self.rect.bottom > SCREEN_HEIGHT):
            self.rect.top = 0
            self.rect.center = (random.randint(220, SCREEN_WIDTH-220), 0)
 
      def draw(self, Surface):
        Surface.blit(self.image, self.rect)

      def GetPoints(self):
           global SCORE
           if pygame.sprite.spritecollideany(P1,coins):
               if SPEED < 10:
                  SCORE += 1
               if SPEED > 10:
                   SCORE +=2
leftlines = []
leftline1 = Rectangle(300, -200, COLORROAD, 7, 150, 3)
leftline2 = Rectangle(300, 0, COLORROAD, 7, 150, 3)
leftline3 = Rectangle(300, 200, COLORROAD, 7, 150, 3)
leftline4 = Rectangle(300, 400, COLORROAD, 7, 150, 3)
leftlines.extend([leftline1, leftline2, leftline3, leftline4])


rightlines = []
rightline1 = Rectangle(500, -200, COLORROAD, 7, 150, 3)
rightline2 = Rectangle(500, 0, COLORROAD, 7, 150, 3)
rightline3 = Rectangle(500, 200, COLORROAD, 7, 150, 3)
rightline4 = Rectangle(500, 400, COLORROAD, 7, 150, 3)
rightlines.extend([rightline1, rightline2, rightline3, rightline4])

P1 = Player()
E1 = Enemy()
C1 = Coin()




INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)


coins = pygame.sprite.Group()
coins.add(C1)




enemies = pygame.sprite.Group()
enemies.add(E1)


CongratText = "Congritulations, You Win!"
CongratText2 = "You are the Greatest!"

WinText = font3.render(CongratText,True,PURPLE)
WinText2 = font2.render(CongratText2,True,PURPLE)




all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)


end = pygame.image.load("dead.png") 
def winUpdate():
        for l in leftlines:
            l.draw()
            l.fall()
            if l.y > 800:
                l.y = -50
        for l in rightlines:
            l.draw()
            l.fall()
            if l.y > 800:
                l.y = -50        

pygame.mixer.music.load('sound.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.1)
while not done:
    bg.fill(WHITE)
    bg.blit(background,(0,0))
    bg.blit(RectForScore,(0,0))
    
    ScoreText = font.render(f'Score:{SCORE}',True,(98,0,117))
    bg.blit(ScoreText,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            done = True
        if event.type == INC_SPEED:
                if SPEED < 15:
                    SPEED += 1



    winUpdate()
        
    
    C1.move()
    C1.GetPoints()

     
    P1.draw(bg)
    E1.draw(bg)
    C1.draw(bg)
         


    





    for entity in all_sprites:
        bg.blit(entity.image, entity.rect)
        entity.move()
 
    #To be run if collision occurs between Player and Enemy


    if SCORE >1000:
           SCORE =1000
           TotalScore = font2.render(f'Your Total Score:{SCORE}',True,PURPLE)
           time.sleep(0.5)
           pygame.mixer.pause()
           bg.blit(deadscene,(0,0))
           pygame.mixer.music.load('TheGreatestSound.mp3')
           pygame.mixer.music.play()
           bg.blit(WinText,(30,400))
           bg.blit(WinText2,(20,500))
           bg.blit(TotalScore,(10,300))  
           pygame.display.update()
           for entity in all_sprites:
                 entity.kill() 
           time.sleep(20)
           pygame.quit()
    
    if pygame.sprite.spritecollideany(P1, enemies):

          time.sleep(0.5)
          pygame.mixer.music.pause()
          TotalScore = font2.render(f'Your Total Score:{SCORE}',True,PURPLE)
          pygame.mixer.music.load('crashmusic.mp3')
          pygame.mixer.music.play()
          f = open("Points.txt","a")
          f.write("You got" + " " + str(SCORE) + " Points.\n" )



          bg.blit(deadscene,(0,0))
          bg.blit(end,(200,200))
          bg.blit(TotalScore,(60,270))  
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(5)
          pygame.quit()







    FPS.tick(120)
    pygame.display.update()



pygame.quit()    