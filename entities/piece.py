from .constants import DARK_GREEN, WHITE, SQUARE_SIZE, GREY, TRAP
import pygame

class Piece:

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        if self.row % 2 == 0:
            self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
            self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2 + 10
        else:
            self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2 + 35
            self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2 + 10

    def draw(self, win):
        win.blit(TRAP, (self.x - 30,  self.y - 30))


    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

