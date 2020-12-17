
import pygame
from entities.constants import WIDTH, HEIGHT, SQUARE_SIZE, DARK_GREEN, GREY, BROWN, GREEN
from entities.game import Game
from ai.minmax import minimax
from ai.minmax_alpha_beta import minimaxAlpha_Beta
from ai.algorithm import ai_move
import time

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Trap the mouse')
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    if row % 2 == 1:
        col = (x + 35) // SQUARE_SIZE
        col = col - 1
    else:
        col = x // SQUARE_SIZE
    
    # print(x, y)
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    # 0 - without ai
    # 1 - easy
    # 2 - medium
    # 3 - hard
    # inputLevel = int(input("Select the difficulty:"))
    inputLevel = 1
    while run:
        clock.tick(FPS)
        
        if inputLevel in range(1,4):
            if game.turn == GREY:
                if inputLevel == 1:
                    value, new_board = minimax(game.get_board(), 2, True)
                if inputLevel == 2:
                    value, new_board = minimaxAlpha_Beta(game.get_board(), 3, float('-inf'),float('inf'), True)
                if inputLevel == 3:
                    value, new_board = ai_move(game.get_board(), 3, True)
                game.ai_move(new_board)

        if game.winner() != "False":
            print(game.winner())
            WIN.fill(GREEN)
            textsurface = myfont.render(game.winner(), False, (0, 0, 0))
            WIN.blit(textsurface,(WIDTH//2 - 120, HEIGHT//2 - 120))
            pygame.display.flip()
            run = False
            time.sleep(5)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row , col)
        game.update()
    
main()
