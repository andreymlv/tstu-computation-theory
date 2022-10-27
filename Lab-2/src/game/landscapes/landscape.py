from game.gamestate import Drawable
from game.units.unit import Unit


class Landscape(Drawable):
    def combine(self, unit: Unit) -> str:
        return unit.draw() + self.draw()

    def draw(self) -> str:
        raise NotImplemented()
