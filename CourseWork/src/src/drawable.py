from abc import ABC, abstractmethod

import pygame

from src.position import Position


class Drawable(ABC):
    @abstractmethod
    def draw(self, position: Position) -> pygame.Rect:
        """
        Create drawable element for pygame scene.
        """
        pass
