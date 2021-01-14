import pygame
pygame.font.init()

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 11, 11
SQUARE_SIZE: int = WIDTH // COLS - 5
GREEN = (0, 255, 0)
DARK_GREEN = (0, 200, 0)
BROWN = (165, 42, 42)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
FONT = pygame.font.SysFont('Comic Sans MS', 30)
MOUSE = pygame.transform.scale(pygame.image.load(r'assets\jerry.png'), (SQUARE_SIZE - 10, SQUARE_SIZE - 10))
SQUARE = pygame.transform.scale(pygame.image.load(r'assets\square.png'), (SQUARE_SIZE + 5, SQUARE_SIZE + 20))
TRAP = pygame.transform.scale(pygame.image.load(r'assets\mousetrap.png'), (WIDTH // COLS - 15, WIDTH // COLS - 15))
