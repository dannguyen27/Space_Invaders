from turtle import Turtle, Screen
import random

BULLET_MOVE_DISTANCE = 15
FIRE_DELAY_LEVELUP = 5 

custom_enemy_bullet = "images/resized_enemy_laser.gif"
custom_level4_laser = "images/level4_laser.gif"

class EnemyBullet:

    def __init__(self, enemy_manager, player):
        self.all_bullets = []
        self.bullet_speed = BULLET_MOVE_DISTANCE
        self.enemy_manager = enemy_manager
        self.player = player
        self.counter = 0
        self.fire_delay = 30

        # Register the custom bullet shapes
        self.screen = Screen()
        self.screen.register_shape(custom_enemy_bullet)
        self.screen.register_shape(custom_level4_laser)

    def create_bullet(self):
        if self.enemy_manager.all_enemies:  # Ensure there are enemies to choose from
            rnd_enemy = random.choice(self.enemy_manager.all_enemies)
            self._create_bullet_from_enemy(rnd_enemy, custom_enemy_bullet)
        if self.enemy_manager.level_4_enemies:  # Ensure there are level 4 enemies to choose from
            rnd_level_4_enemy = random.choice(self.enemy_manager.level_4_enemies)
            self._create_bullet_from_enemy(rnd_level_4_enemy, custom_level4_laser)

    def _create_bullet_from_enemy(self, enemy, bullet_shape):
        xcord = enemy.xcor()
        ycord = enemy.ycor()
        
        # Create the bullet at the enemy's position
        new_bullet = Turtle(bullet_shape)
        new_bullet.penup()
        new_bullet.goto(xcord, ycord)  # Immediately set the bullet's starting position
        
        # Point the bullet towards the player
        player_x = self.player.xcor()
        player_y = self.player.ycor()
        angle_to_player = new_bullet.towards(player_x, player_y)
        new_bullet.seth(angle_to_player)
        
        # Only after positioning and setting the direction, add the bullet to the list
        self.all_bullets.append(new_bullet)

    def move_bullets(self):
        for bullet in self.all_bullets:
            bullet.forward(self.bullet_speed)  # Move bullet in the direction it was pointed

    def spawn_bullets(self):
        if self.counter >= self.fire_delay:
            self.create_bullet()
            self.counter = 0
        else:
            self.counter += 1
        self.move_bullets()

    def level_up(self):
        self.fire_delay = max(10, self.fire_delay - FIRE_DELAY_LEVELUP)  # Set a minimum fire delay
