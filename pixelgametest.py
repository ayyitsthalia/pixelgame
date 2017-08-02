#No background, edges complete
import pygame
import os

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
        dist = 1
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
        elif self.y >= 400:
            self.y = 0
        elif self.y <= 0:
            self.y = 400

    def draw(self, surface):
        """ Draw on surface"""
        surface.blit(self.image, (self.x, self.y))
pygame.init()
screen = pygame.display.set_mode((640, 400))

cat = Cat()
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    cat.handle_keys()
    cat.update()
    screen.fill((255, 255, 255))
    cat.draw(screen)
    pygame.display.update()

    clock.tick(40)
