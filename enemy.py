from turtle import Turtle, Screen

# Initial speed of enemy movement; higher values make enemies move faster.
STARTING_MOVE_DISTANCE = 4

# Amount by which the enemy speed increases with each level-up.
MOVE_INCREMENT = 2

# Initial number of rows of enemies.
STARTING_ENEMY_AMOUNT_ROW = 1

# Initial number of columns of enemies.
STARTING_ENEMY_AMOUNT_COLUMN = 1

# Number of rows and columns to add to the enemy grid with each level-up.
ENEMY_INCREASE = 1

# Attributes for Level 4 special enemies
LEVEL_4_ENEMY_GIF = "images/level4_ship.gif"
LEVEL_4_ENEMY_SPEED = 6
LEVEL_4_SPACING_X = 125
LEVEL_4_SPACING_Y = 50

custom_enemy_gif = "images/resized_enemy_ship.gif"

class EnemyManager:
    def __init__(self):
        self.screen = Screen()
        self.screen.addshape(custom_enemy_gif)  # Register the custom enemy shape
        self.screen.addshape(LEVEL_4_ENEMY_GIF)  # Register the level 4 enemy shape

        self.all_enemies = []
        self.level_4_enemies = []  # List to hold level 4 specific enemies
        self.enemy_speed = STARTING_MOVE_DISTANCE
        self.level_4_enemy_speed = LEVEL_4_ENEMY_SPEED  # Separate speed for level 4 enemies
        self.level = 1  # Initialize level
        self.create_enemies(STARTING_ENEMY_AMOUNT_ROW, STARTING_ENEMY_AMOUNT_COLUMN)

    def create_enemies(self, rows, columns):
        # Clear existing enemies
        for enemy in self.all_enemies + self.level_4_enemies:
            enemy.hideturtle()
        self.all_enemies.clear()
        self.level_4_enemies.clear()
        
        """Create a grid of default enemies"""
        start_x = -150  
        start_y = 150  # Lower starting Y-coordinate for default enemies
        spacing_x = 50
        spacing_y = 40

        for row in range(rows):  
            for col in range(columns):  
                new_enemy = Turtle()
                new_enemy.shape(custom_enemy_gif)  # Use the default enemy ship shape
                new_enemy.penup()
                new_enemy.goto(start_x + col * spacing_x, start_y - row * spacing_y)
                self.all_enemies.append(new_enemy)

        if self.level == 4:
            # Create level 4 specific enemies behind the default enemies
            level_4_start_x = -150  
            level_4_start_y = start_y + 100
            for row in range(1):  # You can adjust the number of rows/columns
                for col in range(3):  
                    new_level_4_enemy = Turtle()
                    new_level_4_enemy.shape(LEVEL_4_ENEMY_GIF)  # Use the level 4 enemy ship shape
                    new_level_4_enemy.penup()
                    new_level_4_enemy.goto(level_4_start_x + col * LEVEL_4_SPACING_X, 
                                        level_4_start_y - row * LEVEL_4_SPACING_Y)
                    self.level_4_enemies.append(new_level_4_enemy)

    def move_enemies(self):
        """Move default enemies left to right and down"""
        for enemy in self.all_enemies:
            new_x = enemy.xcor() + self.enemy_speed
            enemy.setx(new_x)

        """Move level 4 specific enemies left to right and down"""
        for enemy in self.level_4_enemies:
            new_x = enemy.xcor() + self.level_4_enemy_speed
            enemy.setx(new_x)

        # Check if any enemy has reached the edge of the screen and reverse direction
        if any(enemy.xcor() > 215 or enemy.xcor() < -215 for enemy in self.all_enemies + self.level_4_enemies):
            self.enemy_speed *= -1  # Reverse direction for default enemies
            self.level_4_enemy_speed *= -1  # Reverse direction for level 4 enemies
            self.move_down()

    def move_down(self):
        """Move all enemies down"""
        for enemy in self.all_enemies:
            new_y = enemy.ycor() - MOVE_INCREMENT
            enemy.sety(new_y)
        
        for enemy in self.level_4_enemies:
            new_y = enemy.ycor() - MOVE_INCREMENT
            enemy.sety(new_y)

    def level_up(self):
        """Increase the difficulty by speeding up enemies and adding more rows/columns"""
        self.enemy_speed += MOVE_INCREMENT  # Increase speed for default enemies
        self.level_4_enemy_speed += MOVE_INCREMENT  # Increase speed for level 4 enemies
        self.level += 1  # Increment the level

        rows = STARTING_ENEMY_AMOUNT_ROW + ENEMY_INCREASE * (self.level - 1)  # Adjust number of rows
        columns = STARTING_ENEMY_AMOUNT_COLUMN + ENEMY_INCREASE * (self.level - 1)  # Adjust number of columns
        self.create_enemies(rows, columns)  # Create new enemies with updated row/column values
