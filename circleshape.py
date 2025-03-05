import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    print("CircleShape constru called")
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, center = self.position, radius = self.radius, width = 2, color='white')

    def update(self,dt):
        self.position += self.velocity * dt

    def is_colliding(self,circle):
        center1 = self.position
        center2 = circle.position
        distance = pygame.math.Vector2.distance_to(center1,center2)

        return  distance < (self.radius + circle.radius)