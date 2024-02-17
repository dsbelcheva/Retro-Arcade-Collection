import pygame

class Monster:
    def __init__(self, x, y, image, speed):
        self.image =  pygame.image.load(image)
        self.rect = self.image.get_rect(topright=(x, y))
        self.active = False
        self.speed = speed
        self.health = 100

    def activate(self):
        self.active = True

    def update(self, target_pos):
        if self.active:
            if self.rect.x > target_pos[0]:
                self.rect.x -= self.speed
            elif self.rect.x < target_pos[0]:
                self.rect.x += self.speed

    def take_damage(self, damage):
        if self.health > 0:
            self.health -= damage
        else:
            self.active = False
            return

    def draw(self, screen):
        if self.active:
            screen.blit(self.image, self.rect.topleft)
