import colorama
from game.interface.drawable import Drawable


class Cursor(Drawable):
    # TODO: If field is `everlasting`, then made cursor always look in center of the screen.
    def draw(self) -> str:
        return colorama.Back.RED
