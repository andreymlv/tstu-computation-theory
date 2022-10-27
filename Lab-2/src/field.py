from dataclasses import dataclass

from cell import Cell
from position import Position


@dataclass()
class Field:
    width: int
    height: int
    cells: list[list[Cell]]

    def is_possible_move(self, position: Position) -> bool:
        return self.width > position.x >= 0 and self.height > position.y >= 0

    def render(self) -> list[list[str]]:
        result: list[list[str]] = [[""] * self.width] * self.height
        for x in range(self.height):
            for y in range(self.width):
                result[x][y] = self.cells[x][y].draw()
        return result
