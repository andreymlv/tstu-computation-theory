from unittest import TestCase

from game.units.base import Base
from game.units.melee import Melee
from game.weapons.sword import Sword


class TestBase(TestCase):
    def test_produce(self):
        base_empty = Base(True, 10, [])
        warrior = Melee(10, 10, 10, Sword(10, 10, 10))
        self.assertEqual(base_empty.produce(warrior), Base(True, 10, [warrior]))
        base_full = Base(True, 2, [warrior])
        self.assertEqual(base_full.produce(warrior), Base(False, 2, [warrior, warrior]))
        self.assertEqual(base_full.produce(warrior).produce(warrior), Base(False, 2, [warrior, warrior]))

    def test_is_crushed(self):
        base = Base(True, 10, [Melee(10, 10, 10, Sword(10, 10, 10))])
        self.assertFalse(base.is_crushed())
        base = Base(True, 10, [Melee(0, 10, 10, Sword(10, 10, 10))])
        self.assertTrue(base.is_crushed())
        base = Base(True, 10, [])
        self.assertTrue(base.is_crushed())
