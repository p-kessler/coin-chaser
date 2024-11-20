import pygame
from random import randint


class CoinChaser:
    def __init__(self):
        pygame.init()

        # set size of pygame window
        window_height = 480
        window_width = 640
        self.window = pygame.display.set_mode((window_width, window_height))

        # load in the images used in the game
        self.robot = pygame.image.load("images/robot.png")
        self.coin = pygame.image.load("images/coin.png")
        self.monster = pygame.image.load("images/monster.png")

        # set initial robot character coordinates
        self.robot_x = 100
        self.robot_y = 100

        # set initial coin (random) coin coordinates
        self.coin_x = randint(0, 580)
        self.coin_y = randint(0, 420)

        self.monster_x = 600
        self.monster_y = 400

        # set number of lives and points at start of game 
        self.lives = 3
        self.points = 0

        pygame.display.set_caption("Coin Chaser")

        # set font
        # set messages that will be displayed if certain events happen

        self.game_font = pygame.font.SysFont("Arial", 20)
        self.exit_game = self.game_font.render(f"esc = exit game", True, (0, 0, 0))
        self.rules = self.game_font.render(f"Collect 10 coins to win!", True, (0, 0, 0))
        self.arrows = self.game_font.render(f"Use the arrows to move", True, (0, 0, 0))
        self.game_over = self.game_font.render(f"Game over, better luck next time :(", True, (0, 0, 0))
        self.victory = self.game_font.render(f"You won the game! Congratulations!", True, (0, 0, 0))


        self.clock = pygame.time.Clock()

        self.main_loop()


    def main_loop(self):
        # loops through all methods to move characters/increase score and lives
        while True:
            self.check_events()
            self.update_movement()
            self.draw_window()
            self.monster_follow()
            self.move_coin()
            self.does_monster_touch()
            self.current_lives()
            self.total_points()

            self.clock.tick(60)

    def check_events(self):
        # Handle events like quitting or pressing escape
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()


    def update_movement(self):
        # control the movement of the robot
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.move_robot(0, -5)
        if keys[pygame.K_RIGHT]:
            self.move_robot(0, 5)
        if keys[pygame.K_UP]:
            self.move_robot(-5, 0)
        if keys[pygame.K_DOWN]:
            self.move_robot(5, 0)
    
    # Show current lives and points
    def current_lives(self):
        return self.game_font.render(f"Lives: {self.lives}", True, (0, 0, 0))

    def total_points(self):
        return self.game_font.render(f"Points: {self.points}", True, (0, 0, 0))
    

            
            
    # move robot and make sure it stays within bouds of scren
    def move_robot(self, move_y: int, move_x: int):

        self.robot_x += move_x
        self.robot_y += move_y
        
        if self.robot_x <= 0:
            self.robot_x = 0
        if self.robot_x + self.robot.get_width() >= 640:
            self.robot_x = 640 - self.robot.get_width()
        
        if self.robot_y <= 0:
            self.robot_y = 0
        if self.robot_y >= 480 - self.robot.get_height():
            self.robot_y = 480 - self.robot.get_height()

    # makes the monster follow the robot at a specified speed
    def monster_follow(self):

        if self.points == 10:
            self.monster_x = 700
            self.monster_y = 700
        else:
            if self.robot_x > self.monster_x:
                self.monster_x += 1.5
            if self.robot_x < self.monster_x:
                self.monster_x -= 1.5
            if self.robot_y > self.monster_y:
                self.monster_y += 1.5
            if self.robot_y < self.monster_y:
                self.monster_y -= 1.5

    # check if the monster is touching the robot
    def does_monster_touch(self):
        if (
            self.robot_x + self.robot.get_width() >= self.monster_x and
            self.robot_x <= self.monster_x + self.monster.get_width() and
            self.robot_y + self.robot.get_height() >= self.monster_y and
            self.robot_y <= self.monster_y + self.monster.get_height()
        ):
            self.robot_x = 0
            self.robot_y = 0
            self.monster_x = 600
            self.monster_y = 420
            self.lives -= 1
        
    # if robot touches coin, increase points and then change coordinates
    def move_coin(self):
        if (
            self.robot_x + self.robot.get_width() >+ self.coin_x and
            self.robot_x <= self.coin_x + self.coin.get_width() and
            self.robot_y + self.robot.get_height() >= self.coin_y and
            self.robot_y <= self.coin_y + self.coin.get_height()
        ):
            self.points += 1
            self.coin_x = randint(0, 590)
            self.coin_y = randint(0, 420)


    def draw_window(self):

        if self.lives == 0:
            self.window.fill((255, 255, 255))
            self.window.blit(self.game_over, (165, 200))

        elif self.points == 10:
            self.window.fill((255, 255, 255))
            self.window.blit(self.victory, (165, 200))
        else:
            self.window.fill((100, 255, 255))
            self.window.blit(self.robot, (self.robot_x, self.robot_y))
            self.window.blit(self.coin, (self.coin_x, self.coin_y))
            self.window.blit(self.monster, (self.monster_x, self.monster_y))
            self.window.blit(self.current_lives(), (10, 0))
            self.window.blit(self.total_points(), (500, 0))
            self.window.blit(self.exit_game, (400, 450))
            self.window.blit(self.rules, (200, 0))
            self.window.blit(self.arrows, (25, 450))

        pygame.display.flip()

if __name__ == "__main__":
    CoinChaser()



