import colorama
from game.landscapes.landscape import Landscape


class Grass(Landscape):
    def draw(self) -> str:
        return colorama.Back.GREEN
