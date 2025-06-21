# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import Player
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player_1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               return

       updatable.update(dt) 
       screen.fill("black")
       
       for item in drawable:
           item.draw(screen)

       pygame.display.flip()
       
       dt = clock.tick(60) / 1000

# ensures main() function is only called when file run directly
# won't run if it's imported as a module
if __name__ == "__main__":
    main()