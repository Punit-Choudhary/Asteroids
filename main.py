import pygame
import math
import random

pygame.init()

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
lives = 3
score = 0

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
                        (random.choice([-1 * self.w - 5, s_width + 5]),
                        random.randrange(0, s_height - self.h))])

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
    font = pygame.font.SysFont('arial', 30)
    livesText = font.render('Lives: ' + str(lives), 1, (255, 255, 255))
    playAgainText = font.render('Press Space to Play Again', 1, (255, 255, 255))
    scoreText = font.render('Score: ' + str(score), 1, (255, 255, 255))


    for a in asteroids:
        a.draw(win)

    for b in playerBullets:
        b.draw(win)
    if gameover:
        win.blit(playAgainText, (s_width // 2 - playAgainText.get_width() // 2, s_height // 2 - playAgainText.get_height() // 2))

    win.blit(scoreText, (s_width - scoreText.get_width() - 25, 25))
    win.blit(livesText, (25, 25))
    pygame.display.update()


player = Player()
playerBullets = []
asteroids = []
count = 0
run = True
while run:
    clock.tick(60)
    count += 1
    if not gameover:
        
        if count % 50 == 0:
            rn = random.choice([1, 1, 1, 2, 2, 3])
            asteroids.append(Asteroid(rn))

        player.updateLocation()
        for b in playerBullets:
            b.move()

            if b.checkOffScreen():
                playerBullets.pop(playerBullets.index(b))
            
        for a in asteroids:
            a.x += a.xv
            a.y += a.yv

            if (player.x >= a.x and player.x <= a.x + a.w) or (player.x + player.width >= a.x and player.x + player.width <= a.x + a.w):
                if (player.y >= a.y and player.y <= a.y + a.h) or (player.y + player.height >= a.y and player.y + player.height <= a.y + a.h):
                    lives -= 1
                    asteroids.pop(asteroids.index(a))
                    break

            # Asteroid bullet collision
            for b in playerBullets:
                if (b.x >= a.x and b.x <= a.x + a.w) or b.x + b.w >= a.x and b.x + b.w <= a.x + a.w:
                    if (b.y >= a.y and b.y <= a.y + a.h) or b.y + b.h >= a.y and b.y + b.h <= a.y + a.h:

                        if a.rank == 3:
                            score += 10
                            na1 = Asteroid(2)
                            na2 = Asteroid(2)
                            na1.x = a.x
                            na2.x = a.x
                            na1.y = a.y
                            na2.y = a.y

                            asteroids.append(na1)
                            asteroids.append(na2)

                        elif a.rank == 2:
                            score += 20
                            na1 = Asteroid(1)
                            na2 = Asteroid(1)
                            na1.x = a.x
                            na2.x = a.x
                            na1.y = a.y
                            na2.y = a.y

                            asteroids.append(na1)
                            asteroids.append(na2)
                        else:
                            score += 30

                        asteroids.pop(asteroids.index(a))
                        playerBullets.pop(playerBullets.index(b))
        
        if lives <= 0:
            gameover = True
        
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
                else:
                    gameover = False
                    lives = 3
                    score = 0
                    asteroids.clear()
            if event.key == pygame.K_q:
                run = False
    
    redrawGameWindow()
pygame.quit()
