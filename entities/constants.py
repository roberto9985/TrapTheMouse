import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 11, 11
SQUARE_SIZE = WIDTH//COLS - 5
GREEN = (0,255,0)
DARK_GREEN = (0, 200, 0)
BROWN = (165,42,42)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREY = (128,128,128)

MOUSE  = pygame.transform.scale(pygame.image.load('assets\jerry.png'), (SQUARE_SIZE, SQUARE_SIZE))
SQUARE = pygame.transform.scale(pygame.image.load('assets\square.png'),(SQUARE_SIZE + 5, SQUARE_SIZE + 20))
TRAP   = pygame.transform.scale(pygame.image.load('assets\mousetrap.png'),(WIDTH//COLS - 15, WIDTH//COLS - 15))
