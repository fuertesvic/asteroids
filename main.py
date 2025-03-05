import pygame
from asteroidfield import AsteroidField
from asteroid import Asteroid
from constants import * 
from player import Player
from shot import Shot
def main():
    
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Sets up the GUI window
    clock = pygame.time.Clock()                                     # Sets up the clock for the game loop    
    dt = 0                              # This variable will be used to store time between user input

    # Initialization of groups 
    updatable = pygame.sprite.Group()           # All updatable objects
    drawable  = pygame.sprite.Group()           # All drawable objects
    asteroids = pygame.sprite.Group()           # All asteroid objects
    shots     = pygame.sprite.Group()           # All shot objects

    Player.containers        = (updatable, drawable)
    Asteroid.containers      = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable, )
    Shot.containers          = (updatable, drawable, shots)
    
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)     # Create a "player" instance
    asteroid_field = AsteroidField() 

    while True:
        for event in pygame.event.get():    # Make sure the 'x' works to quit the game
            if event.type == pygame.QUIT:
                print("Exiting asteroids")
                return
        
        screen.fill(color='black')
        
        updatable.update(dt)
        
        for object in asteroids:
            if player.is_colliding(object):
                print("GameOver")
                return
        
        
        for object in drawable:
            object.draw(screen)
         
        elapsed = clock.tick(60)             # Pause for 1/60th of a second and get how many time has passed
        dt = elapsed / 1000                   # Convert to seconds
        pygame.display.flip()                 # Refresh the screen

if __name__ == "__main__":
    main()
