#!/usr/bin/env python3

import colorama

from game.display.cell import Cell
from game.display.field import Field
from game.display.position import Position
from game.display.screen import Screen
from game.landscapes.grass import Grass
from game.state.gamestate import GameState
from game.units.base import Base
from game.units.blank import Blank
from game.units.cursor import Cursor
from game.utils import clear_screen, dimensions

if __name__ == "__main__":
    colorama.init()
    clear_screen()
    print(colorama.Fore.RED + "Welcome to the game!" + colorama.Style.RESET_ALL)
    input("To start the game press any key")
    clear_screen()
    height, width = map(lambda d: d // 2, dimensions())
    # width: int = 5
    # height: int = 2
    init_cells: list[list[Cell]] = []
    for x in range(width):
        for y in range(height):
            if y == 0:
                init_cells.append([])
            init_cells[x].append(Cell(Position(x, y), Blank(), Blank(), Grass()))
    init_cells[0][0] = Cell(Position(0, 0), Blank(), Cursor(), Grass())
    game_state: GameState = GameState(
        Field(Screen(width, height), init_cells),
        Base(True, (width + height) // 2, []),
        Position(0, 0),
        False,
    )
    print(f"Please choose your base location on your field {width}x{height}.")

    while not game_state.is_over():
        clear_screen()
        game_state.render()
        game_state = game_state.poll()
        game_state = game_state.next()

    colorama.deinit()
