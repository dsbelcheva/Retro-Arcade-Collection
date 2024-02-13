import pygame
from runner import Runner
from obstacle import Platform
from coin import Coin
from item import Item
from monster import Monster

SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 720
background_position_1 = [0, 0]
background_position_2 = [SCREEN_WIDTH, 0]

def move_background():
    global background_position_1, background_position_2

    speed = 3

    background_position_1[0] -= speed
    background_position_2[0] -= speed

    if background_position_1[0] <= -SCREEN_WIDTH:
        background_position_1[0] = SCREEN_WIDTH
    if background_position_2[0] <= -SCREEN_WIDTH:
        background_position_2[0] = SCREEN_WIDTH

def start_game(monster_activation_threshold):
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Jump 'n' Run Kingdom")
    clock = pygame.time.Clock()
    font = pygame.font.Font('freesansbold.ttf', 28)
    background_image1 = pygame.image.load('../images/background_jump.jpg')
    background_image1 = pygame.transform.scale(background_image1, (SCREEN_WIDTH, SCREEN_HEIGHT))
    background_image2 = pygame.image.load('../images/background2_jump.jpg')
    background_image2 = pygame.transform.scale(background_image2, (SCREEN_WIDTH, SCREEN_HEIGHT))

    winner_image = pygame.image.load("../images/winner.png").convert_alpha()
    lose_image = pygame.image.load("../images/game_over.png").convert_alpha()

    axe = None
    shield = None
    running = True
    game_over = False
    total_coins_generated = 2
    runner = Runner('../images/runner.png', 0, SCREEN_HEIGHT - 360)
    monster = Monster(SCREEN_WIDTH, 160, '../images/monster.png', 1)
    shield_img = pygame.image.load('../images/shield.png')
    axe_img= pygame.image.load('../images/axe.png')
    platforms = Platform.generate_platforms()
    coins = Coin.generate_coins()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        move_background()
        screen.blit(background_image1, background_position_1)
        screen.blit(background_image2, background_position_2)
        keys = pygame.key.get_pressed()
        runner.handle_movement(keys)
        runner.apply_gravity()
        runner.draw(screen)

        for platform in platforms:
            platform.update(runner.speed//2)
            platform.draw(screen)

        for coin in coins:
            coin.update(runner.speed//2)
            coin.draw(screen)

        if  platforms and platforms[-1].rect.x <= SCREEN_WIDTH - 1000 and total_coins_generated < monster_activation_threshold :
            platforms.extend(Platform.generate_platforms())
            coins.extend(Coin.generate_coins())
            total_coins_generated += 2
        elif not platforms and total_coins_generated < monster_activation_threshold:
            platforms.extend(Platform.generate_platforms())
            coins.extend(Coin.generate_coins())
            total_coins_generated += 2

        runner.collect_coins(coins)
        runner.check_platform_collisions(platforms)

        if runner.health == 0:
            game_over = True
            victory = False

        if runner.balance == 10 and not runner.has_axe:
            axe = Item(axe_img, 100, SCREEN_HEIGHT - 400)

        if runner.balance == 20 and not runner.has_shield:
            shield = Item(shield_img, 200, SCREEN_HEIGHT - 500) 

        if axe and runner.rect.colliderect(axe.rect):
            runner.has_axe = True
            axe = None
        elif shield and runner.rect.colliderect(shield.rect):
            runner.has_shield = True
            shield = None

        if axe:
            axe.draw(screen)
        elif shield:
            shield.draw(screen)  

        if total_coins_generated >= monster_activation_threshold and not monster.active:
            monster.active = True

        if monster.active:
            monster.update(runner.rect.center)
            monster.draw(screen)

        victory = False
        if monster.active and runner.rect.colliderect(monster.rect):
            monster.health = 20
            runner.attack_monster(monster, total_coins_generated)      
            if monster.health <= 0:
                monster.active = False
                game_over=True
                victory = True
            if runner.health <= 0:
                game_over = True
                victory = False
    
        if game_over:
            screen.fill((0, 0, 0))
            if victory:
                screen.blit(winner_image, (SCREEN_WIDTH // 2 - winner_image.get_width() // 2, SCREEN_HEIGHT // 2 - winner_image.get_height() // 2))
            else:
                screen.blit(lose_image, (SCREEN_WIDTH // 2 - lose_image.get_width() // 2, SCREEN_HEIGHT // 2 - lose_image.get_height() // 2))
            pygame.display.flip() 
        else:
            result = font.render(f"Score: {runner.balance}", True, (255, 255, 255))
            screen.blit(result, (10, 10))
            health_runner = font.render(f"Health Runner: {runner.health}", True, (255, 255, 255))
            screen.blit(health_runner, (10, 50))
            health_monster = font.render(f"Health Monster: {monster.health}", True, (255, 255, 255))
            screen.blit(health_monster, (910, 10))

        pygame.display.flip()
        clock.tick(60)

pygame.quit()