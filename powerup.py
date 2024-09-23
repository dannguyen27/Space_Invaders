import random
from turtle import Turtle
import time

LEFT_BOUNDARY = -215  # Adjusted for 500px width screen
RIGHT_BOUNDARY = 215  # Adjusted for 500px width screen
FIXED_Y_POSITION = -280  # Fixed Y position where the power-up will spawn
POWERUP_MIN = 10
POWERUP_MAX = 15

POWER_UP_CUSTOM = "images/powerup.gif"

class PowerUpManager(Turtle):
    def __init__(self):
        super().__init__()
        self.screen = Turtle().getscreen()  # Get screen from the Turtle environment
        self.screen.addshape(POWER_UP_CUSTOM)
        self.shape(POWER_UP_CUSTOM)
        self.penup()
        self.hideturtle()  # Initially hide the power-up
        self.all_powerups = []  # List to keep track of all power-ups
        self.next_spawn_time = time.time() + random.randint(POWERUP_MIN,POWERUP_MAX)

    def spawn(self):
        current_time = time.time()
        if current_time > self.next_spawn_time:
            """Spawn a new power-up at a random x position on the fixed y position."""
            random_x = random.randint(LEFT_BOUNDARY, RIGHT_BOUNDARY)
            self.goto(random_x, FIXED_Y_POSITION)
            self.showturtle()
            self.all_powerups.append(self)  # Add itself to the list of power-ups
            self.next_spawn_time = current_time + random.randint(10, 20)  # Set next spawn time


    def remove(self):
        """Hide and remove the power-up from the list."""
        self.hideturtle()
        if self in self.all_powerups:
            self.all_powerups.remove(self)
