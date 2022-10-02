#!/usr/bin/env python3

"""This is a console game.
"""

import logging
import math

import termcolor

import utils
from field import Field
from position import Position
from units.squad.melee import Melee
from weapon.melee.sword import Sword

if __name__ == '__main__':
    logging.basicConfig(filename='debug.log', filemode='w', format='%(asctime)s %(message)s',
                        encoding='utf-8', level=logging.DEBUG)
    termcolor.cprint('Welcome to the game!', "red")
    print('Please configure size of your field:')
    dims = utils.dimensions()
    width: int = abs(min(int(input('\tWidth  (e.g. 20 or 30) = ')), dims[0]))
    height: int = abs(min(int(input('\tHeight (e.g. 20 or 30) = ')), dims[1]))
    print(f'Please choose your base location on your field {width}x{height}:')

    # init_base = BaseFactory()
    # init_landscape: list[Unit] = []
    # init_neutrals: list[Unit] = []
    # init_units: list[Unit] = [init_base, init_landscape, init_neutrals]
    max_weaponed: int = math.floor(width * height * 0.5)
    init_field: Field = Field(width, height, max_weaponed, [Melee(Position(0, 0), Sword())])
    # game_state: Game = Game(init_field, init_units)
    init_field.render()
    logging.info('Game is initialized.')

    # while not game_state.is_over():
    #     utils.clear_screen()
    #     game_state.render()
    #     utils.poll()
    #     game_state = Game()

    logging.info('Game is over.')
