from unittest import TestCase

import colorama

from game.display.cell import Cell
from game.display.position import Position
from game.landscapes.grass import Grass
from game.units.base import Base
from game.units.blank import Blank


class TestCell(TestCase):
    def test_draw(self):
        cell = Cell(Position(0, 0), Base(False, 0, []), Blank(), Blank(), Grass())
        self.assertEqual(cell.draw(), colorama.Back.GREEN + " ")

    def test_can_enter(self):
        self.fail()
