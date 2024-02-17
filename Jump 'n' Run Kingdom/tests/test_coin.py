import unittest
from unittest.mock import Mock, patch
from coin import Coin, SCREEN_WIDTH

class TestCoin(unittest.TestCase):
    @patch('pygame.image.load')
    def setUp(self, mock_image_load):
        self.mock_image = Mock()
        self.mock_rect = Mock(x=100, y=100)
        self.mock_image.get_rect.return_value = self.mock_rect
        mock_image_load.return_value = self.mock_image
        self.coin = Coin(100, 100, '../images/coin.png')

    def test_update_moves_coin_left(self):
        original_x = self.coin.rect.x
        self.coin.update(5)
        self.assertEqual(self.coin.rect.x, original_x - 5)

    @patch('coin.random.randint')
    def test_generate_coins_creates_coins_at_expected_positions(self, mock_randint):
        mock_randint.side_effect = [100, 200]
        coins = Coin.generate_coins(num_coins=2, distance_between=40)
        self.assertEqual(len(coins), 2)
        expected_x_positions = [SCREEN_WIDTH + i * 40 for i in range(2)]
        expected_y_positions = [100, 200]
        for i, coin in enumerate(coins):
            self.assertEqual(coin.rect.center[0], expected_x_positions[i])
            self.assertEqual(coin.rect.center[1], expected_y_positions[i])

    def test_draw_calls_screen_blit_with_correct_arguments(self):
        screen_mock = Mock()
        self.coin.draw(screen_mock)
        screen_mock.blit.assert_called_once_with(self.mock_image, self.coin.rect.topleft)

if __name__ == '__main__':
    unittest.main()
