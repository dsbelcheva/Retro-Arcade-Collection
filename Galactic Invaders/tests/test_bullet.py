import unittest
from unittest.mock import MagicMock, patch
import pygame
from bullet import Bullet

class TestBullet(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.mock_image = MagicMock()
        self.mock_rect = MagicMock(center=(100, 200))
        self.mock_image.get_rect.return_value = self.mock_rect

    def tearDown(self):
        pygame.quit()

    @patch('pygame.image.load')
    def test_move(self, mock_load):
        mock_load.return_value = self.mock_image
        bullet = Bullet(100, 200, '../images/bullet.png')
        original_y = bullet.y
        bullet.move()
        self.assertEqual(bullet.y, original_y + bullet.speed)
        self.assertEqual(bullet.rect.y, original_y + bullet.speed)

if __name__ == '__main__':
    unittest.main()

