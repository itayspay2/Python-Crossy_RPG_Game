# Pygame development 


# Gain access to the pygame library
import pygame
import os
import sys





SCREEN_TITLE = 'Crossy RPG'
# Size of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800



# Color according to RGB codes
WHITE_COLOR = (255,255,255)
BLACK_COLOR = (0,0,0)

# Clock used to update game events and frames
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('comicsans',75)


class Game:
    
    # Typical rate of 60, equilvalent to FPS
    TICK_RATE = 60


    # Initializer for the game class to set up the width, height, and title.
    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        # Create the window of specified size in white to display the game
        self.game_screen = pygame.display.set_mode((width, height))
        # Set the game window color to white
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)


    def run_game_loop(self, level_speed):
        is_game_over = False
        direction = 0
        did_win = False
        
        


        player_character = PlayerCharacter('player.png', 375, 700, 50, 50)
        
        enemy_0 = NonPlayerCharacter('enemy.png', 20, 600, 50, 50)
        enemy_0.SPEED *= level_speed
        
        enemy_1 = NonPlayerCharacter('enemy.png', self.width - 40, 400, 50, 50)
        enemy_1.SPEED *= level_speed
        
        enemy_2 = NonPlayerCharacter('enemy.png', 20, 200, 50, 50)
        enemy_2.SPEED *= level_speed
        
        treasure = GameObject('treasure.png', 375, 50, 50,50)
        gameBackground = GameObject('background.png', 0, 0, 800,800)
        
        # Main game loop, used to update all gameplay such as movement, checks, and graphics
        # Runs until is_game_over = True
        while not is_game_over:
           

            # A loop to get all of the events occuring at any given time
            # Events are most often mouse movement, mouse and button clicks, or exit events
            for event in pygame.event.get():
                # If we have a quit type event (exit out)then exit out of the game loop
                if event.type == pygame.QUIT:
                    quit()
                    
                # Detect when key is pressed down
                elif event.type == pygame.KEYDOWN:
                    # Move up if up key is pressed
                    if event.key == pygame.K_UP:
                        direction = 1
                    # Move down if down key is pressed
                    elif event.key == pygame.K_DOWN:
                        direction = -1

                # Detect when key is released    
                elif event.type == pygame.KEYUP:
                    # Stop movement when key no longer pressed
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0
                        direction2 = 0


                print(event)
            

            # Redraw the screen to be a blank white window
            self.game_screen.fill(WHITE_COLOR)
            gameBackground.draw(self.game_screen)

            treasure.draw(self.game_screen)
            
            # Update the player position
            player_character.move(direction, self.height)
            # Draw the player at the new position
            player_character.draw(self.game_screen)

            # Move and draw the enemy character
            enemy_0.move(self.width)
            enemy_0.draw(self.game_screen)

            if level_speed > 2:
                # Move and draw the enemy character
                enemy_1.move(self.width)
                enemy_1.draw(self.game_screen)

            if level_speed > 4:
                # Move and draw the enemy character
                enemy_2.move(self.width)
                enemy_2.draw(self.game_screen)
                

            if player_character.detect_collision(enemy_0):
                is_game_over = True
                did_win = False
                text = font.render('You Lose',True, BLACK_COLOR)
                self.game_screen.blit(text,(300,350))
                pygame.display.update()
                clock.tick(1)
                break

            if player_character.detect_collision(enemy_1):
                is_game_over = True
                did_win = False
                text = font.render('You Lose',True, BLACK_COLOR)
                self.game_screen.blit(text,(300,350))
                pygame.display.update()
                clock.tick(1)
                break

            if player_character.detect_collision(enemy_2):
                is_game_over = True
                did_win = False
                text = font.render('You Lose',True, BLACK_COLOR)
                self.game_screen.blit(text,(300,350))
                pygame.display.update()
                clock.tick(1)
                break
                
            if player_character.detect_collision(treasure):
                is_game_over = True
                did_win = True
                text = font.render('You Win',True, BLACK_COLOR)
                self.game_screen.blit(text,(300,350))
                pygame.display.update()
                clock.tick(1)
                break


            # Update all game graphics
            pygame.display.update()
            # Tick the clock to update everything within the game
            clock.tick(self.TICK_RATE)

        if did_win:
            self.run_game_loop(level_speed + 1)
        elif is_game_over == True:
            self.run_game_loop(level_speed - 1)
            
            
            
                
        
            



class GameObject:

    def __init__(self, image_path, x, y, width, height):
        # Load the player image from the file directory
        object_image = pygame.image.load(image_path)
        # Rescale the player image
        self.image = pygame.transform.scale(object_image, (width,height))

        self.x_pos = x
        self.y_pos = y

        self.width = width
        self.height = height

    # Draw the object by blitting it ont the background (game screen)
    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))

# Class to represent the character controlled by the player
class PlayerCharacter(GameObject):

    # How many tiles thecharacter moves per second
    SPEED = 10

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    # Move function will move character up if direction > 0 and down if < 0
    def move(self, direction,max_height):
        if direction > 0:
            self.y_pos -= self.SPEED
        elif direction < 0:
            self.y_pos += self.SPEED


        # Make sure the character never goes past the bottom of the screen  
        if self.y_pos >= max_height - 40:
            self.y_pos = max_height - 40


    def detect_collision(self, other_body):
        if self.y_pos > other_body.y_pos + other_body.height:
            return False
        elif self.y_pos + self.height < other_body.y_pos:
            return False
        if self.x_pos > other_body.x_pos + other_body.width:
            return False
        elif self.x_pos + self.width < other_body.x_pos:
            return False
    
        return True
        
            
        



# Class to represent the character controlled by the player
class NonPlayerCharacter(GameObject):

    # How many tiles thecharacter moves per second
    SPEED = 10

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    # Move function will move character up if direction > 0 and down if < 0
    def move(self, max_width):
        if self.x_pos <= 20:
            self.SPEED = abs(self.SPEED)
        elif self.x_pos >= max_width - 40:
            self.SPEED = -abs(self.SPEED)
        self.x_pos += self.SPEED

        
        

        

pygame.init()

new_game = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop(1)

    





# Quit pygame and the program
pygame.quit()
quit()
