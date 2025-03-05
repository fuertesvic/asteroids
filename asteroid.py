import pygame
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, center = self.position, radius = self.radius, width = 2, color='white')

    def update(self,dt):
        self.position += self.velocity * dt