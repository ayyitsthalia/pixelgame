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
display_width = 680
display_height = 530
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('The Forest') ## title
icon = pygame.image.load('nickright.png') ### icon
pygame.display.set_icon(icon)

##########  images sources  #############
bg1 = pygame.image.load("darkroom.png") ##dark room


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

######################### talk to cat ################
def talk_cat ():
    start = True
    gameDisplay.fill(black)
    message_to_screen("The cat guides me out of the room, and I find myself in this dark, sad, ", white, -200, size = "okie")
    message_to_screen(" mysterious world filled my strange fantasy creatures. It looks like ", white, -180, size = "okie")
    message_to_screen(" my worst nightmare. All of sudden, a butterfly zooms in front of ", white, -160, size = "okie")
    message_to_screen(" me and steals my bracelet. 'Hey, that's mine! Give it back to me!'", white, -140, size = "okie")
    message_to_screen(" The butterfly turns into a fairy and tells me, 'Calm down. ", white, -120, size = "okie")
    message_to_screen(" I'll give it back, you just need to do something for me.", white, -100, size = "okie")
    message_to_screen(" I have this precious item that was broken up into pieces and spread ", white, -80, size = "okie")
    message_to_screen(" throughout this world. I need you to find those pieces and put them back together.", white, -60, size = "okie")
    message_to_screen(" I'll be back when you have completed the task.' She disappears, and ", white, -40, size = "okie")
    message_to_screen(" I turn over to the cat with a bewildered look on my face. The cat, ", white, -20, size = "okie")
    message_to_screen(" such a helpful creature, disappears, saying, 'It's nap time.' They both", white, 0, size = "okie")
    message_to_screen(" leave me alone on this long, winding path.", white, 20, size = "okie")

    ### type ENTER to go back to the currentScreen

    while start:
        pygame.display.update()
        clock.tick(40)

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

    def draw(self, surface):
        # to move the cat freely :D
        """ Draw on surface"""
        surface.blit(self.image, (player.x, player.y))

################# cat ################
class Cat(object):
    def __init__(self):
        self.image = pygame.image.load("nickright.png")
        self.x = 300
        self.y = 300

    def draw(self, surface):
        # to move the cat freely :D
        """ Draw on surface"""
        surface.blit(self.image, (self.x, self.y))

    def touch(self, player):
        if ((self.x - 10) == (player.x + 10) and (self.y == player.y)) or ((self.x == player.x) and (self.y + 10) == (player.y - 10)) or ((self.x +10) == (player.x - 10) and (self.y == player.y)) or ((self.x == player.x) and (self.y - 10) == (player.y + 10)):
            talk_cat()

################## M E S S A G E S #####################################

######## py.game.font.Font - custom font downloaded  #####
pygame.font.init()
all_fonts = pygame.font.get_fonts()
okfont = pygame.font.SysFont("timesnewromanps", 5)
smallfont = pygame.font.SysFont("timesnewromanps", 25)
mediumfont = pygame.font.SysFont("timesnewromanps", 50)
largefont = pygame.font.SysFont("timesnewromanps", 100)

##########   define the message/ dialogs to the AI ###############
def message_to_screen(msg,color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg,color, size)
    textRect.center = (display_width / 2), (display_height / 2)+y_displace
    gameDisplay.blit(textSurf, textRect)

############ to make the dialogs pretty (if needed) ################
def text_objects(text,color,size):
    if size == "okie":
        textSurface = smallfont.render(text, True, white)
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
cat = Cat()
currentScreen = bg1
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
            cat.draw(gameDisplay)
            cat.touch(player)
            pygame.display.update()
            gameDisplay.fill((0,0,0))
            gameDisplay.blit(currentScreen, (0,0))
            clock.tick(40)


################### I N T R O   S C R E E N  #################################
def gameIntro ():
    intro = True
    ########### layout of the intro screen #####################
    gameDisplay.fill(white)
    message_to_screen("The Forest", green, -100, size = "large")
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
                    gameStart()


                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        pygame.display.update()
        clock.tick(40)

############# S T A R T I N G   T H E   G A M E ##########################

############start###
def gameStart ():
    start = True
    gameDisplay.fill(black)
    message_to_screen("It\'s 4 AM and my alarm rings as usual, as it does every day. I wish I ", white, -180, size = "okie")
    message_to_screen("could sleep in like every other teenager, but I have to get to work. ", white, -160, size = "okie")
    message_to_screen("My parents refuse to pay my college tuition, so I have to work two ", white, -140, size = "okie")
    message_to_screen("jobs and attend my classes, all within 24 hours! Tired and sleep-deprived, ", white, -120, size = "okie")
    message_to_screen("I get up out of my bed, get dressed and go to work. It feels like a normal ", white, -100, size = "okie")
    message_to_screen("day as I take the customers\' orders and make them their drinks, when ", white, -80, size = "okie")
    message_to_screen("all of a sudden I find myself on the ground and all I can see is darkness...", white, -60, size = "okie")
    message_to_screen("Press enter to continue", white, 100, size = "small")

    while start:
        for event in pygame.event.get(): ### choice to exit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    intro = False
                    game_running()

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        pygame.display.update()
        clock.tick(40)


#############
pygame.init()
gameIntro()
gameStart()


pygame.quit()
quit()

gameLoop()
