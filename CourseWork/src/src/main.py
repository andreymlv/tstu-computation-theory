#!/usr/bin/env python3
import pygame

from game import Game
from disk import Disk
from tower import Tower


def main() -> None:
    pygame.init()
    game: Game = Game(
        [Tower([Disk(1), Disk(2), Disk(3)]), Tower([]), Tower([])],
        pygame.time.Clock(),
        pygame.display.set_mode((300, 300)),
        False,
    )
    game.init()
    while not game.over:
        game = game.poll()
        game.render()
    pygame.quit()


if __name__ == "__main__":
    main()
