from unittest import TestCase

from game.display.cell import Cell
from game.display.field import Field
from game.display.position import Position
from game.display.screen import Screen
from game.landscapes.grass import Grass
from game.units.base import Base
from game.units.blank import Blank
from game.units.cavalry import Cavalry
from game.units.cursor import Cursor
from game.units.melee import Melee
from game.units.range import Range
from game.weapons.bow import Bow
from game.weapons.sword import Sword


class TestField(TestCase):
    def setUp(self) -> None:
        cells: list[list[Cell]] = []
        max_warriors = (10 + 10) // 2
        for x in range(10):
            for y in range(10):
                if y == 0:
                    cells.append([])
                cells[x].append(
                    Cell(
                        Position(x, y),
                        Base(False, max_warriors, []),
                        Blank(),
                        Blank(),
                        Grass(),
                    )
                )
        cells[0][0] = Cell(
            Position(0, 0),
            Base(
                True,
                max_warriors,
                [
                    Melee(10, 8, 4, Sword(128, 8, 1)),
                    Range(10, 8, 4, Bow(128, 8, 1)),
                    Cavalry(10, 8, 4, Sword(128, 8, 1)),
                ],
            ),
            Blank(),
            Cursor(),
            cells[0][0].landscape,
        )
        cells[3][3] = Cell(
            Position(3, 3),
            Base(
                True,
                max_warriors,
                [],
            ),
            Melee(10, 8, 4, Sword(128, 8, 1)),
            Blank(),
            cells[3][3].landscape,
        )
        cells[3][4] = Cell(
            Position(3, 4),
            Base(
                True,
                max_warriors,
                [],
            ),
            Cavalry(10, 8, 4, Sword(128, 8, 1)),
            Blank(),
            cells[5][5].landscape,
        )
        self.field = Field(Screen(10, 10), cells)

    def test_move_cursor(self):
        new = self.field.move_cursor(Position(0, 0), Position(0, 1))
        self.assertEqual(new.cells[0][0].cursor.draw(), Blank().draw())
        self.assertEqual(new.cells[0][1].cursor.draw(), Cursor().draw())

    def test_move_unit(self):
        new = self.field.move_unit(Position(3, 3), Position(3, 2))
        self.assertEqual(new.cells[3][3].unit.draw(), Blank().draw())

    def test_swap_cell(self):
        new = self.field.swap_cell(Position(3, 3), Position(3, 2))
        self.assertEqual(new.cells[3][3].unit.draw(), Blank().draw())
        self.assertEqual(
            new.cells[3][2].unit.draw(), Melee(10, 10, 10, Sword(10, 10, 1)).draw()
        )

    def test_is_inside(self):
        self.assertTrue(self.field.is_inside(Position(0, 0)))
        self.assertFalse(self.field.is_inside(Position(-1, 0)))

    def test_is_possible_move(self):
        self.assertTrue(self.field.is_possible_move(Position(3, 3), Position(3, 2)))
        self.assertTrue(self.field.is_possible_move(Position(3, 3), Position(3, 4)))
        self.assertFalse(self.field.is_possible_move(Position(0, 0), Position(0, -1)))

    def test_can_move_in(self):
        self.assertFalse(self.field.can_move_in(Position(3, 3)))
        self.assertTrue(self.field.can_move_in(Position(3, 2)))
