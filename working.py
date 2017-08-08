import pygame
import os
import sys
import time, math
from pygame.locals import *

##########  COLORS ############################
white = (255,255,255)
black = (0,0,0)

red = (250,128,114)
light_red = (255,0,0)

yellow = (200,200,0)
light_yellow = (255,255,0)

green = (60,179,113)
light_green = (0,255,0)

purple = (147,112,219)
blue = (176,196,222)



######### Title and icon ###########################
display_width = 680
display_height = 530
global gameDisplay
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('The Forest') ## title
icon = pygame.image.load('nickright.png') ### icon
pygame.display.set_icon(icon)

##########  images sources  #############
bg1 = pygame.image.load("4left.png")
bg2 = pygame.image.load("3left.png")
bg3 = pygame.image.load("3right.png")
bg4 = pygame.image.load("2left.png")
bg5 = pygame.image.load("2right.png")
bg6 = pygame.image.load("1left.png")
bg7 = pygame.image.load("1right.png")
bg8 = pygame.image.load("4right.png")

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
        if player.y >= 530:
            if currentScreen == bg1: ## stays in bg1
                player.y = 400
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
                player.y = 400

        elif player.y <= 0:
            if currentScreen == bg1: ##move down to bg2
                player.y = 530
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg2,(0,0))
                currentScreen = bg2

            elif currentScreen == bg2: ##move down to bg4
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg4,(0,0))
                currentScreen = bg4
                player.y = 530

            elif currentScreen == bg3: ##move down to bg5
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg5,(0,0))
                currentScreen = bg5
                player.y = 530

            elif currentScreen == bg4: ##move down to bg6
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg6,(0,0))
                currentScreen = bg6
                player.y = 530

            elif currentScreen == bg5: ##move down to bg7
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg7,(0,0))
                currentScreen = bg7
                player.y = 530

            elif currentScreen == bg6: ##stays in bg6
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg6,(0,0))
                currentScreen = bg6
                player.y = 100

            elif currentScreen == bg7: ##stays in bg7
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg7,(0,0))
                currentScreen = bg7
                player.y = 100

            elif currentScreen == bg8: ##move down to bg3
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg3,(0,0))
                currentScreen = bg3
                player.y = 0

        elif player.x <= 0: #### M O V E  L E F T #########
            if currentScreen == bg1: ##stays in bg1
                player.x = 30
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg1,(0,0))
                currentScreen = bg1

            elif currentScreen == bg2: ##stays in bg2
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg2,(0,0))
                currentScreen = bg2
                player.x = 30

            elif currentScreen == bg3: ##move left to bg2
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg2,(0,0))
                currentScreen = bg2
                player.x = 680

            elif currentScreen == bg4: ##stays in bg4
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg4,(0,0))
                currentScreen = bg4
                player.x = 30

            elif currentScreen == bg5: ##move left to bg4
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg4,(0,0))
                currentScreen = bg4
                player.x = 680


            elif currentScreen == bg6: ##stay in bg6
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg6,(0,0))
                currentScreen = bg6
                player.x = 30

            elif currentScreen == bg7: ##move left to bg6
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg6,(0,0))
                currentScreen = bg6
                player.x = 680

            elif currentScreen == bg8: ##stays in bg8
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg8,(0,0))
                currentScreen = bg8
                player.x = 30

        elif player.x >= 680: #### M O V E  R I G H T #########
            if currentScreen == bg1: ##stays in bg1
                player.x = 580
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
                player.x = 580

            elif currentScreen == bg4: ##move right to bg5
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg5,(0,0))
                currentScreen = bg5
                player.x = 0

            elif currentScreen == bg5: ##stays in bg5
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg5,(0,0))
                currentScreen = bg5
                player.x = 580

            elif currentScreen == bg6: ##move right to bg7
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg7,(0,0))
                currentScreen = bg7
                player.x = 0

            elif currentScreen == bg7: ##stay in bg7
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg7,(0,0))
                currentScreen = bg7
                player.x = 580

            elif currentScreen == bg8: ##stay in bg8
                gameDisplay.fill((0,0,0))
                gameDisplay.blit(bg8,(0,0))
                currentScreen = bg8
                player.x = 580

     ###### The sprite is going from top to bottom :D

    def draw(self, surface):
        # to move the cat freely :D
        """ Draw on surface"""
        surface.blit(self.image, (player.x, player.y))

################## C A T ##############################################
class Cat(object):
    def __init__(self):
        self.image = pygame.image.load("nickright.png")
        self.x = 92
        self.y = 247

    def paint(self, surface):
        if currentScreen == bg1:
            surface.blit(self.image, (self.x, self.y))
        else:
            pass

    def touch(self, player):
        if abs((self.x - player.x) < 10) and abs((self.y - player.y) < 10):
            if currentScreen == bg1:
                talk_to_cat()
            else:
                pass

################## F A R M E R ##############################################
class Farmer(object):
    def __init__(self):
        self.image = pygame.image.load("sprite_farmer0.png")
        self.x = 310
        self.y = 12

    def color(self, surface):
        if currentScreen == bg2:
            surface.blit(self.image, (self.x, self.y))
        else:
            pass

    def contact(self, player):
        if abs((self.x - player.x) < 10) and abs((self.y - player.y) < 10):
            if currentScreen == bg2:
                talk_to_farmer()
            else:
                pass

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
        textSurface = mediumfont.render(text, True, green)
    elif size == "large":
        textSurface = largefont.render(text, True, black)
    return textSurface, textSurface.get_rect()

