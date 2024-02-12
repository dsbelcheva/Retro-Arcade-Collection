import pygame


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720
runner_img = pygame.image.load('../images/runner.png')

class Runner:
    def __init__(self, runner_image, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.speed = 5
        self.velocity_y = 0
        self.on_ground = False
        self.image = self.image = pygame.image.load(runner_image)
        self.health = 100
        self.balance = 0
        self.has_axe = False
        self.has_shield = False

    def handle_movement(self, keys_pressed):
        if keys_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys_pressed[pygame.K_SPACE] and self.on_ground:
            self.jump()

    def jump(self):
        if self.on_ground:
            self.velocity_y = -16
            self.on_ground = False

    def apply_gravity(self):
        self.rect.y += self.velocity_y
        self.velocity_y += 0.5
        self.on_ground = False
        if self.rect.bottom >= 380:
            self.rect.bottom = 380
            self.on_ground = True
            self.velocity_y = 0

    def check_platform_collisions(self, platforms):
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                platforms.remove(platform)
                self.take_damage(10)

    def collect_coins(self, coins):
        for coin in coins[:]:
            if self.rect.colliderect(coin.rect):
                coins.remove(coin)
                self.balance+=1

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            print("DEAD!GAME OVER!")

    def attack_monster(self, monster):
        if self.has_axe and self.has_shield and self.balance >= 50:
            monster.take_damage(20)
        else:
            self.take_damage(20)

    def draw(self, screen):
        screen.blit(self.image, self.rect)