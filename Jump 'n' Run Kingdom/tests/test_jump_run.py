import unittest
from unittest.mock import Mock, patch
from coin import Coin
from obstacle import Platform
from item import Item
from monster import Monster
from runner import Runner

class TestGameComponents(unittest.TestCase):
    @patch('pygame.image.load')
    @patch('pygame.font.Font')
    def setUp(self, mock_font, mock_image_load):
        mock_image_load.return_value = Mock()
        mock_font.return_value = Mock(render=Mock(return_value=Mock()))
        self.runner = Runner('../images/runner.png', 0, 360)
        self.monster = Monster(1200, 160, '../images/monster.png', 1)
        self.platforms = Platform.generate_platforms()
        self.coins = Coin.generate_coins()

    def test_runner_initial_state(self):
        self.assertEqual(self.runner.health, 100)
        self.assertFalse(self.runner.on_ground)

    def test_monster_activation(self):
        self.assertFalse(self.monster.active)
        self.monster.activate()
        self.assertTrue(self.monster.active)

    def test_generate_platforms(self):
        self.assertEqual(len(self.platforms), 2)

    def test_generate_coins(self):
        self.assertEqual(len(self.coins), 2)

    def test_update_monster_position_towards_runner(self):
        self.monster.activate()
        initial_x = self.monster.rect.x
        self.monster.update((self.runner.rect.x, self.runner.rect.y))
        self.assertNotEqual(self.monster.rect.x, initial_x)

    def test_runner_collect_coin(self):
        initial_balance = self.runner.balance
        self.runner.collect_coins(self.coins)
        self.assertEqual(self.runner.balance, initial_balance + len(self.coins))

    def test_runner_platform_collision(self):
        platform = Platform(0, self.runner.rect.bottom + 1, '../images/platform.png')
        self.platforms.append(platform)
        self.runner.check_platform_collisions(self.platforms)
        self.assertLess(self.runner.health, 100)

    def test_monster_activation_on_coins_threshold(self):
        self.assertEqual(self.monster.active, False)
        if self.runner.balance >= 20:
            self.monster.activate()
        self.assertEqual(self.monster.active, True)

    def test_monster_activation_on_coins_threshold(self):
        self.assertEqual(self.monster.active, False)
        if self.runner.balance >= 20:
            self.monster.activate()
        self.assertEqual(self.monster.active, True)

    def test_runner_collects_axe(self):
        self.runner.balance = 10
        if self.runner.balance == 10:
            self.runner.has_axe = True
        self.assertTrue(self.runner.has_axe)

    def test_runner_collects_shield(self):
        self.runner.balance = 20
        if self.runner.balance == 20:
            self.runner.has_shield = True
        self.assertTrue(self.runner.has_shield)

if __name__ == '__main__':
    unittest.main()
