from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(1, 5)
        self.penup()
        # self.speed("fastest")
        self.goto(0, -270)

    def move_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def move_left(self):
        new_x1 = self.xcor() - 20
        self.goto(new_x1, self.ycor())