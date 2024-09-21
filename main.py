from turtle import Screen
from player import Player
from enemy import EnemyManager
from enemy_bullet import EnemyBullet
import time
from player_bullet import PlayerBullet
from score import Scoreboard
from blockade import Blockade

custom_background = "images/background.gif"
class Game:
    def __init__(self):
        # Initialization code
        self.screen = Screen()
        self.screen.setup(width=500, height=600)
        self.screen.bgcolor("black")
        self.screen.tracer(0)
        self.screen.bgpic(custom_background) 

        self.player = Player()
        self.enemy_manager = EnemyManager()
        self.enemy_bullet_manager = EnemyBullet(self.enemy_manager, self.player)
        self.player_bullet_manager = PlayerBullet(self.player)
        self.scoreboard = Scoreboard()

        self.blockades = self.create_blockades()
        self.setup_controls()
        # Update the screen once after everything is initialized
        self.screen.update()

    def create_blockades(self):
        positions = [(-150, -150), (0, -150), (150, -150), (-75, -200), (75, -200)]
        return [Blockade(position) for position in positions]


    def setup_controls(self):
        self.screen.listen()
        self.screen.onkey(self.player.go_left, "Left")
        self.screen.onkey(self.player.go_right, "Right")
        self.screen.onkey(self.player_bullet_manager.create_bullet, "space")

    def check_player_bullet_collisions(self):
        for bullet in self.player_bullet_manager.all_bullets:
            for enemy in self.enemy_manager.all_enemies:
                if bullet.distance(enemy) < 20:
                    enemy.hideturtle()
                    self.enemy_manager.all_enemies.remove(enemy)
                    bullet.hideturtle()
                    self.player_bullet_manager.all_bullets.remove(bullet)
                    self.scoreboard.increase_score()
                    break

            # Check collisions with level 4 enemies
            for enemy in self.enemy_manager.level_4_enemies:
                if bullet.distance(enemy) < 20:
                    enemy.hideturtle()
                    self.enemy_manager.level_4_enemies.remove(enemy)
                    bullet.hideturtle()
                    self.player_bullet_manager.all_bullets.remove(bullet)
                    self.scoreboard.increase_score()
                    break  # Exit inner loop after a hit

    def player_hit(self):
            self.screen.bgcolor("red")  # Change the screen color to red
            self.screen.update()
            time.sleep(0.1)  # Pause for 0.1 seconds to show the red flash
            self.screen.bgcolor("black") 
        


    def check_for_bullet_on_bullet_collision(self):
        for bullet in self.player_bullet_manager.all_bullets:
            for enemy_bullet in self.enemy_bullet_manager.all_bullets:
                if bullet.distance(enemy_bullet) <13:
                    enemy_bullet.hideturtle()
                    bullet.hideturtle()
                    self.player_bullet_manager.all_bullets.remove(bullet)
                    self.enemy_bullet_manager.all_bullets.remove(enemy_bullet)


    def check_enemy_bullet_collisions(self):
        for bullet in self.enemy_bullet_manager.all_bullets:
            if bullet.distance(self.player) < 20:
                self.scoreboard.lose_life()
                self.player_hit()
                self.scoreboard.update_scoreboard()
                bullet.hideturtle()
                self.enemy_bullet_manager.all_bullets.remove(bullet)
                if self.scoreboard.lives == 0:  # Check if lives are 0
                    self.scoreboard.game_over()
                    return True  # Indicate that the game is over

  
    def check_blockade_collisions(self):
        for bullet in self.enemy_bullet_manager.all_bullets:
            for block in self.blockades:
                if bullet.distance(block) < 20:
                    block.hit()
                    bullet.hideturtle()
                    self.enemy_bullet_manager.all_bullets.remove(bullet)
                    
                    if block.durability <= 0:  # Check if the block is destroyed
                        self.blockades.remove(block)
                        block.hideturtle()  # Ensure the block is hidden when removed
                    break


        for player_bullet in self.player_bullet_manager.all_bullets:
            for block in self.blockades:
                if player_bullet.distance(block) < 20:
                    player_bullet.hideturtle()
                    self.player_bullet_manager.all_bullets.remove(player_bullet)
                    break
                
    
    def game_over(self):
        # Display "Game Over"
        self.scoreboard.game_over()
        self.screen.update()  # Ensure the "Game Over" message is shown
        
        # Remove all objects from the screen
        for enemy in self.enemy_manager.all_enemies:
            enemy.hideturtle()
        for bullet in self.enemy_bullet_manager.all_bullets:
            bullet.hideturtle()
        for bullet in self.player_bullet_manager.all_bullets:
            bullet.hideturtle()
        for block in self.blockades:
            block.hideturtle()

        # Display a message asking if the player wants to play again
        self.screen.clear()
        self.screen.bgcolor("black")
        self.scoreboard.play_again()

        # Bind the play again and quit keys
        self.screen.onkey(self.play_again, "p")
        self.screen.onkey(self.quit_game, "q")
        self.screen.listen()

        # Keep the screen open
        self.screen.mainloop()  # Keeps the screen open and responsive


    def quit_game(self):
        self.screen.bye()  # Close the screen gracefully

    def play_again(self):
        self.screen.clear()  # Clear the screen before restarting
        self.__init__()  # Reinitialize the game
        self.main_loop()  # Restart the main game loop

    def clear_bullets(self):
    # Hide and remove all enemy bullets
        for bullet in self.enemy_bullet_manager.all_bullets:
            bullet.hideturtle()
        self.enemy_bullet_manager.all_bullets.clear()

        # Hide and remove all player bullets
        for bullet in self.player_bullet_manager.all_bullets:
            bullet.hideturtle()
        self.player_bullet_manager.all_bullets.clear()


    def main_loop(self):
        game_is_on = True
        while game_is_on:
            self.enemy_manager.move_enemies()
            self.enemy_bullet_manager.spawn_bullets()
            self.player_bullet_manager.move_bullets()
            self.screen.update()

            if not self.enemy_manager.all_enemies:
                self.enemy_manager.level_up()
                self.enemy_bullet_manager.level_up()
                self.clear_bullets()
                self.scoreboard.level_up()
                

            if self.check_enemy_bullet_collisions():  # Check if the game is over
                game_is_on = False
                self.game_over()  # Handle game over logic

            self.check_player_bullet_collisions()
            self.check_blockade_collisions()
            self.check_for_bullet_on_bullet_collision()

            time.sleep(0.1)  # Adjust as necessary for game speed

def main():
    game = Game()
    game.main_loop()

if __name__ == "__main__":
    main()
