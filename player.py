from turtle import Turtle, Screen

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
LEFT_BOUNDARY = -215  # Adjusted for 500px width screen
RIGHT_BOUNDARY = 215  # Adjusted for 500px width screen


custom_player_gif = "images/resized_ship.gif"

class Player(Turtle):

    def __init__(self):
        super().__init__()
        # Register the custom shape
        self.screen = Screen()
        self.screen.register_shape(custom_player_gif)
        
        self.shape(custom_player_gif)  # Set the shape to the custom GIF
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_left(self):
        new_x = self.xcor() - MOVE_DISTANCE
        if new_x > LEFT_BOUNDARY:  # Check boundary
            self.setx(new_x)

    def go_right(self):
        new_x = self.xcor() + MOVE_DISTANCE
        if new_x < RIGHT_BOUNDARY:  # Check boundary
            self.setx(new_x)

    def go_to_start(self):
        self.goto(STARTING_POSITION)
