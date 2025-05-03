from turtle import Screen
from paddles import Paddle, Ball
from scorebored import ScoreBord
import time


screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=1000, height=700)
screen.tracer(0)

r_paddle = Paddle((460, 0))
l_paddle = Paddle((-460, 0))
ball = Ball()
scorebored = ScoreBord()


screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game_is_on = True
while game_is_on:

    time.sleep(ball.move_speed)
    screen.update()
    # Detect collision with the wall
    if ball.ycor() > 340 or ball.ycor() < -340:
        ball.bounce_y()

    # Detect collision with paddle
    if (ball.distance(r_paddle) < 60 and ball.xcor() > 440) or (ball.distance(l_paddle) < 60 and ball.xcor() < -440):
        ball.bounce_x()
# Detect When a paddle misses the ball
    if ball.xcor() >= 500:
        ball.reset_position()
        scorebored.leftscore()
        scorebored.updatescore()

    if ball.xcor() <= -500:
        ball.reset_position()
        scorebored.rightscore()
        scorebored.updatescore()

    ball.move()


screen.exitonclick()
