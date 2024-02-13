import unittest
from unittest.mock import Mock, patch
from coin import Coin, SCREEN_WIDTH

class TestCoin(unittest.TestCase):
    @patch('coin_module.pygame.image.load')
    def setUp(self, mock_image_load):
        self.mock_image = Mock()
        self.mock_image.get_rect.return_value = Mock(center=(0, 0))
        mock_image_load.return_value = self.mock_image

        self.coin = Coin(100, 100, '../images/coin.png')

    def test_update_moves_coin_left(self):
        original_x = self.coin.rect.x
        self.coin.update(5)
        self.assertEqual(self.coin.rect.x, original_x - 5)

    @patch('coin_module.random.randint', return_value=100)
    def test_generate_coins_creates_coins(self, mock_randint):
        coins = Coin.generate_coins()
        self.assertEqual(len(coins), 2)
        for i, coin in enumerate(coins):
            self.assertEqual(coin.rect.x, SCREEN_WIDTH + i * 40)
            self.assertEqual(coin.rect.y, 100)

    def test_draw_calls_screen_blit(self):
        screen_mock = Mock()
        self.coin.draw(screen_mock)
        screen_mock.blit.assert_called_with(self.mock_image, self.coin.rect.topleft)

if __name__ == '__main__':
    unittest.main()
