import pygame
import random

SCREEN_WIDTH = 740
SCREEN_HEIGHT = 700

class EnemyCar:
    def __init__(self, x, y, speed, image_path):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.speed = -self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_off_screen(self):
        return self.rect.top > SCREEN_HEIGHT
    
    @staticmethod
    def generate_enemy(enemies_list, images_path, speed=0.6):
        new_enemy_x = random.randint(0, SCREEN_WIDTH - 74)
        image_path = random.choice(images_path)
        new_enemy = EnemyCar(new_enemy_x, -74, speed, image_path)
        enemies_list.append(new_enemy)