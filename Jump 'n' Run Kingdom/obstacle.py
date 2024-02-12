import random
import pygame


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720
PLATFORM_WIDTH = 132
platform_img = pygame.image.load('../images/platform.png')

class Platform:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, player_speed):
        self.rect.x -= player_speed

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)


def generate_platforms(platform_height=SCREEN_HEIGHT - 360, num_platforms=2, distance_between=200):
    platforms = []
    for i in range(num_platforms):
        x = SCREEN_WIDTH + i * (PLATFORM_WIDTH + distance_between)
        platforms.append(Platform(x, platform_height, platform_img))
    return platforms