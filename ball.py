from turtle import Turtle


class Ball(Turtle):

    def __init__(self) -> None:
        super().__init__()
        """Define/construct/initialize the ball inheriting turtle class
        and with it's own attributes and methods"""
        self.shape("circle")
        self.color("white")
        self.shapesize(1)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """Keep the ball moving, having new x_move and y_move
        attributes value changed every time."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Reverse the ball direction by changing;
        y coordinate positive value to negative."""
        self.y_move *= -1

    def bounce_x(self):
        """Reverse the ball direction by changing;
        x coordinates positive value to negative. Also,
        increase speed whenever paddle hits the ball"""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """Move ball to center of screen and reset the
        ball speed back to original value."""
        self.goto(0, 0)
        self.move_speed = 0.1
