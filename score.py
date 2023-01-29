from turtle import Turtle

score = [0]
FONT = ("Arial", 16, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.penup()
        self.goto(0, 270)
        with open("high-score.txt") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.update_score()
        self.hideturtle()

    # draws scoreboard on screen
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align="center", font=FONT)

    # increase score by 1 point
    def increase_score(self):
        self.score += 1
        self.update_score()

    # resets game and score
    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            # store highscore in file
            with open("high-score.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()







