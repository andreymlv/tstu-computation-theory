from unittest import TestCase

import colorama

from game.display.cell import Cell
from game.display.position import Position
from game.landscapes.grass import Grass
from game.units.base import Base
from game.units.blank import Blank
from game.units.melee import Melee
from game.weapons.sword import Sword


class TestCell(TestCase):
    def test_draw(self):
        cell = Cell(Position(0, 0), Base(False, 0, []), Blank(), Blank(), Grass())
        self.assertEqual(cell.draw(), colorama.Back.GREEN + " ")

    def test_can_enter(self):
        cell = Cell(Position(0, 0), Base(False, 0, []), Blank(), Blank(), Grass())
        self.assertTrue(cell.can_enter())
        cell = Cell(Position(0, 0), Base(True, 2, [Melee(10, 10, 10, Sword(10, 10, 1))]),
                    Melee(10, 10, 10, Sword(10, 10, 1)), Blank(), Grass())
        self.assertFalse(cell.can_enter())
