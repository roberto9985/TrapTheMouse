from entities.constants import GREY, ROWS, COLS
from .heuristic import get_available_moves
import random


def heuristic_function(test_table):
    """Summary or Description of the Function

        This function is used for the last level of difficulty.
         Its principle is to follow the shortest path to one of the edges of the board.

    """
    test_mouse_row = test_table.mouse_row
    test_mouse_col = test_table.mouse_col
    min_list = []
    count_left, count_right, count_up_left, count_up_right, count_down_left, count_down_right = 0, 0, 0, 0, 0, 0

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
                count_up_left = float('inf')
                break
            if (test_mouse_row - up_left) == 0 or (test_mouse_col - up_left_j) == 0:
                break
        min_list.append(count_up_left)

        up_right_j = 0
        for up_right in range(1, ROWS):
            if up_right % 2 == 0:
                up_right_j += 1
            if (test_mouse_row - up_right) == 0 or (test_mouse_col + up_right_j) == COLS:
                break
            if test_table.board[test_mouse_row - up_right][test_mouse_col + up_right_j] == 0:
                count_up_right += 1
            else:
                count_up_right = float('inf')
                break
        min_list.append(count_up_right)

        down_left_j = 0
        for down_left in range(1, ROWS):
            if down_left % 2 == 1:
                down_left_j += 1
            if (down_left + test_mouse_row) == ROWS or (test_mouse_col - down_left_j) == 0:
                break
            if test_table.board[test_mouse_row + down_left][test_mouse_col - down_left_j] == 0:
                count_down_left += 1
            else:
                count_down_left = float('inf')
                break
        min_list.append(count_down_left)

        down_right_j = 0
        for down_right in range(1, ROWS):
            if down_right % 2 == 0:
                down_right_j += 1
            if (down_right + test_mouse_row) == ROWS or (down_right_j + test_mouse_col) == COLS:
                break

            if test_table.board[test_mouse_row + down_right][test_mouse_col + down_right_j] == 0:
                count_down_right += 1
            else:
                count_down_right = float('inf')
                break
        min_list.append(count_down_right)
    else:
        up_left_j = 0
        for up_left in range(1, ROWS):
            if up_left % 2:
                up_left_j += 1
            if test_table.board[test_mouse_row - up_left][test_mouse_col - up_left_j] == 0:
                count_up_left += 1
            else:
                count_up_left = float('inf')
                break
            if (test_mouse_row - up_left) == 0 or (test_mouse_col - up_left_j) == 0:
                break
        min_list.append(count_up_left)

        up_right_j = 0
        for up_right in range(1, ROWS):
            if up_right % 2 == 1:
                up_right_j += 1
            if (test_mouse_row - up_right) == 0 or (test_mouse_col + up_right_j) == COLS:
                break

            if test_table.board[test_mouse_row - up_right][test_mouse_col + up_right_j] == 0:
                count_up_right += 1
            else:
                count_up_right = float('inf')
                break
        min_list.append(count_up_right)

        down_left_j = 0
        for down_left in range(1, ROWS):
            if down_left % 2 == 0:
                down_left_j += 1
            if (down_left + test_mouse_row) == ROWS or (test_mouse_col - down_left_j) == 0:
                break

            if test_table.board[test_mouse_row + down_left][test_mouse_col - down_left_j] == 0:
                count_down_left += 1
            else:
                count_down_left = float('inf')
                break
        min_list.append(count_down_left)

        down_right_j = 0
        for down_right in range(1, ROWS):
            if down_right % 2 == 1:
                down_right_j += 1
            if (down_right + test_mouse_row) == ROWS or (down_right_j + test_mouse_col) == COLS:
                break

            if test_table.board[test_mouse_row + down_right][test_mouse_col + down_right_j] == 0:
                count_down_right += 1
            else:
                count_down_right = float('inf')
                break
        min_list.append(count_down_right)
        random.shuffle(min_list)
    return min(min_list)


def custom_ai_move(table_test, depth, max_turn):
    """Summary or Description of the Function

        This function is inspired by MinMax but we will no longer calculate the possible decisions where obstacles can
         be placed by the player, we will always choose the shortest path to one of the sides of the board based on the
          result of the heuristic_function().

    """
    if depth == 0 or table_test.winner != "False":
        return heuristic_function(table_test), table_test

    if max_turn:
        min_eval = float('inf')
        best_move = None

        for move in get_available_moves(table_test, GREY):
            evaluation = custom_ai_move(move, depth - 1, True)[0]
            min_eval = min(min_eval, evaluation)
            if min_eval == evaluation:
                best_move = move
        return min_eval, best_move
