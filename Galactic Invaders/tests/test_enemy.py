import unittest
from unittest.mock import Mock, patch
import random
import pygame
from enemy import Enemy, SCREEN_WIDTH, SCREEN_HEIGHT

class TestEnemy(unittest.TestCase):
    @patch('pygame.image.load')
    def setUp(self, mock_load):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.enemy = Enemy(100, 100, 2, '../images/enemy.png')
        self.enemy.image = Mock()

    def test_update(self):
        original_y = self.enemy.rect.y
        self.enemy.update()
        self.assertEqual(self.enemy.rect.y, original_y + self.enemy.speed, "Enemy did not move down correctly.")

    def test_is_off_screen(self):
        self.enemy.rect.y = SCREEN_HEIGHT + 1
        self.assertTrue(self.enemy.is_off_screen(), "Enemy should be considered off screen.")

    def test_is_hit(self):
        bullet = Mock()
        bullet.rect = self.enemy.rect
        self.assertTrue(self.enemy.is_hit([bullet]), "Enemy should be considered hit.")

    @patch('random.randint')
    def test_generate_enemy(self, mock_randint):
        enemies_list = []
        mock_randint.return_value = 100
        Enemy.generate_enemy(enemies_list, '../images/enemy.png')
        self.assertEqual(len(enemies_list), 1, "Enemy was not added to the list.")
        self.assertIsInstance(enemies_list[0], Enemy, "Generated object is not an instance of Enemy.")

    def test_draw(self):
        with patch('pygame.Surface.blit') as mock_blit:
            self.enemy.draw(self.screen)
            mock_blit.assert_called_once_with(self.enemy.image, self.enemy.rect)

if __name__ == '__main__':
    unittest.main()
