import unittest
from unittest.mock import patch, MagicMock

SCREEN_WIDTH = 900


class TestPlayer(unittest.TestCase):

    @patch('galacticinvaders.bullet.Bullet')
    @patch('pygame.image.load')
    def setUp(self, mock_load, mock_bullet):
        mock_image = MagicMock()
        mock_image.convert_alpha.return_value = mock_image
        mock_load.return_value = mock_image

        mock_rect = MagicMock()
        mock_rect.width = 50
        mock_rect.height = 50
        mock_rect.bottomleft = (100, 100)
        mock_image.get_rect.return_value = mock_rect

        from galacticinvaders.player import Player
        self.player = Player(100, 100, 5, '../images/player.png')

    def test_move_left(self):
        initial_x = self.player.x
        self.player.move_left()
        self.assertTrue(self.player.x < initial_x)

    def test_move_right(self):
        initial_x = self.player.x
        self.player.move_right()
        self.assertTrue(self.player.x > initial_x)
        self.assertTrue(self.player.x + self.player.rect.width <= SCREEN_WIDTH)

    def test_shoot(self):
        bullets = []
        self.player.shoot(bullets, '../images/bullet.png')
        self.assertEqual(len(bullets), 1)


if __name__ == '__main__':
    unittest.main()
