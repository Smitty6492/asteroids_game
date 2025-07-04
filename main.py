# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Boots Asteroids")
    
    # ✅ Frame rate control setup
    clock = pygame.time.Clock()
    dt = 0  # delta time in seconds
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Create groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    # Attach groups to classes
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables,)  # only updatable
    
    
    # ✅ Create the player in the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # GAME LOOP
    while True:
        # Step 1: Check for quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the game loop cleanly
        
        
        
        #player.update(dt)           # ✅ Add this line
        
        # Draw the 
        updatables.update(dt)
        
        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                #pygame.quit()
                sys.exit()
                #return
        
        screen.fill("black")  # Fill the screen with black
        
        for obj in drawables:
            obj.draw(screen)
        
        
        #player.draw(screen)   # ✅ Draw the player
        pygame.display.flip() # Refresh the screen
        
        # ✅ Cap at 60 FPS and store delta time
        dt = clock.tick(60) / 1000  # dt in seconds

if __name__ == "__main__":
    main()