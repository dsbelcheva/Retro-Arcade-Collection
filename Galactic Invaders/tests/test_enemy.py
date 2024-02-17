import unittest
from unittest.mock import Mock, patch
import pygame
from galacticinvaders.enemy import Enemy, SCREEN_WIDTH, SCREEN_HEIGHT


class TestEnemy(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def tearDown(self):
        pygame.quit()

    def test_init(self):
        mock_image = Mock()
        enemy = Enemy(100, 100, 2, '../images/enemy.png')
        self.assertEqual(enemy.rect.x, 100)
        self.assertEqual(enemy.rect.y, 100)
        self.assertEqual(enemy.speed, 2)

    def test_update(self):
        enemy = Enemy(100, 100, 2, '../images/enemy.png')
        original_y = enemy.rect.y
        enemy.update()
        self.assertEqual(enemy.rect.y, original_y + enemy.speed)

    def test_is_off_screen(self):
        enemy = Enemy(100, SCREEN_HEIGHT + 1, 2, '../images/enemy.png')
        self.assertTrue(enemy.is_off_screen())

    def test_is_hit(self):
        bullet = Mock()
        bullet.rect = pygame.Rect(100, 100, 10, 10)
        enemy = Enemy(100, 100, 2, '../images/enemy.png')
        self.assertTrue(enemy.is_hit([bullet]))

    @patch('random.randint')
    def test_generate_enemy(self, mock_randint):
        enemies_list = []
        mock_randint.return_value = 100
        Enemy.generate_enemy(enemies_list, '../images/enemy.png')
        self.assertEqual(len(enemies_list), 1)
        self.assertIsInstance(enemies_list[0], Enemy)


if __name__ == '__main__':
    unittest.main()
