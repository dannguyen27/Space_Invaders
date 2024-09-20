# TODO: Define bullet
# TODO: Firing Mechanism
# TODO: Bullet Movement
# TODO: Collision Detection
# TODO: Managing Multiple Bullets


from turtle import Turtle
import random
from player import Player
import time

BULLET_MOVE_DISTANCE= 15



class PlayerBullet:

    def __init__(self, player):
        self.all_bullets = []
        self.bullet_speed = BULLET_MOVE_DISTANCE
        self.player = player
        self.last_shot_time = 0  # Track time of the last shot
        self.shoot_cooldown = 1.25  #seconds between shots

    def create_bullet(self):
        """Create a bullet at the player's position if cooldown allows"""
        current_time = time.time()
        if current_time - self.last_shot_time > self.shoot_cooldown:
            xcord = self.player.xcor()
            ycord = self.player.ycor()
            new_bullet = Turtle("square")
            new_bullet.shapesize(stretch_wid=0.1, stretch_len=1)  # Thin bullet
            new_bullet.penup()
            new_bullet.color("green")
            new_bullet.seth(90)  # Point the bullet upwards
            new_bullet.goto(xcord, ycord)
            self.all_bullets.append(new_bullet)
            self.last_shot_time = current_time  # Update last shot time

    def move_bullets(self):
        """Move all bullets upwards"""
        for bullet in self.all_bullets:
            bullet.sety(bullet.ycor() + self.bullet_speed)

           


        