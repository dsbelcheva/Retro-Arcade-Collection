import random
import pygame

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

class Enemy:
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

    def is_hit(self, bullets):
        for bullet in bullets:
            if self.rect.colliderect(bullet.rect):
                bullets.remove(bullet)
                return True
        return False
    
    @staticmethod
    def generate_enemy(enemies_list, image_path, speed=2):
        new_enemy_x = random.randint(0, SCREEN_WIDTH - 64)
        new_enemy = Enemy(new_enemy_x, -64, speed, image_path)
        enemies_list.append(new_enemy)
