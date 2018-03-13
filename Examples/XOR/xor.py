import sys
import random
import math
import numpy
import pygame
import pygame.gfxdraw
from pygame.locals import *

#PYGAME INIT------------------------------------------------------------------------------------------------

pygame.init()

DISPLAY_WIDTH = 1200
DISPLAY_HEIGHT = 900
DISPLAY_AREA = DISPLAY_WIDTH * DISPLAY_HEIGHT
DS = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))


# FUNCTIONS ------------------------------------------------------------------------------------------------ FUNCTIONS
def event_handler():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

#LOADING DATA-------------------------------------------------------------------------------------------------



#MAIN LOOP---------------------------------------------------------------------------------------------------

while True:
    event_handler()
    pygame.draw.rect(DS,(0,0,0),(97,97,286,286),0)





    pygame.display.update()
    DS.fill([255, 255, 255])