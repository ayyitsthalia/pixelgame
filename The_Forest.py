import pygame
import os
import sys
import time, math
from pygame.locals import *

################  C O L O R S ################
white = (255,255,255)
black = (0,0,0)

red = (250,128,114)

green = (60,179,113)

purple = (147,112,219)
blue = (176,196,222)



################ T I T L E / I C O N ################
display_width = 680
display_height = 530
global gameDisplay
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('The Forest') ## title
icon = pygame.image.load('butterfly.png') ### icon
pygame.display.set_icon(icon)

################ I M A G E  S O U R C E S  ################
bg1 = pygame.image.load("4left.png")
bg2 = pygame.image.load("3left.png")
bg3 = pygame.image.load("3right.png")
bg4 = pygame.image.load("2left.png")
bg5 = pygame.image.load("2right.png")
bg6 = pygame.image.load("1left.png")
bg7 = pygame.image.load("1right.png")
bg8 = pygame.image.load("4right.png")
bg9 = pygame.image.load("fairy.png")
playerimg = pygame.image.load('MC.png')
giff = pygame.image.load("giphy.gif").convert_alpha()
ty = pygame.image.load("thanks.png")

clock = pygame.time.Clock()
currentScreen = bg1
global gameOver #### global gameOver
global player  ##for the mc
global running ## tu run the game

################ C O N T I N U E  G A M E  ################
def gameLoop():
    global gameOver
    gameExit = False
    gameOver = False

################ M A I N   C H A R A C T E R ################
class Player(object):
    def __init__(self):
        # define player
        self.image = pygame.image.load("MC.png")
        self.x = 50
        self.y = 50

    def handle_keys(self):         # player movement
      #  for event in pygame.event.get():
           # if event.type == KEYDOWN:
                key = pygame.key.get_pressed()
                dist = 10
                if key[pygame.K_DOWN]:
                    self.y = self.y + dist
                    self.image = pygame.image.load("MC.png")

                elif key[pygame.K_UP]:
                    self.y = self.y - dist
                    self.image = pygame.image.load("MCback.png")

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

################  C A T ################
class Cat(object):
    def __init__(self):
        self.image = pygame.image.load("cat.png")
        self.x = 90
        self.y = 247

    def paint(self, surface):
        if currentScreen == bg1:
            surface.blit(self.image, (self.x, self.y))
        else:
            pass

    def touch(self, player):
        if abs((self.x - player.x)) < 15 and abs((self.y - player.y)) < 15:
            if currentScreen == bg1:
                talk_to_cat()
            else:
                pass

################  F A R M E R ################
class Farmer(object):
    def __init__(self):
        self.image = pygame.image.load("farmer.png")
        self.x = 310
        self.y = 12

    def color(self, surface):
        if currentScreen == bg2:
            surface.blit(self.image, (self.x, self.y))
        else:
            pass

    def contact(self, player):
        if abs((self.x - player.x)) < 15 and abs((self.y - player.y)) < 15:
            if currentScreen == bg2:
                talk_to_farmer()
            else:
                pass

################ U N I C O R N ################
class Unicorn(object):
    def __init__(self):
        self.image = pygame.image.load("unicorn.png")
        self.x = 516
        self.y = 147

    def create(self, surface):
        if currentScreen == bg7:
            surface.blit(self.image, (self.x, self.y))
        else:
            pass

    def feel(self, player):
        if abs((self.x - player.x)) < 15 and abs((self.y - player.y)) < 15:
            if currentScreen == bg7:
                talk_to_unicorn()
            else:
                pass
################ R O C K ################
class Rock(object):
    def __init__(self):
        self.image = pygame.image.load("rock.png")
        self.x = 518
        self.y = 190

    def create(self, surface):
        if currentScreen == bg7:
            surface.blit(self.image, (self.x, self.y))
        else:
            pass

    def feel(self, player):
        if abs((self.x - player.x)) < 15 and abs((self.y - player.y)) < 15:
            if currentScreen == bg3:
                talk_to_rock()
            else:
                pass

################  M  O  M ################
class Mom(object):
    def __init__(self):
        self.image = pygame.image.load("mom.png")
        self.x = 438
        self.y = 113

    def art(self, surface):
        if currentScreen == bg8:
            surface.blit(self.image, (self.x, self.y))
        else:
            pass

    def sense(self, player):
        if abs((self.x - player.x)) < 15 and abs((self.y - player.y)) < 15:
            if currentScreen == bg8:
                talk_to_mom()
            else:
                pass

