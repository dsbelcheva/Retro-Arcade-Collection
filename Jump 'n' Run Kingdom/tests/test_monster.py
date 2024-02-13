import unittest
from unittest.mock import Mock, patch
from monster import Monster

class TestMonster(unittest.TestCase):
    def setUp(self):
        self.mock_pygame_rect = patch('pygame.Rect').start()
        self.mock_pygame_image_load = patch('pygame.image.load').start()
        self.monster = Monster(100, 100, 'fake_image_path', 5)

    def tearDown(self):
        patch.stopall()

    def test_activate_sets_active_true(self):
        self.monster.activate()
        self.assertTrue(self.monster.active)

    def test_update_moves_towards_target(self):
        self.monster.activate()
        target_pos = (90, 100)
        self.monster.update(target_pos)
        self.assertTrue(self.monster.rect.x < 100)

        target_pos = (110, 100)
        self.monster.update(target_pos)
        self.assertTrue(self.monster.rect.x > 90)

    def test_take_damage_decreases_health(self):
        initial_health = self.monster.health
        self.monster.take_damage(10)
        self.assertEqual(self.monster.health, initial_health - 10)

        self.monster.take_damage(90)
        self.assertFalse(self.monster.active)

    def test_draw_calls_screen_blit_when_active(self):
        screen_mock = Mock()
        self.monster.activate()
        self.monster.draw(screen_mock)
        screen_mock.blit.assert_called()

if __name__ == '__main__':
    unittest.main()
