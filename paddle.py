import turtle
class Paddle(turtle.Turtle):
    ''' creating paddles and aligning it to the corners of the screen both sides'''

    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.setheading(90)
        self.goto(position)


class pdl_moves:
    """PAddle movement control"""
    def __init__(self,pdl):
        self.pdl= pdl

    def up(self):
        if (self.pdl.ycor() < 240):
            self.pdl.sety(self.pdl.ycor()+30)


    def down(self):
        if (self.pdl.ycor() >= -220):
            self.pdl.sety(self.pdl.ycor()-30)