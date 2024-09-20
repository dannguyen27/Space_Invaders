from turtle import Turtle


class Blockade(Turtle):
    def __init__(self, position):   
        super().__init__()
        self.durability = 3  # Starting durability
        self.colors = ["green", "yellow", "red"]  # Color states
        self.shape("square")
        self.penup()
        self.goto(position)  # Set initial position
        self.color(self.colors[self.durability - 1])  # Set initial color

    def hit(self):
        self.durability -= 1
        if self.durability > 0:
            self.color(self.colors[self.durability - 1])  # Change color
        else:
            self.hideturtle()  # Remove/blockade
