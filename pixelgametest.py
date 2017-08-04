import pygame
import os
import time

#images/sprite
img_path = 'nickright.png'
imgMC = 'sprite_MCmain.png'
img_MC2 = 'sprite_MC02.png'
img_f = 'sprite_farmer2.png'
bg1 = 'Map002w.png'
bg2 = 'sky1.png'
bg3 = 'searoute800x640.png'
bg4 = 'download.png'

class Cat(object):
    def __init__(self):
        """The constructor of the class"""
        self.image = pygame.image.load(img_path)
        self.x = 20
        self.y = 490

    def handle_keys(self):
        """Handle Keys"""
        key = pygame.key.get_pressed()
        dist = 10
        if key[pygame.K_DOWN]:
            self.y += dist
        elif key[pygame.K_UP]:
            self.y -=dist
        if key[pygame.K_RIGHT]:
            self.x += dist
        elif key[pygame.K_LEFT]:
            self.x -= dist

    def update(self):
        if self.x >= 800:
            self.x = 0
        elif self.x <= 0:
            self.x = 800
        if self.y >= 600:
            self.y = 0
        elif self.y <= 0:
            self.y = 600

    def draw(self, surface):
        """Draw on surface"""
        surface.blit(self.image, (self.x, self.y))

class MC(object):
    def __init__(self):
        """The constructor of the class"""
        self.image = pygame.image.load(imgMC)
        self.x = 300
        self.y = 300

    def moving_keys(self):
        """Handle Keys"""
        key = pygame.key.get_pressed()
        dist = 3
        if key[pygame.K_s]:
            self.y += dist
        elif key[pygame.K_w]:
            self.y -=dist
        if key[pygame.K_d]:
            self.x += dist
        elif key[pygame.K_a]:
            self.x -= dist

    def loop(self):
        if self.x >= 800:
            self.x = 0
        elif self.x <= 0:
            self.x = 800
        if self.y >= 600:
            self.y = 0
        elif self.y <= 0:
            self.y = 600

    def paint(self, surface):
        """Draw on surface"""
        surface.blit(self.image, (self.x, self.y))

class Farmer(object):
    def __init__(self):
        """The constructor of the class"""
        self.image = pygame.image.load(img_f)
        self.x = 500
        self.y = 500

    def handle_keys(self):
        """Handle Keys"""
        key = pygame.key.get_pressed()
        dist = 10
        if key[pygame.K_k]:
            self.y += dist
        elif key[pygame.K_i]:
            self.y -=dist
        if key[pygame.K_l]:
            self.x += dist
        elif key[pygame.K_j]:
            self.x -= dist

    def update(self):
        if self.x >= 800:
            self.x = 0
        elif self.x <= 0:
            self.x = 800
        if self.y >= 600:
            self.y = 0
        elif self.y <= 0:
            self.y = 600

    def draw(self, surface):
        """Draw on surface"""
        surface.blit(self.image, (self.x, self.y))


pygame.init()
screen = pygame.display.set_mode((800, 600))

screen.fill(((0,0,0)))
bg1 = pygame.image.load(bg1)
bg2 = pygame.image.load(bg2)
bg3 = pygame.image.load(bg3)
bg4 = pygame.image.load(bg4)
screen.blit(bg1,(0,0))

farmer = Farmer()
mc = MC()
currentMc = imgMC
cat = Cat()
currentScreen = bg1
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
    # from Bcakground 1 to Background 2 (going up)
    if cat.y >= 600:
        if currentScreen == bg1:
            cat.y = 0
            screen.fill((0,0,0))
            screen.blit(bg2,(0,0))
            currentScreen = bg2

        elif currentScreen == bg2:
            screen.fill((0,0,0))
            screen.blit(bg2,(0,0))
            currentScreen = bg2
            cat.y = 600

    elif cat.y <= 0:
        if currentScreen == bg2:
            cat.y = 600
            screen.fill((0,0,0))
            screen.blit(bg1,(0,0))
            currentScreen = bg1

        elif currentScreen == bg1:
            screen.fill((0,0,0))
            screen.blit(bg1,(0,0))
            currentScreen = bg1
            cat.y = 0
#Background 1 and Background 3 (going left)
    if cat.x >= 800:
        if currentScreen == bg1:
            cat.x = 0
            screen.fill((0,0,0))
            screen.blit(bg3,(0,0))
            currentScreen = bg3

        elif currentScreen == bg3:
            screen.fill((0,0,0))
            screen.blit(bg3,(0,0))
            currentScreen = bg3
            cat.x = 800

    elif cat.x <= 0:
        if currentScreen == bg3:
            cat.x = 800
            screen.fill((0,0,0))
            screen.blit(bg1,(0,0))
            currentScreen = bg1

        elif currentScreen == bg1:
            screen.fill((0,0,0))
            screen.blit(bg1,(0,0))
            currentScreen = bg1
            cat.x = 0
#Background 3 and Background 4 (going down)
    if cat.y >= 600:
        if currentScreen == bg3:
            cat.y = 0
            screen.fill((0,0,0))
            screen.blit(bg4,(0,0))
            currentScreen = bg4

        elif currentScreen == bg4:
            screen.fill((0,0,0))
            screen.blit(bg4,(0,0))
            currentScreen = bg4
            cat.y = 600

    elif cat.y <= 0:
        if currentScreen == bg4:
            cat.y = 600
            screen.fill((0,0,0))
            screen.blit(bg3,(0,0))
            currentScreen = bg3

        elif currentScreen == bg3:
            screen.fill((0,0,0))
            screen.blit(bg1,(0,0))
            currentScreen = bg3
            cat.y = 0


    mc.moving_keys()
    mc.loop()
    cat.handle_keys()
    cat.update()
    farmer.handle_keys()
    farmer.update()
    screen.fill((0,0,0))
    screen.blit(currentScreen,(0,0))
    mc.paint(screen)
    cat.draw(screen)
    farmer.draw(screen)
    pygame.display.update()
    clock.tick(40)
