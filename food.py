from turtle import Turtle
from random import randint
import snake


class Food:
    def __init__(self):
        self.food_creation()

    def food_creation(self):
        self.food = Turtle()
        self.food.penup()
        self.food.shape("circle")
        self.food.color("green")
        self.foodx = randint(-370, 370)
        self.foody = randint(-370, 370)
        self.food.goto(self.foodx, self.foody)
        self.food.shapesize(stretch_len=0.8, stretch_wid=0.8)
        return self.food

    def food_collide_snake(self):
        if snake.Snake.all_square_initial[0].distance(self.food) < 15:
            self.food.reset()
            self.food.hideturtle()
            self.food_creation()
            return True
