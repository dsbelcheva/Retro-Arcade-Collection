import unittest
from unittest.mock import patch, MagicMock
import pygame
from player import Player 
from enemy import Enemy 
from galactic_invaders import start_game

class TestSpaceInvadersGame(unittest.TestCase):
    @patch('pygame.image.load')
    @patch('pygame.display.set_mode')
    def setUp(self, mock_set_mode, mock_load):
        pygame.init = MagicMock()
        pygame.display.set_mode = MagicMock(return_value=MagicMock())
        self.mock_screen = pygame.display.set_mode((900, 600))
        mock_load.return_value = MagicMock()

    @patch('player.Player.move_left')
    @patch('player.Player.move_right')
    def test_player_movement(self, mock_move_right, mock_move_left):
        player = Player(450, 550, 5, '../images/spaceship.png')
        player.move_left()
        mock_move_left.assert_called_once()
        player.move_right()
        mock_move_right.assert_called_once()

    @patch('enemy.Enemy.generate_enemy')
    def test_generate_enemy(self, mock_generate_enemy):
        enemies = []
        Enemy.generate_enemy(enemies, '../images/enemy.png')
        mock_generate_enemy.assert_called_once_with(enemies, '../images/enemy.png', speed=2)

    @patch('bullet.Bullet')
    def test_player_shoot(self, MockBullet):
        player = Player(450, 550, 5, '../images/spaceship.png')
        bullets = []
        player.shoot(bullets, '../images/bullet.png')
        self.assertTrue(len(bullets) > 0, "Bullet was not added on shooting.")


if __name__ == '__main__':
    unittest.main()
