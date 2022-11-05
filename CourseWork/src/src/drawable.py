from abc import ABC, abstractmethod

import pygame


class Drawable(ABC):
    @abstractmethod
    def draw(self) -> pygame.Rect:
        """
        Create drawable element for pygame scene.
        """
        pass
