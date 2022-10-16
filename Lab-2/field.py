from typing import Callable

from object import Object
from position import Position


class Field:
    edge = '#'

    def __init__(self, width: int, height: int, max_weaponed: int, objects: list[Object]):
        self.width = width
        self.height = height
        # TODO: 'maximum weaponed' should be controlled by Base or Game class
        self.max_weaponed = max_weaponed
        self.objects = objects

    def is_possible_move(self, position: Position) -> bool:
        return position.x > self.width or position.y > self.height or position.x < 0 or position.y < 0

    def render(self) -> str:
        # TODO: Return colored 2D list and render it in the `Game` class
        result = ''
        result += self.edge * (self.width + 2) + '\n'
        for y in range(self.height):
            result += self.edge
            is_object_on_line: Callable[[Object], bool] = lambda u: u.position.y == y
            objects_on_line: list[Object] = list(filter(is_object_on_line, self.objects))
            if objects_on_line:
                for x in range(self.width):
                    for obj in objects_on_line:
                        if obj.position.x == x:
                            result += obj.draw()
                        else:
                            result += ' '
            else:
                result += ' ' * self.width
            result += self.edge + '\n'
        result += self.edge * (self.width + 2) + '\n'
        return result
