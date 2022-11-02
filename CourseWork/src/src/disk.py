import pygame

from dataclasses import dataclass

from drawable import Drawable
from printable import Printable


@dataclass()
class Disk(Drawable, Printable):
    size: int

    def print(self) -> str:
        return self.size * "#"

    def draw(self) -> pygame.Rect:
        return super().draw()
