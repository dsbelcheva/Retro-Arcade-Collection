import unittest
from unittest.mock import MagicMock, patch
from obstacle import Platform, SCREEN_WIDTH, SCREEN_HEIGHT, PLATFORM_WIDTH

class TestPlatform(unittest.TestCase):

    def setUp(self):
        self.mock_load_patcher = patch('pygame.image.load')
        self.mock_load = self.mock_load_patcher.start()
        mock_surface = MagicMock()
        self.mock_rect = MagicMock()
        mock_surface.get_rect.return_value = self.mock_rect
        self.mock_load.return_value = mock_surface
        self.mock_rect.x = 0
        self.mock_rect.y = 0

    def tearDown(self):
        self.mock_load_patcher.stop()

    def test_platform_initialization(self):
        x, y = 100, SCREEN_HEIGHT - 360
        self.mock_rect.x = x
        self.mock_rect.y = y
        platform = Platform(x, y, '../images/platform.png')
        self.assertEqual(platform.rect.x, x)
        self.assertEqual(platform.rect.y, y)
        self.mock_load.assert_called_once_with('../images/platform.png')

    def test_update(self):
        player_speed = 5
        initial_x = 100
        self.mock_rect.x = initial_x
        platform = Platform(initial_x, SCREEN_HEIGHT - 360, '../images/platform.png')
        platform.update(player_speed)
        self.assertEqual(platform.rect.x, initial_x - player_speed)

    @patch('obstacle.Platform.generate_platforms', return_value=[MagicMock(), MagicMock()])
    def test_generate_platforms(self, mock_generate_platforms):
        num_platforms = 2
        platforms = Platform.generate_platforms(num_platforms=num_platforms)
        self.assertEqual(len(platforms), num_platforms)
        for i, platform in enumerate(platforms):
            expected_x = SCREEN_WIDTH + i * (PLATFORM_WIDTH + 200)
            self.assertTrue(mock_generate_platforms.called)

if __name__ == '__main__':
    unittest.main()



