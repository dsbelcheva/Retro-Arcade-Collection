import unittest
from unittest.mock import patch
import pygame
from epicrace.player import Player


class TestPlayer(unittest.TestCase):
    @patch('pygame.image.load')
    def test_player_initial_position(self, mock_image_load):
        mock_image = pygame.Surface((50, 50))
        mock_image_load.return_value = mock_image
        player = Player('../images/car.png', 100, 150, 5)
        self.assertEqual(player.x, 100)
        self.assertEqual(player.y, 150)

    @patch('pygame.image.load')
    def test_player_movement(self, mock_image_load):
        mock_image = pygame.Surface((50, 50))
        mock_image_load.return_value = mock_image
        keys_pressed = {
            pygame.K_LEFT: False,
            pygame.K_RIGHT: True,
            pygame.K_UP: False,
            pygame.K_DOWN: False
        }
        player = Player('../images/car.png', 100, 150, 5)
        player.update(keys_pressed)
        self.assertEqual(player.rect.x, 105)


if __name__ == '__main__':
    unittest.main()
