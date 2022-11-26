from collections.abc import Callable
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

    def hanoi_recursive(
        self, strategy: Callable[[int, int, int, int], list[tuple[int, int]]]
    ) -> list:
        def helper(steps: list, history: list) -> list:
            if len(steps) == 0:
                return history
            return helper(steps[1:], history + [history[-1].step(steps[0])])

        return helper(
            strategy(len(self.towers[0].disks), 0, len(self.towers) - 1, 1), [self]
        )

    def hanoi(
        self, strategy: Callable[[int, int, int, int], list[tuple[int, int]]]
    ) -> list:
        steps: list[tuple[int, int]] = strategy(
            len(self.towers[0].disks), 0, len(self.towers) - 1, 1
        )
        history: list = [self]
        for step in steps:
            history.append(history[-1].step(step))
        return history

    def hanoi_iterative(self) -> list:
        disks: int = len(self.towers[0].disks)
        source: int = 0
        target: int = len(self.towers) - 1
        temp: int = 1
        history: list = [self]
        total: int = 2**disks - 1
        if disks % 2 == 0:
            for i in range(total):
                if i % 3 == 0:
                    if history[-1].can_move(source, temp):
                        history.append(history[-1].step((source, temp)))
                    else:
                        history.append(history[-1].step((temp, source)))
                elif i % 3 == 1:
                    if history[-1].can_move(source, target):
                        history.append(history[-1].step((source, target)))
                    else:
                        history.append(history[-1].step((target, source)))
                else:
                    if history[-1].can_move(temp, target):
                        history.append(history[-1].step((temp, target)))
                    else:
                        history.append(history[-1].step((target, temp)))
        else:
            for i in range(total):
                if i % 3 == 0:
                    if history[-1].can_move(source, target):
                        history.append(history[-1].step((source, target)))
                    else:
                        history.append(history[-1].step((target, source)))
                elif i % 3 == 1:
                    if history[-1].can_move(source, temp):
                        history.append(history[-1].step((source, temp)))
                    else:
                        history.append(history[-1].step((temp, source)))
                else:
                    if history[-1].can_move(temp, target):
                        history.append(history[-1].step((temp, target)))
                    else:
                        history.append(history[-1].step((target, temp)))
        return history

    def step(self, move: tuple[int, int]):
        return self.move(move[0], move[1])

    def can_move(self, from_tower: int, to_tower: int) -> bool:
        return self.towers[from_tower].can_pop() and self.towers[to_tower].can_push(
            self.towers[from_tower].last()
        )

    def print(self) -> str:
        return super().print()