################ F A I R Y ################
class Fairy(object):
    def __init__(self):
        self.image = pygame.image.load("fairy.png")
        self.x = 383
        self.y = 217

    def scribble(self, surface):
        if currentScreen == bg9:
            surface.blit(self.image, (self.x, self.y))
        else:
            pass

    def hit(self, player):
        if abs((self.x - player.x)) < 15 and abs((self.y - player.y)) < 15:
            if currentScreen == bg9:
                talk_to_fairy()
            else:
                pass

################ M E S S A G E S ################
######## py.game.font.Font - custom font downloaded  #####
pygame.font.init()
all_fonts = pygame.font.get_fonts()
okfont = pygame.font.SysFont("04b03", 16)
ok1font = pygame.font.SysFont("04b03", 16)
kfont = pygame.font.SysFont("04b03", 20)
smallfont = pygame.font.SysFont("04b03", 16)
small1font = pygame.font.SysFont("04b03", 16)
small2font = pygame.font.SysFont("04b03", 25)
mediumfont = pygame.font.SysFont("04b03", 45)
medium1font = pygame.font.SysFont("04b03", 45)
medium2font = pygame.font.SysFont("04b03", 45)
largefont = pygame.font.SysFont("04b03", 90)
large1font = pygame.font.SysFont("04b03", 90)
large2font = pygame.font.SysFont("04b03", 90)

################ define the message/ dialogs to the AI ################
def message_to_screen(msg,color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg,color, size)
    textRect.center = (display_width / 2), (display_height / 2)+y_displace
    gameDisplay.blit(textSurf, textRect)

################to make the dialogue pretty (if needed) ################
def text_objects(text,color,size):
    if size == "okie":
        textSurface = okfont.render(text, True, white)
    if size == "okie1":
        textSurface = ok1font.render(text, True, blue)
    if size == "k":
        textSurface = kfont.render(text, True, white)
    elif size == "small":
        textSurface = smallfont.render(text, True, red)
    elif size == "small1":
        textSurface = small1font.render(text, True, black)
    elif size == "small2":
        textSurface = small2font.render(text, True, purple)
    elif size == "medium":
        textSurface = mediumfont.render(text, True, green)
    elif size == "medium1":
        textSurface = medium1font.render(text, True, blue)
    elif size == "large":
        textSurface = largefont.render(text, True, black)
    elif size == "large1":
        textSurface = large1font.render(text, True, purple)
    elif size == "large2":
        textSurface = large2font.render(text, True, green)
    return textSurface, textSurface.get_rect()

################ G A M E   P L A Y ################
player = Player()
cat = Cat()
farmer = Farmer()
unicorn = Unicorn()
rock = Rock()
mom = Mom()
fairy = Fairy()
currentScreen = bg1
################################################
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
            unicorn.create(gameDisplay)
            unicorn.feel(player)
            mom.art(gameDisplay)
            mom.sense(player)
            fairy.scribble(gameDisplay)
            fairy.hit(player)
            player.update()
            pygame.display.update()
            gameDisplay.fill((0,0,0))
            gameDisplay.blit(currentScreen, (0,0))
            clock.tick(40)



################ I N T R O   S C R E E N  ################
def gameIntro ():
    intro = True
    ########### layout of the intro screen #####################
    gameDisplay.fill(white)
    message_to_screen("The Forest", green, -30, size = "large2")
    message_to_screen("Press ENTER to play or ESCAPE to quit", red, 160, size = "small")
    message_to_screen("Press BACKSPACE to see the instructions", red, 180, size = "small")
    message_to_screen("Press SPACE to view the Game Makers", red, 200, size = "small")

    while intro:
        for event in pygame.event.get(): ### choice to exit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    intro = False
                    gameStart()

                elif event.key == pygame.K_SPACE:
                    intro = False
                    gameMaker()

                elif event.key == pygame.K_BACKSPACE:
                    intro = False
                    gameInstructions()

                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        pygame.display.update()
        clock.tick(40)

################ S T A R T I N G   T H E   G A M E ################
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

