from typing import NamedTuple

from src.gamestate import GameState, HelpState


class Game(NamedTuple):
    state: GameState | HelpState

    def poll(self):
        return Game(self.state.poll())

    def render(self) -> None:
        return self.state.render()

    def next(self):
        return Game(self.state.next())

    def log(self) -> str:
        return f"{self.state.__class__.__name__} {self.state.towers} " + self.state.log()
