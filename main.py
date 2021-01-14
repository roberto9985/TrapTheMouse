import pygame
from entities.constants import WIDTH, HEIGHT, SQUARE_SIZE, GREY, GREEN, FONT
from entities.game import Game
from ai.minmax import minimax
from ai.minmax_alpha_beta import minimax_alpha_beta
from ai.algorithm import custom_ai_move
import time

FPS = 240

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Trap the mouse')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    if row % 2 == 1:
        col = (x + 35) // SQUARE_SIZE
        col = col - 1
    else:
        col = x // SQUARE_SIZE
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    input_level = int(input("Select the difficulty:"))
    # input_level = 3
    while run:
        clock.tick(FPS)

        if input_level in range(1, 4):
            new_board = None
            if game.turn == GREY:
                if input_level == 1:
                    value, new_board = minimax(game.get_board(), 2, True)
                if input_level == 2:
                    value, new_board = minimax_alpha_beta(game.get_board(), 3, float('-inf'), float('inf'), True)
                if input_level == 3:
                    value, new_board = custom_ai_move(game.get_board(), 4, True)
                if new_board is not None:
                    game.ai_move(new_board)

        if game.winner() != "False":
            print(game.winner())
            WIN.fill(GREEN)
            text_surface = FONT.render(game.winner(), False, (0, 0, 0))
            WIN.blit(text_surface, (WIDTH // 2 - 120, HEIGHT // 2 - 120))
            pygame.display.flip()
            run = False
            time.sleep(5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
        game.update()


main()
