import pygame
import math
import random

s_width = 800
s_height = 800

bg = pygame.image.load('asteroidsImages/starbg.png')
alienImg = pygame.image.load('asteroidsImages/alienShip.png')
playerRocket = pygame.image.load('asteroidsImages/spaceRocket.png')
star = pygame.image.load('asteroidsImages/star.png')
asteroid50 = pygame.image.load('asteroidsImages/asteroid50.png')
asteroid100 = pygame.image.load('asteroidsImages/asteroid100.png')
asteroid150 = pygame.image.load('asteroidsImages/asteroid150.png')

pygame.display.set_caption("Asteroids ~~ Punit Choudhary")
win = pygame.display.set_mode((s_width, s_height))

clock = pygame.time.Clock()

gameover = False

class Player(object):
    def __init__(self):
        self.img = playerRocket
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.x = s_width // 2
        self.y = s_height // 2

        self.angle = 0
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.width // 2, self.y - self.sine * self.height // 2)



    def draw(self, win):
        #win.blit(self.img, [self.x, self.y, self.width, self.height])
        win.blit(self.rotatedSurf, self.rotatedRect)

    def turnLeft(self):
        self.angle += 5
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.width // 2, self.y - self.sine * self.height // 2)

    def turnRight(self):
        self.angle -= 5
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.width // 2, self.y - self.sine * self.height // 2)
    
    def moveForward(self):
        self.x += self.cosine * 6
        self.y -= self.sine * 6
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.width // 2, self.y - self.sine * self.height // 2)
    
    def updateLocation(self):
        if self.x > s_width + 50:
            self.x = 0
        elif self.x < 0 - self.width:
            self.x = s_width
        elif self.y < -50:
            self.y = s_height
        elif self.y > s_height + 50:
            self.y = 0

class Bullet(object):
    def __init__(self):
        self.point = player.head
        self.x, self.y = self.point
        self.w = 4
        self.h = 4
        self.c = player.cosine
        self.s = player.sine
        self.xv = self.c * 10
        self.yv = self.s * 10

    def move(self):
        self.x += self.xv
        self.y -= self.yv

    def draw(self, win):
        pygame.draw.rect(win, (255, 255, 255), [self.x, self.y, self.w, self.h])
    
    def checkOffScreen(self):
        if self.x < -50 or self.x > s_width or self.y > s_height or self.y < -50:
            return True

class Asteroid(object):
    def __init__(self, rank):
        self.rank = rank
        if self.rank == 1:
            self.image = asteroid50
        elif self.rank == 2:
            self.image = asteroid100
        else:
            self.image = asteroid150
        self.w = 50 * rank
        self.h = 50 * rank
        self.ranPoint = random.choice([(random.randrange(0, s_width - self.w),
                        random.choice([-1 * self.h - 5, s_height + 5])),
                        (random.choice([-1 * self.w - 5, s_width + 5])),
                        random.randrange(0, s_height - self.h)])

        self.x, self.y = self.ranPoint

        if self.x < s_width // 2:
            self.xdir = 1
        else:
            self.xdir = -1
        
        if self.y < s_height // 2:
            self.ydir = 1
        else:
            self.ydir = -1
        
        self.xv = self.xdir * random.randrange(1, 3)
        self.yv = self.ydir * random.randrange(1, 3)
    

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

def redrawGameWindow():
    win.blit(bg, (0,0))
    player.draw(win)
    
    for b in playerBullets:
        b.draw(win)

    pygame.display.update()


player = Player()
playerBullets = []
asteroids = []
count = 0
run = True
while run:
    clock.tick(60)
    if not gameover:
        player.updateLocation()
        for b in playerBullets:
            b.move()

            if b.checkOffScreen():
                playerBullets.pop(playerBullets.index(b))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.turnLeft()
        if keys[pygame.K_RIGHT]:
            player.turnRight()
        if keys[pygame.K_UP]:
            player.moveForward()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not gameover:
                    playerBullets.append(Bullet())
            if event.key == pygame.K_q:
                run = False
    
    redrawGameWindow()
pygame.quit()
