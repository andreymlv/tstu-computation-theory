#!/usr/bin/env python3
import pygame

from src.disk import Disk
from src.game import Game
from src.gamestate import GameState, init
from src.tower import Tower


def main() -> None:
    pygame.init()
    first_tower_disks: list[Disk] = list(map(lambda x: Disk(x), range(5, 0, -1)))
    game: Game = Game(
        state=GameState(
            towers=[
                Tower(first_tower_disks),
                Tower([]),
                Tower([]),
            ],
            over=False,
        )
    )
    init()
    while not game.state.over:
        game.render()
        game = game.poll()
        game = game.next()
    pygame.quit()


if __name__ == "__main__":
    main()