################ I N S T R U C T I O N S ################
def gameInstructions ():
    instructions = True
    ########### layout of the intro screen #####################
    gameDisplay.fill(white)
    message_to_screen("INSTRUCTIONS", purple, -180, size = "large1")
    message_to_screen("OBJECTIVE", blue, -90, size = "medium1")
    message_to_screen("To complete all the tasks by finding her purpose in life.", black, -60, size = "small1")
    message_to_screen("GAMEPLAY", blue, 20, size = "medium1")
    message_to_screen("Use the arrow keys to move the character around area.", black, 50, size = "small1")
    message_to_screen("Get close to the NPC to interact.", black, 70, size = "small1")
    message_to_screen("Press A, S, or D to make decisions.", black, 90, size = "small1")
    message_to_screen("Press ENTER to return to the title screen", red, 180, size = "small")

    while instructions:
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

################ S U F F E R I N G ################
def gif(x,y):
    gameDisplay.blit(giff, (x,y))

x = 90
y = 50

def gameSuffer ():
    suffer = True
    gameDisplay.fill(white)
    gif(x,y)
    message_to_screen("Press ENTER to return to the title screen", red, 180, size = "small")

    while suffer:
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
################G A M E   M A K E R ################
def gameMaker ():
    maker = True
    gameDisplay.fill(white)
    message_to_screen("Game Makers", black, -150, size = "large")
    message_to_screen("Amala Akkiraju", blue, -30, size = "medium1")
    message_to_screen("Nhi Nguyen", blue, 0, size = "medium1")
    message_to_screen("Samantha Tam", blue, 30, size = "medium1")
    message_to_screen("Thalia Nguyen", blue, 60, size = "medium1")
    message_to_screen("Press SPACE for no good reason!", red, 160, size = "small")
    message_to_screen("Press ENTER to return to the title screen", red, 180, size = "small")

    while maker:
        for event in pygame.event.get(): ### choice to exit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    intro = False
                    gameIntro()

                elif event.key == pygame.K_SPACE:
                    intro = False
                    gameSuffer()

                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        pygame.display.update()
        clock.tick(40)

################  T A L K   T O   C A T ################
def talk_to_cat ():
    talk_cat = True
    gameDisplay.fill(black)
    message_to_screen("The cat guides me out of the room, and I find myself in this dark, sad, ", white, -200, size = "okie")
    message_to_screen("mysterious world filled my strange fantasy creatures. It looks like my worst ", white, -180, size = "okie")
    message_to_screen("nightmare. All of sudden, a butterfly zooms in front of me and steals my ", white, -160, size = "okie")
    message_to_screen("bracelet. 'Hey, that\'s mine! Give it back!' The butterfly turns into a ", white, -140, size = "okie")
    message_to_screen("fairy and tells me, 'Calm down, I\'ll give it back, you just need to do ", white, -120, size = "okie")
    message_to_screen("something for me. I have this precious item that was broken up into ", white, -100, size = "okie")
    message_to_screen("pieces and spread throughout this world. I need you to find those pieces ", white, -80, size = "okie")
    message_to_screen("and put them back together. I\'ll be back when you have completed the task.' ", white, -60, size = "okie")
    message_to_screen("She disappears, and I turn over to the cat with a bewildered look on my ", white, -40, size = "okie")
    message_to_screen("face. The cat, such a helpful creature, disappears, saying, 'It\'s my ", white, -20, size = "okie")
    message_to_screen("nap time! They both leave me alone on this long, winding path", white, 0, size = "okie")

    message_to_screen("Type A to go on the journey or S to ignore the cat", blue, 40, size = "okie1")

    while talk_cat:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:

                    intro = False
                    global currentScreen
                    currentScreen = bg2
                    player.x = 10
                    player.y = 10
                    talk_cat = False

                elif event.key == pygame.K_s:
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

