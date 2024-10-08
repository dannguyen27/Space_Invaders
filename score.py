from turtle import Turtle
import time

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()  # Initialize Turtle
        self.score = 0  # Start with 0 score
        self.level = 1
        self.lives = 3
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-240, 270)  # Adjusted for new screen dimensions
        self.update_scoreboard()
        

    def increase_score(self):
        self.score += 50
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def play_again(self):
        self.goto(0, -30)
        self.write("Play Again : P  Quit: Q", align="center", font=FONT)


    def level_up(self):
        self.clear()
        self.level += 1
        self.goto(0, 0)
        time.sleep(1)
        self.write("LEVEL UP", align="center", font=FONT)
        self.getscreen().update()
        time.sleep(1)

        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-240, 270)  # Reset position for scoreboard
        self.write(f"Score: {self.score}", align="left", font=FONT)
        self.goto(-240, 245)  # Adjust vertical position for level
        self.write(f"Level: {self.level}", align="left", font=FONT)
        self.goto(-240, 220)  # Adjust vertical position for level
        self.write(f"Lives {self.lives}", align="left", font=FONT)

    def lose_life(self):
        self.lives -=1