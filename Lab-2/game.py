import keyboard

import utils
from base import Base
from cursor import Cursor
from field import Field
from position import Position


class Game:

    def __init__(self, field: Field, base: Base, cursor: Cursor, quit_required: bool):
        self.quit_required = quit_required
        self.cursor = cursor
        self.field = field
        self.base = base

    def poll(self):
        cursor = self.cursor
        move = self.cursor.position
        quit_required = self.quit_required
        event = keyboard.read_event(True)
        if event.event_type == keyboard.KEY_DOWN:
            match event.name:
                case 'w':
                    move = Position(self.cursor.position.x, self.cursor.position.y + 1)
                case 'a':
                    move = Position(self.cursor.position.x + 1, self.cursor.position.y)
                case 's':
                    move = Position(self.cursor.position.x, self.cursor.position.y - 1)
                case 'd':
                    move = Position(self.cursor.position.x - 1, self.cursor.position.y)
                case 'q':
                    quit_required = True
                case _:
                    print(event.name)
        utils.flush_input()
        if self.field.is_possible_move(move):
            cursor = Cursor(move)
        return Game(Field(self.field.width, self.field.height, self.field.max_weaponed, [cursor]), self.base, cursor,
                    quit_required)

    def render(self):
        print(self.field.render())

    def is_over(self) -> bool:
        # return self.base.is_crushed() or self.quit_required
        return self.quit_required

    def next(self):
        return Game(self.field, self.base, self.cursor, self.quit_required)
