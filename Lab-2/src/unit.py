from dataclasses import dataclass

from drawable import Drawable


@dataclass()
class Unit(Drawable):
    def draw(self) -> str:
        raise NotImplemented()
