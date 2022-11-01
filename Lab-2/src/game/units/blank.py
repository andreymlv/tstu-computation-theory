from game.interface.drawable import Drawable


class Blank(Drawable):
    def draw(self) -> str:
        return " "
