import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 11, 11
SQUARE_SIZE = WIDTH//COLS
GREEN = (0,255,0)
DARK_GREEN = (0, 200, 0)
BROWN = (165,42,42)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREY = (128,128,128)

MOUSE  = pygame.transform.scale(pygame.image.load('assets\jerry.png'), (WIDTH//COLS, WIDTH//COLS))
SQUARE = pygame.transform.scale(pygame.image.load('assets\square.png'),(WIDTH//COLS, WIDTH//COLS))
TRAP   = pygame.transform.scale(pygame.image.load('assets\mousetrap.png'),(WIDTH//COLS - 15, WIDTH//COLS - 15))
