import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self,x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt


    