################ T A L K   T O   F A R M E R ################
def talk_to_farmer ():
    talk_farmer = True
    gameDisplay.fill(black)
    message_to_screen("All by myself, I walk along the path when I see an old ", white, -200, size = "okie")

    message_to_screen("farmer frowning about something. Since I have nothing better  ", white, -180, size = "okie")
    message_to_screen("to do, I go over and ask him what happened. He explains to me,", white, -160, size = "okie")
    message_to_screen("'My plants are under attack from the vicious slime viruses and ", white, -140, size = "okie")
    message_to_screen("the harvest is about to come soon. If I don\'t save my plants I ", white, -120, size = "okie")
    message_to_screen(" won\'t have any food to give my family. Can you help me?'", white, -100, size= "okie")

    message_to_screen("Type A to sing and calm the farmer ", blue, -60, size = "okie1")
    message_to_screen("Type S to set fire and kill all the slimes", blue, -40, size = "okie1")
    message_to_screen("Type D to ignore the farmer ", blue, -20, size = "okie1")

    while talk_farmer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    intro = False
                    gameDisplay.fill(black)
                    message_to_screen("Fortunately, the slimes seem to enjoy my song and start", white, -180, size = "okie")
                    message_to_screen("to melt and disappear. Thrilled, the farmer thanks me and", white, -160, size = "okie")
                    message_to_screen("gives me two things: a 'fruit-like' object that can change", white, -140, size = "okie")
                    message_to_screen("color and a little seashell. I walk back to the path when I", white, -120, size = "okie")
                    message_to_screen("find a piece of paper underneath one of the plants. It says,", white, -100, size = "okie")
                    message_to_screen("'Having a soft heart in a cruel world is courage, not weakness.'", white, -80, size = "okie")

                    message_to_screen("Press ENTER to continue your journey", red, 180, size = "small")

                elif event.key == pygame.K_RETURN:
                    global currentScreen
                    currentScreen = bg7
                    player.x = 50
                    player.y = 50
                    talk_farmer = False

                elif event.key == pygame.K_s:
                    intro = False
                    gameDisplay.fill(black)
                    message_to_screen("The good thing is, the slime is gone (which was what I was supposed to do),", white, -180, size = "okie")
                    message_to_screen("but I accidentally killed all of the plants as well. The farmer, ", white, -160, size = "okie")
                    message_to_screen("outraged, strikes me and I black out. I end up in the dark room", white, -140, size = "okie")
                    message_to_screen("I was in when I first started.", white, -120, size = "okie")
                    message_to_screen("Press SPACE to start your journey again", red, 180, size = "small")

                elif event.key == pygame.K_d:
                    intro = False
                    gameDisplay.fill(black)
                    message_to_screen("I walk away from the farmer, feeling a little bad, but in no mood", white, -180, size = "okie")
                    message_to_screen("to help to help this farmer. All of a sudden, a bright light flashes", white, -160, size = "okie")
                    message_to_screen("over my eyes and I find myself in the dark room with the cat.", white, -140, size = "okie")

                    message_to_screen("Press SPACE to start your journey again", red, 180, size = "small")

                elif event.key == pygame.K_SPACE:
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

################ T A L K   T O   U N I C O R N ################
def talk_to_unicorn ():
    talk_unicorn = True
    gameDisplay.fill(black)
    message_to_screen("I see a pond in the distance and go over there to rest for", white, -200, size = "okie")
    message_to_screen("a while. I hear a cry behind me and look over to find a unicorn crying. ", white, -180, size = "okie")
    message_to_screen("I ask him what\'s wrong and he says, 'I\'m so sad and I don\'t like how", white, -160, size = "okie")
    message_to_screen("I look because I\'m as pretty as the other unicorns and everyone teases ", white, -140, size = "okie")
    message_to_screen("me.' I need to help him somehow. ", white, -120, size = "okie")

    message_to_screen("Type A to give the unicorn a seashell", blue, -60, size = "okie1")
    message_to_screen("Type S to compliment the unicorn", blue, -40, size = "okie1")
    message_to_screen("Type D to give the fruit to the unicorn ", blue, -20, size = "okie1")

    while talk_unicorn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    intro = False
                    gameDisplay.fill(black)
                    message_to_screen("When I was giving him the seashell I accidentally dropped it into", white, -180, size = "okie")
                    message_to_screen("the pond. The shell grew into a beautiful long horn. I take it and", white, -160, size = "okie")
                    message_to_screen("put it on top of the unicorn\'s head making him beautiful. Grateful,", white, -140, size = "okie")
                    message_to_screen("the unicorn thanks me and gives me another piece of paper saying,", white, -120, size = "okie")
                    message_to_screen("'let love for youself set you free of them.' I sigh and put the ", white, -100, size = "okie")
                    message_to_screen("paper in my back pocket and continue along", white, -80, size = "okie")

                    message_to_screen("Press ENTER to continue your journey", red, 180, size = "small")

                elif event.key == pygame.K_RETURN:
                    global currentScreen
                    currentScreen = bg8
                    player.x = 50
                    player.y = 50
                    talk_unicorn = False

                elif event.key == pygame.K_s:
                    intro = False
                    gameDisplay.fill(black)
                    message_to_screen("'Society is never nice to anyone anyways.'The unicorn gets angry", white, -180, size = "okie")
                    message_to_screen("and says,'The same goes for you.' I think to myself,'Wow he'\s mean,", white, -160, size = "okie")
                    message_to_screen("no wonder he doesn\'t have any friends.' Funnily enough, I soon find", white, -140, size = "okie")
                    message_to_screen("myself in back in the dark room.", white, -120, size = "okie")

                    message_to_screen("Press SPACE to restart your journey", red, 180, size = "small")

                elif event.key == pygame.K_d:
                    intro = False
                    gameDisplay.fill(black)
                    message_to_screen("The unicorn is allergic to the fruit and has a reaction. Well,", white, -180, size = "okie")
                    message_to_screen("how was I supposed to know. He gets mad at me and beats me up.", white, -160, size = "okie")
                    message_to_screen("I black out and find myself back in the dark room with the cat", white, -140, size = "okie")

                    message_to_screen("Press SPACE to restart your journey", red, 180, size = "small")

                elif event.key == pygame.K_SPACE:
                    global currentScreen
                    currentScreen = bg1
                    player.x = 10
                    player.y = 10
                    talk_unicorn = False

                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        pygame.display.update()
        clock.tick(40)

