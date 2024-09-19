# TODO: Define Enemy class
# TODO: Initialize enemy attributes like position, speed, and shape
# TODO: Create a method to move enemies left to right and down
# TODO: Implement logic to handle collision with player bullets
# TODO: Add enemy respawn or destruction logic

from turtle import Turtle

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class EnemyManager:
    def __init__(self):
        self.all_enemies = []
        self.enemy_speed = STARTING_MOVE_DISTANCE
        self.create_enemies()

    def create_enemies(self):
        """Create a grid of enemies"""
        start_x = -200
        start_y = 250
        spacing_x = 50
        spacing_y = 40

        for row in range(5):  # 5 rows
            for col in range(11):  # 11 columns
                new_enemy = Turtle("square")
                new_enemy.shapesize(stretch_wid=1, stretch_len=2)
                new_enemy.penup()
                new_enemy.color("red")
                new_enemy.goto(start_x + col * spacing_x, start_y - row * spacing_y)
                self.all_enemies.append(new_enemy)

    def move_enemies(self):
        """Move enemies left to right and down"""
        # Move enemies horizontally
        for enemy in self.all_enemies:
            new_x = enemy.xcor() + self.enemy_speed
            enemy.setx(new_x)

        # Check if any enemy has reached the edge of the screen
        if any(enemy.xcor() > 280 or enemy.xcor() < -280 for enemy in self.all_enemies):
            self.enemy_speed *= -1  # Reverse direction
            self.move_down()

    def move_down(self):
        """Move all enemies down"""
        for enemy in self.all_enemies:
            new_y = enemy.ycor() - MOVE_INCREMENT
            enemy.sety(new_y)
