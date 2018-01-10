import turtle

wn=turtle.Screen()
wn.bgcolor("lightblue")
grotto=turtle.Turtle()
obstacle = (0,100)

def moveForward():
    grotto.forward(50)
    if round(grotto.xcor(),0) == obstacle[0] and round(grotto.ycor(),0) == obstacle[1]:
        print("crash")
        grotto.write("Crash!")
def turnLeft():
    grotto.left(90)
    
def turnRight():
    grotto.right(90)
    
def quitGame():
    wn.bye()
    
def move50(x,y):
    grotto.forward(50)
    
wn.onkey(moveForward, "Up")
wn.onkey(turnLeft, "Left")
wn.onkey(turnRight, "Right")
wn.onkey(quitGame, "q")
wn.textinput("NIM", "Name of first player:")
grotto.onclick(move50)

wn.listen()
wn.mainloop()