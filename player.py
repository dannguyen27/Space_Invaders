# TODO Define Player class
# TODO Initialize player attributes like position, speed, and shape
# TODO Create a method to move the player left and right
# TODO Create a method to ensure player boundaries (not moving off-screen)
# TODO Add a method to handle player shooting

from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    #Player movement left
    def go_left(self):
        x = self.xcor() - MOVE_DISTANCE
        self.setx(x)

    #Player movement Right
    def go_right(self):
        x = self.xcor() + MOVE_DISTANCE
        self.setx(x)       

    #Player starting position
    def go_to_start(self):
        self.goto(STARTING_POSITION)
