import pygame

SCREEN_WIDTH = 740
SCREEN_HEIGHT = 700

class Player:
    def __init__(self, image_path, x, y, speed):
        self.image = pygame.image.load(image_path)
        self.x = x
        self.y = y
        self.speed = speed
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, keys_pressed):
        if keys_pressed[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys_pressed[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH - self.image.get_width():
            self.rect.x += self.speed
        if keys_pressed[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys_pressed[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT - self.image.get_height():
            self.rect.y += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)