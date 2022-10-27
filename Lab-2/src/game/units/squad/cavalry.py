from game.combatable import Combatable
from game.units.unit import Unit


class Cavalry(Unit, Combatable):
    def draw(self) -> str:
        return "C"
