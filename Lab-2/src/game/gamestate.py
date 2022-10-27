from dataclasses import dataclass
from typing import Self

import keyboard

import utils
from game.cell import Cell
from game.cursor import Cursor
from game.field import Field
from position import Position
from units.base import Base
from units.blankunit import BlankUnit


@dataclass()
class GameState:
    field: Field
    base: Base
    cursor: Position
    quit_required: bool

    def poll(self) -> Self:
        cursor = self.cursor
        move = self.cursor
        quit_required = self.quit_required
        event = keyboard.read_event(True)
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
                    for line in self.field.cells:
                        for cell in line:
                            pass
                case "q":
                    # TODO: ask to save.
                    quit_required = True
                case _:
                    pass
        utils.flush_input()
        if self.field.is_possible_move(move):
            self.field.cells[cursor.x][cursor.y] = Cell(
                cursor,
                BlankUnit(),
                BlankUnit(),
                self.field.cells[cursor.x][cursor.y].landscape,
            )
            self.field.cells[move.x][move.y] = Cell(
                move,
                Cursor(),
                BlankUnit(),
                self.field.cells[move.x][move.y].landscape,
            )
            return GameState(
                Field(self.field.width, self.field.height, self.field.cells),
                self.base,
                move,
                quit_required,
            )
        return GameState(
            Field(self.field.width, self.field.height, self.field.cells),
            self.base,
            cursor,
            quit_required,
        )

    def render(self) -> None:
        field: list[list[str]] = self.field.render()
        to_draw = ""
        for row in field:
            for obj in row:
                to_draw += obj
            to_draw += "\n"
        print(to_draw)

    def is_over(self) -> bool:
        # return self.base.is_crushed() or self.quit_required
        return self.quit_required

    def next(self) -> Self:
        return GameState(self.field, self.base, self.cursor, self.quit_required)
