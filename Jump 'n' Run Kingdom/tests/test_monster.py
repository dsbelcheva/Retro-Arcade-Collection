import unittest
from unittest.mock import Mock, patch
import pygame
from monster import Monster

class TestMonster(unittest.TestCase):
    @patch('pygame.image.load')
    def setUp(self, mock_load):
        mock_image = Mock()
        mock_image.get_rect.return_value = pygame.Rect(0, 0, 50, 50)
        mock_load.return_value = mock_image

        self.monster = Monster(100, 100, '../images/monster.png', 5)

    def test_activate(self):
        self.assertFalse(self.monster.active, "Monster should not be active initially")
        self.monster.activate()
        self.assertTrue(self.monster.active, "Monster should be active after activation")

    def test_update_moves_towards_target_left(self):
        self.monster.activate()
        initial_x = self.monster.rect.x
        self.monster.update((initial_x - 10, 100))
        self.assertEqual(self.monster.rect.x, initial_x - 5, "Monster should move left towards the target")

    def test_update_moves_towards_target_right(self):
        self.monster.activate()
        initial_x = self.monster.rect.x
        self.monster.update((initial_x + 10, 100))
        self.assertEqual(self.monster.rect.x, initial_x + 5, "Monster should move right towards the target")

    def test_take_damage(self):
        initial_health = self.monster.health
        self.monster.take_damage(10)
        self.assertEqual(self.monster.health, initial_health - 10, "Monster should take damage correctly")

    @patch('pygame.Surface')
    def test_draw_calls_screen_blit_when_active(self, mock_surface):
        screen_mock = mock_surface.return_value
        self.monster.activate()
        self.monster.draw(screen_mock)
        screen_mock.blit.assert_called_once_with(self.monster.image, self.monster.rect.topleft)

if __name__ == '__main__':
    unittest.main()