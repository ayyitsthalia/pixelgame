import pygame
import os
import sys
import time
from pygame.locals import *

pygame.init()

#COLORS
white = (255,255,255)
black = (0,0,0)

red = (200,0,0)
light_red = (255,0,0)

yellow = (200,200,0)
light_yellow = (255,255,0)

green = (34,177,76)
light_green = (0,255,0)
#COLORS

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Aight')
#game Title

icon = pygame.image.load(r'/Users/Thalia/Desktop/pixelart/player/sprite_01.png')
pygame.display.set_icon(icon)
#icon

playerimg = pygame.image.load(r'/Users/Thalia/Desktop/pixelart/player/sprite_01.png')
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self,image):
        self.player = pygame.image.load(r'/Users/Thalia/Desktop/pixelart/player/sprite_01.png')
        self.p_rect = self.player.get_rect()

#info on movement
block_size = 20
FPS = 30

####py.game.font.Font - custom font downloaded
smallfont = pygame.font.SysFont(None, 25)
mediumfont = pygame.font.SysFont(None, 50)
largefont = pygame.font.SysFont(None, 100)

def gameIntro():
    intro = True
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen("Welcome to ___", green, -100, size = "large")
        message_to_screen("...", black, -30, size = "small")
        message_to_screen("...", black, 10, size = "small")
        message_to_screen("...", black, 50, size = "small")
        message_to_screen("Press C to play or Q to quit", black, 180, size = "small")

        #button
        pygame.draw.rect(gameDisplay,green,(150,500,100,50))
        pygame.draw.rect(gameDisplay,green,(350,500,100,50))
        pygame.draw.rect(gameDisplay,green,(550,500,100,50))

        button("play", 150,500,100,50, green, light_green, action="play")
        button("controls", 350,500,100,50, yellow, light_yellow, action="controls")
        button("quit", 550,500,100,50, red, light_red, action ="quit")

        pygame.display.update()
        clock.tick(15)

def button(text, x, y, width, height, inactive_color, active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()

            if action == "controls":
                game_controls()

            if action == "play":
                gameLoop()

            if action == "main":
                game_intro()

    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x,y,width,height))
    text_to_button(text,black,x,y,width,height)

def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
    gameDisplay.blit(textSurf, textRect)


#displace makes it so not everything is in the center from textRect.center
def message_to_screen(msg,color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg,color, size)
    textRect.center = (display_width / 2), (display_height / 2)+y_displace
    gameDisplay.blit(textSurf, textRect)
#TEXT


#event is the commands (arrow keys etc...)
def gameLoop():
    gameExit = False
    gameOver = False

    lead_x = 300
    lead_y = 300

    lead_x_change = 0
    lead_y_change = 0

    while not gameExit:

        #gameover functionality
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over", red, y_displace=-50, size = "large")
            message_to_screen("press C to play again or Q to quit",black, 50, size = "medium")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        #MOVEMENT
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                    #lead_y_change tells us to keep y at 0 when moving the x axis so there's no diagonal movement.
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
            #stop continious movement
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    lead_x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    lead_y_change = 0

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
                gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.blit(playerimg)

        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, block_size, block_size])
        pygame.display.update()



        clock.tick(FPS)

    pygame.quit()
    quit()

gameIntro()
gameLoop()
