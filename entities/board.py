import pygame
import random
from .constants import GREEN, ROWS, DARK_GREEN, SQUARE_SIZE, COLS, WHITE, SQUARE, BROWN, GREY, MOUSE
from .piece import Piece
from .mousepiece import Mouse

class Board:
    def __init__(self):
        self.board = []
        self.mouseX = 0
        self.mouseY = 0
        self.create_board()
    
    def draw_squares(self, win):
        win.fill(GREEN)
        for row in range(ROWS):
            for col in range(COLS):
                win.blit(SQUARE, (row*SQUARE_SIZE, col*SQUARE_SIZE))

    def create_board(self):
        numberList = range(6,11)
        obstacles = random.choice(numberList)
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                self.board[row].append(0)   
        for obj in range(obstacles):
            rowobj = random.choice(range(ROWS))
            colobj = random.choice(range(COLS))
            self.board[rowobj][colobj] = Piece(rowobj,colobj, BROWN)
        find = ROWS//2
        while True:
            if self.board[find][COLS//2] == 0:
                self.board[find][COLS//2] = Mouse(find, COLS//2, GREY)
                self.mouseX,self.mouseY = find,COLS//2
                break
            else:
                find += 1           


    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)


    def add(self, row, col):
        self.board[row][col] = Piece(row, col, BROWN)

    def move(self, row, col):
            self.board[self.mouseX][self.mouseY] = 0
            self.board[row][col] = Mouse(row, col, GREY)
            self.mouseX,self.mouseY = row, col
            
    def get_piece(self, row, col):
        return self.board[row][col]

    
    def winner(self):
        if self.mouseX in [0, ROWS - 1] or self.mouseY in [0, COLS - 1]:
            return "Mouse escaped"
        for x in [-1,0,1]:
            for y in [-1,0,1]:
                if(self.board[self.mouseX + x][self.mouseY + y]) == 0:
                    return "False"
        return "Mouse was caught"

