from dataclasses import dataclass

import pygame

from src.disk import Disk
from src.printable import Printable
from src.tower import Tower


def init() -> None:
    pygame.display.set_caption("Hanoi Tower")


@dataclass()
class Game(Printable):
    towers: list[Tower]
    clock: pygame.time.Clock = pygame.time.Clock()
    window: pygame.surface.Surface = pygame.display.set_mode((300, 300))
    over: bool = False

    def poll(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return Game(self.towers, self.clock, self.window, True)
        return self

    def render(self) -> None:
        self.window.fill((255, 255, 255))
        pygame.display.update()
        self.clock.tick(60)

    def move(self, from_tower: int, to_tower: int):
        if self.can_move(from_tower, to_tower):
            towers: list[Tower] = self.towers.copy()
            temp_disk: Disk = towers[from_tower].last()
            towers[from_tower] = towers[from_tower].pop()
            towers[to_tower] = towers[to_tower].push(temp_disk)
            return Game(towers, self.clock, self.window, self.over)
        return self

    def can_move(self, from_tower: int, to_tower: int) -> bool:
        return self.towers[from_tower].can_pop() and self.towers[to_tower].can_push(
            self.towers[from_tower].last()
        )

    def print(self) -> str:
        return super().print()
