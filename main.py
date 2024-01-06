
# Press W D S A for up right down and left

import time
from turtle import Screen, Turtle
from food import Food
from score import Score
from snake import Snake

is_moving = True

def up():
    if snake.all_square[0].heading() != 270:
        snake.all_square[0].setheading(90)


def left():
    if snake.all_square[0].heading() != 0:
        snake.all_square[0].setheading(180)


def right():
    if snake.all_square[0].heading() != 180:
        snake.all_square[0].setheading(0)


def down():
    if snake.all_square[0].heading() != 90:
        snake.all_square[0].setheading(270)

def gameover():
    game = Turtle()
    game.penup()
    game.hideturtle()
    game.goto(0, 0)
    game.color("Black")
    game.write(f"Game Over", move=False, align='center', font=('Arial', 28, 'normal'))

screen = Screen()
screen.setup(830, 820)
screen.listen()
screen.title("Snake Game")
screen.tracer(0)

screen.onkey(fun=up, key="w")
screen.onkey(fun=left, key="a")
screen.onkey(fun=right, key="d")
screen.onkey(fun=down, key="s")
snake = Snake()
food = Food()
score = Score()


while is_moving:
    time.sleep(0.3)
    snake.move()
    for i in snake.all_square:
        if i == snake.all_square[0]:
            pass
        elif snake.all_square[0].distance(i) < 10:
            score.increase_high_score()
            snake.snake_reset_positions()

    collide = food.food_collide_snake()
    if collide is True:
        score.reset_score()
        snake.snake_body_parts()

    wall_hit = snake.check_wall_hit()
    if wall_hit is True:
        score.increase_high_score()
        snake.snake_reset_positions()

    screen.update()
screen.exitonclick()
