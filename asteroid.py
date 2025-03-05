import pygame
import random
from circleshape import *
from constants import *
class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
    
    def split(self):
        # If the asteroid is too small, just kill it
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        
        # Otherwise, kill it and split it
        self.kill()
        angle = random.uniform(20,50)
        velocity1 = self.velocity.rotate( angle) # Set the velocities for the new asteroids, will be similar to parent asteroid.
        velocity2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS  # Bigger asteroids split into two medium asteroids, medium into two small...etc
        
        # Create two new asteroids with the updated radius and velocities
        new_asteroid_one = Asteroid (self.position.x, self.position.y, new_radius)
        new_asteroid_two = Asteroid (self.position.x, self.position.y, new_radius)
        new_asteroid_one.velocity = velocity1 * 1.2
        new_asteroid_two.velocity = velocity2 * 1.2
        
