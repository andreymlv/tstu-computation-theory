from game.interface.drawable import Drawable
from game.interface.combatable import Combatable


class Cavalry(Drawable, Combatable):
    def draw(self) -> str:
        return "C"
