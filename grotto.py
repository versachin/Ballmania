import turtle

wn=turtle.Screen()
wn.bgcolor("lightblue")
grotto=turtle.Turtle()
maze=turtle.Turtle()

obstacle = (0.100)
grotto.penup()
grotto.left(90)
grotto.forward(100)


def moveForward():
    grotto.forward(10)
    if round(grotto.xcor(),0) == obstacle[0] and round(grotto.ycor(),0) == obstacle[1]:
        print("crash")
        grotto.write("CRASH!")
def turnLeft():
    grotto.left(90)
    
def turnRight():
    grotto.right(90)
    
def quitGame():
    wn.bye()
    
def move50(x,y):
    grotto.forward(10)

    
wn.onkey(moveForward, "Up")
wn.onkey(turnLeft, "Left")
wn.onkey(turnRight, "Right")
wn.onkey(quitGame, "q")
wn.textinput("NIM", "Name of first player:")
grotto.onclick(move50)
def maze_func(turt):
    turt.right(90)
    turt.forward(200)
    turt.left(90)
    turt.forward(300)
    turt.penup()
    turt.forward(37.5)
    turt.pendown()
    turt.left(90)
    turt.forward(200)
    turt.left(90)
    turt.forward(275)
    turt.penup()
    turt.forward(25)
    turt.left(90)
    turt.pendown()
    turt.forward(175)
    turt.left(90)
    turt.forward(275)
    
maze_func(maze)
wn.listen()
wn.mainloop()