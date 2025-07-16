from turtle import Turtle

class Block:
    def __init__(self):
        self.blocks = []
        self.x = -265
        self.y = 65
        self.more_blocks = 0
        while self.more_blocks < 5:
            for _ in range(1, 10):
                new = Turtle("square")
                new.color("white")
                new.penup()
                new.shapesize(2, 3)
                new.goto(self.x, self.y)
                self.blocks.append(new)
                self.x += 65
            self.x = -265
            self.y += 45
            self.more_blocks += 1
