import pygame, sys, math
import time
import random
import os
from pygame.locals import *

pygame.init()

black = (0,0,0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
bg1 = pygame.image.load("background1.png")
bg2 = pygame.image.load("background2.png")
currentScreen = bg1
img_path = 'sprite_0.png'
display_width = 640
display_height = 500

gameDisplay = pygame.display.set_mode((display_width, display_height))
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def game_intro():
    global currentScreen
    intro = True
    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # if cat.x > 600:
        #     if currentScreen == bg1:
        #         cat.x = 0
        #         # screen.fill((0,0,0))
        #         # screen.blit(bg2,(0,0))
        #         currentScreen = bg2
        #
        #     elif currentScreen == bg2:
        #         # screen.fill((0,0,0))
        #         # screen.blit(bg2,(0,0))
        #         currentScreen = bg2
        #         cat.x = 600
        #
        # elif cat.x < 0:
        #     if currentScreen == bg2:
        #         cat.x = 600
        #         # screen.fill((0,0,0))
        #         # screen.blit(bg1,(0,0))
        #         currentScreen = bg1
        #
        #     elif currentScreen == bg1:
        #         # screen.fill((0,0,0))
        #         # screen.blit(bg1,(0,0))
        #         currentScreen = bg1
        #         cat.x = 0
 ###### The sprite is going from top to bottom :D

        #cat.boundaries()
        cat.handle_keys()
        cat.boundaries()
        screen.fill((255, 255, 255))
        screen.blit(currentScreen, (0,0))
        cat.draw(screen)
        #cat.boundaries()
        #gameDisplay.fill(white)
        #largeText = pygame.font.Font('freesansbold.ttf',115)
        #TextSurf, TextRect = text_objects("A bit Racey", largeText)
        #TextRect.center = ((display_width/2),(display_height/2))
        #gameDisplay.blit(TextSurf, TextRect)
        button("Choice 1",150,390,100,50,green,bright_green,"wrong")
        button("Choice 2",350,390,100,50,red,bright_red, "wrong1")

        pygame.display.update()
        clock.tick(15)

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    #print(mouse)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "wrong":
                    #***action for what happens when you click button goes here
                    print("bye")
            elif action == "wrong1":
                    print("adios")
            elif action == "right":
                    print ("hello")
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(100/2)), (y+(50/2)))
    gameDisplay.blit(textSurf, textRect)

class Cat(object):
    def __init__(self):
        """The constructor of the class"""
        self.image = pygame.image.load(img_path)
        self.x = 0
        self.y = 0

    def handle_keys(self):
        """ Handle Keys """
        key = pygame.key.get_pressed()
        dist = 5
        if key[pygame.K_DOWN]:
            self.y += dist
        elif key[pygame.K_UP]:
            self.y -=dist
        if key[pygame.K_RIGHT]:
            self.x += dist
        elif key[pygame.K_LEFT]:
            self.x -= dist

    def draw(self, surface):
        """ Draw on surface"""
        surface.blit(self.image, (self.x, self.y))
    def boundaries(self):
        if self.x >= 600:
            if currentScreen == bg1:
                self.x = 0
                screen.fill((0,0,0))
                screen.blit(bg2,(0,0))
                currentScreen = bg2

            elif currentScreen == bg2:
                screen.fill((0,0,0))
                screen.blit(bg2,(0,0))
                currentScreen = bg2
                self.x = 600

        elif self.x <= 0:
            if currentScreen == bg2:
                self.x = 600
                screen.fill((0,0,0))
                screen.blit(bg1,(0,0))
                currentScreen = bg1

            elif currentScreen == bg1:
                screen.fill((0,0,0))
                screen.blit(bg1,(0,0))
                currentScreen = bg1
                self.x = 0


# Start of main program
#pygame.init()
screen = pygame.display.set_mode((640, 500))

##background
screen.fill((0,0,0)) ## to clean background
bg1 = pygame.image.load("background1.png")
bg2 = pygame.image.load("background2.png")

#currentScreen = bg1
cat = Cat()
clock = pygame.time.Clock()
#StartScreen = Background_img()

#running = True
#while running:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            pygame.quit()
#            running = False

    #button("Choice 1",150,450,100,50,green,bright_green,"wrong")
    #button("Choice 2",350,450,100,50,red,bright_red, "wrong1")

##    if cat.y >= 320:
#        if currentScreen == bg1:
#            cat.y = 0
#            screen.fill((0,0,0))
#            screen.blit(bg2,(0,0))
#            currentScreen = bg2


#        elif currentScreen == bg2:
#            screen.fill((0,0,0))
#            screen.blit(bg2,(0,0))
#            currentScreen = bg2
#            cat.y = 320
##        if currentScreen == bg2:
#            cat.y = 320
#            screen.fill((0,0,0))
#            screen.blit(bg1,(0,0))
#            currentScreen = bg1

#        elif currentScreen == bg1:
#            screen.fill((0,0,0))
#            screen.blit(bg1,(0,0))
#            currentScreen = bg1
#            cat.y = 0
 ###### The sprite is going from top to bottom :D


#    cat.handle_keys()
#    screen.fill((255, 255, 255))
#    screen.blit(currentScreen, (0,0))
#    cat.draw(screen)
#    pygame.display.update()
game_intro()
clock.tick(40)
