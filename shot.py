# shot.py
import pygame
from circleshape import CircleShape
from constants import *


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        for group in self.containers:
            group.add(self)
    
    
    def draw(self, screen):
        pygame.draw.circle(screen,"blue", self.position, self.radius, 2)
       
        
    def update(self, dt):
        self.position += self.velocity * dt
        