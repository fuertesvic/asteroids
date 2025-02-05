import pygame
from constants import * 


def main():

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Sets up the GUI window
    
    while True:
        for event in pygame.event.get():    # Make sure the 'x' works to quit the game
            if event.type == pygame.QUIT:
                return
        
        screen.fill(color='black')
        pygame.display.flip()       # Refresh the screen

if __name__ == "__main__":
    main()
