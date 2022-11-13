from typing import NamedTuple, Self
from game.state.gamestate import GameState


class Game(NamedTuple):
    state: GameState

    def is_over(self) -> bool:
        return self.state.is_over()

    def print(self) -> None:
        self.state.print()

    def poll(self) -> Self:
        return Game(self.state.poll())

    def next(self) -> Self:
        return Game(self.state.next())
