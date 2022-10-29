from game.interface.drawable import Drawable


class Cursor(Drawable):
    def draw(self) -> str:
        return "+"
