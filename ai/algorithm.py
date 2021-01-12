import pygame
from copy import deepcopy
from entities.constants import BROWN, GREY, ROWS, COLS

def heuristicFunction(copyTable):
    curr_x = copyTable.mouseX 
    curr_y = copyTable.mouseY
    min_list = []
    count_left, count_right, count_up_left, count_up_right, count_down_left, count_down_right = 0, 0, 0, 0, 0, 0

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
                count_up_left = float('inf')
                break
            if (curr_x - up_left) == 0 or (curr_y - up_left_j) == 0:
                break
        min_list.append(count_up_left)

        up_right_j = 0
        for up_right in range(1, ROWS):
            if up_right % 2 == 0:
                up_right_j += 1
            if (curr_x - up_right) == 0 or (curr_y + up_right_j) == COLS:
                break
            if copyTable.board[curr_x - up_right][curr_y + up_right_j] == 0:
                count_up_right += 1
            else:
                count_up_right = float('inf')
                break
        min_list.append(count_up_right)

        down_left_j = 0
        for down_left in range(1, ROWS):
            if down_left % 2 == 1:
                down_left_j += 1
            if (down_left + curr_x) == ROWS or (curr_y - down_left_j) == 0:
                break
            if copyTable.board[curr_x + down_left][curr_y - down_left_j] == 0:
                count_down_left += 1
            else:
                count_down_left = float('inf')
                break
        min_list.append(count_down_left)

        down_right_j = 0
        for down_right in range(1, ROWS):
            if down_right % 2 == 0:
                down_right_j += 1
            if (down_right + curr_x) == ROWS or (down_right_j + curr_y) == COLS:
                break

            if copyTable.board[curr_x + down_right][curr_y + down_right_j] == 0:
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
            if copyTable.board[curr_x - up_left][curr_y - up_left_j] == 0:
                count_up_left += 1
            else:
                count_up_left = float('inf')
                break
            if (curr_x - up_left) == 0 or (curr_y - up_left_j) == 0:
                break
        min_list.append(count_up_left)

        up_right_j = 0
        for up_right in range(1, ROWS):
            if up_right % 2 == 1:
                up_right_j += 1
            if (curr_x - up_right) == 0 or (curr_y + up_right_j) == COLS:
                break

            if copyTable.board[curr_x - up_right][curr_y + up_right_j] == 0:
                count_up_right += 1
            else:
                count_up_right = float('inf')
                break
        min_list.append(count_up_right)

        down_left_j = 0
        for down_left in range(1, ROWS):
            if down_left % 2 == 0:
                down_left_j += 1
            if (down_left + curr_x) == ROWS or (curr_y - down_left_j) == 0:
                break

            if copyTable.board[curr_x + down_left][curr_y - down_left_j] == 0:
                count_down_left += 1
            else:
                count_down_left = float('inf')
                break
        min_list.append(count_down_left)

        down_right_j = 0
        for down_right in range(1, ROWS):
            if down_right % 2 == 1:
                down_right_j += 1
            if (down_right + curr_x) == ROWS or (down_right_j + curr_y) == COLS:
                break

            if copyTable.board[curr_x + down_right][curr_y + down_right_j] == 0:
                count_down_right += 1
            else:
                count_down_right = float('inf')
                break
        min_list.append(count_down_right)

    return min(min_list)


def ai_move(tableTest, depth, max_turn):
    if depth == 0 or tableTest.winner() != "False":
        return heuristicFunction(tableTest),tableTest
    
    if max_turn:
        minEval = float('inf')
        best_move = None
        
        for move in get_available_moves(tableTest, GREY): 
            evaluation = ai_move(move, depth-1, True)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move 
        return (minEval, best_move)

def get_available_moves(Board, color):
    moves = []
    if color == GREY:
        if Board.mouseX % 2 == 0:
            for x in [-1, 0, 1]:
                for y in [-1, 0]:
                    if Board.board[Board.mouseX + x][Board.mouseY + y] == 0:
                        aux_board = deepcopy(Board)
                        aux_board.move((Board.mouseX + x), (Board.mouseY + y))
                        moves.append(aux_board)
            # Special case
            if Board.board[Board.mouseX][Board.mouseY + 1] == 0:
                aux_board = deepcopy(Board)
                aux_board.move((Board.mouseX), (Board.mouseY + 1))
                moves.append(aux_board)

        elif Board.mouseX % 2 == 1:
            for x in [-1, 0, 1]:
                for y in [0, 1]:
                    if Board.board[Board.mouseX + x][Board.mouseY + y] == 0:
                        aux_board = deepcopy(Board)
                        aux_board.move((Board.mouseX + x), (Board.mouseY + y))
                        moves.append(aux_board)
            # Special case
            if Board.board[Board.mouseX][Board.mouseY - 1] == 0:
                aux_board = deepcopy(Board)
                aux_board.move((Board.mouseX), (Board.mouseY - 1))
                moves.append(aux_board)

    else:
        for row in range(ROWS):
            for col in range(COLS):
                if Board.board[row][col] == 0:
                    aux_board = deepcopy(Board)
                    aux_board.add(row, col)
                    moves.append(aux_board)
    for move in moves:
        print(move.mouseX, move.mouseY)
    print('----------------------')
    return moves
    
                        
    