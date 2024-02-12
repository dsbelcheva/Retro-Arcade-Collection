import pygame

monster_img = pygame.image.load('../images/monster.png')

class Monster:
    def __init__(self, x, y, image, speed):
        self.image = monster_img
        self.rect = self.image.get_rect(topright=(1200, 160))
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
        self.health -= damage
        if self.health <= 0:
            self.active = False

    def draw(self, screen):
        if self.active:
            screen.blit(self.image, self.rect.topleft)
