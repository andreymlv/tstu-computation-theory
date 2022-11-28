from dataclasses import dataclass

import pygame

from src.drawable import Drawable
from src.position import Position
from src.printable import Printable
from src.size import Size


@dataclass()
class Disk(Drawable, Printable):
    # Should be unsigned and greater then zero
    weight: int

    def print(self) -> str:
        return self.weight * "#"

    def draw(self, position: Position, size: Size) -> pygame.Rect:
        return pygame.Rect(position, size)
