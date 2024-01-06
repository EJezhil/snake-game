from turtle import Turtle
import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    all_square_initial = []
    all_square_growing = []
    all_square = []

    def __init__(self):
        self.snake_body_creation()
        self.all_square = self.all_square_initial + self.all_square_growing

    def snake_body_creation(self):
        for i in STARTING_POSITIONS:
            self.a = Turtle()
            self.a.penup()
            self.a.shape("square")
            self.a.color("black")
            self.a.speed("slow")
            self.a.goto(i)
            self.all_square_initial.append(self.a)

    def snake_body_parts(self):
        self.a1 = Turtle()
        self.a1.penup()
        self.a1.shape("square")
        self.a1.color("black")
        self.a1.speed("slow")
        x = self.all_square[-1].xcor()
        y = self.all_square[-1].ycor()
        self.a1.goto(x, y)
        self.all_square.append(self.a1)
        self.all_square_growing.append(self.a1)

    def move(self):

        for parts in range(len(self.all_square) - 1, 0, -1):
            partx = self.all_square[parts - 1].xcor()
            party = self.all_square[parts - 1].ycor()
            self.all_square[parts].goto(partx, party)
        self.all_square[0].forward(22)

    def check_wall_hit(self):
        if self.all_square[0].xcor() < -380 or self.all_square[0].xcor() > 380 or self.all_square[0].ycor() < -380 or \
                self.all_square[0].ycor() > 380:
            return True

    def snake_reset_positions(self):
        for i in self.all_square_growing:
            i.reset()
            i.hideturtle()
        self.sliced_list_wanted = self.all_square[0:3]
        self.all_square = self.sliced_list_wanted
        for i in self.all_square:
            i.reset()
            i.penup()

