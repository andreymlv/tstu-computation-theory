from game.interface.drawable import Drawable


class Landscape(Drawable):
    def combine(self, unit: Drawable) -> str:
        return self.draw() + unit.draw()
