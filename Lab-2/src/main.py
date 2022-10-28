#!/usr/bin/env python3

import colorama

from game.cell import Cell
from game.cursor import Cursor
from game.field import Field
from game.gamestate import GameState
from game.landscapes.grass import Grass
from game.position import Position
from game.units.base import Base
from game.units.blank import Blank
from game.utils import clear_screen, dimensions

if __name__ == "__main__":
    colorama.init()
    clear_screen()
    print(colorama.Fore.RED + "Welcome to the game!" + colorama.Style.RESET_ALL)
    input("To start the game press any key")
    clear_screen()
    dims: tuple[int, int] = dimensions()
    # width: int = dims[0] // 2
    # height: int = dims[1] // 2
    width: int = 2
    height: int = 2
    init_cells: list[list[Cell]] = []
    for y in range(height):
        for x in range(width):
            if x == 0:
                init_cells.append([])
            init_cells[y].append(Cell(Position(x, y), Blank(), Blank(), Grass()))
    init_cells[0][0] = Cell(Position(0, 0), Blank(), Cursor(), Grass())
    game_state: GameState = GameState(
        Field(width, height, init_cells),
        Base(True, (width + height) // 2, []),
        Position(0, 0),
        False,
    )
    print(f"Please choose your base location on your field {width}x{height}.")

    while not game_state.is_over():
        clear_screen()
        game_state.render()
        game_state = game_state.poll()
        # game_state = game_state.next()

    colorama.deinit()
