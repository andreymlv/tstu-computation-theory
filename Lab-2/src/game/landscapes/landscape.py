from game.interface.drawable import Drawable


class Landscape(Drawable):
    def combine(self, unit: Drawable) -> str:
        return unit.draw() + self.draw()

    def draw(self) -> str:
        raise NotImplementedError()
