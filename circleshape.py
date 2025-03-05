import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        print("CircleShape Constructor called")
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def is_colliding(self,circle):
        center1 = self.position
        center2 = circle.position
        distance = pygame.math.Vector2.distance_to(center1,center2)

        return  distance < (self.radius + circle.radius)