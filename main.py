import pygame

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

    def draw(self, win):
        win.blit(self.img, [self.x, self.y, self.width, self.height])
        

def redrawGameWindow():
    win.blit(bg, (0,0))
    player.draw(win)
    pygame.display.update()


player = Player()
run = True
while run:
    clock.tick(60)
    if not gameover:
        pass

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    redrawGameWindow()
pygame.quit()
