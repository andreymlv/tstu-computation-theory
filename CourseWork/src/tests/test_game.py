from unittest import TestCase

from src.disk import Disk
from src.game import Game
from src.tower import Tower


class TestGame(TestCase):
    def test_move(self):
        game_expected = Game([Tower([]), Tower([]), Tower([])])
        game_expected.towers[0] = game_expected.towers[0].push(Disk(3)).push(Disk(2)).push(Disk(1))
        game_expected = game_expected.move(0, 1)
        game_actual = Game([Tower([Disk(3), Disk(2)]), Tower([Disk(1)]), Tower([])])
        self.assertEqual(game_expected, game_actual, "Game states aren't equal.")
        game_expected = game_expected.move(0, 1)
        self.assertEqual(game_expected, game_actual, "Game states aren't equal.")
        game_expected = game_expected.move(0, 2)
        game_actual = Game([Tower([Disk(3)]), Tower([Disk(1)]), Tower([Disk(2)])])
        self.assertEqual(game_expected, game_actual, "Game states aren't equal.")
        game_expected = game_expected.move(1, 2)
        game_actual = Game([Tower([Disk(3)]), Tower([]), Tower([Disk(2), Disk(1)])])
        self.assertEqual(game_expected, game_actual, "Game states aren't equal.")
        game_expected = game_expected.move(1, 2)
        game_actual = Game([Tower([Disk(3)]), Tower([]), Tower([Disk(2), Disk(1)])])
        self.assertEqual(game_expected, game_actual, "Game states aren't equal.")
