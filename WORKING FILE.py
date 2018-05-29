# import turtle
import pygame
from pygame.locals import *

pygame.init()
white = (0, 200, 200)
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('MAZERUNNER')
clock = pygame.time.Clock()
SCREENRECT = Rect(0, 0, 640, 480)

player = pygame.image.load("ball.gif")
playerrect = player.get_rect()

crashed = False


def load_image(file):
    "loads an image, prepares it for play"
    file = os.path.join(main_dir, 'data', file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s' % (file, pygame.get_error()))
    return surface.convert()


def load_images(*files):
    imgs = []
    for file in files:
        imgs.append(load_image(file))
    return imgs


#class maze(pygame.sprite.Sprite):


class Player(pygame.sprite.Sprite):
    speed = 10
    bounce = 24

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=SCREENRECT.midbottom)
        self.reloading = 0
        self.origtop = self.rect.top
        self.facing = -1

    def move(self, direction):
        if direction: self.facing = direction
        self.rect.move_ip(direction * self.speed, 0)
        self.rect = self.rect.clamp(SCREENRECT)
        if direction < 0:
            self.image = self.images[0]
        elif direction > 0:
            self.image = self.images[1]
        self.rect.top = self.origtop - (self.rect.left // self.bounce % 2)


class maze(pygame.sprite.Sprite):

    def move_ball(x, y):
        gameDisplay.blit(player, (x, y))


def game_loop():
    global paused
    global crashed

    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0
    y_change = 0

    def main(winstyle=0):
        # Initialize pygame
        """pygame.init()
        if pygame.mixer and not pygame.mixer.get_init():
            print('Warning, no sound')
            pygame.mixer = None"""

        # Set the display mode
        winstyle = 0  # |FULLSCREEN
        bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
        screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

        # Load images, assign to sprite classes
        # (do this before the classes are used, after screen setup)
        img = load_image('ball.gif')
        Player.images = [img, pygame.transform.flip(img, 1, 0)]
        # img = load_image('explosion1.gif')
        # Explosion.images = [img, pygame.transform.flip(img, 1, 1)]
        # Alien.images = load_images('alien1.gif', 'alien2.gif', 'alien3.gif')
        # Bomb.images = [load_image('bomb.gif')]
        # Shot.images = [load_image('shot.gif')]

        # decorate the game window
        # icon = pygame.transform.scale(Alien.images[0], (32, 32))
        # pygame.display.set_icon(icon)
        # pygame.display.set_caption('Pygame Aliens')
        # pygame.mouse.set_visible(0)

        # create the background, tile the bgd image
        bgdtile = load_image('background.gif')
        background = pygame.Surface(SCREENRECT.size)
        for x in range(0, SCREENRECT.width, bgdtile.get_width()):
            background.blit(bgdtile, (x, 0))
        screen.blit(background, (0, 0))
        pygame.display.flip()

        # load the sound effects
        # boom_sound = load_sound('boom.wav')
        # shoot_sound = load_sound('car_door.wav')
        # if pygame.mixer:
        # music = os.path.join(main_dir, 'data', 'house_lo.wav')
        # pygame.mixer.music.load(music)
        # pygame.mixer.music.play(-1)

        # Initialize Game Groups
        # aliens = pygame.sprite.Group()
        # shots = pygame.sprite.Group()
        # bombs = pygame.sprite.Group()
        # all = pygame.sprite.RenderUpdates()
        # lastalien = pygame.sprite.GroupSingle()

        # assign default groups to each sprite class
        Player.containers = all
        # Alien.containers = aliens, all, lastalien
        # Shot.containers = shots, all
        # Bomb.containers = bombs, all
        # Explosion.containers = all
        # Score.containers = all

        # Create Some Starting Values
        global score
        # alienreload = ALIEN_RELOAD
        # kills = 0
        clock = pygame.time.Clock()

        # initialize our starting sprites
        global SCORE
        player = Player()
        Alien()  # note, this 'lives' because it goes into a sprite group
        if pygame.font:
            all.add(Score())

    while not crashed:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            print(event)
        gameDisplay.blit(player, playerrect)
        pygame.display.update()
        clock.tick(60)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
                pygame.display.update()
                gameDisplay.blit(player, playerrect)
            if event.key == pygame.K_RIGHT:
                x_change = 5
            if event.key == pygame.K_UP:
                y_change = -5
            if event.key == pygame.K_DOWN:
                y_change = 5
                pygame.display.update()
                gameDisplay.blit(player, playerrect)
            if event.key == pygame.K_p:
                paused = True
                pause()
                pygame.display.update()
                gameDisplay.blit(player, playerrect)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0

        x += x_change
        y += y_change
        gameDisplay.fill(white)
        maze.move_ball(x, y)
        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()

# wn=turtle.Screen()
# wn.bgcolor("lightblue")
# grotto=turtle.Turtle()
# maze=turtle.Turtle()


# obstacle = (0.100)
# grotto.penup()
# grotto.left(90)
# grotto.forward(100)


# def moveForward():
#   grotto.forward(10)
#  if round(grotto.xcor(),0) == obstacle[0] and round(grotto.ycor(),0) == obstacle[1]:
#     print("crash")
#    grotto.write("CRASH!")
# def turnLeft():
#   grotto.left(90)
#
# def turnRight():
#   grotto.right(90)

# def quitGame():
#   wn.bye()

# def move50(x,y):
#   grotto.forward(10)


# wn.onkey(moveForward, "Up")
# wn.onkey(turnLeft, "Left")
# wn.onkey(turnRight, "Right")
# wn.onkey(quitGame, "q")
# wn.textinput("NIM", "Name of first player:")
# grotto.onclick(move50)
# def maze_func(turt):
#   turt.right(90)
###turt.forward(300)
# turt.penup()
# turt.forward(37.5)
#    turt.pendown()
###  turt.left(90)
#    turt.forward(275)
#   turt.penup()
#  turt.forward(25)
# turt.left(90)
# turt.pendown()
#    turt.forward(175)
#   turt.left(90)
#  turt.forward(275)
# def maze_two(turt):
#   turt.penup()
#  turt.setpos(300,300)
# turt.pendown()
#    turt.right(180)
#   turt.forward(500)
#  turt.left(90)
# turt.forward(250)
#    turt.forward(50)
##  turt.left(90)
#     turt.forward(500)
#  turt.left(90)
# turt.forward(250)
#   turt.penup()
#  turt.forward(50)
# turt.pendown()
# turt.left(90)
#    turt.forward(260)
#   turt.left(90)
#  turt.forward(200)
# turt.left(90)
#  turt.forward(50)
#   turt.left(90)
# turt.forward(50)

"""def make_square(turt,size,x,y):
    turt.penup()
    turt.setpos(x,y)
    turt.pendown()
    for i in range(4):
        turt.right(90)
        turt.forward(size)
make_square(maze,50,100,200)
#maze_func(maze)
wn.listen()
wn.mainloop()"""