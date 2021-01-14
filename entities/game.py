import pygame
from .constants import ROWS, COLS, BROWN, GREY
from .board import Board


class Game:
    """
            The Game object contains:
            turn: indicates, in the current state, the turn of the player who has to make a move
            board: object Board who contains all the pieces of the game
            win: the resolution of the game where all the frames will be rendered
            update(): function used to update new frame on the interface
            select(row, col): function used to select the new position of the piece
            _add(row, col): function used to add new piece
            _move(row, col): function used to move piece
            change_turn(): function used to change turn of the game
            winner(): function used to stop the game if mouse escaped or it's trapped
            get_board(): functions used to return the object board
            ai_move(board): functions used to update the game after ai returns the board with a new position
                            of the mouse

    """
    def __init__(self, win):
        self.turn = BROWN
        self.board = Board()
        self.win = win

    def update(self):
        """Summary or Description of the Function

           This function is used to calculate and update the new position x, y on the game interface,
            based on the row and column values, when calling the function. The positions differ depending,
             on the line because the board is in honeycomb format.

        """
        self.board.draw(self.win)
        pygame.display.update()

    def select(self, row, col):
        """Summary or Description of the Function

           This function is used to verify if the new position, in which we want to move the piece,
            meets all the necessary criteria. In order to better understand what is done here in the folder of this
             project, I have attached a picture (MouseLogicSketch/TrapTheMouseLogic.png) in which I illustrate exactly
              the behavior of this function.

        """
        piece = self.board.get_piece(row, col)
        if row in range(ROWS) and col in range(COLS):
            if piece == 0 and self.turn == BROWN:
                self._add(row, col)
            elif piece == 0 and self.turn == GREY:
                if row % 2 == 0:
                    if (self.board.mouse_row - row) in [-1, 0, 1] and (self.board.mouse_col - col) in [-1, 0]:
                        self._move(row, col)
                    elif (self.board.mouse_row - row) == 0 and (self.board.mouse_col - col) == 1:
                        self._move(row, col)
                elif row % 2 == 1:
                    if (self.board.mouse_row - row) in [-1, 0, 1] and (self.board.mouse_col - col) in [0, 1]:
                        self._move(row, col)
                    elif (self.board.mouse_row - row) == 0 and (self.board.mouse_col - col) == -1:
                        self._move(row, col)

    def _add(self, row, col):
        self.board.add(row, col)
        self.change_turn()

    def _move(self, row, col):
        self.board.move(row, col)
        self.change_turn()

    def change_turn(self):
        """Summary or Description of the Function

           This function is used to change the turn whenever it is called.

        """
        if self.turn == BROWN:
            self.turn = GREY
        else:
            self.turn = BROWN

    def winner(self):
        return self.board.winner

    def get_board(self):
        return self.board

    def ai_move(self, board):
        self.board = board
        self.change_turn()
