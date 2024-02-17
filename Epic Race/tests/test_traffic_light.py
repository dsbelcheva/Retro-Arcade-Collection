import unittest
from unittest.mock import patch, MagicMock
import pygame
from traffic_light import TrafficLight

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
        self.assertEqual(light.current_color, 'RED', "The traffic light should initially be RED.")
        mock_get_ticks.return_value = initial_time + 1501
        light.update()
        self.assertEqual(light.current_color, 'YELLOW', "The traffic light should change to YELLOW.")
        mock_get_ticks.return_value = initial_time + 3002
        light.update()
        self.assertEqual(light.current_color, 'GREEN', "The traffic light should change to GREEN.")
        mock_get_ticks.return_value = initial_time + 4503
        light.update()
        self.assertEqual(light.current_color, 'RED', "The traffic light should cycle back to RED.")

if __name__ == '__main__':
    unittest.main()

