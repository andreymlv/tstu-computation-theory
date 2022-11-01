#!/usr/bin/env python3

import math
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
from game.state.gamestate import GameState
from game.units.base import Base
from game.units.blank import Blank
from game.units.cursor import Cursor
from game.units.melee import Melee
from game.utils import clear_screen, dimensions
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
    init_cells: list[list[Cell]] = []
    random_landscapes: list[Landscape] = [
        Grass(),
        Bush(),
        Rock(),
        Water(),
    ]
    random.shuffle(random_landscapes)
    for x in range(width):
        for y in range(height):
            if y == 0:
                init_cells.append([])
            init_cells[x].append(
                Cell(
                    Position(x, y),
                    Blank(),
                    Blank(),
                    random_landscapes[random.randint(0, len(random_landscapes) - 1)],
                )
            )
    init_cells[0][0] = Cell(Position(0, 0), Blank(), Cursor(), Grass())
    game_state: GameState = GameState(
        Field(Screen(width, height), init_cells),
        Base(True, (width + height) // 2, [Melee(10, 8, 4, Sword(128, 8, 1))]),
        Position(0, 0),
        False,
    )
    print(f"Please choose your base location on your field {width}x{height}.")

    while not game_state.is_over():
        clear_screen()
        game_state.print()
        game_state = game_state.poll()
        game_state = game_state.next()

    colorama.deinit()


if __name__ == "__main__":
    main()
