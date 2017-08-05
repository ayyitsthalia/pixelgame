import pygame
import os
import sys
import time, math
from pygame.locals import *

##########  COLORS ############################
white = (255,255,255)
black = (0,0,0)

red = (200,0,0)
light_red = (255,0,0)

yellow = (200,200,0)
light_yellow = (255,255,0)

green = (34,177,76)
light_green = (0,255,0)

######### Title and icon ###########################
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('bleh') ## title
icon = pygame.image.load('nickright.png') ### icon
pygame.display.set_icon(icon)

##########  images sources  #############
bg1 = pygame.image.load("darkroom.png") ##dark room
bg2 = pygame.image.load("boruto.jpg")   ##fairy scene ***
bg3 = pygame.image.load("Map002.png")   ##map right side
bg4 = pygame.image.load("farmermap.png")##map farmer 
bg5 = pygame.image.load("bed.jpg")      ##map unicorn ***
bg6 = pygame.image.load("S.jpg")        ##map bottom left corner ***
bg7 = pygame.image.load("B.png")        ##map bottom right corner ***
bg8 = pygame.image.load("C.jpg")        ##the boss screen 

playerimg = pygame.image.load('MC1.png')
clock = pygame.time.Clock()
currentScreen = bg1 
global gameOver #### global gameOver
global player  ##for the mc
global running ## tu run the game

####### to continue the game  ###############
def gameLoop():
    global gameOver
    gameExit = False
    gameOver = False


################ M A I N   C H A R A C T E R   ##################
class Player(object):
    def __init__(self):
        # define player
        self.image = pygame.image.load("MC1.png")
        self.x = 50
        self.y = 50

    def handle_keys(self):         # player movement
      #  for event in pygame.event.get():
           # if event.type == KEYDOWN:
                key = pygame.key.get_pressed()
                dist = 10
                if key[pygame.K_DOWN]:                   
                    self.y = self.y + dist
                    self.image = pygame.image.load("MC1.png")

                elif key[pygame.K_UP]:
                    self.y = self.y - dist
                    self.image = pygame.image.load("MCfront.png")

                elif key[pygame.K_RIGHT]:
                    self.x = self.x + dist
                    self.image = pygame.image.load("MCright.png")

                elif key[pygame.K_LEFT]:
                    self.x = self.x - dist
                    self.image = pygame.image.load("MCleft.png")

    def update(self):
        # player moving through different scenes
        global currentScreen 
        if player.y >= 600:
            if currentScreen == bg1: ## stays in bg1
                player.y = 600
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg1,(0,0))
                currentScreen = bg1

            elif currentScreen == bg2: ##move up to bg1
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg1,(0,0))
                currentScreen = bg1
                player.y = 0

            elif currentScreen == bg3: ##move up to bg8
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg8,(0,0))
                currentScreen = bg8
                player.y = 0

            elif currentScreen == bg4: ##move up to bg2
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg2,(0,0))
                currentScreen = bg2
                player.y = 0
                
            elif currentScreen == bg5: ##move up to bg3
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg3,(0,0))
                currentScreen = bg3
                player.y = 0

            elif currentScreen == bg6: ##move up to bg4
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg4,(0,0))
                currentScreen = bg4
                player.y = 0

            elif currentScreen == bg7: ##move up to bg5
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg5,(0,0))
                currentScreen = bg5
                player.y = 0

            elif currentScreen == bg8: ##stays in bg8
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg8,(0,0))
                currentScreen = bg8
                player.y = 600

        elif player.y <= 0:
            if currentScreen == bg1: ##move down to bg2
                player.y = 600
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg2,(0,0))
                currentScreen = bg2

            elif currentScreen == bg2: ##move down to bg4
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg4,(0,0))
                currentScreen = bg4
                player.y = 600 

            elif currentScreen == bg3: ##move down to bg5
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg5,(0,0))
                currentScreen = bg5
                player.y = 600

            elif currentScreen == bg4: ##move down to bg6
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg6,(0,0))
                currentScreen = bg6
                player.y = 600
 
            elif currentScreen == bg5: ##move down to bg7
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg7,(0,0))
                currentScreen = bg7
                player.y = 600

            elif currentScreen == bg6: ##stays in bg6
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg6,(0,0))
                currentScreen = bg6
                player.y = 0

            elif currentScreen == bg7: ##stays in bg7
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg7,(0,0))
                currentScreen = bg7
                player.y = 0

            elif currentScreen == bg8: ##move down to bg3
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg3,(0,0))
                currentScreen = bg3
                player.y = 0

        elif player.x <= 0: #### M O V E  L E F T #########
            if currentScreen == bg1: ##stays in bg1
                player.x = 0
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg1,(0,0))
                currentScreen = bg1

            elif currentScreen == bg2: ##stays in bg2
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg2,(0,0))
                currentScreen = bg2
                player.x = 0 

            elif currentScreen == bg3: ##move left to bg2
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg2,(0,0))
                currentScreen = bg2
                player.x = 800

            elif currentScreen == bg4: ##stays in bg4 
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg4,(0,0))
                currentScreen = bg4
                player.x = 0

            elif currentScreen == bg5: ##move left to bg4
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg4,(0,0))
                currentScreen = bg4
                player.x = 800


            elif currentScreen == bg6: ##stay in bg6
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg6,(0,0))
                currentScreen = bg6
                player.x = 0

            elif currentScreen == bg7: ##move left to bg6
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg6,(0,0))
                currentScreen = bg6
                player.x = 800

            elif currentScreen == bg8: ##stays in bg8
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg8,(0,0))
                currentScreen = bg8
                player.x = 0

        elif player.x >= 800: #### M O V E  R I G H T #########
            if currentScreen == bg1: ##stays in bg1
                player.x = 800
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg1,(0,0))
                currentScreen = bg1

            elif currentScreen == bg2: ##move right to bg3
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg3,(0,0))
                currentScreen = bg3
                player.x = 0 

            elif currentScreen == bg3: ##stays in bg3
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg3,(0,0))
                currentScreen = bg3
                player.x = 800

            elif currentScreen == bg4: ##move right to bg5
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg5,(0,0))
                currentScreen = bg5
                player.x = 0

            elif currentScreen == bg5: ##stays in bg5
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg5,(0,0))
                currentScreen = bg5
                player.x = 800

            elif currentScreen == bg6: ##move right to bg7
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg7,(0,0))
                currentScreen = bg7
                player.x = 0

            elif currentScreen == bg7: ##stay in bg7
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg7,(0,0))
                currentScreen = bg7
                player.x = 800

            elif currentScreen == bg8: ##stay in bg8
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg8,(0,0))
                currentScreen = bg8
                player.x = 800

     ###### The sprite is going from top to bottom :D

    def draw(self, surface):
        # to move the cat freely :D
        """ Draw on surface"""
        surface.blit(self.image, (player.x, player.y))


