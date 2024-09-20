from turtle import Turtle
import random

BULLET_MOVE_DISTANCE = 15
FIRE_DELAY_LEVELUP = 5 

class EnemyBullet:

    def __init__(self, enemy_manager, player):
        self.all_bullets = []
        self.bullet_speed = BULLET_MOVE_DISTANCE
        self.enemy_manager = enemy_manager
        self.player = player
        self.counter = 0
        self.fire_delay = 30

    def create_bullet(self):
        if self.enemy_manager.all_enemies:  # Ensure there are enemies to choose from
            rnd_enemy = random.choice(self.enemy_manager.all_enemies)
            xcord = rnd_enemy.xcor()
            ycord = rnd_enemy.ycor()
            
            # Create the bullet at the enemy's position
            new_bullet = Turtle("square")
            new_bullet.shapesize(stretch_wid=0.1, stretch_len=1)  # Thin bullet
            new_bullet.penup()
            new_bullet.goto(xcord, ycord)  # Immediately set the bullet's starting position
            new_bullet.color("red")
            
            # Point the bullet towards the player
            player_x = self.player.xcor()
            player_y = self.player.ycor()
            angle_to_player = new_bullet.towards(player_x, player_y)
            new_bullet.seth(angle_to_player)
            
            # Only after positioning and setting the direction, add the bullet to the list
            self.all_bullets.append(new_bullet)
        else:
            print("No enemies available to shoot bullets from.")

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
        def level_up(self):
            self.fire_delay = max(10, self.fire_delay - FIRE_DELAY_LEVELUP)  # Set a minimum fire delay

