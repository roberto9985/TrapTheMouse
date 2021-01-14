import random
from .constants import GREEN, ROWS, SQUARE_SIZE, COLS, SQUARE, BROWN, GREY
from .piece import Piece


class Board:
    """
            The Board object contains:
            board: matrix of the game
            mouse_row, mouse_col: position in the matrix of mouse piece
            create_board(): function used to generate the matrix with pieces and the interface
            draw_squares(win): function used to render the table in the interface
            draw(win): function used to render all the pieces from the matrix on the table interface
            add(row, col): function used to add pieces in the board matrix
            move(row, col): function used to move a piece in the board matrix
            get_piece(row, col): function used to get the piece object from the board
            winner(): function used to decide whether the game is over or not

    """
    def __init__(self):
        self.board = []
        self.mouse_row = 0
        self.mouse_col = 0
        self.create_board()

    @staticmethod
    def draw_squares(win):
        """Summary or Description of the Function

           This function is used to color the background of the interface and to render all
            to render all the hexagonal images

        """
        win.fill(GREEN)
        for row in range(ROWS):
            for col in range(COLS):
                if col % 2 == 0:
                    win.blit(SQUARE, (row * SQUARE_SIZE, col * SQUARE_SIZE))
                else:
                    win.blit(SQUARE, (row * SQUARE_SIZE + 33, col * SQUARE_SIZE))

    def create_board(self):
        """Summary or Description of the Function

           This function is used to create the matrix board.
            Each time when game starts, the number of obstacles will be chosen randomly between 6 and 10,
            and their positions will be chosen in the same way, randomly.
             Each time the mouse will be in the middle, except when one of the obstacles has been rendered in its place.
              In this case another position of the mouse will be searched on the next row of the matrix until an
              available position is found.

        """
        number_list = range(6, 11)
        obstacles = random.choice(number_list)
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                self.board[row].append(0)
        for obj in range(obstacles):
            row_obj = random.choice(range(ROWS))
            col_obj = random.choice(range(COLS))
            self.board[row_obj][col_obj] = Piece(row_obj, col_obj, BROWN)
        find = ROWS // 2
        while True:
            if self.board[find][COLS // 2] == 0:
                self.board[find][COLS // 2] = Piece(find, COLS // 2, GREY)
                self.mouse_row, self.mouse_col = find, COLS // 2
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
        """Summary or Description of the Function

           This function is used to move the mouse on the board.

        """
        self.board[self.mouse_row][self.mouse_col] = 0
        self.board[row][col] = Piece(row, col, GREY)
        self.mouse_row, self.mouse_col = row, col

    def get_piece(self, row, col):
        return self.board[row][col]

    @property
    def winner(self):
        """Summary or Description of the Function

           This function is used to check if the mouse is on one side of the board,
            or if it is surrounded by traps.The game runs as long as this function
             returns False.

        """
        if self.mouse_row in [0, ROWS - 1] or self.mouse_col in [0, COLS - 1]:
            return "Mouse escaped"
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if (self.board[self.mouse_row + x][self.mouse_col + y]) == 0:
                    return "False"
        return "Mouse was caught"
