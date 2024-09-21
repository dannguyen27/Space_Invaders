from turtle import Turtle, Screen
import random

#Bullet Speed
BULLET_MOVE_DISTANCE = 15

#Bullet Speed Increase Per Level Up
FIRE_DELAY_LEVELUP = 5 

custom_enemy_bullet = "images/resized_enemy_laser.gif"
custom_level4_laser = "images/level4_laser.gif"
custom_level5_laser = "images/level5_laser.gif"

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
        self.screen.register_shape(custom_level5_laser)

    def create_bullet(self):
        if self.enemy_manager.all_enemies and random.random() < 0.9:  # 50% chance for default enemies to shoot
            rnd_enemy = random.choice(self.enemy_manager.all_enemies)
            self._create_bullet_from_enemy(rnd_enemy, custom_enemy_bullet)
        
        if self.enemy_manager.level_4_enemies and random.random() < 0.8:  # 50% chance for level 4 enemies to shoot
            rnd_level_4_enemy = random.choice(self.enemy_manager.level_4_enemies)
            self._create_bullet_from_enemy(rnd_level_4_enemy, custom_level4_laser)
        
        if self.enemy_manager.level_5_enemies and random.random() < 0.7:  # 50% chance for level 5 enemies to shoot
            rnd_level_5_enemy = random.choice(self.enemy_manager.level_5_enemies)
            self._create_bullet_from_enemy(rnd_level_5_enemy, custom_level5_laser)


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
