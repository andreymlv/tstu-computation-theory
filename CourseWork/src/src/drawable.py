import pygame
from abc import ABC, abstractmethod


class Drawable(ABC):
    @abstractmethod
    def print(self) -> str:
        pass

    @abstractmethod
    def draw(self) -> pygame.Rect:
        pass
