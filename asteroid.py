import pygame
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        
    def draw(self, screen):
        print(f"Draw from Asteroid called, object has self.position: {self.position} and self.radius {self.radius}")
        pygame.draw.circle(screen, center = self.position, radius = self.radius, width = 2, color='white')

    def update(self,dt):
        self.position += self.velocity * dt