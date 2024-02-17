import unittest
from mysticblocks.figure import Figure, colors


class TestFigure(unittest.TestCase):
    def setUp(self):
        self.figure = Figure(5, 0)

    def test_initialization(self):
        self.assertEqual(self.figure.x, 5)
        self.assertEqual(self.figure.y, 0)
        self.assertTrue(0 <= self.figure.type < len(Figure.figures))
        self.assertTrue(1 <= self.figure.color < len(colors))

    def test_rotation(self):
        initial_rotation = self.figure.rotation
        self.figure.rotate()
        self.assertNotEqual(initial_rotation, self.figure.rotation)

    def test_special_figure(self):
        special_counts = [
            Figure(0, 0).is_special for _ in range(10)].count(True)
        self.assertEqual(special_counts, 2)

    def test_move_down(self):
        initial_y = self.figure.y
        self.figure.y += 1
        self.assertEqual(self.figure.y, initial_y + 1)

    def test_move_left(self):
        initial_x = self.figure.x
        self.figure.x -= 1
        self.assertEqual(self.figure.x, initial_x - 1)

    def test_move_right(self):
        initial_x = self.figure.x
        self.figure.x += 1
        self.assertEqual(self.figure.x, initial_x + 1)

    def test_rotation_at_edge(self):
        self.figure.x = 0
        self.figure.rotate()
        self.figure.x = 9
        self.figure.rotate()


if __name__ == '__main__':
    unittest.main()
