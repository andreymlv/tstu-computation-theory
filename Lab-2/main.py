#!/usr/bin/env python3

import logging
import math

import colorama

import utils
from cursor import Cursor
from field import Field
from game import Game
from object import Object
from position import Position
from units.unit import Unit

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
    init_landscapes: list[Unit] = []
    init_units: list[Unit] = []
    init_objects: list[Object] = [None, *init_landscapes, *init_units]
    max_weaponed: int = math.floor(width * height * 0.5)
    init_field: Field = Field(width, height, max_weaponed, init_objects)
    game_state: Game = Game(init_field, None, Cursor(Position(0, 0)), False)
    print(init_field.render())
    print(f'Please choose your base location on your field {width}x{height}.')
    logging.info('Game is initialized.')

    while not game_state.is_over():
        utils.clear_screen()
        game_state.render()
        game_state = game_state.next().poll()

    logging.info('Game is over.')
    colorama.deinit()
    logging.info('Colors are disabled.')
