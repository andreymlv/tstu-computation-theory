import pygame

from dataclasses import dataclass

from drawable import Drawable
from disk import Disk


@dataclass()
class Tower(Drawable):
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
        return len(self.disks) == 0 or self.last().size > disk.size

    def can_pop(self) -> bool:
        return len(self.disks) > 0

    def print(self) -> str:
        return super().print()

    def draw(self) -> pygame.Rect:
        return super().draw()
