import unittest
from unittest.mock import patch, MagicMock
import pygame
from epicrace.enemy_car import EnemyCar, SCREEN_WIDTH, SCREEN_HEIGHT


class TestEnemyCar(unittest.TestCase):
    def setUp(self):
        pygame.init()
        pygame.display.set_mode((1, 1))
        patcher = patch('pygame.image.load', return_value=MagicMock())
        self.addCleanup(patcher.stop)
        self.mock_load = patcher.start()
        self.enemy_car = EnemyCar(100, 100, 5, '../images/car1.png')

    def tearDown(self):
        pygame.quit()

    def test_init(self):
        self.assertEqual(self.enemy_car.rect.topleft, (100, 100))
        self.assertEqual(self.enemy_car.speed, 5)
        self.mock_load.assert_called_once_with('../images/car1.png')

    def test_update_within_bounds(self):
        initial_y = self.enemy_car.rect.y
        self.enemy_car.update()
        self.assertEqual(self.enemy_car.rect.y, initial_y + 5)

    def test_update_change_direction(self):
        self.enemy_car.rect.right = SCREEN_WIDTH
        self.enemy_car.update()
        self.assertEqual(self.enemy_car.speed, -5)

    @patch('pygame.Surface.blit')
    def test_draw(self, mock_blit):
        screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.enemy_car.draw(screen)
        mock_blit.assert_called_with(self.enemy_car.image, self.enemy_car.rect)

    def test_is_off_screen(self):
        self.enemy_car.rect.top = SCREEN_HEIGHT + 1
        self.assertTrue(self.enemy_car.is_off_screen())

    @patch('random.randint', return_value=100)
    @patch('random.choice', return_value='../images/car1.png')
    def test_generate_enemy(self, mock_choice, mock_randint):
        enemies_list = []
        EnemyCar.generate_enemy(
            enemies_list, ['../images/car1.png', '../images/car2.png'])
        self.assertEqual(len(enemies_list), 1)
        self.assertIsInstance(enemies_list[0], EnemyCar)
        self.assertEqual(enemies_list[0].rect.topleft, (100, -74))


if __name__ == '__main__':
    unittest.main()
