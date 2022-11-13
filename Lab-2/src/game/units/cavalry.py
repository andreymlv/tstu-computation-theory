from game.interface.combatable import Combatable
from game.interface.drawable import Drawable


class Cavalry(Drawable, Combatable):
    name = "Cavalry"

    def draw(self) -> str:
        return "C"
