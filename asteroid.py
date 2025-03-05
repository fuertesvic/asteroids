import pygame
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
    def split(self):
        self.kill()