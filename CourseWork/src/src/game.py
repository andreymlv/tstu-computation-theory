from typing import NamedTuple

from src.gamestate import GameState


class Game(NamedTuple):
    state: GameState

    def poll(self):
        return Game(self.state.poll())

    def render(self) -> None:
        return self.state.render()

    def next(self):
        return Game(self.state.next())
