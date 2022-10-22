from object import Object
from position import Position


class Cursor(Object):
    def __init__(self, position: Position):
        super().__init__(position)

    def draw(self) -> str:
        return "+"
