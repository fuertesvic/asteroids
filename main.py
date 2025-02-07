import pygame
from constants import * 


def main():

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Sets up the GUI window
    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():    # Make sure the 'x' works to quit the game
            if event.type == pygame.QUIT:
                return
        
        screen.fill(color='black')
        pygame.display.flip()                 # Refresh the screen 
        clock.tick(60)             # Pause for 1/60th of a second and get how many time has passed
        #dt = elapsed / 1000                   # Convert to seconds

if __name__ == "__main__":
    main()
