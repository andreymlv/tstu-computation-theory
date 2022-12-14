from dataclasses import dataclass

import pygame

from src.disk import Disk
from src.drawable import Drawable
from src.position import Position
from src.printable import Printable
from src.size import Size


@dataclass()
class Tower(Drawable, Printable):
    disks: list[Disk]

    def push(self, disk: Disk):
        if self.can_push(disk):
            return Tower(self.disks + [disk])
        return self

    def pop(self):
        if self.can_pop():
            return Tower(self.disks[:-1])
        return self

    def last(self) -> Disk:
        return self.disks[-1]

    def can_push(self, disk: Disk) -> bool:
        return len(self.disks) == 0 or self.last().weight > disk.weight

    def can_pop(self) -> bool:
        return len(self.disks) > 0

    def print(self) -> str:
        return super().print()

    def draw(self, position: Position, size: Size) -> pygame.Rect:
        return pygame.Rect(position, size)
