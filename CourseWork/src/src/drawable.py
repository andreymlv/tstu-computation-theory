import pygame
from abc import ABC, abstractmethod


class Drawable(ABC):
    @abstractmethod
    def draw(self) -> pygame.Rect:
        pass
