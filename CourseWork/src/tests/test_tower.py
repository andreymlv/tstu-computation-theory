from unittest import TestCase

from src.disk import Disk
from src.tower import Tower


class TestTower(TestCase):
    def test_push(self):
        tower_actual: Tower = Tower([])
        tower_actual: Tower = tower_actual.push(Disk(1))
        tower_expected: Tower = Tower([Disk(1)])
        self.assertEqual(tower_actual, tower_expected, "Towers aren't equal.")
        tower_actual: Tower = tower_actual.push(Disk(2))
        tower_expected: Tower = Tower([Disk(1)])
        self.assertEqual(tower_actual, tower_expected, "Towers aren't equal.")
        tower_actual: Tower = Tower([Disk(2), Disk(1)])
        tower_expected: Tower = Tower([Disk(2), Disk(1)])
        self.assertEqual(tower_actual, tower_expected, "Towers aren't equal.")

    def test_pop(self):
        tower_actual: Tower = Tower([Disk(1)])
        tower_actual: Tower = tower_actual.pop()
        tower_expected: Tower = Tower([])
        self.assertEqual(tower_actual, tower_expected, "Towers aren't equal.")
        tower_actual: Tower = Tower([]).pop()
        tower_expected: Tower = Tower([])
        self.assertEqual(tower_actual, tower_expected, "Towers aren't equal.")

    def test_last(self):
        disk_actual = Tower([Disk(1)]).last()
        disk_expected = Disk(1)
        self.assertEqual(disk_actual, disk_expected, "Disks aren't equal.")
