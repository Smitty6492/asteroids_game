import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y): 
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown_timer = 0
        for group in self.containers:
            group.add(self)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt 
    
    
    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    
    def shoot(self):
        if self.cooldown_timer > 0:
            return              # Can't shoot yet!
        shot = Shot(self.position.x, self.position.y)
        velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        shot.velocity = velocity
        self.cooldown_timer = PLAYER_SHOOT_COOLDOWN     # Start cooldown
        
    
    def update(self, dt):
        if self.cooldown_timer > 0:
            self.cooldown_timer -= dt 
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)  # Turn left
        if keys[pygame.K_d]:
            self.rotate(dt)   # Turn right
        if keys[pygame.K_w]:  
            self.move(dt)     # Move forward
        if keys[pygame.K_s]:
            self.move(-dt)    # Move backward
        if keys[pygame.K_SPACE]:
            self.shoot()      # Fire bullets
            
        