################ T A L K   T O   R O C K ################
def talk_to_rock ():
    talk_rock = True
    gameDisplay.fill(black)
    gameDisplay.fill(black)
    message_to_screen("Night is begining to fall and I decide to take a break. I\'m", white, -200, size = "okie")
    message_to_screen("about to sit on a rock when I hear a tiny voice yelling 'STOOPP!!'", white, -180, size = "okie")
    message_to_screen("Surprised, I stand up and look for the source of the sound.", white, -160, size = "okie")
    message_to_screen("I look at the ground and see a small rock looking at me in anger", white, -140, size = "okie")
    message_to_screen("A group of big rocks witnessed the scene and laughed and mocked", white, -120, size = "okie")
    message_to_screen("the little rock. The little rock was embarrassed and angry.", white, -100, size = "okie")
    message_to_screen("I felt bad for the little rock and told the big rocks to stop", white, -80, size = "okie")
    message_to_screen("laughing. They pause, and erupt in an even louder laughter", white, -60, size = "okie")
    message_to_screen("Annoyed, I think of something to help the little rock and stop", white, -40, size = "okie")
    message_to_screen("their rudeness.", white, -20, size = "okie")

    message_to_screen("Type A to use a hammer to break the big rocks", blue, -60, size = "okie1")
    message_to_screen("Type S to play the flute", blue, -40, size = "okie1")
    message_to_screen("Type D to read the book from the unicorn", blue, -20, size = "okie1")

    while talk_rock:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    intro = False
                    gameDisplay.fill(black)
                    message_to_screen("I use the hammer the unicorn gave me to break the big rocks into", white, -140, size = "okie")
                    message_to_screen("little rocks. The rocks get mad and start attacking me. The little", white, -120, size = "okie")
                    message_to_screen("rock watches me get crushed in fear of being bullied by the other rocks.", white, -100, size = "okie")

                    message_to_screen("Press SPACE to restart your journey", red, 180, size = "small")

                elif event.key == pygame.K_s:
                    intro = False
                    gameDisplay.fill(black)
                    message_to_screen("I play the flute given to me by the unicorn but I haven\'t played the", white, -140, size = "okie")
                    message_to_screen("flute in a few years and I play a high pitched squeaky sound, irritating", white, -120, size = "okie")
                    message_to_screen("the rocks. They surround me and crush me. ", white, -100, size = "okie")

                    message_to_screen("Press SPACE to restart your journey", red, 180, size = "small")

                elif event.key == pygame.K_d:
                    intro = False
                    gameDisplay.fill(black)
                    message_to_screen("I use the book the unicorn gave me. I open it, realizing that", white, -180, size = "okie")
                    message_to_screen("the book is empty. I panic and just stand there. After a while,", white, -160, size = "okie")
                    message_to_screen("I tell a story about a beautiful garden, a story my mom used to", white, -140, size = "okie")
                    message_to_screen("as a child. The rocks thank me for bringing them joy and life", white, -140, size = "okie")
                    message_to_screen("in their boring life. I walk away contently and I pass by a cave,", white, -140, size = "okie")
                    message_to_screen("I see a piece of paper wedged between the rocks of the cave. I", white, -140, size = "okie")
                    message_to_screen("wiggle out the piece of paper and read it. 'There is no love without'", white, -140, size = "okie")
                    message_to_screen("forgiveness and there is no forgiveness without love.' I don\'t understand", white, -140, size = "okie")
                    message_to_screen("and keep walking straight.", white, -140, size = "okie")

                    message_to_screen("Press ENTER to continue your journey", red, 180, size = "small")

                elif event.key == pygame.K_RETURN:
                    global currentScreen
                    currentScreen = bg8
                    player.x = 50
                    player.y = 50
                    talk_rock = False

                elif event.key == pygame.K_SPACE:
                    global currentScreen
                    currentScreen = bg1
                    player.x = 10
                    player.y = 10
                    talk_rock = False

                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        pygame.display.update()
        clock.tick(40)
