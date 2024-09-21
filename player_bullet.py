from turtle import Turtle, Screen
import time

custom_player_bullet = "images/resized_player_laser.gif"

BULLET_MOVE_DISTANCE = 20

class PlayerBullet:

    def __init__(self, player):
        self.all_bullets = []
        self.bullet_speed = BULLET_MOVE_DISTANCE
        self.player = player
        self.last_shot_time = 0  # Track time of the last shot
        self.shoot_cooldown = 1.25  # Seconds between shots

        # Register the custom bullet shape
        self.screen = Screen()
        self.screen.register_shape(custom_player_bullet)

    def create_bullet(self):
        """Create a bullet at the player's position if cooldown allows"""
        current_time = time.time()
        if current_time - self.last_shot_time > self.shoot_cooldown:
            xcord = self.player.xcor()
            ycord = self.player.ycor()
            new_bullet = Turtle(custom_player_bullet)  # Use the custom shape
            new_bullet.penup()
            new_bullet.goto(xcord, ycord)
            self.all_bullets.append(new_bullet)
            self.last_shot_time = current_time  # Update last shot time

    def move_bullets(self):
        """Move all bullets upwards"""
        for bullet in self.all_bullets:
            bullet.sety(bullet.ycor() + self.bullet_speed)
