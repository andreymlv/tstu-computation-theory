from position import Position


class Object:
    def __init__(self, position: Position):
        self.position = position

    def draw(self) -> str:
        return ""