################ T A L K   T O   M O M ################
def talk_to_mom ():
    talk_mom = True
    gameDisplay.fill(black)
    message_to_screen("'What are you doing?' My heart almost jumps out of my chest. It\'s Mom!", white, -200, size = "okie")
    message_to_screen("I turn around and face her and explain my whole situation, but she spats, ", white, -180, size = "okie")
    message_to_screen("'Why did you leave my all alone in the house?' Fear creeps into my chest", white, -160, size = "okie")
    message_to_screen(" as she continues, 'Are you dumping your mom just like your useless dad?", white, -140, size = "okie")
    message_to_screen("Who do you think you are? You are nothing to me. You are nothing but a ", white, -120, size = "okie")
    message_to_screen("hinderance to me and that useless father of yours. However, I won\'t ", white, -100, size = "okie")
    message_to_screen("just abandon you. I can give you a choice. You either come live ", white, -80, size = "okie")
    message_to_screen("with me or get out of my house and live with your terrible Dad.' ", white, -60, size = "okie")

    message_to_screen("Type A to say 'I love both of you so I decide to live alone.'", blue, 0, size = "okie1")
    message_to_screen("Type S to say 'I want to live with both of you guys. I love you both!'", blue, 20, size = "okie1")

    while talk_mom:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    intro = False
                    gameDisplay.fill(black)
                    message_to_screen("I stand there crying but smiling at the same time to Mom.", white, -180, size = "okie")
                    message_to_screen("'Mom, I know dad has done many bad things to you, but he", white, -160, size = "okie")
                    message_to_screen("still loves you a lot, as much as I do. I know both of you", white, -140, size = "okie")
                    message_to_screen("have made mistakes, but I forgive you. You don\'t have to worry", white, -120, size = "okie")
                    message_to_screen("about me anymore. I\'ll take care of myself.' I smile at my mom", white, -100, size = "okie")
                    message_to_screen("as she slowly disappears. As she fades away, she mouths,'We are", white, -80, size = "okie")
                    message_to_screen("proud of you.'", white, -60, size = "okie")

                    message_to_screen("Press ENTER to continue", red, 180, size = "small")

                elif event.key == pygame.K_RETURN:
                    global currentScreen
                    currentScreen = bg9
                    player.x = 50
                    player.y = 50
                    talk_mom = False

                elif event.key == pygame.K_s:
                    intro = False
                    gameDisplay.fill(black)
                    message_to_screen("I shout out, leaving Mom surprised, 'I love you Mom and I love'", white, -180, size = "okie")
                    message_to_screen("Dad, please don't think of me that way. We're family, remember!", white, -160, size = "okie")
                    message_to_screen("And you know, Dad loves you more than I do, so you shouldn\'t be", white, -140, size = "okie")
                    message_to_screen("saying such mean things about him.' Mom becomes furious and shouts,", white, -120, size = "okie")
                    message_to_screen("'So you are on Dad's side. I took care of you for so many years", white, -100, size = "okie")
                    message_to_screen("and this is how you treat me? You disappoint me. I should have ", white, -80, size = "okie")
                    message_to_screen("just dumped you with those nuns at the church nearby.' Mom runs over", white, -60, size = "okie")
                    message_to_screen("to me and chokes me. 'Mom...' I gasped and wake up again in the dark", white, -40, size = "okie")
                    message_to_screen("room.", white, -20, size = "okie")

                    message_to_screen("Press SPACE to restart your journey", red, 180, size = "small")

                elif event.key == pygame.K_SPACE:
                    global currentScreen
                    currentScreen = bg1
                    player.x = 10
                    player.y = 10
                    talk_mom = False

                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        pygame.display.update()
        clock.tick(40)

