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

    def update(self):
        if self.x >= 640:
            self.x = 0
        elif self.x <= 0:
            self.x = 640
        if self.y >= 400:
            self.y = 0
        elif self.y <= 0:
            self.y = 400

    def draw(self, surface):
        """ Draw on surface"""
        surface.blit(self.image, (self.x, self.y))

pygame.init()
screen = pygame.display.set_mode((640, 400))

screen.fill((0,0,0))
bg1 = pygame.image.load("backgroundtest.png").convert_alpha()
screen.blit(bg1,(0,0))
bg2 = pygame.image.load("background2.png").convert_alpha()
screen.blit(bg2,(0,0))





cat = Cat()
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    screen.fill((0,0,0))
    screen.blit(bg1,(0,0))
    screen.blit(bg2,(0,0))

    cat.handle_keys()
    cat.update()
    cat.draw(screen)

    pygame.display.update()


    clock.tick(40)
