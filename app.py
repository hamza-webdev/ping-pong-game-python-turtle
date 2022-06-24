import turtle

wind = turtle.Screen()
wind.title("Ping Pong ZAHRA")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)


# madhrab 1
madrab1 = turtle.Turtle()
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

# functions
def madrab1_up():
    y = madrab1.ycor()
    y += 20
    madrab1.sety(y)

def madrab1_down():
    y = madrab1.ycor()
    y -= 20
    madrab1.sety(y)

# functions
def madrab2_up():
    y = madrab2.ycor()
    y += 20
    madrab2.sety(y)

def madrab2_down():
    y = madrab2.ycor()
    y -= 20
    madrab2.sety(y)

#keyboard bindings
wind.listen()
wind.onkeypress(madrab1_up, "w")
wind.onkeypress(madrab1_down, "x")
wind.onkeypress(madrab2_up, "l")
wind.onkeypress(madrab2_down, "m")


while True:
    wind.update()








