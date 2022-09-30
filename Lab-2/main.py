#!/usr/bin/env python3

import logging
from base import Base
from field import Field
from game import Game
from object import Object
from unit import Unit


if __name__ == '__main__':
    logging.basicConfig(filename='debug.log', filemode='w', format='%(asctime)s %(message)s',
                        encoding='utf-8', level=logging.DEBUG)

    init_base = Base()
    init_landscape: list[Unit] = []
    init_neutrals: list[Unit] = []
    init_objects: list[Object] = [init_base, init_landscape, init_neutrals]
    init_field: Field = Field(20, 20, 20, init_objects)
    game_state: Game = Game()

    logging.info('Game is initialized.')

    while not game_state.is_over():
        game_state = Game()

    logging.info('Game is over.')
