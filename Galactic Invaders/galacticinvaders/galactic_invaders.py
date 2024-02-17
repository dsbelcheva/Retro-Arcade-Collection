import pygame
from .player import Player
from .enemy import Enemy


SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600


def start_game(mode, max_number_of_enemies):
    pygame.init()
    screen = pygame.display.set_mode((900, 600))
    pygame.display.set_caption("Space Invaders")
    background_image = pygame.image.load('../images/background_galactic.jpg')
    background_image = pygame.transform.scale(background_image, (900, 600))
    player = Player(350, 460, 5, '../images/spaceship.png')
    enemies = []
    bullets = []
    player_lives = 3
    font = pygame.font.Font('freesansbold.ttf', 28)
    clock = pygame.time.Clock()
    Enemy.generate_enemy(enemies, '../images/enemy.png')

    winner_image = pygame.image.load("../images/winner.png").convert_alpha()
    lose_image = pygame.image.load("../images/game_over.png").convert_alpha()
    game_over = False

    last_enemy_spawn_time = pygame.time.get_ticks()
    number_of_enemies = 1
    running = True
    can_shoot = True

    while running:
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    can_shoot = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move_left()
        if keys[pygame.K_RIGHT]:
            player.move_right()
        if keys[pygame.K_SPACE] and can_shoot:
            player.shoot(bullets, '../images/bullet.png')
            can_shoot = False

        screen.blit(background_image, (0, 0))
        player.draw(screen)

        if current_time - last_enemy_spawn_time > 1500 and number_of_enemies < max_number_of_enemies:
            if mode == 'default':
                Enemy.generate_enemy(enemies, '../images/enemy.png')
            else:
                Enemy.generate_enemy(enemies, '../images/enemy.png', 3)
            number_of_enemies += 1
            last_enemy_spawn_time = current_time

        for enemy in enemies[:]:
            enemy.update()
            if enemy.is_off_screen():
                enemies.remove(enemy)
                player_lives -= 1
            elif enemy.is_hit(bullets):
                enemies.remove(enemy)
                player.score += 1

        victory = False
        if player_lives == 0:
            game_over = True
            victory = False
        elif player.score == max_number_of_enemies and player_lives > 0:
            game_over = True
            victory = True

        for enemy in enemies:
            enemy.draw(screen)

        for bullet in bullets:
            bullet.move()
            if bullet.y < 0:
                bullets.remove(bullet)
            else:
                bullet.draw(screen)

        if game_over:
            screen.fill((0, 0, 0))
            if victory:
                screen.blit(winner_image, (SCREEN_WIDTH // 2 - winner_image.get_width() //
                            2, SCREEN_HEIGHT // 2 - winner_image.get_height() // 2))
            else:
                screen.blit(lose_image, (SCREEN_WIDTH // 2 - lose_image.get_width() //
                            2, SCREEN_HEIGHT // 2 - lose_image.get_height() // 2))
            pygame.display.flip()
        else:
            result = font.render(
                f"Lives: {player_lives}", True, (255, 255, 255))
            screen.blit(result, (10, 10))
            health_runner = font.render(
                f"Score: {player.score}", True, (255, 255, 255))
            screen.blit(health_runner, (10, 50))

        pygame.display.flip()
        clock.tick(60)


pygame.quit()
