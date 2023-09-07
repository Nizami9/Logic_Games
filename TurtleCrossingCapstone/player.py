from turtle import Turtle, Screen

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

        # if self.player.ycor() >= FINISH_LINE_Y:
        #     print("You win")

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    # def go_left(self):
    #     new_y = self.ycor() - MOVE_DISTANCE
    #     self.player.goto(self.xcor(), new_y)

    # def go_right(self):
    #     new_y = self.ycor() + MOVE_DISTANCE
    #     self.player.goto(self.xcor(), new_y)
