from typing import NamedTuple
import pygame

from tower import Tower


class Game(NamedTuple):
    towers: list[Tower]
    clock: pygame.time.Clock
    window: pygame.surface.Surface
    over: bool

    def init(self) -> None:
        pygame.display.set_caption("Hanoi Tower")

    def poll(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return Game(self.towers, self.clock, self.window, True)
        return self

    def render(self) -> None:
        self.window.fill((255, 255, 255))
        pygame.display.update()
        self.clock.tick(60)
