from combatable import Combatable
from unit import Unit


class Cavalry(Unit, Combatable):
    def draw(self) -> str:
        return "C"
