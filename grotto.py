#import turtle
import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('MAZERUNNER')
clock = pygame.time.Clock()

player = pygame.image.load("ball.gif")
playerrect = player.get_rect()

crashed = False


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
        if event.key == pygame.K_RIGHT:
            x_change = 5
        if event.key == pygame.K_p:
            paused = True
            pause()

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            x_change = 0

x += x_change
gameDisplay.fill(white)


pygame.quit()
quit()




x += x_change
gameDisplay.fill(white)
#wn=turtle.Screen()
#wn.bgcolor("lightblue")
#grotto=turtle.Turtle()
#maze=turtle.Turtle()

"""main_dir = os.path.split(os.path.abspath(__file__))[0]

def load_image(file):
    "loads an image, prepares it for play"
    file = os.path.join(main_dir, 'data', file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    return surface.convert()

def load_images(*files):
    imgs = []
    for file in files:
        imgs.append(load_image(file))
    return imgs

class mazerunner(pygame.sprite.Sprite):
    speed = 10
    images = []
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=SCREENRECT.midbottom)
        self.reloading = 0
        self.origtop = self.rect.top
        self.facing = -1

    def move(self, direction):
        if direction: self.facing = direction
        self.rect.move_ip(direction*self.speed, 0)
        self.rect = self.rect.clamp(SCREENRECT)
        if direction < 0:
            self.image = self.images[0]
        elif direction > 0:
            self.image = self.images[1]
        self.rect.top = self.origtop - (self.rect.left//self.bounce%2)

    def gunpos(self):
        pos = self.facing*self.gun_offset + self.rect.centerx
        return pos, self.rect.top"""








#obstacle = (0.100)
#grotto.penup()
#grotto.left(90)
#grotto.forward(100)



#def moveForward():
 #   grotto.forward(10)
  #  if round(grotto.xcor(),0) == obstacle[0] and round(grotto.ycor(),0) == obstacle[1]:
   #     print("crash")
    #    grotto.write("CRASH!")
#def turnLeft():
 #   grotto.left(90)
  #
#def turnRight():
 #   grotto.right(90)
    
#def quitGame():
 #   wn.bye()
    
#def move50(x,y):
 #   grotto.forward(10)

    
#wn.onkey(moveForward, "Up")
#wn.onkey(turnLeft, "Left")
#wn.onkey(turnRight, "Right")
#wn.onkey(quitGame, "q")
#wn.textinput("NIM", "Name of first player:")
#grotto.onclick(move50)
#def maze_func(turt):
 #   turt.right(90)
  ###turt.forward(300)
    #turt.penup()
    #turt.forward(37.5)
#    turt.pendown()
###  turt.left(90)
#    turt.forward(275)
 #   turt.penup()
  #  turt.forward(25)
   # turt.left(90)
    #turt.pendown()
#    turt.forward(175)
 #   turt.left(90)
  #  turt.forward(275)
#def maze_two(turt):
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
    #turt.left(90)
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