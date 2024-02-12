import pygame


shield_img = pygame.image.load('../images/shield.png')
axe_img= pygame.image.load('../images/axe.png')

class Item:
    def __init__(self, image, x, y):
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)
