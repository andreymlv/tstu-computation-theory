#!/usr/bin/env python3
import pygame

from src.disk import Disk
from src.game import Game, init
from src.hanoi import hanoi_recursive
from src.tower import Tower


def main() -> None:
    pygame.init()
    game: Game = Game(
        [Tower([]).push(Disk(3)).push(Disk(2)).push(Disk(1)), Tower([]), Tower([])]
    )
    init()
    # while not game.over:
    #     game = game.poll()
    #     game.render()
    print(game.hanoi(hanoi_recursive))
    pygame.quit()


if __name__ == "__main__":
    main()