################ T A L K   T O   F A I R Y ################
def talk_to_fairy ():
    talk_fairy = True
    gameDisplay.fill(black)
    message_to_screen("As my mom vanishes, the fairy reappears, and states, 'You have had ", white, -200, size = "okie")
    message_to_screen("many hardships with your family, yet you kept a kind and unique", white, -180, size = "okie")
    message_to_screen("heart throughout the journey. Because of that, I shall grant you ", white, -160, size = "okie")
    message_to_screen("a wish. To get home, you have to choose between the drawing and ", white, -140, size = "okie")
    message_to_screen("the bracelet. With the drawing, you will go back to the reality ", white, -120, size = "okie")
    message_to_screen("of an unloved daughter, but a stronger heart. With the bracelet,", white, -100, size = "okie")
    message_to_screen("you will go to another universe where you have different parents,", white, -80, size = "okie")
    message_to_screen("but you will be loved. You can only choose one, dear.' ", white, -60, size = "okie")

    message_to_screen("Type A to choose the drawing", blue, 0, size = "okie1")
    message_to_screen("Type S to choose the bracelet", blue, 20, size = "okie1")

    while talk_fairy:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    intro = False
                    gameDisplay.fill(black)
                    message_to_screen("I open my eyes and blink several times. I rub my eyes", white, -180, size = "okie")
                    message_to_screen("and realize I\'m in a hospital.'Was that all a dream?'", white, -160, size = "okie")
                    message_to_screen("As I get up slowly, I hear a loud commotion", white, -140, size = "okie")
                    message_to_screen("outside the door. The door was then forced open by Mom", white, -120, size = "okie")
                    message_to_screen("and Dad. I was flabbergasted. They both cry out, seeing ", white, -100, size = "okie")
                    message_to_screen("how I was fine and run over to hug me. 'We\'re sorry for ", white, -80, size = "okie")
                    message_to_screen("what we did. We should\'ve been better parents.' I smile,", white, -60, size = "okie")
                    message_to_screen("knowing that I would have achieved great things even if I was by myself.", white, -40, size = "okie")

                    message_to_screen("Press ENTER", red, 180, size = "small")

                elif event.key == pygame.K_RETURN:
                    intro = False
                    gameThanks()

                elif event.key == pygame.K_s:
                    intro = False
                    gameDisplay.fill(black)
                    message_to_screen("I open my eyes and see that I\'m in a dungeon. I try", white, -180, size = "okie")
                    message_to_screen("to get out but my hands are chained. The door opens", white, -160, size = "okie")
                    message_to_screen("up and a woman, whom I know is my mother, comes in.", white, -140, size = "okie")
                    message_to_screen("She throws me a dress and orders me to get ready.", white, -120, size = "okie")
                    message_to_screen("'Time to act like a loving family,' my 'mother' ", white, -100, size = "okie")
                    message_to_screen("smiles with an evil grin. Realization dawns on me.", white, -80, size = "okie")
                    message_to_screen("Indeed, I did have new parents, and I was 'loved.'", white, -60, size = "okie")
                    message_to_screen("You failed to find your purpose in life. ", white, -20, size = "okie")

                    message_to_screen("Press SPACE to restart the game.", red, 180, size = "small")

                elif event.key == pygame.K_SPACE:
                    global currentScreen
                    currentScreen = bg1
                    player.x = 10
                    player.y = 10
                    talk_fairy = False

                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        pygame.display.update()
        clock.tick(40)

################ G A M E   T H A N K S ################
def thank(x,y):
    gameDisplay.blit(ty, (0,0))

def gameThanks():
    thanks = True
    gameDisplay.fill(white)
    thank(0,0)
    message_to_screen("You have found your purpose in life! Great job!", purple, -80, size = "small2")
    message_to_screen("Thank you for playing!", white, -20, size = "k")
    message_to_screen("Press ENTER to return to the title screen", red, 220, size = "small")

    while thanks:
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

################################################
pygame.init()
pygame.display.init()
gameIntro()
gameStart()
gameMaker()
gameInstructions()
gameThanks()

pygame.quit()
pygame.display.quit()
quit()

gameLoop()
