from dataclasses import dataclass

from game.drawable import Drawable


@dataclass()
class Unit(Drawable):
    def draw(self) -> str:
        raise NotImplementedError()
