# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # GAME LOOP
    while True:
        # Step 1: Check for quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the game loop cleanly
        
        # Step 3: Draw to the screen
        screen.fill("black")  # Fill the screen with black
        pygame.display.flip()  # Refresh the screen

if __name__ == "__main__":
    main()