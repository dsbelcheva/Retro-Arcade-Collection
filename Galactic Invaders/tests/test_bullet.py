import unittest
from unittest.mock import Mock, patch
import pygame
from bullet import Bullet

class TestBullet(unittest.TestCase):
    @patch('pygame.image.load')
    def setUp(self, mock_load):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.bullet = Bullet(100, 100, '../images/bullet.png')
        self.bullet.image = Mock()

    def test_move(self):
        original_y = self.bullet.y
        self.bullet.move()
        self.assertEqual(self.bullet.y, original_y + self.bullet.speed, "Куршумът не се е преместил правилно.")

    def test_draw(self):
        with patch('pygame.Surface.blit') as mock_blit:
            self.bullet.draw(self.screen)
            mock_blit.assert_called_with(self.bullet.image, (self.bullet.x, self.bullet.y))

if __name__ == '__main__':
    unittest.main()