import sys
import random
import math
import numpy
import pygame
import pygame.gfxdraw
from pygame.locals import *
from nn import NeuralNetwork

#VARIABLES--------------------------------------
hidden_neurons = 4
bias = True
lrate = 0.1
#PYGAME INIT------------------------------------------------------------------------------------------------





pygame.init()

DISPLAY_WIDTH = 1000
DISPLAY_HEIGHT = 700
DISPLAY_AREA = DISPLAY_WIDTH * DISPLAY_HEIGHT
DS = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("XOR")

myFont =pygame.font.Font("FFFFORWA.TTF",35)
typewriter =pygame.font.Font("rm_typerighter_medium.ttf",45)
fnumbers = pygame.font.Font("rm_typerighter_medium.ttf",25)
options = typewriter.render("options",1,(255,255,255))
title = myFont.render("XOR learning simulation",1,(255,255,255))
hneurons = typewriter.render("hidden neurons : "+ str(hidden_neurons),1,(255,255,255))
biast = typewriter.render("Bias : ",1,(255,255,255))
lratet = typewriter.render("Learning rate : "+ str(lrate),1,(255,255,255))
falset = fnumbers.render("= 0",1,(255,255,255))
truet = fnumbers.render("= 1",1,(255,255,255))
numbers = []
for i in range(0,11,1):
    numbers.append(fnumbers.render(str(i/10),1,(255,255,255)))


# FUNCTIONS ------------------------------------------------------------------------------------------------ FUNCTIONS
def event_handler():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

#LOADING DATA-------------------------------------------------------------------------------------------------
brain =  NeuralNetwork([2,4,1],0.1)
res =10
cols = 30
rows = 30
#RESET FUNCTION---------------------------------------------------------------------
def resetf():
    global brain
    brain =  NeuralNetwork([2,hidden_neurons,1],lrate,bias)
    print("reset")
#BUTTON FUNCTION--------------------------------------------------------------------
class button():
    def __init__(self, normalcolor,overcolor, x, y, width, height,func, text=''):
        self.overcolor = overcolor
        self.normalcolor = normalcolor
        self.func= func
        self.color = self.normalcolor
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.clicked =True
    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 30)
            text = font.render(self.text, 1, (255, 255, 255))
            win.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))
        if self.isOver(mouse):
            self.color = self.overcolor
            if(mouseP[0]==1 and not self.clicked):
                self.func()
                self.clicked = True
            if(mouseP[0]==0):
                self.clicked = False

        else:
            self.color = self.normalcolor

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False





def more():
    global hidden_neurons
    global hneurons
    hidden_neurons +=1
    hneurons = typewriter.render("hidden neurons : " + str(hidden_neurons), 1, (255, 255, 255))
    resetf()
def less():
    global hidden_neurons
    global hneurons
    if(hidden_neurons>1):
        hidden_neurons -=1
        hneurons = typewriter.render("hidden neurons : " + str(hidden_neurons), 1, (255, 255, 255))
        resetf()

def biasf():
    global bias
    global biasb
    bias = not bias
    biasb = button((50, 50, 50), (100, 100, 100), 355 + 100, 582, 70, 25, biasf, str(bias))
    resetf()
    print(bias)

def ml():
    global lrate
    global lratet
    lratet = typewriter.render("Learning rate : "+ str(round(lrate,2)),1,(255,255,255))
    lrate +=0.02
    resetf()

def ll():
    global lrate
    global lratet
    lratet = typewriter.render("Learning rate : "+ str(round(lrate,2)),1,(255,255,255))
    lrate -=0.02
    resetf()

reset =button((50,50,50),(100,100,100),50,450,100,50,resetf,"Reset")
m = button((50,50,50),(100,100,100),228,603-40,16,16,more,"+")
l = button((50,50,50),(100,100,100),228,649-40,16,16,less,"-")
biasb = button((50,50,50),(100,100,100),355+100,582,70,25,biasf,str(bias))
mlb = button((50,50,50),(100,100,100),633+200,563,16,16,ml,"+")
llb = button((50,50,50),(100,100,100),633+200,609,16,16,ll,"-")
#SLIDER FUNCTION------------------------------



#TRAIN FUNCTION---------------------------------------------------------------------
def train():
    for i in range(100):


        brain.train([1, 1], [0])
        brain.train([1, 0], [1])
        brain.train([0, 1], [1])
        brain.train([0, 0], [0])


#MAIN LOOP---------------------------------------------------------------------------------------------------

while True:
    mouse = pygame.mouse.get_pos()
    mouseP = pygame.mouse.get_pressed()

    train()
    event_handler()

    #PREWIEV


    #pygame.draw.line(DS,(255,255,255),(20,98),(50,98),1)
    #pygame.draw.line(DS, (255, 255, 255), (20, 74), (353, 74), 1)
    #pygame.draw.line(DS, (255, 255, 255), (20, 74), (20, 353), 1)
    #pygame.draw.rect(DS,(255,255,255),(47,97,306,306),0)

    for i in range(11):
        DS.blit(numbers[i], (42+i*30, 90))
        DS.blit(numbers[i], (26, 107 +i *29))
    for i in range(cols):
        for j in range(rows):
            x1 =  i / cols
            x2 =  j / rows
            #print([x1,x2])
            y = brain.predict([x1,x2])
            #print(y)
            pygame.draw.rect(DS,(255-y*255,255-y*255,255-y*255),(50 + j*res,110+ i*res,res,res),0)

    pygame.draw.rect(DS, (255, 255, 255), (50, 415, 10, 10), 0)
    pygame.draw.rect(DS, (0, 0, 0), (150, 415, 10, 10), 0)
    DS.blit(falset, (70, 414))
    DS.blit(truet, (170, 414))
    #NEURONS
    for i in range(2):
        pygame.draw.circle(DS,(240,240,240),(500,200+ i* 100),20,2)
    for i in range(brain.nodes[1]):
        pygame.draw.circle(DS, (240, 240, 240), (650, 100 + i * int((400/brain.nodes[1])-1)), 24 - brain.nodes[1], 2)
    pygame.draw.circle(DS, (240, 240, 240), (800, 250), 20, 2)

    #MENU
    reset.draw(DS,(255,255,255))
    DS.blit(title,(DISPLAY_WIDTH/2-250,20))
    pygame.draw.rect(DS, (255, 255, 255), (50, 535, 900, 130), 1)
    pygame.draw.rect(DS, (42, 42, 42), (80, 520, 100, 20), 0)
    DS.blit(options, (89, 520))

    DS.blit(hneurons, (60, 620-40))
    DS.blit(biast,(290+100,580))
    DS.blit(lratet,(470+200,580))

    m.draw(DS,(255,255,255))
    l.draw(DS, (255, 255, 255))
    biasb.draw(DS,(255,255,255))
    mlb.draw(DS, (255, 255, 255))
    llb.draw(DS, (255, 255, 255))
    pygame.display.update()


    DS.fill([42, 42, 42])