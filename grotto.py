#import turtle
import pygame

pygame.init()
white = (0, 200, 200)
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('MAZERUNNER')
clock = pygame.time.Clock()

player = pygame.image.load("ball.gif")
playerrect = player.get_rect()

crashed = False

def move_ball(x, y):
    gameDisplay.blit(player, (x, y))




def game_loop():
    global paused
    global crashed

    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0
    y_change = 0

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
        move_ball(x,y)
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()







#wn=turtle.Screen()
#wn.bgcolor("lightblue")
#grotto=turtle.Turtle()
#maze=turtle.Turtle()










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