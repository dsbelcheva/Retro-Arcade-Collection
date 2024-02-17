import unittest
from mysticblocks.game_engine import MysticBlocks

class TestMysticBlocks(unittest.TestCase):
    def setUp(self):
        self.game = MysticBlocks(20, 10)

    def test_game_initialization(self):
        self.assertEqual(self.game.state, "start")
        self.assertEqual(len(self.game.field), 20)
        for row in self.game.field:
            self.assertEqual(len(row), 10)
            self.assertTrue(all(cell == 0 for cell in row))

    def test_collision_at_start(self):
        self.game.new_figure()
        self.game.figure.y = 0
        self.assertFalse(self.game.collision())

    def test_line_clearing(self):
        self.game.field[-1] = [1] * 10
        self.game.remove_lines()
        self.assertTrue(all(cell == 0 for cell in self.game.field[-1]))

    def test_game_over_directly(self):
        self.game = MysticBlocks(20, 10)
        for x in range(self.game.width):
            self.game.field[0][x] = 1
        self.game.new_figure()
        self.game.figure.y = 0 
        self.game.freeze()
        self.assertEqual(self.game.state, "gameover")
        
    def test_figure_rotation_without_collision(self):
        self.game.new_figure()
        initial_image = self.game.figure.image()
        self.game.rotate()
        rotated_image = self.game.figure.image()
        self.assertNotEqual(initial_image, rotated_image)

    def test_move_figure_side_without_collision(self):
        self.game.new_figure()
        initial_x = self.game.figure.x
        self.game.go_side(1)
        self.assertNotEqual(self.game.figure.x, initial_x)
        self.assertFalse(self.game.collision())

    def test_special_block_generation(self):
        special_blocks_generated = 0
        for _ in range(20):
            self.game.new_figure()
            if self.game.figure.is_special:
                special_blocks_generated += 1
        expected_special_blocks = 20 // 5
        self.assertEqual(special_blocks_generated, expected_special_blocks)

if __name__ == '__main__':
    unittest.main()