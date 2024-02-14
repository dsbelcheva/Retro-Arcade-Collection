import unittest
from unittest.mock import Mock, patch
import pygame
from player import Player
from bullet import Bullet

SCREEN_WIDTH = 900

class TestPlayer(unittest.TestCase):
    @patch('pygame.image.load')
    def setUp(self, mock_load):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, 600))
        self.player = Player(450, 550, 5, '../images/spaceship.png')
        self.player.image = Mock()
        self.bullets = []

    def test_move_left(self):
        original_x = self.player.x
        self.player.move_left()
        self.assertEqual(self.player.x, original_x - self.player.speed, "Player did not move left correctly.")

    def test_move_right(self):
        original_x = self.player.x
        self.player.move_right()
        self.assertEqual(self.player.x, original_x + self.player.speed, "Player did not move right correctly.")

    def test_draw(self):
        with patch('pygame.Surface.blit') as mock_blit:
            self.player.draw(self.screen)
            mock_blit.assert_called_once_with(self.player.image, (self.player.x, self.player.y))

    @patch('bullet.Bullet')
    def test_shoot(self, mock_bullet):
        self.player.shoot(self.bullets, '../images/bullet.png')
        self.assertEqual(len(self.bullets), 1, "Shooting did not add a bullet to the bullets list.")
        mock_bullet.assert_called_once()

if __name__ == '__main__':
    unittest.main()
