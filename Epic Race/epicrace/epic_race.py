import pygame
import random
from .player import Player
from .enemy_car import EnemyCar
from .traffic_light import TrafficLight

SCREEN_WIDTH, SCREEN_HEIGHT = 740, 700
FPS = 60

pygame.init()
ENEMY_SPAWN = pygame.USEREVENT + 1
pygame.time.set_timer(ENEMY_SPAWN, 1000)
tank_SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(tank_SPAWN_EVENT, 5000)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Epic Race")
font = pygame.font.Font('freesansbold.ttf', 28)
clock = pygame.time.Clock()

background_image1 = pygame.image.load('../images/race.jpg')
background_image1 = pygame.transform.scale(background_image1, (SCREEN_WIDTH, SCREEN_HEIGHT))
background_image2 = pygame.image.load('../images/race2.jpg')
background_image2 = pygame.transform.scale(background_image2, (SCREEN_WIDTH, SCREEN_HEIGHT))

background_position_1 = [0, 0]
background_position_2 = [0, -SCREEN_HEIGHT]

def move_background():
    global background_position_1, background_position_2

    speed = 0.4

    background_position_1[1] += speed
    background_position_2[1] += speed

    if background_position_1[1] >= SCREEN_HEIGHT:
        background_position_1[1] = -SCREEN_HEIGHT
    if background_position_2[1] >= SCREEN_HEIGHT:
        background_position_2[1] = -SCREEN_HEIGHT
class Game:
    def __init__(self, number_of_cars=10):
        self.running = True
        self.game_active = False
        self.player =  Player('../images/car.png', SCREEN_WIDTH / 2, SCREEN_HEIGHT - 180, 1)
        self.tanks = []
        self.enemies = []
        self.lives = 3
        self.traffic_light = TrafficLight()
        self.enemy_car_images = [
            '../images/car1.png',
            '../images/car2.png',
            '../images/car3.png',
            '../images/car4.png',
            '../images/car5.png',
            '../images/car6.png',
            '../images/car7.png',
            '../images/car8.png',
        ]
        self.current_number_of_cars = 0
        self.tank_image = pygame.image.load("../images/tank.png").convert_alpha()
        self.winner_image = pygame.image.load("../images/winner.png").convert_alpha()
        self.lose_image = pygame.image.load("../images/game_over.png").convert_alpha()
        self.game_over = False
        self.victory = False
        self.number_of_cars = number_of_cars
    
    def spawn_tank(self):
        x = random.randint(0, SCREEN_WIDTH - self.tank_image.get_width())
        y = random.randint(0, SCREEN_HEIGHT - self.tank_image.get_height())
        self.tanks.append({"image": self.tank_image, "rect": self.tank_image.get_rect(topleft=(x, y))})

    def check_collisions_with_fuel(self):
        for fuel_can in self.tanks[:]:
            if self.player.rect.colliderect(fuel_can["rect"]):
                self.lives += 1
                self.tanks.remove(fuel_can)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_s and not self.game_active:
                    self.traffic_light.start()
                if event.type == ENEMY_SPAWN and self.game_active and self.current_number_of_cars < self.number_of_cars:
                    EnemyCar.generate_enemy(self.enemies, self.enemy_car_images)
                    self.current_number_of_cars += 1
                if event.type == tank_SPAWN_EVENT and self.game_active:
                    self.spawn_tank()


            screen.blit(background_image1, background_position_1)
            screen.blit(background_image2, background_position_2)
            self.player.draw(screen)

            keys_pressed = pygame.key.get_pressed()
            self.traffic_light.update()
            if self.traffic_light.current_color == 'GREEN':
                self.game_active = True

            if not self.game_active:
                self.traffic_light.draw(screen)
            else:
                move_background()
                self.player.update(keys_pressed)
                for fuel_can in self.tanks[:]:
                    fuel_can["rect"].y += 0.5
                    if fuel_can["rect"].top > SCREEN_HEIGHT:
                        self.tanks.remove(fuel_can)
                    elif self.player.rect.colliderect(fuel_can["rect"]):
                        self.lives += 1
                        self.tanks.remove(fuel_can)
                for fuel_can in self.tanks:
                    screen.blit(fuel_can["image"], fuel_can["rect"])
                for enemy in self.enemies[:]:
                    enemy.draw(screen)
                    enemy.update()
                    if enemy.is_off_screen():
                        self.enemies.remove(enemy)
                    elif self.player.rect.colliderect(enemy.rect):
                        self.lives -= 1
                        self.enemies.remove(enemy)
                        if self.lives <= 0:
                            self.game_over = True
                            break
            if self.current_number_of_cars >= self.number_of_cars and self.lives > 0:
                self.game_over = True
                self.victory = True
            elif self.lives <= 0:
                self.game_over = True
                self.victory = False

            if self.game_over:
                screen.fill((0, 0, 0))
                if self.victory:
                    screen.blit(self.winner_image, (SCREEN_WIDTH // 2 - self.winner_image.get_width() // 2, SCREEN_HEIGHT // 2 - self.winner_image.get_height() // 2))
                else:
                    screen.blit(self.lose_image, (SCREEN_WIDTH // 2 - self.lose_image.get_width() // 2, SCREEN_HEIGHT // 2 - self.lose_image.get_height() // 2))
            else:
                result = font.render(f"Lives: {self.lives}", True, (0, 0, 0))
                screen.blit(result, (10, 10))

            pygame.display.flip()

        pygame.quit()
