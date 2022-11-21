#!/usr/bin/sudo python3

import random

import colorama

from game.display.cell import Cell
from game.display.field import Field
from game.display.position import Position
from game.display.screen import Screen
from game.landscapes.bush import Bush
from game.landscapes.grass import Grass
from game.landscapes.landscape import Landscape
from game.landscapes.rock import Rock
from game.landscapes.water import Water
from game.state.game import Game
from game.state.gamestate import GameState
from game.units.base import Base
from game.units.blank import Blank
from game.units.cavalry import Cavalry
from game.units.cursor import Cursor
from game.units.melee import Melee
from game.units.range import Range
from game.utils import clear_screen, dimensions, flush_input
from game.weapons.bow import Bow
from game.weapons.sword import Sword


def main() -> None:
    colorama.init()
    clear_screen()
    print(colorama.Fore.RED + "Welcome to the game!" + colorama.Style.RESET_ALL)
    input("To start the game press any key")
    clear_screen()
    width, height = map(lambda d: d // 2, dimensions())
    # width: int = 5
    # height: int = 2
    cells: list[list[Cell]] = []
    landscapes: list[Landscape] = [
        Grass(),
        Bush(),
        Rock(),
        Water(),
    ]
    max_warriors = (width + height) // 2
    for x in range(width):
        for y in range(height):
            if y == 0:
                cells.append([])
            cells[x].append(
                Cell(
                    Position(x, y),
                    Base(False, max_warriors, []),
                    Blank(),
                    Blank(),
                    landscapes[random.randint(0, len(landscapes) - 1)],
                )
            )
    cells[0][0] = Cell(
        Position(0, 0),
        Base(
            True,
            max_warriors,
            [
                Melee(10, 8, 4, Sword(128, 8, 1)),
                Range(10, 8, 4, Bow(128, 8, 1)),
                Cavalry(10, 8, 4, Sword(128, 8, 1)),
            ],
        ),
        Blank(),
        Cursor(),
        cells[0][0].landscape,
    )

    # debug
    cells[3][3] = Cell(
        Position(3, 3),
        Base(
            True,
            max_warriors,
            [],
        ),
        Melee(10, 8, 4, Sword(128, 8, 1)),
        Blank(),
        cells[3][3].landscape,
    )
    cells[5][5] = Cell(
        Position(5, 5),
        Base(
            True,
            max_warriors,
            [],
        ),
        Cavalry(10, 8, 4, Sword(128, 8, 1)),
        Blank(),
        cells[5][5].landscape,
    )

    game: Game = Game(
        GameState(
            Field(Screen(width, height), cells),
            Position(0, 0),
            Position(0, 0),
            False,
        )
    )

    while not game.is_over():
        clear_screen()
        game.print()
        game = game.next()
        # Blocks game loop.
        game = game.poll()

    flush_input()
    colorama.deinit()


if __name__ == "__main__":
    main()
