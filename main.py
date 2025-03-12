import pygame #bring in pygame library 
from constants import * # from constants.py import everything


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH} Screen height: {SCREEN_HEIGHT}")
    pygame.init() #Initialize pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        pygame.display.flip()
        













if __name__ == "__main__":
    main()
