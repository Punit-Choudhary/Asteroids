import pygame
import math

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
        self.head = (self.x + self.cosine + self.width // 2, self.y - self.sine * self.height // 2)

    def turnRight(self):
        self.angle -= 5
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine + self.width // 2, self.y - self.sine * self.height // 2)
    
    def moveForward(self):
        self.x += self.cosine * 6
        self.y -= self.sine * 6
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine + self.width // 2, self.y - self.sine * self.height // 2)


def redrawGameWindow():
    win.blit(bg, (0,0))
    player.draw(win)
    pygame.display.update()


player = Player()
run = True
while run:
    clock.tick(60)
    if not gameover:
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
    
    redrawGameWindow()
pygame.quit()
