from .constants import SQUARE_SIZE, TRAP, MOUSE, BROWN


class Piece:
    """
        The Piece object contains:
        row, col: position in the matrix,
        color: the color of the piece to distinguish obstacles from mouse
        x, y: position of the piece in the game interface
        calc_pos(): function to calculate x, y based on row, col
    """
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        """Summary or Description of the Function

            This function is used to calculate and update the new position x, y on the game interface,
             based on the row and column values, when calling the function. The positions differ depending,
              on the row because the board is in honeycomb format.

        """
        if self.row % 2 == 0:
            self.x = (SQUARE_SIZE * self.col + SQUARE_SIZE // 2) - 30
            self.y = (SQUARE_SIZE * self.row + SQUARE_SIZE // 2) - 20
        else:
            self.x = (SQUARE_SIZE * self.col + SQUARE_SIZE // 2) + 5
            self.y = (SQUARE_SIZE * self.row + SQUARE_SIZE // 2) - 20

    def draw(self, win):
        """Summary or Description of the Function

            This function renders the piece on the interface.

        """
        if self.color == BROWN:
            win.blit(TRAP, (self.x,  self.y))
        else:
            win.blit(MOUSE, (self.x, self.y))

    def move(self, row, col):
        """Summary or Description of the Function

            This function updates the row and column of the piece where it will be moved in the matrix and calls
             the calc_pos function described above.

        """
        self.row = row
        self.col = col
        self.calc_pos()
