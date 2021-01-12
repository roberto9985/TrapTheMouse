from copy import deepcopy
from entities.constants import BROWN, GREY, ROWS, COLS

def heuristicFunction(copyTable):
    curr_x = copyTable.mouseX
    curr_y = copyTable.mouseY
    count_left, count_right, count_up_left, count_up_right, count_down_left, count_down_right = 0, 0, 0, 0, 0, 0
    min_list = []

    for left in range(curr_y):
        if copyTable.board[curr_y][left] == 0:
            count_left += 1
        else:
            count_left = float('inf')
            break
    min_list.append(count_left)

    for right in range(curr_y + 1, COLS):
        if copyTable.board[curr_x][right] == 0:
            count_right += 1
        else:
            count_right = float('inf')
            break
    min_list.append(count_right)

    if curr_x % 2 == 0:
        up_left_j = 0
        for up_left in range(1, ROWS):
            if up_left % 2 == 1:
                up_left_j += 1
            if copyTable.board[curr_x - up_left][curr_y - up_left_j] == 0:
                count_up_left += 1
            else:
                count_up_left = 0
                break
            if (curr_x - up_left) == 0 or (curr_y - up_left_j) == 0:
                break

        up_right_j = 0
        for up_right in range(1, ROWS):
            if up_right % 2 == 0:
                up_right_j += 1
            if (curr_x - up_right) == 0 or (curr_y + up_right_j) == COLS:
                break
            if copyTable.board[curr_x - up_right][curr_y + up_right_j] == 0:
                count_up_right += 1
            else:
                count_up_right = 0
                break

        down_left_j = 0
        for down_left in range(1, ROWS):
            if down_left % 2 == 1:
                down_left_j += 1
            if (down_left + curr_x) == ROWS or (curr_y - down_left_j) == 0:
                break
            if copyTable.board[curr_x + down_left][curr_y - down_left_j] == 0:
                count_down_left += 1
            else:
                count_down_left = 0
                break

        down_right_j = 0
        for down_right in range(1, ROWS):
            if down_right % 2 == 0:
                down_right_j += 1
            if (down_right + curr_x) == ROWS or (down_right_j + curr_y) == COLS:
                break

            if copyTable.board[curr_x + down_right][curr_y + down_right_j] == 0:
                count_down_right += 1
            else:
                count_down_right = 0
                break

    else:
        up_left_j = 0
        for up_left in range(1, ROWS):
            if up_left % 2:
                up_left_j += 1
            if copyTable.board[curr_x - up_left][curr_y - up_left_j] == 0:
                count_up_left += 1
            else:
                count_up_left = 0
                break
            if (curr_x - up_left) == 0 or (curr_y - up_left_j) == 0:
                break

        up_right_j = 0
        for up_right in range(1, ROWS):
            if up_right % 2 == 1:
                up_right_j += 1
            if (curr_x - up_right) == 0 or (curr_y + up_right_j) == COLS:
                break

            if copyTable.board[curr_x - up_right][curr_y + up_right_j] == 0:
                count_up_right += 1
            else:
                count_up_right = 0
                break

        down_left_j = 0
        for down_left in range(1, ROWS):
            if down_left % 2 == 0:
                down_left_j += 1
            if (down_left + curr_x) == ROWS or (curr_y - down_left_j) == 0:
                break

            if copyTable.board[curr_x + down_left][curr_y - down_left_j] == 0:
                count_down_left += 1
            else:
                count_down_left = 0
                break

        down_right_j = 0
        for down_right in range(1, ROWS):
            if down_right % 2 == 1:
                down_right_j += 1
            if (down_right + curr_x) == ROWS or (down_right_j + curr_y) == COLS:
                break

            if copyTable.board[curr_x + down_right][curr_y + down_right_j] == 0:
                count_down_right += 1
            else:
                count_down_right = 0
                break

    sum_available = count_left + count_right + count_up_left + count_up_right + count_down_left + count_down_right
    print("Left: ", count_left, "Right ", count_right, "Down-Left ", count_down_left, "Down-Right", count_down_right)
    return sum_available