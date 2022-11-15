from dataclasses import dataclass
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
                    warriors: tuple[list[Combatable], int] = (
                        self.field.cells[self.cursor.x][self.cursor.y].base.warriors,
                        0,
                    )
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
            "Usage: 'wasd' to move cursor.\nPress 'space' to do some action.\nPress 'q' to quit.\n"
            + self.field.render(),
            "Cell:",
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
    names: tuple[list[Combatable], int]

    def poll(self) -> GameState:
        if self.field.cells[self.cursor.x][self.cursor.y].can_enter():
            return self
        if self.field.cells[self.cursor.x][self.cursor.y].unit.draw() != " ":
            clear_screen()
            print("Manage unit: 'm' for move.")
            self.print()
            event: keyboard.KeyboardEvent = keyboard.read_event(True)
            if event.event_type == keyboard.KEY_DOWN:
                match event.name:
                    case "m":
                        return GameMove(
                            self.field, self.base, self.cursor, self.quit_required
                        ).poll()
                    case _:
                        pass
        elif self.field.cells[self.cursor.x][self.cursor.y].base.draw() != " ":
            names: list[str] = []
            for i, warrior in enumerate(self.names[0]):
                if i == self.names[1]:
                    names.append(
                        colorama.Fore.GREEN + warrior.name + colorama.Style.RESET_ALL
                    )
                else:
                    names.append(warrior.name)
            colored_names = " ".join(names)
            clear_screen()
            print("Base:", colored_names)
            self.print()
            event: keyboard.KeyboardEvent = keyboard.read_event(True)
            if event.event_type == keyboard.KEY_DOWN:
                match event.name:
                    case "a" | "left" | "h":
                        warriors = self.names
                        if self.names[1] > 0:
                            warriors = (warriors[0], warriors[1] - 1)
                        return GameSelect(
                            self.field,
                            self.base,
                            self.cursor,
                            self.quit_required,
                            warriors,
                        ).poll()
                    case "d" | "right" | "l":
                        warriors = self.names
                        if self.names[1] < len(self.names[0]) - 1:
                            warriors = (warriors[0], warriors[1] + 1)
                        return GameSelect(
                            self.field,
                            self.base,
                            self.cursor,
                            self.quit_required,
                            warriors,
                        ).poll()
                    case "space":
                        # If there is no space for placinig warrior around base: do nothing.
                        # If there is space for placing warrior around base:
                        # place warrior on filed and remove that warrior from base.
                        return self
                    case _:
                        pass
        return self.poll()


@dataclass()
class GameMove(GameState):
    def poll(self) -> GameState:
        move: Position = self.cursor
        clear_screen()
        self.print()
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
                    return GameState(
                        self.field, self.base, self.cursor, self.quit_required
                    ).poll()
                case _:
                    pass
        if self.field.is_inside(move):
            field: Field = self.field.move_unit(self.cursor, move).move_cursor(
                self.cursor, move
            )
            return GameMove(field, self.base, move, self.quit_required).poll()
        return self
