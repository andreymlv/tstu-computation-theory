from abc import ABC, abstractmethod

import pygame

from src.position import Position
from src.size import Size


class Drawable(ABC):
    @abstractmethod
    def draw(self, position: Position, size: Size) -> pygame.Rect:
        """
        Create drawable element for pygame scene.
        """
        pass
