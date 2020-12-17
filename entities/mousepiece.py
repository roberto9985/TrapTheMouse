from .constants import DARK_GREEN, WHITE, SQUARE_SIZE, GREY, MOUSE
import pygame

class Mouse:
    
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
        win.blit(MOUSE, (self.x - 25,  self.y - 50))


    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()
