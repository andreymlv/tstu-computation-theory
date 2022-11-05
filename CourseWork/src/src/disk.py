from dataclasses import dataclass

import pygame

from src.drawable import Drawable
from src.printable import Printable


@dataclass()
class Disk(Drawable, Printable):
    # Should be unsigned
    size: int

    def print(self) -> str:
        return self.size * "#"

    def draw(self) -> pygame.Rect:
        return super().draw()
