import pygame
from constants import * 
from player import *

def main():
    
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Sets up the GUI window
    clock = pygame.time.Clock()                                     # Sets up the clock for the game loop    
    dt = 0                              # This variable will be used to store time between user input

    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)     # Create a "player" instance


    while True:
        for event in pygame.event.get():    # Make sure the 'x' works to quit the game
            if event.type == pygame.QUIT:
                print("Exiting asteroids")
                return
        
        screen.fill(color='black')
        player.draw(screen)
        player.update(dt)
         
        elapsed = clock.tick(60)             # Pause for 1/60th of a second and get how many time has passed
        dt = elapsed / 1000                   # Convert to seconds
        pygame.display.flip()                 # Refresh the screen

if __name__ == "__main__":
    main()
