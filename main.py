from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

# (1) Create 800 x 600 screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("WenJun's Pong Game")
screen.tracer(0)  # turn off the animation, so the paddle won't "move" to the coordinate

# (2) create paddle (by creating class method)

right_paddle = Paddle((370, 0))

left_paddle = Paddle((-380, 0))

# move the paddle (up adn down function in paddle class)
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

# (3) Create ball
ball = Ball()

# (6)Record score
score = Score()

on_game = True


while on_game:
    time.sleep(ball.move_speed)  # to make the ball move slower
    screen.update()  # update the screen without the moving animation from center to the side of screen
    ball.move()

    # (4) Detect collision with upper and lower walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # (5) Detect paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 340:  # distance only measured from center
        ball.rebounce()

    if ball.distance(left_paddle) < 40 and ball.xcor() > -390:
        ball.rebounce()

    if ball.xcor() > 395:
        score.left_paddle_score()
        ball.restart()

    if ball.xcor() < -395:
        score.right_paddle_score()
        ball.restart()

screen.exitonclick()
