import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def split(self):
        from pygame.sprite import Group
        self.kill() # Always remove the original asteroid
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return      # Don't split small asteroids
        
        # Calculate new smaller radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        # Generate a random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)
        
        # Two new velocity directions, rotated from the original
        new_velocity_1 = self.velocity.rotate(random_angle) * 1.2
        new_velocity_2 = self.velocity.rotate(-random_angle) * 1.2

        # Spawn two new asteroids at the same position
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = new_velocity_1

        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2.velocity = new_velocity_2
    
        if len(Asteroid.containers[0]) >= MAX_ASTEROIDS:
            return          # Skip splitting if too many asteriods
        
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    