from turtle import Turtle

STARTING_MOVE_DISTANCE = 3
MOVE_INCREMENT = 0.75
STARTING_ENEMY_AMOUNT_ROW = 2
STARTING_ENEMY_AMOUNT_COLUMN = 4
ENEMY_INCREASE = 1

class EnemyManager:
    def __init__(self):
        self.all_enemies = []
        self.enemy_speed = STARTING_MOVE_DISTANCE
        self.level = 1  # Initialize level
        self.create_enemies(STARTING_ENEMY_AMOUNT_ROW, STARTING_ENEMY_AMOUNT_COLUMN)

    def create_enemies(self, rows, columns):
        # Clear existing enemies
        for enemy in self.all_enemies:
            enemy.hideturtle()
        self.all_enemies.clear()
        
        """Create a grid of enemies"""
        start_x = -150  # Adjusted for smaller screen
        start_y = 200   # Adjusted for smaller screen
        spacing_x = 50
        spacing_y = 40


        for row in range(rows):  
            for col in range(columns):  
                new_enemy = Turtle("turtle")
                new_enemy.seth(270)
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
        if any(enemy.xcor() > 215 or enemy.xcor() < -215 for enemy in self.all_enemies):
            self.enemy_speed *= -1  # Reverse direction
            self.move_down()

    def move_down(self):
        """Move all enemies down"""
        for enemy in self.all_enemies:
            new_y = enemy.ycor() - MOVE_INCREMENT
            enemy.sety(new_y)

    def level_up(self):
        self.enemy_speed += MOVE_INCREMENT
        self.level += 1  # Increment the level
        rows = STARTING_ENEMY_AMOUNT_ROW + ENEMY_INCREASE * (self.level - 1)  # Adjust number of rows
        columns = STARTING_ENEMY_AMOUNT_COLUMN + ENEMY_INCREASE * (self.level - 1)  # Adjust number of columns
        self.create_enemies(rows, columns)  # Create new enemies with updated row/column values
