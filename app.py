import turtle

wind = turtle.Screen() # create a screen
wind.title("Ping Pong ZAHRA") # setthe title
wind.bgcolor("black") # set bg color
wind.setup(width=800, height=600)
wind.tracer(0)


# madhrab 1
madrab1 = turtle.Turtle() #create madrab2
madrab1.speed(0)
madrab1.shape("square")
madrab1.color("blue")
madrab1.shapesize(stretch_wid=5, stretch_len=1)
madrab1.penup()
madrab1.goto(-370, 0)

# madhrab2
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.shapesize(stretch_wid=5, stretch_len=1)
madrab2.penup()
madrab2.goto(370, 0)

# madhrab3
madrab3 = turtle.Turtle()
madrab3.speed(0)
madrab3.shape("square")
madrab3.color("orange")
madrab3.shapesize(stretch_wid=1, stretch_len=5)
madrab3.penup()
madrab3.goto(0, 270)

# madhrab4
madrab4 = turtle.Turtle()
madrab4.speed(0)
madrab4.shape("square")
madrab4.color("green")
madrab4.shapesize(stretch_wid=1, stretch_len=5)
madrab4.penup()
madrab4.goto(0, -270)

# ball 1
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1 # vitesse de la balle
ball.dy = 0.1 # move the ball's dy to 2.5px

# score
score1= 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Blue : 0 <======> Red : 0", align="center", font=("Courrier", 24, "normal"))

# functions
def madrab1_up():
    y = madrab1.ycor() # get the y coordinate of madrab1
    y += 30 # add 20 to y coordinate
    madrab1.sety(y) # set the ball to start moving

def madrab1_down():
    y = madrab1.ycor()
    y -= 30
    madrab1.sety(y)

# functions
def madrab2_up():
    y = madrab2.ycor()
    y += 30
    madrab2.sety(y)

def madrab2_down():
    y = madrab2.ycor()
    y -= 30
    madrab2.sety(y)

#keyboard bindings
wind.listen() # tell the window to listen to keyboard events
wind.onkeypress(madrab1_up, "w") #when the key w is pressed, call the function madrab1_up
wind.onkeypress(madrab1_down, "x")
wind.onkeypress(madrab2_up, "l")
wind.onkeypress(madrab2_down, "m")


while True:
    wind.update()
    #move the ball
    ball.setx(ball.xcor() + ball.dx) # ball starts at 0 and every time loops run ---> +0,2 xaxis
    ball.sety(ball.ycor() + ball.dy)  # ball starts at 0 and every time loops run ---> +0,2 yaxis

    #border Y top check by ball
    if ball.ycor() > 290: # if the ball touch the top of window y=300px then this ball change direction refleted by dy -1
        ball.sety(290)
        ball.dy *= -1

    #border Y down check by ball topborder= +300px, bottom border= -300px, ball is 20px
    if ball.ycor() < -290: # if the ball touch the top of window y=300px then this ball change direction refleted by dy -1
        ball.sety(-290)  # set y coor +290
        ball.dy *= -1  # reverse direction , making +0,2 ---> -0,2

    #border X top check by ball
    if ball.xcor() > 390: # if the ball touch the top of window y=300px then this ball change direction refleted by dy -1
        #ball.setx(390)
        ball.goto(0,0) # si ya un but alors la balle go to center for new game
        ball.dx *= -1 # reverse the x direction
        score1 += 1
        score.clear()
        score.write("Blue : {} <======> Red :{}  ".format(score1, score2), align="center", font=("Courrier", 24, "normal"))

    #border X top check by ball
    if ball.xcor() < -390: # if the ball touch the top of window y=300px then this ball change direction refleted by dy -1
        # ball.setx(-390)
        ball.goto(0,0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("Blue : {} <======> Red :{}  ".format(score1, score2), align="center", font=("Courrier", 24, "normal"))

    #tasadom madrab and ball
    if(ball.xcor() > 340 and ball.xcor() <350) and (ball.ycor() < madrab2.ycor() +40 and ball.ycor() > madrab2.ycor() - 40 ):
        ball.setx(340)
        ball.dx *= -1

    if(ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < madrab1.ycor() +40 and ball.ycor() > madrab1.ycor() - 40 ):
        ball.setx(-340)
        ball.dx *= -1
