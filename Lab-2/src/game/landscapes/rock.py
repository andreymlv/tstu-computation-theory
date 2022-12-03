import colorama

from game.landscapes.landscape import Landscape


class Rock(Landscape):
    def draw(self) -> str:
        return colorama.Back.BLACK
