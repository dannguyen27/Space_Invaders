from turtle import Turtle, Screen

custom_blockade = "images/custom_blockade.gif"
low_hp_blockade = "images/custom_blockade_low_hp.gif"

class Blockade(Turtle):
    def __init__(self, position):   
        super().__init__()
        self.durability = 3  # Starting durability
        self.screen = Screen()
        self.screen.register_shape(custom_blockade)
        self.screen.register_shape(low_hp_blockade)
        
        self.shape(custom_blockade)  # Set the shape to the custom GIF
        self.penup()
        self.goto(position)  # Set initial position

    def hit(self):
        self.durability -= 1
        if self.durability == 1:
            self.shape(low_hp_blockade)
        elif self.durability <= 0:
            self.hideturtle()  # Remove/blockade
