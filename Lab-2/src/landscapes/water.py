from landscape import Landscape


class Water(Landscape):
    def draw(self) -> str:
        return "~"