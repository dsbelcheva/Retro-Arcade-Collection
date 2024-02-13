import pygame

class Item:
    def __init__(self, image, x, y):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)
