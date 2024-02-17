import unittest
from unittest.mock import Mock, patch
from runner import Runner

class TestRunner(unittest.TestCase):
    def setUp(self):
        self.mock_pygame_rect = patch('pygame.Rect').start()
        self.mock_pygame_image_load = patch('pygame.image.load').start()
        self.runner = Runner('fake_image_path', 100, 100)

    def tearDown(self):
        patch.stopall()

    def test_jump_changes_velocity_and_on_ground_status(self):
        self.runner.on_ground = True
        self.runner.jump()
        self.assertEqual(self.runner.velocity_y, -16)
        self.assertFalse(self.runner.on_ground)

    def test_collect_coins_increases_balance(self):
        coins = [Mock()]
        self.runner.collect_coins(coins)
        self.assertEqual(self.runner.balance, 1)
        self.assertEqual(len(coins), 0)

    def test_take_damage_decreases_health(self):
        initial_health = self.runner.health
        self.runner.take_damage(10)
        self.assertEqual(self.runner.health, initial_health - 10)

    def test_attack_monster_with_requirements(self):
        self.runner.has_axe = True
        self.runner.has_shield = True
        self.runner.balance = 50
        monster = Mock()
        self.runner.attack_monster(monster, 100)
        monster.take_damage.assert_called_with(20)

    def test_attack_monster_without_requirements(self):
        self.runner.has_axe = False
        self.runner.has_shield = False
        self.runner.balance = 10
        monster = Mock()
        self.runner.attack_monster(monster, 100)
        self.assertEqual(self.runner.health, 80)

if __name__ == '__main__':
    unittest.main()
