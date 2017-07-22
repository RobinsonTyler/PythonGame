import pygame
import sys
from pygame.locals import *

WIN_SIZE = (480, 320)

pygame.init()

FPS = 60
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode(WIN_SIZE)

UPDATE_BLOCKS = []

testPos = [0, 0]
directX = 1
directY = 1
pygame.display.set_caption("This is going to be great")

testImage = pygame.image.load("res/Test.png")

while True:  #Main Game Loop
    DISPLAYSURF.fill((0, 0, 0))
    for event in pygame.event.get():    #Event handling
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    UPDATE_BLOCKS.insert(0, DISPLAYSURF.blit(testImage, (testPos)))

    testPos[0] += directX
    testPos[1] += directY
    if testPos[0] < 0 or testPos[0] + 64 > WIN_SIZE[0]:
        directX *= -1
    if testPos[1] < 0 or testPos[1] + 64 > WIN_SIZE[1]:
        directY *= -1
    pygame.display.update(UPDATE_BLOCKS)
    fpsClock.tick(FPS)