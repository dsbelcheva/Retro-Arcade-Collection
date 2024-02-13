import pygame
from player import Player
from bullet import Bullet


pygame.init()
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Space Invaders")
background_image = pygame.image.load('../images/background_galactic.jpg')
background_image = pygame.transform.scale(background_image, (900, 600))
player = Player(350,460,5,'../images/spaceship.png')
bullets = []
font = pygame.font.Font('freesansbold.ttf', 28)
clock = pygame.time.Clock()


running = True
can_shoot = True
while running:
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
        print(len(bullets))
    
    screen.blit(background_image, (0, 0))
    player.draw(screen)

    for bullet in bullets:
        bullet.move()
        if bullet.y < 0:
            bullets.remove(bullet)
        else:
            bullet.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()