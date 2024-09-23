from turtle import Turtle, Screen
import time

custom_player_bullet = "images/resized_player_laser.gif"

BULLET_MOVE_DISTANCE = 20
POWERUP_TIME = 8
POWERUP_SPEED = 40


class PlayerBullet:

    def __init__(self, player):
        self.all_bullets = []
        self.bullet_speed = BULLET_MOVE_DISTANCE
        self.player = player
        self.last_shot_time = 0  # Track time of the last shot
        self.shoot_cooldown = 1.25  # Seconds between shots
        self.next_spawn_time = time.time() + POWERUP_TIME

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

    def speed_powerup(self):
        self.bullet_speed = POWERUP_SPEED #Increase bullet speed for powerup

        def reset_speed():
            self.bullet_speed = BULLET_MOVE_DISTANCE  # Reset bullet speed after power-up duration
            
            # Schedule the reset to happen after 8 seconds (8000 ms)
            self.screen.ontimer(reset_speed, POWERUP_TIME * 1000)


 