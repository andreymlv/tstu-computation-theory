#!/usr/bin/env python3

"""This is a console game.
"""

import logging
import math

import colorama

import utils
from field import Field
from position import Position
from units.squad.range import Range
from weapon.range.bow import Bow

if __name__ == '__main__':
    logging.basicConfig(filename='debug.log', filemode='w', format='%(asctime)s %(message)s',
                        encoding='utf-8', level=logging.DEBUG)
    logging.info('Logging is enabled.')
    colorama.init()
    logging.info('Colors are enabled.')
    print(colorama.Fore.RED + 'Welcome to the game!' + colorama.Style.RESET_ALL)
    input('To start the game press any key')
    utils.clear_screen()
    dims = utils.dimensions()
    width: int = dims[0] - 8
    height: int = dims[1] - 8

    # init_landscape: list[Unit] = []
    # init_neutrals: list[Unit] = []
    # init_units: list[Unit] = [init_base, init_landscape, init_neutrals]
    max_weaponed: int = math.floor(width * height * 0.5)
    init_field: Field = Field(width, height, max_weaponed, [Range(Position(5, 5), Bow())])
    # game_state: Game = Game(init_field, init_units)
    print(init_field.render())
    print(f'Please choose your base location on your field {width}x{height}.')
    logging.info('Game is initialized.')

    # while not game_state.is_over():
    #     utils.clear_screen()
    #     game_state.render()
    #     utils.poll()
    #     game_state = Game()

    logging.info('Game is over.')
