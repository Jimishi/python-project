import turtle

window = turtle.Screen()
window.title("Project Pong")
window.bgcolor("black")
window.setup(width=800, height = 600)

#   Paddle Left
paddle_left = turtle.Turtle()
paddle_left.speed(0) #Speed of animation
paddle_left.shape("square") #There are built in shapes from Turtle
paddle_left.shapesize(stretch_wid=5, stretch_len=1)
paddle_left.color("blue")
paddle_left.penup() #remove the line drawn from moving the square 
paddle_left.goto(-350, 0)

#   Paddle Right
paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape("square")
paddle_right.shapesize(stretch_wid=5,stretch_len=1)
paddle_right.color("red")
paddle_right.penup()
paddle_right.goto(350, 0)

#   Ball
ball = turtle.Turtle()
ball.speed("fas")
ball.shape("square")
ball.color("white")
ball.penup()
ball.deltax = 2 #Everytime the ball moves, it moves by 2 pixels
ball.deltay = 2

#   Functions 
##  Left Paddle
def paddle_left_up():
    y = paddle_left.ycor() #ycor from turtle method, returns y coordinates 
    y += 20
    paddle_left.sety(y)

def paddle_left_down():
    y = paddle_left.ycor() #ycor from turtle method, returns y coordinates 
    y -= 20
    paddle_left.sety(y) 

##  Right Paddle
def paddle_right_up():
    y = paddle_right.ycor() #ycor from turtle method, returns y coordinates 
    y += 20
    paddle_right.sety(y)

def paddle_right_down():
    y = paddle_right.ycor() #ycor from turtle method, returns y coordinates 
    y -= 20
    paddle_right.sety(y) 

#   Keyboard binding
window.listen() #listen() is a turtle method that waits for key input
window.onkeypress(paddle_left_up, "w")
window.onkeypress(paddle_left_down, "s") 

window.onkeypress(paddle_right_up, "Up")
window.onkeypress(paddle_right_down, "Down") 

while True:
    window.update()

    #   Move the boll
    ball.setx(ball.xcor() + ball.deltax) 
    ball.sety(ball.ycor() + ball.deltay)

    #   Border checking
    if  ball.ycor() > 290:
        ball.sety(290)
        ball.deltay *= -1 #Reverses direction

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.deltay *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0) 
        ball.deltax *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.deltax *= -1

    #   Paddle Collision
    if  (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_right.ycor() + 40 and ball.ycor() > paddle_right.ycor() -50):
            ball.setx(340)
            ball.deltax *= -1

    if  (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_left.ycor() + 40 and ball.ycor() > paddle_left.ycor() -50):
            ball.setx(-340)
            ball.deltax *= -1