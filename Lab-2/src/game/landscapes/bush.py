from game.landscapes.landscape import Landscape


class Bush(Landscape):
    def draw(self) -> str:
        return "*"
