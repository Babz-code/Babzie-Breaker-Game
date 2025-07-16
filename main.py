from turtle import Screen
from paddle import Paddle
from ball import Ball
from block import Block
import time
from scoreboard import Scoreboard
from lives import Lives

screen = Screen()
screen.title("Babzie's Breaker Game")
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)


my_paddle = Paddle()
my_ball = Ball()

my_block = Block()
all_blocks = my_block.blocks
print(all_blocks)

score = Scoreboard()
lives = Lives()




screen.listen()
screen.onkey(my_paddle.move_right, "Right")
screen.onkey(my_paddle.move_left, "Left")


is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    my_ball.move_ball()

    #Detect collision with the side walls
    if my_ball.xcor() < -290 or my_ball.xcor() > 290:
        my_ball.side_wall_bounce()

    #Detect collision with upper wall
    if my_ball.ycor() > 290:
        my_ball.bounce_y()

    #Detect collision with paddle
    if my_ball.distance(my_paddle) < 50 and my_ball.ycor() < -250:
        my_ball.bounce_y()

    #Detect collision with block
    for item in range(len(all_blocks)):
        if my_ball.distance(all_blocks[item]) < 30:
            all_blocks[item].goto(1000, 1000)
            all_blocks[item].clear()
            my_ball.bounce_y()
            score.add_to_score()

    #Detect collision with wall behind paddle
    if -300 > my_ball.ycor() > -320:
        lives.lose_a_live()
        my_ball.reset_ball()

    #Detect when lives equals zero
    if lives.live == 0:
        is_game_on = False
        score.game_over()

screen.exitonclick()