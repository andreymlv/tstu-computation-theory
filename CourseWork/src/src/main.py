#!/usr/bin/env python3
import pygame

from src.disk import Disk
from src.game import Game, init
from src.tower import Tower


def main() -> None:
    pygame.init()
    game: Game = Game([Tower([Disk(1), Disk(2), Disk(3)]), Tower([]), Tower([])])
    init()
    while not game.over:
        game = game.poll()
        game.render()
    pygame.quit()


if __name__ == "__main__":
    main()
