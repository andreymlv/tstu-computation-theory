#!/usr/bin/env python3
import pygame

from src.disk import Disk
from src.game import Game
from src.gamestate import HelpState, GameState, init
from src.tower import Tower


def main() -> None:
    pygame.init()
    first_tower_disks: list[Disk] = list(map(lambda x: Disk(x), range(3, 0, -1)))
    game: Game = Game(
        state=HelpState(
            towers=[
                Tower(first_tower_disks),
                Tower([]),
                Tower([]),
            ],
            over=False,
            help_text="Welcome to the game!\nIf you are confused with controls always use F1 button.\nUsage:\nF1 - Help Menu\nESC - Go Back\nq - Quit",
            caller=GameState(
                [
                    Tower(first_tower_disks),
                    Tower([]),
                    Tower([]),
                ],
                False,
            ),
        )
    )
    init()
    while not game.state.over:
        print(game.log())
        game.render()
        pygame.display.update()
        pygame.time.Clock().tick(60)
        game = game.poll()
        game = game.next()
    pygame.quit()


if __name__ == "__main__":
    main()
