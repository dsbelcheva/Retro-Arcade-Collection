import unittest
from unittest.mock import patch
import pygame
from epicrace.traffic_light import TrafficLight


class TestTrafficLight(unittest.TestCase):
    @patch('pygame.image.load')
    @patch('pygame.time.get_ticks')
    def test_traffic_light_cycle(self, mock_get_ticks, mock_image_load):
        mock_image = pygame.Surface((10, 10))
        mock_image_load.return_value = mock_image
        light = TrafficLight()
        initial_time = 1000
        mock_get_ticks.return_value = initial_time
        light.start()
        light.update()
        self.assertEqual(light.current_color, 'RED')
        mock_get_ticks.return_value = initial_time + 1501
        light.update()
        self.assertEqual(light.current_color, 'YELLOW')
        mock_get_ticks.return_value = initial_time + 3002
        light.update()
        self.assertEqual(light.current_color, 'GREEN')
        mock_get_ticks.return_value = initial_time + 4503
        light.update()
        self.assertEqual(light.current_color, 'RED')


if __name__ == '__main__':
    unittest.main()
