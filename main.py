import pygame
import constants
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state



def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # Screen width: 1280
    # Screen height: 720
    while True:
        log_state()
        # check for closing the window...
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        # refresh the screen
        pygame.display.flip()


if __name__ == "__main__":
    main()
