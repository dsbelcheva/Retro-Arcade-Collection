import unittest
from mysticblocks.game_engine import MysticBlocks


class TestMysticBlocks(unittest.TestCase):
    def setUp(self):
        self.game = MysticBlocks(20, 10)

    def test_new_figure(self):
        self.game.new_figure()
        self.assertIsNotNone(self.game.figure)

    def test_collision_false_at_start(self):
        self.game.new_figure()
        self.assertFalse(self.game.collision())

    def test_remove_lines(self):
        self.game.field[-1] = [1] * 10
        self.game.remove_lines()
        self.assertTrue(all(cell == 0 for cell in self.game.field[-1]))

    def test_go_down_collision(self):
        self.game.new_figure()
        initial_y = self.game.figure.y
        self.game.go_down()
        self.assertTrue(self.game.figure.y > initial_y)

    def test_freeze(self):
        self.game.new_figure()
        initial_figure = self.game.figure
        self.game.freeze()
        self.assertNotEqual(initial_figure, self.game.figure)

    def test_rotate(self):
        self.game.new_figure()
        initial_rotation = self.game.figure.rotation
        self.game.rotate()
        self.assertNotEqual(initial_rotation, self.game.figure.rotation)

    def test_game_over(self):
        self.game.new_figure()
        self.game.figure.y = 0
        while not self.game.collision():
            self.game.go_down()
        self.game.freeze()


if __name__ == '__main__':
    unittest.main()
