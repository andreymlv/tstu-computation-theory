#!/usr/bin/env python3
import pygame

from src.disk import Disk
from src.game import Game, init
from src.hanoi import hanoi_recursive
from src.tower import Tower


def main() -> None:
    pygame.init()
    first_tower_disks: list[Disk] = list(map(lambda x: Disk(x), range(3, 0, -1)))
    game: Game = Game(
        [
            Tower(first_tower_disks),
            Tower([]),
            Tower([]),
        ]
    )
    init()
    # while not game.over:
    #     game = game.poll()
    #     game.render()
    print(game.hanoi(hanoi_recursive)[-1])
    pygame.quit()


if __name__ == "__main__":
    main()
