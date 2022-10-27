#!/usr/bin/env python3

import logging

import colorama

from cell import Cell
from cursor import Cursor
from field import Field
from game import Game
from landscapes.grass import Grass
from position import Position
from units.blankunit import BlankUnit
from utils import clear_screen, dimensions

if __name__ == "__main__":
    logging.basicConfig(
        filename="debug.log",
        filemode="w",
        format="%(asctime)s %(message)s",
        encoding="utf-8",
        level=logging.DEBUG,
    )
    logging.info("Logging is enabled.")
    colorama.init()
    logging.info("Colors are enabled.")
    clear_screen()
    print(colorama.Fore.RED + "Welcome to the game!" + colorama.Style.RESET_ALL)
    input("To start the game press any key")
    clear_screen()
    dims: tuple[int, int] = dimensions()
    # width: int = dims[0] // 2
    # height: int = dims[1] // 2
    width: int = 5
    height: int = 3
    init_cells: list[list[Cell]] = [[]] * width
    for x in range(width):
        for y in range(height):
            init_cells[x].append(
                Cell(Position(x, y), BlankUnit(), BlankUnit(), Grass())
            )
    init_cells[0][0] = Cell(Position(0, 0), BlankUnit(), Cursor(), Grass())
    print(init_cells)
    init_field: Field = Field(width, height, init_cells)
    game_state: Game = Game(init_field, None, Position(0, 0), False)
    print(f"Please choose your base location on your field {width}x{height}.")
    logging.info("Game is initialized.")

    while not game_state.is_over():
        clear_screen()
        game_state.render()
        game_state = game_state.poll()

    logging.info("Game is over.")
    colorama.deinit()
    logging.info("Colors are disabled.")
