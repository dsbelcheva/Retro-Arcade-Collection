import pygame
from .game_engine import MysticBlocks
from .figure import colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
SIZE = (400, 500)
FPS = 20


def draw_game(screen, game):
    screen.fill(WHITE)
    for i in range(game.height):
        for j in range(game.width):
            pygame.draw.rect(screen, GRAY, [
                             game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
            if game.field[i][j] > 0:
                pygame.draw.rect(screen, colors[game.field[i][j]],
                                 [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

    if game.figure is not None:
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in game.figure.image():
                    pygame.draw.rect(screen, colors[game.figure.color],
                                     [game.x + game.zoom * (j + game.figure.x) + 1,
                                      game.y + game.zoom *
                                      (i + game.figure.y) + 1,
                                      game.zoom - 2, game.zoom - 2])


def draw_text(screen, game):
    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render("Score: " + str(game.score), True, BLACK)
    screen.blit(text, [0, 0])
    if game.state == "gameover":
        font1 = pygame.font.SysFont('Calibri', 65, True, False)
        text_game_over = font1.render("Game Over !", True, (180, 34, 22))
        text_game_over1 = font1.render("Press ESC", True, BLACK)
        screen.blit(text_game_over, [25, 200])
        screen.blit(text_game_over1, [50, 265])


def start_game(mode):
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Mystic Blocks")
    done = False
    clock = pygame.time.Clock()
    game = MysticBlocks(20, 10, mode)
    counter = 0
    pressing_down = False

    while not done:
        if game.figure is None:
            game.new_figure()
        counter += 1
        if counter > 100000:
            counter = 0

        if counter % (FPS // (game.level if game.mode == 'speed' else 1) // 2) == 0 or pressing_down:
            if game.state == "start":
                game.go_down()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.rotate()
                elif event.key == pygame.K_DOWN:
                    pressing_down = True
                elif event.key == pygame.K_LEFT:
                    game.go_side(-1)
                elif event.key == pygame.K_RIGHT:
                    game.go_side(1)
                elif event.key == pygame.K_SPACE:
                    game.go_space()
                elif event.key == pygame.K_ESCAPE:
                    game.__init__(20, 10)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    pressing_down = False

        draw_game(screen, game)
        draw_text(screen, game)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
