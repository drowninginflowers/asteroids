import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BACKGROUND_COLOR,
)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    AsteroidField.containers = updatables
    Asteroid.containers = (updatables, drawables, asteroids)
    Player.containers = (updatables, drawables)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatables.update(dt)

        screen.fill(BACKGROUND_COLOR)
        for sprite in drawables:
            sprite.draw(screen)

        pygame.display.flip()

        # limit framerate to 60fps
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
