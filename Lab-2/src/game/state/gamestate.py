from dataclasses import dataclass
from time import sleep
from typing import Self
import colorama

import keyboard

from game.display.field import Field
from game.display.position import Position
from game.interface.combatable import Combatable
from game.utils import clear_screen


@dataclass()
class GameState:
    field: Field
    base: Position
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
                    warriors: list[tuple[Combatable, bool]] = list()
                    if self.cursor == self.base:
                        warriors: list[tuple[Combatable, bool]] = list(
                            map(
                                lambda warrior: (warrior, False),
                                self.field.cells[self.cursor.x][
                                    self.cursor.y
                                ].base.warriors,
                            )
                        )
                        warriors[0] = (warriors[0][0], True)
                    return GameSelect(
                        self.field, self.base, self.cursor, self.quit_required, warriors
                    ).poll()
                case "q":
                    # TODO: ask to save game state.
                    quit_required = True
                case _:
                    pass
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
            self.field.cells[self.cursor.x][self.cursor.y],
        )

    def is_over(self) -> bool:
        return (
            self.field.cells[self.base.x][self.base.y].base.is_crushed()
            or self.quit_required
        )

    def next(self) -> Self:
        return GameState(self.field, self.base, self.cursor, self.quit_required)


@dataclass()
class GameSelect(GameState):
    names: list[tuple[Combatable, bool]]

    def poll(self) -> GameState:
        if self.field.cells[self.cursor.x][self.cursor.y].can_enter():
            return self
        if self.field.cells[self.cursor.x][self.cursor.y].unit.draw() != " ":
            event: keyboard.KeyboardEvent = keyboard.read_event(True)
            if event.event_type == keyboard.KEY_DOWN:
                match event.name:
                    case "a" | "left" | "h":
                        return self.poll()
                    case "d" | "right" | "l":
                        return self.poll()
                    case "space":
                        return self
        elif self.field.cells[self.cursor.x][self.cursor.y].base.draw() != " ":
            names: str = " ".join(
                map(
                    lambda w: colorama.Fore.GREEN + w[0].name + colorama.Style.RESET_ALL if w[1] else w[0].name,
                    self.names,
                )
            )
            clear_screen()
            print(names)
            self.print()
            event: keyboard.KeyboardEvent = keyboard.read_event(True)
            if event.event_type == keyboard.KEY_DOWN:
                match event.name:
                    case "a" | "left" | "h":
                        warriors = self.names
                        return GameSelect(self.field, self.base, self.cursor, self.quit_required, warriors).poll()
                    case "d" | "right" | "l":
                        return self.poll()
                    case "space":
                        return self
        return self.poll()
