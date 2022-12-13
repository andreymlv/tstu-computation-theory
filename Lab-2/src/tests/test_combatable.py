from unittest import TestCase

from game.interface.combatable import Combatable
from game.weapons.weapon import Weapon


class TestCombatable(TestCase):
    def test_is_dead(self):
        warrior = Combatable(10, 10, 10, Weapon(10, 10, 10))
        self.assertFalse(warrior.is_dead())
        warrior_dead = Combatable(0, 10, 10, Weapon(10, 10, 10))
        self.assertTrue(warrior_dead.is_dead())
        warrior_dead_negative = Combatable(-12, 10, 10, Weapon(10, 10, 10))
        self.assertTrue(warrior_dead_negative.is_dead())
