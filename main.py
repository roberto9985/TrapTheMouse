
import pygame
from entities.constants import WIDTH, HEIGHT, SQUARE_SIZE, DARK_GREEN, GREY, BROWN
from entities.game import Game
from ai.minmax import minimax
from ai.minmax_alpha_beta import minimaxAlpha_Beta
from ai.algorithm import ai_move

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Trap the mouse')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    # 0 - without ai
    # 1 - easy
    # 2 - medium
    # 3 - hard
    inputLevel = int(input("Select the difficulty:"))

    while run:
        clock.tick(FPS)
        
        if inputLevel in range(1,4):
            if game.turn == GREY:
                if inputLevel == 1:
                    value, new_board = minimax(game.get_board(), 2, True)
                if inputLevel == 2:
                    value, new_board = minimaxAlpha_Beta(game.get_board(), 2, float('-inf'),float('inf'), True)
                if inputLevel == 3:
                    value, new_board = ai_move(game.get_board(), 3, True)
                game.ai_move(new_board)
            

        if game.winner() != "False":
            print(game.winner())
            run = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row , col)
        game.update()
    
main()
