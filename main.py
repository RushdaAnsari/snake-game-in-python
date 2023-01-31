import turtle
from turtle import Screen
from snake_body import Snake
from food import Food
from score import Score
import keyboard
import time

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

# classes
snake = Snake()
food = Food()
score = Score()
FONT = ("Arial", 16, "normal")

# event listeners
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collide with food
    if snake.head.distance(food) < 13:
        food.refresh()
        snake.extend()
        score.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset_game()
        snake.reset_snake()

    #  detect collision with snake tail
    for segment in snake.segments[1:]:
        # if head collides with segments then game over
        if snake.head.distance(segment) < 10:
            score.reset_game()
            snake.reset_snake()
            turtle.color("yellow")
            turtle.write("Game Over", align="center", font=FONT)
            game_is_on = False

    # pause button
    if keyboard.is_pressed("p"):
        time.sleep(2)
        continue

    # quit button
    if keyboard.is_pressed("q"):
        turtle.color("yellow")
        turtle.write("Game Exited", align="center", font=FONT)
        game_is_on = False




screen.exitonclick()