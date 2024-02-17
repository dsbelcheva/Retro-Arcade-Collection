import pygame
from .bullet import Bullet

SCREEN_WIDTH = 900


class Player:
    def __init__(self, x, y, speed, image_path):
        self.x = x
        self.y = y
        self.speed = speed
        self.score = 0
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(bottomleft=(x, y))

    def move_left(self):
        if self.x > 0:
            self.x -= self.speed
            self.rect.x = self.x

    def move_right(self):
        if self.x + self.rect.width < SCREEN_WIDTH:
            self.x += self.speed
            self.rect.x = self.x

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def shoot(self, bullets, bullet_image):
        bullet = Bullet(self.x + self.rect.width // 2, self.y, bullet_image)
        bullets.append(bullet)
