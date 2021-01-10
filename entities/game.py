import pygame
from .constants import DARK_GREEN, WHITE, BLUE, SQUARE_SIZE, ROWS, COLS, BROWN, GREY
from .board import Board

class Game:
    def __init__(self, win):
        self._init()
        self.win = win
    
    def update(self):
        self.board.draw(self.win)
        pygame.display.update()

    def _init(self):
        self.turn = BROWN
        self.board = Board()

    def select(self, row, col):
        # print(row,col)
        # print(self.board.mouseX,self.board.mouseY)
        piece = self.board.get_piece(row, col)
        if row in range(ROWS) and col in range(COLS):  
            if piece == 0 and self.turn == BROWN:        
                self._add(row, col)
            elif piece == 0 and self.turn == GREY:
                if row % 2 == 0:
                    if (self.board.mouseX - row) in [-1, 0, 1] and (self.board.mouseY - col) in [-1, 0]:
                        self._move(row, col)
                    elif (self.board.mouseX - row) == 0 and (self.board.mouseY - col) == 1:
                        self._move(row, col)
                elif row % 2 == 1:
                    if (self.board.mouseX - row) in [-1, 0, 1] and (self.board.mouseY - col) in [ 0, 1]:
                        self._move(row, col)
                    elif (self.board.mouseX - row) == 0 and (self.board.mouseY - col) == -1:
                        self._move(row, col)


    def _add(self, row, col):
        self.board.add(row, col)
        self.change_turn()

    def _move(self, row, col):
        self.board.move(row, col)
        self.change_turn()

    def change_turn(self):
        if self.turn == BROWN:
            self.turn = GREY
        else:
            self.turn = BROWN

    def winner(self):
        return self.board.winner()

    def get_board(self):
        return self.board

    def ai_move(self, board):
        self.board = board
        self.change_turn()
