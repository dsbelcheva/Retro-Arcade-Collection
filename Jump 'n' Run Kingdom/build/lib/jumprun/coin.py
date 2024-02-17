import random
import pygame

SCREEN_WIDTH = 1200


class Coin:
    def __init__(self, x, y, image):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(center=(x, y))

    def update(self, player_speed):
        self.rect.x -= player_speed

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    @staticmethod
    def generate_coins(num_coins=2, distance_between=40):
        coins = []
        for i in range(num_coins):
            coin_x = SCREEN_WIDTH + i * distance_between
            coin_y = random.randint(0, 500)
            coins.append(Coin(coin_x, coin_y, '../images/coin.png'))
        return coins
