from typing import Callable

from units.unit import Unit


class Field:
    edge = '#'

    def __init__(self, width: int, height: int, max_weaponed: int, units: list[Unit]):
        self.width = width
        self.height = height
        self.max_objects = max_weaponed
        self.units = units

    def render(self):
        print(self.edge * (self.width + 2))
        for y in range(self.height):
            print(self.edge, end='')
            is_unit_on_line: Callable[[Unit], bool] = lambda u: u.position.y == y
            units_on_line: list[Unit] = list(filter(is_unit_on_line, self.units))
            if units_on_line:
                for x in range(self.width):
                    for unit in units_on_line:
                        if unit.position.x == x:
                            print(unit.draw(), end='')
                        else:
                            print(' ', end='')
            else:
                print(' ' * self.width, end='')
            print(self.edge)
        print(self.edge * (self.width + 2))
