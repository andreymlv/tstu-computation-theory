from units.unit import Unit


class Cursor(Unit):
    def draw(self) -> str:
        return "+"
