import pygame
import sys
from pygame.locals import *

WIN_SIZE = (480, 320)

pygame.init()

FPS = 60
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode(WIN_SIZE)

testPos = 0
direct = 1
pygame.display.set_caption("This is going to be great")

testImage = pygame.image.load("res/Test.png")

while True:  #Main Game Loop
    DISPLAYSURF.fill((0, 0, 0))
    for event in pygame.event.get():    #Event handling
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.blit(testImage, (testPos, WIN_SIZE[1]/2))
    testPos += direct
    if testPos < 0 or testPos > WIN_SIZE[0]:
        direct *= -1
    pygame.display.update()
    fpsClock.tick(FPS)