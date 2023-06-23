from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.goto(-100, 300)
        self.update_scoreboard()
        self.hideturtle()


    def update_scoreboard(self):
        self.clear()
        self.goto(-150, 250)
        self.write(f'Level: {self.score}', align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align='center', font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()