############# G A M E   P L A Y ##########################
#global player
player = Player()
cat = Cat()
farmer = Farmer()
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
            cat.paint(gameDisplay)
            cat.touch(player)
            farmer.color(gameDisplay)
            farmer.contact(player)
            player.update()
            pygame.display.update()
            gameDisplay.fill((0,0,0))
            gameDisplay.blit(currentScreen, (0,0))
            clock.tick(40)


################### I N T R O   S C R E E N  #################################
def gameIntro ():
    intro = True
    ########### layout of the intro screen #####################
    global gameDisplay
    gameDisplay.fill(white)
    message_to_screen("The Forest", green, -30, size = "large")
    message_to_screen("Press ENTER to play or ESCAPE to quit.", blue, 160, size = "small")
    message_to_screen("Press SPACE to view the Game Makers.", blue, 180, size = "small")

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    intro = False
                    gameStart()

                elif event.key == pygame.K_SPACE:
                    intro = False
                    gameMaker()

                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        pygame.display.update()
        clock.tick(40)

############# G A M E   M A K E R ##########################

def gameMaker ():
    maker = True
    gameDisplay.fill(white)
    message_to_screen("Game Makers", purple, -150, size = "large")
    message_to_screen("Amala Akkiraju", black, -70, size = "medium")
    message_to_screen("Nhi Nguyen", black, -40, size = "medium")
    message_to_screen("Samantha Tam", black, -10, size = "medium")
    message_to_screen("Thalia Nguyen", black, 20, size = "medium")
    message_to_screen("Press ENTER to return to the title screen.", red, 180, size = "small")

    while maker:
        for event in pygame.event.get(): ### choice to exit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    intro = False
                    gameIntro()

                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        pygame.display.update()
        clock.tick(40)


#############  T A L K   T O   C A T   ############################
def talk_to_cat ():
    talk_cat = True
    gameDisplay.fill(black)
    message_to_screen("The cat guides me out of the room, and I find myself in this dark, sad, ", white, -200, size = "okie")
    message_to_screen("mysterious world filled my strange fantasy creatures. It looks like my worst ", white, -180, size = "okie")
    message_to_screen("nightmare. All of sudden, a butterfly zooms in front of me and steals my ", white, -160, size = "okie")
    message_to_screen("bracelet. 'Hey, that's mine! Give it back!' The butterfly turns into a ", white, -140, size = "okie")
    message_to_screen("fairy and tells me, 'Calm down, I'll give it back, you just need to do ", white, -120, size = "okie")
    message_to_screen("something for me. I have this precious item that was broken up into ", white, -100, size = "okie")
    message_to_screen("pieces and spread throughout this world. I need you to find those pieces ", white, -80, size = "okie")
    message_to_screen("and put them back together. I'll be back when you have completed the task.' ", white, -60, size = "okie")
    message_to_screen("She disappears, and I turn over to the cat with a bewildered look on my ", white, -40, size = "okie")
    message_to_screen("face. The cat, such a helpful creature, disappears, saying, 'It's my ", white, -20, size = "okie")
    message_to_screen("nap time~' They both leave me alone on this long, winding path", white, 0, size = "okie")

    message_to_screen("type y to go on the journey or n to ignore the cat", light_red, 40, size = "okie")

    while talk_cat:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    intro = False
                    global currentScreen
                    currentScreen = bg2
                    player.x = 10
                    player.y = 10
                    talk_cat = False

                elif event.key == pygame.K_n:
                    intro = False
                    global currentScreen
                    currentScreen = bg1
                    player.x = 10
                    player.y = 10
                    talk_cat = False

                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        pygame.display.update()
        clock.tick(40)

#############  T A L K   T O   F A R M E R   ############################
def talk_to_farmer ():
    talk_farmer = True
    gameDisplay.fill(black)
    message_to_screen("All by myself, I walk along the path when I see an old ", white, -200, size = "okie")

    message_to_screen("farmer frowning about something. Since I have nothing better  ", white, -180, size = "okie")
    message_to_screen("to do, I go over and ask him what happened. He explains to me,", white, -160, size = "okie")
    message_to_screen("'My plants are under attack from the vicious slime viruses and ", white, -140, size = "okie")
    message_to_screen("the harvest is about to come soon. If I don't save my plants I ", white, -120, size = "okie")
    message_to_screen(" won't have any food to give my family. Can you help me?'", white, -100, size= "okie")

    message_to_screen("type a to sing and calm the farmer ", white, -60, size = "okie")
    message_to_screen("type b to set fire and kill all the slimes", white, -40, size = "okie")
    message_to_screen("type c to ignore the farmer ", white, -20, size = "okie")

    while talk_farmer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    intro = False
                    global currentScreen
                    currentScreen = bg7
                    player.x = 50
                    player.y = 50
                    talk_farmer = False

                elif event.key == pygame.K_b:
                    intro = False
                    global currentScreen
                    currentScreen = bg1
                    player.x = 10
                    player.y = 10
                    talk_farmer = False

                elif event.key == pygame.K_c:
                    intro = False
                    global currentScreen
                    currentScreen = bg1
                    player.x = 10
                    player.y = 10
                    talk_farmer = False

                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        pygame.display.update()
        clock.tick(40)

############# S T A R T I N G   T H E   G A M E ##########################
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
                    start = False

                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        pygame.display.update()
        clock.tick(40)
#############
pygame.init()
gameIntro()
gameStart()
gameMaker()
pygame.quit()
quit()

gameLoop()
