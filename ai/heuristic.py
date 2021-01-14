from entities.constants import GREY, ROWS, COLS
from copy import deepcopy


def heuristic_function(test_table):
    """Summary or Description of the Function

          This heuristic function helps the minmax algorithm to make the decision.
           We could say that this function represents the brain of the mouse.
           The better this function, the better decisions the mouse will make.
            The main idea of this function is to calculate the area that contains the fewest obstacles.
             For this, the mouse will propagate its possible movements to the edge of the board.
              When there is an obstacle on one of the roads, that road will become 0.
               In order to better understand I have attached a picture that you can find it in
               'MouseLogicSketch/MouseAvailableMoves.png'

    """
    test_mouse_row = test_table.mouse_row
    test_mouse_col = test_table.mouse_col
    count_left, count_right, count_up_left, count_up_right, count_down_left, count_down_right = 0, 0, 0, 0, 0, 0
    min_list = []

    for left in range(test_mouse_col):
        if test_table.board[test_mouse_col][left] == 0:
            count_left += 1
        else:
            count_left = float('inf')
            break
    min_list.append(count_left)

    for right in range(test_mouse_col + 1, COLS):
        if test_table.board[test_mouse_row][right] == 0:
            count_right += 1
        else:
            count_right = float('inf')
            break
    min_list.append(count_right)

    if test_mouse_row % 2 == 0:
        up_left_j = 0
        for up_left in range(1, ROWS):
            if up_left % 2 == 1:
                up_left_j += 1
            if test_table.board[test_mouse_row - up_left][test_mouse_col - up_left_j] == 0:
                count_up_left += 1
            else:
                count_up_left = 0
                break
            if (test_mouse_row - up_left) == 0 or (test_mouse_col - up_left_j) == 0:
                break

        up_right_j = 0
        for up_right in range(1, ROWS):
            if up_right % 2 == 0:
                up_right_j += 1
            if (test_mouse_row - up_right) == 0 or (test_mouse_col + up_right_j) == COLS:
                break
            if test_table.board[test_mouse_row - up_right][test_mouse_col + up_right_j] == 0:
                count_up_right += 1
            else:
                count_up_right = 0
                break

        down_left_j = 0
        for down_left in range(1, ROWS):
            if down_left % 2 == 1:
                down_left_j += 1
            if (down_left + test_mouse_row) == ROWS or (test_mouse_col - down_left_j) == 0:
                break
            if test_table.board[test_mouse_row + down_left][test_mouse_col - down_left_j] == 0:
                count_down_left += 1
            else:
                count_down_left = 0
                break

        down_right_j = 0
        for down_right in range(1, ROWS):
            if down_right % 2 == 0:
                down_right_j += 1
            if (down_right + test_mouse_row) == ROWS or (down_right_j + test_mouse_col) == COLS:
                break

            if test_table.board[test_mouse_row + down_right][test_mouse_col + down_right_j] == 0:
                count_down_right += 1
            else:
                count_down_right = 0
                break

    else:
        up_left_j = 0
        for up_left in range(1, ROWS):
            if up_left % 2:
                up_left_j += 1
            if test_table.board[test_mouse_row - up_left][test_mouse_col - up_left_j] == 0:
                count_up_left += 1
            else:
                count_up_left = 0
                break
            if (test_mouse_row - up_left) == 0 or (test_mouse_col - up_left_j) == 0:
                break

        up_right_j = 0
        for up_right in range(1, ROWS):
            if up_right % 2 == 1:
                up_right_j += 1
            if (test_mouse_row - up_right) == 0 or (test_mouse_col + up_right_j) == COLS:
                break

            if test_table.board[test_mouse_row - up_right][test_mouse_col + up_right_j] == 0:
                count_up_right += 1
            else:
                count_up_right = 0
                break

        down_left_j = 0
        for down_left in range(1, ROWS):
            if down_left % 2 == 0:
                down_left_j += 1
            if (down_left + test_mouse_row) == ROWS or (test_mouse_col - down_left_j) == 0:
                break

            if test_table.board[test_mouse_row + down_left][test_mouse_col - down_left_j] == 0:
                count_down_left += 1
            else:
                count_down_left = 0
                break

        down_right_j = 0
        for down_right in range(1, ROWS):
            if down_right % 2 == 1:
                down_right_j += 1
            if (down_right + test_mouse_row) == ROWS or (down_right_j + test_mouse_col) == COLS:
                break

            if test_table.board[test_mouse_row + down_right][test_mouse_col + down_right_j] == 0:
                count_down_right += 1
            else:
                count_down_right = 0
                break

    sum_available = count_left + count_right + count_up_left + count_up_right + count_down_left + count_down_right
    return sum_available


def get_available_moves(board, color):
    moves = []
    if color == GREY:
        if board.mouse_row % 2 == 0:
            for x in [-1, 0, 1]:
                for y in [-1, 0]:
                    if board.board[board.mouse_row + x][board.mouse_col + y] == 0:
                        aux_board = deepcopy(board)
                        aux_board.move((board.mouse_row + x), (board.mouse_col + y))
                        moves.append(aux_board)
            # Special case
            if board.board[board.mouse_row][board.mouse_col + 1] == 0:
                aux_board = deepcopy(board)
                aux_board.move(board.mouse_row, (board.mouse_col + 1))
                moves.append(aux_board)

        elif board.mouse_row % 2 == 1:
            for x in [-1, 0, 1]:
                for y in [0, 1]:
                    if board.board[board.mouse_row + x][board.mouse_col + y] == 0:
                        aux_board = deepcopy(board)
                        aux_board.move((board.mouse_row + x), (board.mouse_col + y))
                        moves.append(aux_board)
            # Special case
            if board.board[board.mouse_row][board.mouse_col - 1] == 0:
                aux_board = deepcopy(board)
                aux_board.move(board.mouse_row, (board.mouse_col - 1))
                moves.append(aux_board)

    else:
        for row in range(ROWS):
            for col in range(COLS):
                if board.board[row][col] == 0:
                    aux_board = deepcopy(board)
                    aux_board.add(row, col)
                    moves.append(aux_board)
    return moves
