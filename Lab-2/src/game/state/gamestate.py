from typing import Self, NamedTuple

import keyboard

from game.display.field import Field
from game.display.position import Position
from game.units.base import Base
from game.utils import flush_input


class GameState(NamedTuple):
    field: Field
    base: Base
    cursor: Position
    quit_required: bool

    def poll(self) -> Self:
        move: Position = self.cursor
        quit_required: bool = self.quit_required
        event: keyboard.KeyboardEvent = keyboard.read_event(True)
        if event.event_type == keyboard.KEY_DOWN:
            match event.name:
                case "w" | "up" | "k":
                    move = Position(self.cursor.x, self.cursor.y - 1)
                case "a" | "left" | "h":
                    move = Position(self.cursor.x - 1, self.cursor.y)
                case "s" | "down" | "j":
                    move = Position(self.cursor.x, self.cursor.y + 1)
                case "d" | "right" | "l":
                    move = Position(self.cursor.x + 1, self.cursor.y)
                case "space":
                    pass
                case "q":
                    # TODO: ask to save.
                    quit_required = True
                case _:
                    pass
        flush_input()
        if self.field.is_inside(move):
            field: Field = self.field.move_cursor(self.cursor, move)
            return GameState(
                field,
                self.base,
                move,
                quit_required,
            )
        return GameState(
            self.field,
            self.base,
            self.cursor,
            quit_required,
        )

    def print(self) -> None:
        print(
            self.field.render(),
            self.cursor,
            self.field.cells[self.cursor.x][self.cursor.y],
        )

    def is_over(self) -> bool:
        return self.base.is_crushed() or self.quit_required

    def next(self) -> Self:
        return GameState(self.field, self.base, self.cursor, self.quit_required)
