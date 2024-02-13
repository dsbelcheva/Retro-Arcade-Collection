import unittest
from unittest.mock import Mock, patch
from obstacle import Platform, SCREEN_WIDTH, SCREEN_HEIGHT

class TestPlatform(unittest.TestCase):
    @patch('platform_module.pygame.image.load')
    def setUp(self, mock_image_load):
        self.mock_image = Mock()
        self.mock_image.get_rect.return_value = Mock(topleft=(0, 0))
        mock_image_load.return_value = self.mock_image

        self.platform = Platform(100, SCREEN_HEIGHT - 360, '../images/platform.png')

    def test_update_moves_platform_left(self):
        original_x = self.platform.rect.x
        self.platform.update(5)
        self.assertEqual(self.platform.rect.x, original_x - 5)

    @patch('platform_module.pygame.image.load')
    def test_generate_platforms_creates_platforms(self, mock_image_load):
        mock_image_load.return_value = self.mock_image
        platforms = Platform.generate_platforms()
        self.assertEqual(len(platforms), 2)
        for platform in platforms:
            self.assertTrue(platform.rect.x > SCREEN_WIDTH)
            self.assertEqual(platform.rect.y, SCREEN_HEIGHT - 360)

    def test_draw_calls_screen_blit(self):
        screen_mock = Mock()
        self.platform.draw(screen_mock)
        screen_mock.blit.assert_called_with(self.mock_image, self.platform.rect.topleft)

if __name__ == '__main__':
    unittest.main()
