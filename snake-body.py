from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-30, 0), (-60, 0)]
MOVE_DISTANCE = 15
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # draws snake on screen
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    # creates snakes body
    def add_segment(self, position):
        snake = Turtle("square")
        snake.shapesize(stretch_len=0.7, stretch_wid=0.7)
        snake.color("forest green")
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)

    # resets snakes position
    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    # extend snake by adding segments to the last segment
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # make it move forward
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # snake moves up
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    # snake moves down
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # snake moves left
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # snake moves right
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