################## M E S S A G E S #####################################

######## py.game.font.Font - custom font downloaded  #####
pygame.font.init()
all_fonts = pygame.font.get_fonts()
smallfont = pygame.font.SysFont("comicsansms", 25)
mediumfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 100)

##########   define the message/ dialogs to the AI ###############
def message_to_screen(msg,color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg,color, size)
    textRect.center = (display_width / 2), (display_height / 2)+y_displace
    gameDisplay.blit(textSurf, textRect)

############ to make the dialogs pretty (if needed) ################
def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text, True, red)
    elif size == "medium":
        textSurface = medfont.render(text, True, green)
    elif size == "large":
        textSurface = largefont.render(text, True, black)
    return textSurface, textSurface.get_rect()

####################################
#global player
player = Player()

currentScreen = bg1
pygame.image.load("bed.jpg")
################ #####################
def game_running ():
    global running
    running = True
    while running :
    ############  when you are not in game over #########
        global gameOver 
        gameOver = False
        while gameOver != True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False

            player.handle_keys()
            player.draw(gameDisplay)
            player.update()
            pygame.display.update()
            gameDisplay.fill((0,0,0))
            gameDisplay.blit(currentScreen, (0,0))
            clock.tick(40)


################### I N T R O   S C R E E N  #################################
def gameIntro ():
    intro = True
    ########### layout of the intro screen #####################
    gameDisplay.fill(white)
    message_to_screen("Welcome to ___", green, -100, size = "large")
    message_to_screen("...", black, -30, size = "small")
    message_to_screen("...", black, 10, size = "small")
    message_to_screen("...", black, 50, size = "small")
    message_to_screen("Press C to play or Q to quit", black, 180, size = "small")

    while intro:
        for event in pygame.event.get(): ### choice to exit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                    game_running()
                   

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        pygame.display.update()
        clock.tick(40)

############# S T A R T I N G   T H E   G A M E ##########################
pygame.init()
gameIntro()

pygame.quit()
quit()


gameLoop()