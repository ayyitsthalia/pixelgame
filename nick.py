import pygame, sys, math
import os
from pygame.locals import *

img_path = 'nickright.png'

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

    """def update(self):
        if self.x >= 640:
            self.x = 0
        elif self.x <= 0:
            self.x = 640
        if self.y >= 400:
            self.y = 0
        elif self.y <= 0:
            self.y = 400"""

    def draw(self, surface):
        """ Draw on surface"""
        surface.blit(self.image, (self.x, self.y))


"""def switching_bg(self):
    if self.y >= 400:
        self.y = 0
        if currentScreen == bg1:
            screen.fill((0,0,0))
            screen.blit(bg2,(0,0))

    elif currentScreen != bg1:
        screen.blit(bg2,(0,0))

class MyBg(object):
    bg_img = switching_bg """

## Start of main program
pygame.init()
screen = pygame.display.set_mode((640, 400))

##background
screen.fill((0,0,0)) ## to clean background

bg1 = pygame.image.load("bed.jpg")

bg2 = pygame.image.load("boruto.jpg")

#bg1 = "bed.jpg"
#bg2 = "bed.jpg"




currentScreen =  bg1
cat = Cat()
clock = pygame.time.Clock()
#StartScreen = Background_img()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    if cat.y >= 400:
        if currentScreen == bg1:
            cat.y = 0
            screen.fill((0,0,0))
            screen.blit(bg2,(0,0))
            currentScreen = bg2

        elif currentScreen == bg2:
            screen.fill((0,0,0))
            screen.blit(bg2,(0,0))
            currentScreen = bg2
            cat.y = 400
    elif cat.y <= 0:
        if currentScreen == bg2:
            cat.y = 400
            screen.fill((0,0,0))
            screen.blit(bg1,(0,0))
            currentScreen = bg1

        elif currentScreen == bg1:
            screen.fill((0,0,0))
            screen.blit(bg1,(0,0))
            currentScreen = bg1
            cat.y = 0
 ###### The sprite is going from top to bottom :D 

    #MyBg.bg_img(self)
    cat.handle_keys()
    #cat.update()
    cat.draw(screen)
    #StartScreen.update()
    pygame.display.update()
    clock.tick(40)
