""" pong game using turtle module """
from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle, pdl_moves
from scoreboard import Scoreboard
import time


"""screen setup"""
screen = Screen()
screen.setup(width= 800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


""" Paddle created """
l_pdl = Paddle((-370,0))
r_pdl = Paddle((370,0))


"""
Ball handling
"""
ball = Ball()
ball.move()


"""
 Paddle handling
 """
left_pdl_controller = pdl_moves(l_pdl)
right_pdl_controller = pdl_moves(r_pdl)

screen.listen()
screen.onkey(fun=right_pdl_controller.up,key="Up")
screen.onkey(fun=right_pdl_controller.down,key="Down")
screen.onkey(fun=left_pdl_controller.up,key="w")
screen.onkey(fun=left_pdl_controller.down,key="s")

# score board
scoreboard = Scoreboard()

game_is_on= True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # collision with wall
    if ball.ycor() >270  or ball.ycor() < -270:
        ball.bounce_y()

    # collision with paddle
    if ( ball.distance(r_pdl) < 50 and ball.xcor() > 340 ) or ( ball.distance(l_pdl) < 50 and ball.xcor() < -340 ):
        ball.bounce_x()

    # if ball misses the paddle
    # for right paddle
    if ball.xcor() > 400 :
        ball.reset_position()
        scoreboard.l_point()

    # for left paddle
    if  ball.xcor() < -400 :
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()