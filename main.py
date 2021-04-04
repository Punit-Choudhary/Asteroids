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

def redrawGameWindow():
    win.blit(bg, (0,0))

    pygame.display.update()

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
