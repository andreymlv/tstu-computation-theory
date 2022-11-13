import colorama
from game.interface.drawable import Drawable

# TODO: If field is `everlasting`, then made cursor always look in center of the screen.
class Cursor(Drawable):
    def draw(self) -> str:
        return colorama.Back.RED
